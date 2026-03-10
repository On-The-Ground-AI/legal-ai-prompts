# Legal Prompts Web App — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a credit-based web app where users describe a legal task in plain English, get a matching AI prompt from the library, and can pay credits to personalise it with their specific context and receive a follow-up prompt chain.

**Architecture:** Single-page React frontend (Vite) hosted on Vercel free tier. Serverless API functions (Vercel Edge Functions) handle all AI calls and Stripe webhooks — API keys never exposed to browser. Supabase handles auth (email magic link + Google OAuth), credit balances, and usage history. Prompt content is fetched directly from the GitHub repo's raw content API.

**Tech Stack:** React + Vite, Tailwind CSS, Vercel (hosting + serverless functions), Supabase (auth + Postgres), Stripe (payments), Google Gemini Flash API (search + classification), Stripe webhooks (credit top-up).

---

## Overview of Tasks

1. Project scaffold + environment setup
2. Supabase schema (users, credits, usage)
3. Auth UI (email magic link + Google)
4. Prompt search (Gemini, free tier)
5. Prompt display UI
6. Credit purchase flow (Stripe)
7. Personalisation engine (Gemini paid call)
8. Follow-up chain generator
9. Credit expiry enforcement
10. Terms of Service page + ToS gate
11. Rate limiting (free tier: 5 searches/day)
12. Deploy to Vercel

---

## Task 1: Project Scaffold

**Files:**
- Create: `package.json`
- Create: `vite.config.js`
- Create: `tailwind.config.js`
- Create: `.env.example`
- Create: `src/main.jsx`
- Create: `src/App.jsx`
- Create: `api/` (Vercel serverless functions directory)

**Step 1: Initialise the project**

```bash
npm create vite@latest legal-prompts-app -- --template react
cd legal-prompts-app
npm install
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
npm install @supabase/supabase-js stripe @stripe/stripe-js
```

**Step 2: Configure Tailwind**

In `tailwind.config.js`:
```js
export default {
  content: ["./index.html", "./src/**/*.{js,jsx}"],
  theme: { extend: {} },
  plugins: [],
}
```

In `src/index.css`:
```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

**Step 3: Create `.env.example`**

```
VITE_SUPABASE_URL=
VITE_SUPABASE_ANON_KEY=
GEMINI_API_KEY=
STRIPE_SECRET_KEY=
STRIPE_WEBHOOK_SECRET=
SUPABASE_SERVICE_ROLE_KEY=
GITHUB_REPO_RAW_BASE=https://raw.githubusercontent.com/On-The-Ground-AI/legal-ai-prompts/main
```

Copy to `.env.local` and fill in real values before running.

**Step 4: Verify dev server runs**

```bash
npm run dev
```
Expected: app loads at `http://localhost:5173`

**Step 5: Commit**

```bash
git init
git add .
git commit -m "feat: scaffold React + Vite + Tailwind project"
```

---

## Task 2: Supabase Schema

**Files:**
- Create: `supabase/schema.sql`

**Step 1: Create schema file**

```sql
-- Users table (extends Supabase auth.users)
create table public.profiles (
  id uuid references auth.users(id) primary key,
  email text not null,
  credits integer not null default 0,
  created_at timestamptz default now()
);

-- Credit packs purchased
create table public.credit_purchases (
  id uuid primary key default gen_random_uuid(),
  user_id uuid references public.profiles(id),
  stripe_payment_intent text,
  pack_name text,           -- 'starter' | 'standard' | 'pro'
  credits_added integer,
  amount_paid integer,      -- in cents (500 = $5)
  expires_at timestamptz,   -- now() + 6 months
  created_at timestamptz default now()
);

-- Credit usage log
create table public.credit_usage (
  id uuid primary key default gen_random_uuid(),
  user_id uuid references public.profiles(id),
  action text,              -- 'search' | 'personalise' | 'chain'
  credits_used integer,
  prompt_file text,         -- e.g. 'volume-3-disputes/V3_01_Pre_Action.md'
  created_at timestamptz default now()
);

-- Free tier rate limiting (IP-based, no login required)
create table public.free_searches (
  ip_hash text primary key,
  search_count integer default 0,
  reset_date date default current_date
);

-- Row level security
alter table public.profiles enable row level security;
alter table public.credit_purchases enable row level security;
alter table public.credit_usage enable row level security;

create policy "Users can read own profile"
  on public.profiles for select using (auth.uid() = id);

create policy "Users can read own purchases"
  on public.credit_purchases for select using (auth.uid() = user_id);

create policy "Users can read own usage"
  on public.credit_usage for select using (auth.uid() = user_id);

-- Trigger: auto-create profile on signup
create or replace function public.handle_new_user()
returns trigger as $$
begin
  insert into public.profiles (id, email)
  values (new.id, new.email);
  return new;
end;
$$ language plpgsql security definer;

create trigger on_auth_user_created
  after insert on auth.users
  for each row execute procedure public.handle_new_user();
```

**Step 2: Run in Supabase SQL editor**

Go to your Supabase project → SQL Editor → paste and run.

**Step 3: Verify tables exist**

Check Table Editor — you should see `profiles`, `credit_purchases`, `credit_usage`, `free_searches`.

**Step 4: Commit**

```bash
git add supabase/schema.sql
git commit -m "feat: add Supabase schema for credits, purchases, usage"
```

---

## Task 3: Auth (Email Magic Link + Google)

**Files:**
- Create: `src/lib/supabase.js`
- Create: `src/components/AuthModal.jsx`
- Modify: `src/App.jsx`

**Step 1: Supabase client**

`src/lib/supabase.js`:
```js
import { createClient } from '@supabase/supabase-js'

export const supabase = createClient(
  import.meta.env.VITE_SUPABASE_URL,
  import.meta.env.VITE_SUPABASE_ANON_KEY
)
```

**Step 2: Enable Google OAuth in Supabase**

In Supabase dashboard → Authentication → Providers → Google → enable and add your Google OAuth credentials. (Create credentials at console.cloud.google.com — OAuth 2.0 Client ID, set redirect URI to `https://[your-project].supabase.co/auth/v1/callback`.)

**Step 3: AuthModal component**

`src/components/AuthModal.jsx`:
```jsx
import { useState } from 'react'
import { supabase } from '../lib/supabase'

export default function AuthModal({ onClose }) {
  const [email, setEmail] = useState('')
  const [sent, setSent] = useState(false)
  const [loading, setLoading] = useState(false)

  async function handleMagicLink(e) {
    e.preventDefault()
    setLoading(true)
    const { error } = await supabase.auth.signInWithOtp({ email })
    if (!error) setSent(true)
    setLoading(false)
  }

  async function handleGoogle() {
    await supabase.auth.signInWithOAuth({
      provider: 'google',
      options: { redirectTo: window.location.origin }
    })
  }

  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
      <div className="bg-white rounded-2xl p-8 w-full max-w-sm shadow-xl">
        <h2 className="text-xl font-semibold mb-6">Sign in to use credits</h2>
        {sent ? (
          <p className="text-green-600">Check your email for a magic link.</p>
        ) : (
          <>
            <form onSubmit={handleMagicLink} className="space-y-4">
              <input
                type="email"
                placeholder="your@email.com"
                value={email}
                onChange={e => setEmail(e.target.value)}
                className="w-full border rounded-lg px-4 py-2"
                required
              />
              <button
                type="submit"
                disabled={loading}
                className="w-full bg-slate-900 text-white rounded-lg py-2"
              >
                {loading ? 'Sending...' : 'Send magic link'}
              </button>
            </form>
            <div className="my-4 text-center text-sm text-gray-400">or</div>
            <button
              onClick={handleGoogle}
              className="w-full border rounded-lg py-2 flex items-center justify-center gap-2"
            >
              <img src="https://www.google.com/favicon.ico" className="w-4 h-4" />
              Continue with Google
            </button>
          </>
        )}
        <button onClick={onClose} className="mt-4 text-sm text-gray-400 w-full text-center">
          Cancel
        </button>
      </div>
    </div>
  )
}
```

**Step 4: Wire auth state into App.jsx**

`src/App.jsx`:
```jsx
import { useEffect, useState } from 'react'
import { supabase } from './lib/supabase'
import AuthModal from './components/AuthModal'
import SearchBox from './components/SearchBox'

export default function App() {
  const [session, setSession] = useState(null)
  const [credits, setCredits] = useState(0)
  const [showAuth, setShowAuth] = useState(false)

  useEffect(() => {
    supabase.auth.getSession().then(({ data }) => setSession(data.session))
    supabase.auth.onAuthStateChange((_e, s) => setSession(s))
  }, [])

  useEffect(() => {
    if (!session) return
    supabase
      .from('profiles')
      .select('credits')
      .eq('id', session.user.id)
      .single()
      .then(({ data }) => setCredits(data?.credits ?? 0))
  }, [session])

  return (
    <div className="min-h-screen bg-slate-50">
      <header className="flex justify-between items-center px-6 py-4 bg-white border-b">
        <span className="font-semibold text-slate-800">The Legal Prompts Library</span>
        {session ? (
          <span className="text-sm text-slate-600">{credits} credits</span>
        ) : (
          <button onClick={() => setShowAuth(true)} className="text-sm text-slate-600 underline">
            Sign in
          </button>
        )}
      </header>
      <main className="max-w-2xl mx-auto px-4 py-12">
        <SearchBox session={session} credits={credits} onNeedAuth={() => setShowAuth(true)} />
      </main>
      {showAuth && <AuthModal onClose={() => setShowAuth(false)} />}
    </div>
  )
}
```

**Step 5: Run and verify login flow works**

```bash
npm run dev
```
Expected: sign in with email, receive magic link, session persists on refresh.

**Step 6: Commit**

```bash
git add src/
git commit -m "feat: add auth with email magic link and Google OAuth"
```

---

## Task 4: Prompt Search (Gemini Free Tier)

**Files:**
- Create: `api/search.js` (Vercel serverless function)
- Create: `src/components/SearchBox.jsx`
- Create: `src/lib/promptIndex.js`

**Step 1: Build the prompt index**

`src/lib/promptIndex.js` — a static map of all files to their topics (so Gemini can classify without reading all 45 files):

```js
export const PROMPT_INDEX = [
  { folder: 'quick-start-packs', file: '01_Litigation_Lawyer_Prompts.md', topics: ['litigation', 'court', 'pleadings', 'dispute', 'trial', 'affidavit', 'injunction'] },
  { folder: 'quick-start-packs', file: '02_Corporate_Lawyer_Prompts.md', topics: ['corporate', 'company', 'incorporation', 'shareholders', 'board', 'governance'] },
  { folder: 'quick-start-packs', file: '03_InHouse_Counsel_Prompts.md', topics: ['in-house', 'general counsel', 'legal team', 'legal ops', 'risk', 'vendor'] },
  { folder: 'quick-start-packs', file: '04_Compliance_Privacy_Prompts.md', topics: ['compliance', 'privacy', 'data protection', 'PDPA', 'GDPR', 'AML'] },
  { folder: 'quick-start-packs', file: '05_Shareholder_Disputes_Prompts.md', topics: ['shareholder dispute', 'oppression', 'minority', 'deadlock', 'buyout'] },
  { folder: 'quick-start-packs', file: '06_Singapore_APAC_Supplement.md', topics: ['singapore', 'ROC', 'ACRA', 'MOM', 'HDB', 'MAS'] },
  { folder: 'quick-start-packs', file: '07_Legal_Admin_Prompts.md', topics: ['admin', 'paralegal', 'filing', 'scheduling', 'billing', 'correspondence'] },
  { folder: 'quick-start-packs', file: '08_Copilot_Quick_Reference.md', topics: ['microsoft copilot', 'word', 'outlook', 'teams', 'excel', 'office 365'] },
  { folder: 'quick-start-packs', file: '09_Prompt_Workflows_Chaining.md', topics: ['workflow', 'chain', 'multi-step', 'sequence', 'process'] },
  { folder: 'volume-2-transactional', file: 'V2_01_Contracts_General.md', topics: ['contract', 'review', 'draft', 'negotiate', 'agreement', 'clause'] },
  { folder: 'volume-2-transactional', file: 'V2_02_Contracts_Specific_Types.md', topics: ['NDA', 'SaaS', 'employment contract', 'JV', 'licensing', 'settlement'] },
  { folder: 'volume-2-transactional', file: 'V2_03_Corporate_Governance.md', topics: ['board resolution', 'minutes', 'AGM', 'EGM', 'director', 'constitution'] },
  { folder: 'volume-2-transactional', file: 'V2_04_MA_Transactions.md', topics: ['M&A', 'merger', 'acquisition', 'due diligence', 'SPA', 'completion'] },
  { folder: 'volume-2-transactional', file: 'V2_05_Banking_Finance.md', topics: ['loan', 'finance', 'security', 'guarantee', 'syndicated', 'green bond'] },
  { folder: 'volume-2-transactional', file: 'V2_06_Venture_Capital_Startups.md', topics: ['startup', 'venture capital', 'term sheet', 'SAFE', 'cap table', 'vesting'] },
  { folder: 'volume-3-disputes', file: 'V3_01_Pre_Action.md', topics: ['demand letter', 'pre-action', 'limitation', 'cease and desist', 'warning letter'] },
  { folder: 'volume-3-disputes', file: 'V3_02_Pleadings_Court_Docs.md', topics: ['statement of claim', 'defence', 'counterclaim', 'pleading', 'court document'] },
  { folder: 'volume-3-disputes', file: 'V3_03_Interlocutory_Applications.md', topics: ['injunction', 'summary judgment', 'discovery', 'security for costs'] },
  { folder: 'volume-3-disputes', file: 'V3_04_Evidence_Witnesses.md', topics: ['AEIC', 'affidavit', 'witness', 'expert', 'evidence', 'privilege'] },
  { folder: 'volume-3-disputes', file: 'V3_05_Trial_Hearing.md', topics: ['trial', 'hearing', 'cross-examination', 'opening', 'closing submission', 'costs'] },
  { folder: 'volume-3-disputes', file: 'V3_06_Arbitration_Mediation.md', topics: ['arbitration', 'mediation', 'SIAC', 'ICC', 'dispute resolution', 'award'] },
  { folder: 'volume-3-disputes', file: 'V3_07_Appeals.md', topics: ['appeal', 'notice of appeal', 'appellate', 'leave to appeal'] },
  { folder: 'volume-4-regulatory', file: 'V4_01_Data_Protection_Privacy.md', topics: ['data protection', 'PDPA', 'GDPR', 'privacy', 'data breach', 'DPIA', 'DSAR'] },
  { folder: 'volume-4-regulatory', file: 'V4_02_Financial_Regulation.md', topics: ['MAS', 'financial regulation', 'AML', 'CFT', 'licensing', 'fintech', 'capital markets'] },
  { folder: 'volume-4-regulatory', file: 'V4_03_Competition_Antitrust.md', topics: ['competition', 'antitrust', 'CCCS', 'merger notification', 'cartel', 'dominance'] },
  { folder: 'volume-4-regulatory', file: 'V4_04_Corporate_Compliance.md', topics: ['ABC', 'anti-bribery', 'sanctions', 'ESG', 'whistleblowing', 'modern slavery'] },
  { folder: 'volume-4-regulatory', file: 'V4_05_Regulatory_Investigations.md', topics: ['regulatory investigation', 'dawn raid', 'regulator', 'internal investigation', 'privilege'] },
  { folder: 'volume-5-practice-areas', file: 'V5_01_Employment_Law.md', topics: ['employment', 'termination', 'redundancy', 'retrenchment', 'HR', 'misconduct', 'fire', 'dismiss'] },
  { folder: 'volume-5-practice-areas', file: 'V5_02_Intellectual_Property.md', topics: ['IP', 'patent', 'trademark', 'copyright', 'trade secret', 'IP enforcement'] },
  { folder: 'volume-5-practice-areas', file: 'V5_03_Real_Estate_Property.md', topics: ['property', 'conveyancing', 'lease', 'HDB', 'strata', 'landlord', 'tenant'] },
  { folder: 'volume-5-practice-areas', file: 'V5_04_Family_Law.md', topics: ['divorce', 'custody', 'maintenance', 'prenuptial', 'matrimonial', 'family'] },
  { folder: 'volume-5-practice-areas', file: 'V5_05_Estate_Planning_Probate.md', topics: ['will', 'trust', 'LPA', 'probate', 'estate', 'inheritance'] },
  { folder: 'volume-5-practice-areas', file: 'V5_06_Immigration.md', topics: ['immigration', 'work pass', 'EP', 'PR', 'citizenship', 'ONE Pass', 'MOM'] },
  { folder: 'volume-5-practice-areas', file: 'V5_07_Criminal_Law.md', topics: ['criminal', 'defence', 'bail', 'mitigation', 'sentencing', 'charge'] },
  { folder: 'volume-5-practice-areas', file: 'V5_08_Tax_Law.md', topics: ['tax', 'GST', 'corporate tax', 'transfer pricing', 'IRAS', 'tax dispute'] },
  { folder: 'volume-5-practice-areas', file: 'V5_09_Insurance_Law.md', topics: ['insurance', 'claim', 'policy', 'D&O', 'cyber insurance', 'subrogation'] },
  { folder: 'volume-5-practice-areas', file: 'V5_10_Personal_Injury_Tort.md', topics: ['personal injury', 'negligence', 'motor accident', 'WICA', 'medical negligence', 'quantum'] },
  { folder: 'volume-6-inhouse-legal-ops', file: 'V6_01_InHouse_Counsel.md', topics: ['in-house', 'GC', 'legal counsel', 'risk register', 'board report', 'legal advice'] },
  { folder: 'volume-6-inhouse-legal-ops', file: 'V6_02_Legal_Operations.md', topics: ['legal ops', 'matter management', 'legal spend', 'outside counsel', 'legal technology'] },
  { folder: 'volume-6-inhouse-legal-ops', file: 'V6_03_Legal_Admin_Paralegal.md', topics: ['paralegal', 'legal admin', 'filing', 'diary', 'billing', 'document management'] },
  { folder: 'volume-6-inhouse-legal-ops', file: 'V6_04_Client_Communication.md', topics: ['client letter', 'advice letter', 'status update', 'engagement letter', 'fee dispute'] },
  { folder: 'volume-6-inhouse-legal-ops', file: 'V6_05_Legal_Marketing_BD.md', topics: ['legal marketing', 'pitch', 'thought leadership', 'directory', 'LinkedIn', 'business development'] },
  { folder: 'volume-7-singapore-apac', file: 'V7_01_Singapore_Civil_Procedure.md', topics: ['ROC 2021', 'Singapore court', 'State Courts', 'High Court', 'SICC', 'enforcement'] },
  { folder: 'volume-7-singapore-apac', file: 'V7_02_Singapore_Corporate.md', topics: ['Companies Act', 'ACRA', 'SGX', 'MAS', 'CCCS', 'Singapore corporate'] },
  { folder: 'volume-7-singapore-apac', file: 'V7_03_Singapore_Employment.md', topics: ['Employment Act', 'MOM Singapore', 'CPF', 'TAFEP', 'retrenchment Singapore'] },
  { folder: 'volume-7-singapore-apac', file: 'V7_04_Singapore_Property.md', topics: ['HDB', 'ABSD', 'Singapore property', 'en bloc', 'strata', 'GCB'] },
  { folder: 'volume-7-singapore-apac', file: 'V7_05_Singapore_Regulatory.md', topics: ['PDPC', 'MAS Singapore', 'IMDA', 'MinLaw', 'Legal Profession Act'] },
  { folder: 'volume-7-singapore-apac', file: 'V7_06_ASEAN_Cross_Border.md', topics: ['ASEAN', 'cross-border', 'choice of law', 'FDI', 'cross-border data transfer'] },
  { folder: 'volume-8-ai-practice', file: 'V8_01_Ethics_AI_Best_Practices.md', topics: ['AI ethics', 'hallucination', 'confidentiality AI', 'billing ethics', 'professional conduct AI'] },
  { folder: 'volume-8-ai-practice', file: 'V8_02_AI_Use_Policies.md', topics: ['AI policy', 'firm AI', 'acceptable use', 'AI governance', 'AI risk'] },
  { folder: 'volume-8-ai-practice', file: 'V8_03_AI_Contract_Clauses.md', topics: ['AI clause', 'AI liability', 'AI IP', 'AI vendor', 'AI contract'] },
]
```

**Step 2: Create the search serverless function**

`api/search.js`:
```js
const { GoogleGenerativeAI } = require('@google/generative-ai')

const PROMPT_INDEX = require('../src/lib/promptIndex.js').PROMPT_INDEX
const GITHUB_BASE = process.env.GITHUB_REPO_RAW_BASE

export default async function handler(req, res) {
  if (req.method !== 'POST') return res.status(405).end()

  const { query, ipHash } = await req.json()
  if (!query) return res.status(400).json({ error: 'No query provided' })

  // Rate limit check (5 free searches/day for unauthenticated users)
  // (Full implementation in Task 11)

  // Use Gemini to classify the query against the index
  const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY)
  const model = genAI.getGenerativeModel({ model: 'gemini-2.0-flash' })

  const indexSummary = PROMPT_INDEX.map(p =>
    `${p.folder}/${p.file}: ${p.topics.join(', ')}`
  ).join('\n')

  const classifyPrompt = `
You are a legal AI assistant. A user has described a legal task.
Your job: identify the single best matching file from this index.

User query: "${query}"

Available files and their topics:
${indexSummary}

Reply with ONLY the folder/file path of the best match. Nothing else.
Example reply: volume-3-disputes/V3_01_Pre_Action.md
`

  const result = await model.generateContent(classifyPrompt)
  const matchedPath = result.response.text().trim()

  // Validate the path exists in our index
  const matched = PROMPT_INDEX.find(p => `${p.folder}/${p.file}` === matchedPath)
  if (!matched) return res.status(200).json({ error: 'No match found' })

  // Fetch the file content from GitHub
  const fileUrl = `${GITHUB_BASE}/${matchedPath}`
  const fileRes = await fetch(fileUrl)
  const content = await fileRes.text()

  // Extract the first 3 prompts from the file (simple heuristic: split on **PROMPT)
  const prompts = content.split('**PROMPT').slice(1, 4).map(p => '**PROMPT' + p.trim())

  res.status(200).json({
    file: matchedPath,
    prompts,
    totalInFile: content.split('**PROMPT').length - 1
  })
}
```

**Step 3: Create SearchBox component**

`src/components/SearchBox.jsx`:
```jsx
import { useState } from 'react'

export default function SearchBox({ session, credits, onNeedAuth }) {
  const [query, setQuery] = useState('')
  const [results, setResults] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  async function handleSearch(e) {
    e.preventDefault()
    setLoading(true)
    setError(null)
    const res = await fetch('/api/search', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ query })
    })
    const data = await res.json()
    if (data.error) setError(data.error)
    else setResults(data)
    setLoading(false)
  }

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-bold text-slate-900 mb-2">Find the right legal AI prompt</h1>
        <p className="text-slate-500">Describe what you need to do. We'll find the prompt.</p>
      </div>
      <form onSubmit={handleSearch} className="flex gap-2">
        <input
          value={query}
          onChange={e => setQuery(e.target.value)}
          placeholder="e.g. I need to terminate a contractor who missed deadlines"
          className="flex-1 border rounded-xl px-4 py-3 text-sm shadow-sm"
          required
        />
        <button
          type="submit"
          disabled={loading}
          className="bg-slate-900 text-white px-6 py-3 rounded-xl text-sm"
        >
          {loading ? '...' : 'Search'}
        </button>
      </form>
      {error && <p className="text-red-500 text-sm">{error}</p>}
      {results && (
        <PromptResults
          results={results}
          session={session}
          credits={credits}
          query={query}
          onNeedAuth={onNeedAuth}
        />
      )}
    </div>
  )
}
```

**Step 4: Install Gemini SDK**

```bash
npm install @google/generative-ai
```

**Step 5: Test search locally**

```bash
npm run dev
```
Type "I need to fire an employee" → should return employment law prompts.
Type "I need to send a demand letter" → should return V3_01_Pre_Action.md prompts.

**Step 6: Commit**

```bash
git add src/ api/
git commit -m "feat: add Gemini-powered prompt search"
```

---

## Task 5: Prompt Display UI

**Files:**
- Create: `src/components/PromptResults.jsx`
- Create: `src/components/PromptCard.jsx`

**Step 1: PromptCard component**

`src/components/PromptCard.jsx`:
```jsx
import { useState } from 'react'

export default function PromptCard({ prompt, index, session, credits, query, onNeedAuth, onPersonalise }) {
  const [copied, setCopied] = useState(false)

  function copy() {
    navigator.clipboard.writeText(prompt)
    setCopied(true)
    setTimeout(() => setCopied(false), 2000)
  }

  // Extract title from first line: **PROMPT X — TITLE**
  const titleMatch = prompt.match(/\*\*PROMPT\s+[\w.]+\s+—\s+(.+?)\*\*/)
  const title = titleMatch ? titleMatch[1] : `Prompt ${index + 1}`

  return (
    <div className="border rounded-xl p-5 bg-white shadow-sm space-y-3">
      <h3 className="font-semibold text-slate-800">{title}</h3>
      <pre className="text-sm text-slate-600 whitespace-pre-wrap font-sans bg-slate-50 rounded-lg p-4 max-h-48 overflow-y-auto">
        {prompt}
      </pre>
      <div className="flex gap-2">
        <button
          onClick={copy}
          className="text-sm border rounded-lg px-4 py-2 hover:bg-slate-50"
        >
          {copied ? '✓ Copied' : 'Copy prompt'}
        </button>
        <button
          onClick={() => session ? onPersonalise(prompt) : onNeedAuth()}
          className="text-sm bg-slate-900 text-white rounded-lg px-4 py-2"
        >
          Personalise for my situation — 8 credits
        </button>
      </div>
    </div>
  )
}
```

**Step 2: PromptResults component**

`src/components/PromptResults.jsx`:
```jsx
import PromptCard from './PromptCard'
import PersonaliseModal from './PersonaliseModal'
import { useState } from 'react'

export default function PromptResults({ results, session, credits, query, onNeedAuth }) {
  const [personalising, setPersonalising] = useState(null)

  return (
    <div className="space-y-4">
      <p className="text-sm text-slate-500">
        Found {results.totalInFile} prompts in <code className="bg-slate-100 px-1 rounded">{results.file}</code>.
        Showing top 3:
      </p>
      {results.prompts.map((prompt, i) => (
        <PromptCard
          key={i}
          prompt={prompt}
          index={i}
          session={session}
          credits={credits}
          query={query}
          onNeedAuth={onNeedAuth}
          onPersonalise={(p) => setPersonalising(p)}
        />
      ))}
      {personalising && (
        <PersonaliseModal
          prompt={personalising}
          query={query}
          session={session}
          credits={credits}
          onClose={() => setPersonalising(null)}
        />
      )}
    </div>
  )
}
```

**Step 3: Commit**

```bash
git add src/components/
git commit -m "feat: add prompt display cards with copy and personalise buttons"
```

---

## Task 6: Stripe Credit Purchase

**Files:**
- Create: `api/create-checkout.js`
- Create: `api/stripe-webhook.js`
- Create: `src/components/BuyCreditsModal.jsx`

**Step 1: Define credit packs (shared constant)**

`src/lib/creditPacks.js`:
```js
export const CREDIT_PACKS = [
  { id: 'starter',  name: 'Starter',  price: 500,  credits: 200,  priceDisplay: '$5'  },
  { id: 'standard', name: 'Standard', price: 1500, credits: 700,  priceDisplay: '$15' },
  { id: 'pro',      name: 'Pro',      price: 3000, credits: 1600, priceDisplay: '$30' },
]
// Credits expire 6 months from purchase
export const CREDIT_EXPIRY_MONTHS = 6
```

**Step 2: Stripe checkout session endpoint**

`api/create-checkout.js`:
```js
const Stripe = require('stripe')

export default async function handler(req, res) {
  if (req.method !== 'POST') return res.status(405).end()
  const { packId, userId, userEmail } = await req.json()

  const PACKS = {
    starter:  { price: 500,  name: 'Starter — 200 credits (6 months)' },
    standard: { price: 1500, name: 'Standard — 700 credits (6 months)' },
    pro:      { price: 3000, name: 'Pro — 1,600 credits (6 months)' },
  }

  const pack = PACKS[packId]
  if (!pack) return res.status(400).json({ error: 'Invalid pack' })

  const stripe = new Stripe(process.env.STRIPE_SECRET_KEY)
  const session = await stripe.checkout.sessions.create({
    payment_method_types: ['card'],
    line_items: [{
      price_data: {
        currency: 'usd',
        product_data: { name: pack.name },
        unit_amount: pack.price,
      },
      quantity: 1,
    }],
    mode: 'payment',
    success_url: `${process.env.APP_URL}?payment=success`,
    cancel_url: `${process.env.APP_URL}?payment=cancelled`,
    metadata: { userId, packId },
    customer_email: userEmail,
  })

  res.status(200).json({ url: session.url })
}
```

**Step 3: Stripe webhook to credit user on payment**

`api/stripe-webhook.js`:
```js
const Stripe = require('stripe')
const { createClient } = require('@supabase/supabase-js')

const CREDITS_BY_PACK = { starter: 200, standard: 700, pro: 1600 }

export default async function handler(req, res) {
  const stripe = new Stripe(process.env.STRIPE_SECRET_KEY)
  const sig = req.headers['stripe-signature']
  let event

  try {
    event = stripe.webhooks.constructEvent(
      await req.text(), sig, process.env.STRIPE_WEBHOOK_SECRET
    )
  } catch (err) {
    return res.status(400).send(`Webhook error: ${err.message}`)
  }

  if (event.type === 'checkout.session.completed') {
    const session = event.data.object
    const { userId, packId } = session.metadata
    const credits = CREDITS_BY_PACK[packId]
    const expiresAt = new Date()
    expiresAt.setMonth(expiresAt.getMonth() + 6)

    const supabase = createClient(
      process.env.SUPABASE_URL,
      process.env.SUPABASE_SERVICE_ROLE_KEY
    )

    // Add credits to profile
    await supabase.rpc('add_credits', { user_id: userId, amount: credits })

    // Log the purchase
    await supabase.from('credit_purchases').insert({
      user_id: userId,
      stripe_payment_intent: session.payment_intent,
      pack_name: packId,
      credits_added: credits,
      amount_paid: session.amount_total,
      expires_at: expiresAt.toISOString(),
    })
  }

  res.status(200).json({ received: true })
}
```

**Step 4: Add `add_credits` RPC function in Supabase SQL editor**

```sql
create or replace function add_credits(user_id uuid, amount integer)
returns void as $$
  update public.profiles set credits = credits + amount where id = user_id;
$$ language sql security definer;
```

**Step 5: BuyCreditsModal component**

`src/components/BuyCreditsModal.jsx`:
```jsx
import { CREDIT_PACKS } from '../lib/creditPacks'

export default function BuyCreditsModal({ session, onClose }) {
  async function handleBuy(packId) {
    const res = await fetch('/api/create-checkout', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        packId,
        userId: session.user.id,
        userEmail: session.user.email
      })
    })
    const { url } = await res.json()
    window.location.href = url
  }

  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
      <div className="bg-white rounded-2xl p-8 w-full max-w-md shadow-xl space-y-4">
        <h2 className="text-xl font-semibold">Buy Credits</h2>
        <p className="text-sm text-slate-500">Credits expire 6 months from purchase.</p>
        {CREDIT_PACKS.map(pack => (
          <button
            key={pack.id}
            onClick={() => handleBuy(pack.id)}
            className="w-full flex justify-between items-center border rounded-xl px-5 py-4 hover:bg-slate-50"
          >
            <div className="text-left">
              <div className="font-semibold">{pack.name}</div>
              <div className="text-sm text-slate-500">{pack.credits} credits</div>
            </div>
            <div className="font-bold text-slate-900">{pack.priceDisplay}</div>
          </button>
        ))}
        <button onClick={onClose} className="text-sm text-slate-400 w-full text-center">Cancel</button>
      </div>
    </div>
  )
}
```

**Step 6: Install Stripe**

```bash
npm install stripe @stripe/stripe-js
```

**Step 7: Test with Stripe test mode**

Use Stripe test card `4242 4242 4242 4242`, expiry any future date, CVC any 3 digits. Verify credits appear in Supabase `profiles` table after payment.

**Step 8: Commit**

```bash
git add api/ src/
git commit -m "feat: add Stripe credit purchase with webhook"
```

---

## Task 7 + 8: Personalisation Engine + Follow-up Chain

**Files:**
- Create: `api/personalise.js`
- Create: `src/components/PersonaliseModal.jsx`

**Step 1: Personalisation serverless function**

`api/personalise.js`:
```js
const { GoogleGenerativeAI } = require('@google/generative-ai')
const { createClient } = require('@supabase/supabase-js')

const CREDIT_COST = 8

export default async function handler(req, res) {
  if (req.method !== 'POST') return res.status(405).end()
  const { basePrompt, userContext, userId } = await req.json()

  const supabase = createClient(
    process.env.SUPABASE_URL,
    process.env.SUPABASE_SERVICE_ROLE_KEY
  )

  // Check credits
  const { data: profile } = await supabase
    .from('profiles')
    .select('credits')
    .eq('id', userId)
    .single()

  if (!profile || profile.credits < CREDIT_COST) {
    return res.status(402).json({ error: 'Insufficient credits' })
  }

  // Check for expired credits
  const { data: purchases } = await supabase
    .from('credit_purchases')
    .select('expires_at')
    .eq('user_id', userId)
    .order('expires_at', { ascending: false })
    .limit(1)

  if (purchases?.length && new Date(purchases[0].expires_at) < new Date()) {
    return res.status(402).json({ error: 'Your credits have expired. Please purchase a new pack.' })
  }

  const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY)
  const model = genAI.getGenerativeModel({ model: 'gemini-2.0-flash' })

  const personalisePrompt = `
You are a legal prompt engineer. Rewrite the following base legal AI prompt so it is personalised to the user's specific situation described below.

BASE PROMPT:
${basePrompt}

USER'S SITUATION:
${userContext}

Instructions:
1. Keep the same structure and professional tone as the base prompt.
2. Insert the user's specific details (jurisdiction, parties, facts, context) into the appropriate placeholders.
3. Remove any [BRACKETED PLACEHOLDERS] that are now filled in.
4. Then write exactly 3 follow-up prompts the user should run AFTER this one, labelled FOLLOW-UP 1, FOLLOW-UP 2, FOLLOW-UP 3.
5. Keep all disclaimers about AI not being legal advice.

Format:
---PERSONALISED PROMPT---
[the rewritten prompt]

---FOLLOW-UP PROMPTS---
FOLLOW-UP 1: [title]
[prompt text]

FOLLOW-UP 2: [title]
[prompt text]

FOLLOW-UP 3: [title]
[prompt text]
`

  const result = await model.generateContent(personalisePrompt)
  const output = result.response.text()

  // Deduct credits
  await supabase.rpc('deduct_credits', { user_id: userId, amount: CREDIT_COST })

  // Log usage
  await supabase.from('credit_usage').insert({
    user_id: userId,
    action: 'personalise+chain',
    credits_used: CREDIT_COST,
  })

  res.status(200).json({ output })
}
```

**Step 2: Add `deduct_credits` RPC in Supabase**

```sql
create or replace function deduct_credits(user_id uuid, amount integer)
returns void as $$
  update public.profiles set credits = credits - amount where id = user_id;
$$ language sql security definer;
```

**Step 3: PersonaliseModal component**

`src/components/PersonaliseModal.jsx`:
```jsx
import { useState } from 'react'

export default function PersonaliseModal({ prompt, query, session, credits, onClose }) {
  const [context, setContext] = useState(query)
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)
  const [copied, setCopied] = useState(false)

  async function handlePersonalise() {
    setLoading(true)
    setError(null)
    const res = await fetch('/api/personalise', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        basePrompt: prompt,
        userContext: context,
        userId: session.user.id,
      })
    })
    const data = await res.json()
    if (data.error) setError(data.error)
    else setResult(data.output)
    setLoading(false)
  }

  function copy(text) {
    navigator.clipboard.writeText(text)
    setCopied(true)
    setTimeout(() => setCopied(false), 2000)
  }

  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4">
      <div className="bg-white rounded-2xl p-6 w-full max-w-2xl shadow-xl space-y-4 max-h-[90vh] overflow-y-auto">
        <h2 className="text-xl font-semibold">Personalise this prompt</h2>
        <p className="text-sm text-slate-500">Costs 8 credits. You have {credits} credits.</p>
        {!result ? (
          <>
            <label className="block text-sm font-medium text-slate-700">
              Describe your specific situation in detail
            </label>
            <textarea
              value={context}
              onChange={e => setContext(e.target.value)}
              rows={5}
              className="w-full border rounded-xl px-4 py-3 text-sm"
              placeholder="e.g. I'm a Singapore company, terminating a full-time employee for gross misconduct after a 3-month performance improvement plan failed. The employee has been with us for 4 years..."
            />
            {error && <p className="text-red-500 text-sm">{error}</p>}
            <div className="flex gap-2">
              <button
                onClick={handlePersonalise}
                disabled={loading}
                className="bg-slate-900 text-white rounded-xl px-6 py-2 text-sm"
              >
                {loading ? 'Personalising...' : 'Personalise (8 credits)'}
              </button>
              <button onClick={onClose} className="text-sm text-slate-400 px-4">Cancel</button>
            </div>
          </>
        ) : (
          <>
            <pre className="text-sm bg-slate-50 rounded-xl p-4 whitespace-pre-wrap font-sans max-h-96 overflow-y-auto">
              {result}
            </pre>
            <div className="flex gap-2">
              <button
                onClick={() => copy(result)}
                className="border rounded-xl px-5 py-2 text-sm hover:bg-slate-50"
              >
                {copied ? '✓ Copied' : 'Copy all'}
              </button>
              <button onClick={onClose} className="text-sm text-slate-400 px-4">Close</button>
            </div>
          </>
        )}
      </div>
    </div>
  )
}
```

**Step 4: Commit**

```bash
git add api/personalise.js src/components/PersonaliseModal.jsx
git commit -m "feat: add personalisation engine with follow-up chain"
```

---

## Task 9: Credit Expiry Enforcement

**Files:**
- Modify: `api/personalise.js` (already handles this — see Task 7)
- Create: `supabase/credit-expiry-check.sql`

**Step 1: Add database-level expiry view**

```sql
-- View: user's active (non-expired) credits
create or replace view public.active_credits as
select
  p.id as user_id,
  p.credits,
  max(cp.expires_at) as latest_expiry
from public.profiles p
left join public.credit_purchases cp on cp.user_id = p.id
group by p.id, p.credits;
```

**Step 2: Add expiry warning to frontend**

In `App.jsx`, after fetching credits, also check expiry date and show a banner if credits expire within 30 days:

```jsx
// Add to the useEffect that fetches credits:
const { data: purchases } = await supabase
  .from('credit_purchases')
  .select('expires_at')
  .eq('user_id', session.user.id)
  .order('expires_at', { ascending: false })
  .limit(1)

if (purchases?.length) {
  const expiry = new Date(purchases[0].expires_at)
  const daysLeft = Math.ceil((expiry - new Date()) / (1000 * 60 * 60 * 24))
  if (daysLeft < 30) setExpiryWarning(`Your credits expire in ${daysLeft} days.`)
}
```

**Step 3: Commit**

```bash
git add supabase/ src/
git commit -m "feat: credit expiry enforcement and warning"
```

---

## Task 10: Terms of Service + ToS Gate

**Files:**
- Create: `src/pages/Terms.jsx`
- Create: `supabase/tos-migration.sql`
- Modify: `src/App.jsx` (ToS acceptance gate)

**Step 1: Add `tos_accepted_at` to profiles**

```sql
alter table public.profiles add column tos_accepted_at timestamptz;
```

**Step 2: Terms page** (key clauses to include — write full prose in the actual page):

`src/pages/Terms.jsx` — must include:
- Service is provided as-is, no uptime guarantee
- We may shut down the service with **60 days' written notice** by email
- We may adjust credit costs (how many credits per action) with **30 days' notice** if API costs increase materially
- Unused credits at shutdown will be refunded pro-rata
- Credits expire 6 months from purchase date, no exceptions
- We may suspend accounts for misuse without refund
- These prompts are not legal advice
- Governing law: Singapore
- Any disputes: Singapore courts

**Step 3: ToS acceptance gate in App.jsx**

After login, check `tos_accepted_at`. If null, show ToS modal before anything else:

```jsx
// In App.jsx, after session is loaded:
if (session && !profile?.tos_accepted_at) {
  return <TosGate onAccept={handleAcceptTos} />
}

async function handleAcceptTos() {
  await supabase
    .from('profiles')
    .update({ tos_accepted_at: new Date().toISOString() })
    .eq('id', session.user.id)
  setProfile(prev => ({ ...prev, tos_accepted_at: new Date().toISOString() }))
}
```

**Step 4: Commit**

```bash
git add src/ supabase/
git commit -m "feat: terms of service page and acceptance gate"
```

---

## Task 11: Rate Limiting (Free Tier)

**Files:**
- Modify: `api/search.js`

**Step 1: Add rate limit check to search function**

In `api/search.js`, before the Gemini call:

```js
// Hash the IP (don't store raw IPs)
const ip = req.headers['x-forwarded-for'] || 'unknown'
const ipHash = await crypto.subtle.digest(
  'SHA-256', new TextEncoder().encode(ip)
).then(buf => Array.from(new Uint8Array(buf)).map(b => b.toString(16).padStart(2, '0')).join(''))

const supabase = createClient(process.env.SUPABASE_URL, process.env.SUPABASE_SERVICE_ROLE_KEY)
const today = new Date().toISOString().split('T')[0]

const { data: rateRow } = await supabase
  .from('free_searches')
  .select('*')
  .eq('ip_hash', ipHash)
  .single()

if (rateRow && rateRow.reset_date === today && rateRow.search_count >= 5) {
  return res.status(429).json({
    error: 'You have used your 5 free searches for today. Sign in and buy credits to continue.'
  })
}

// Upsert the count
await supabase.from('free_searches').upsert({
  ip_hash: ipHash,
  search_count: rateRow?.reset_date === today ? (rateRow.search_count + 1) : 1,
  reset_date: today
})
```

**Step 2: Commit**

```bash
git add api/search.js
git commit -m "feat: rate limit free searches to 5/day per IP"
```

---

## Task 12: Deploy to Vercel

**Files:**
- Create: `vercel.json`

**Step 1: Create vercel.json**

```json
{
  "functions": {
    "api/*.js": {
      "runtime": "nodejs20.x"
    }
  },
  "rewrites": [
    { "source": "/((?!api/).*)", "destination": "/index.html" }
  ]
}
```

**Step 2: Install Vercel CLI and deploy**

```bash
npm install -g vercel
vercel
```

Follow the prompts. When asked about environment variables, add all values from `.env.local`.

**Step 3: Add environment variables in Vercel dashboard**

Go to Project Settings → Environment Variables. Add:
- `GEMINI_API_KEY`
- `STRIPE_SECRET_KEY`
- `STRIPE_WEBHOOK_SECRET`
- `SUPABASE_URL`
- `SUPABASE_SERVICE_ROLE_KEY`
- `APP_URL` (your Vercel deployment URL)
- `GITHUB_REPO_RAW_BASE`

**Step 4: Set up Stripe webhook**

In Stripe dashboard → Webhooks → Add endpoint → your Vercel URL + `/api/stripe-webhook`.
Events to listen for: `checkout.session.completed`.
Copy the webhook signing secret → add to Vercel env as `STRIPE_WEBHOOK_SECRET`.

**Step 5: Update Supabase Auth redirect URLs**

In Supabase → Authentication → URL Configuration:
- Site URL: your Vercel URL
- Redirect URLs: `https://your-app.vercel.app/**`

**Step 6: Final smoke test**

1. Visit the live URL
2. Search for a prompt (free, no login)
3. Hit the 5-search limit
4. Sign in via Google
5. Buy the Starter pack ($5 test card)
6. Verify 200 credits appear
7. Personalise a prompt — verify 8 credits deducted
8. Accept ToS on first login

**Step 7: Commit + tag release**

```bash
git add vercel.json
git commit -m "feat: add Vercel deployment config"
git tag v1.0.0
git push origin main --tags
```

---

## Summary

| What | Detail |
|---|---|
| Free tier | 5 searches/day, IP-limited, Gemini Flash |
| Paid tiers | Starter $5 / Standard $15 / Pro $30 |
| Credits | 200 / 700 / 1,600 |
| Expiry | 6 months from purchase |
| Personalisation cost | 8 credits |
| Your API cost per use | ~$0.003 (Gemini Flash) |
| Revenue per 8-credit use | ~$0.09 (at Starter pricing) |
| Margin | ~30x (well above 3x target) |
| Shutdown protection | 60-day notice in ToS; 30-day notice for credit adjustments |
| Stack | React + Vite, Vercel, Supabase, Stripe, Gemini |

---

*Plan complete. No ChatGPT. No OpenAI. Gemini only for AI calls.*
