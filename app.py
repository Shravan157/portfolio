from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components
import json

BASE_DIR = Path(__file__).parent
RESUME_PATH = BASE_DIR / "assets" / "shravan_resume.pdf"

st.set_page_config(
    page_title="Shravan Parthe",
    page_icon="SP",
    layout="wide",
    initial_sidebar_state="collapsed",
)

CASES = [
    {
        "id": "01", "domain": "FINTECH", "name": "SAHAY",
        "verdict": "Micro-credit underwriting for borrowers who shouldn't need to understand banking software.",
        "signal": "RF credit scoring · 76% accuracy · 19 features · 3-role loan state machine · Aadhaar + PAN OCR",
        "stack": ["FastAPI", "Flutter", "Firebase", "Scikit-learn", "Tesseract OCR", "Stripe"],
        "role": "Full-stack backend + ML", "repo": "https://github.com/Shravan157/Sahay-Loan", "accent": "#b75533",
        "problem": "Small borrowers lose time and confidence when loan systems assume paperwork, branch visits, and manual screening. The product needed to treat credit, identity, repayment, and provider review as one workflow instead of disconnected screens.",
        "decision": "Flutter for the mobile-first client — one codebase for phone and web demos. FastAPI for the decision-heavy backend because Python made ML, OCR, and payment services easier to compose. Firebase Auth + Firestore gave real-time status updates without a separate auth stack. Random Forest for scoring because explainability mattered more than chasing a black-box model.",
        "challenge": "Making the loan state machine honest. KYC extraction, model scoring, admin review, provider decisions, repayment schedules, and notifications all had to agree on the same borrower state. A single inconsistency breaks trust in a credit product.",
        "outcome": "Three-role lending platform. A borrower applies up to ₹1,00,000, completes Aadhaar and PAN extraction through OCR, and moves through approval and EMI repayment without manual KYC entry.",
        "differently": "Stronger audit trail for every model-assisted credit decision. Separate risk-service versioning from the main API. Build a fairness report before calling the model production-ready.",
    },
    {
        "id": "02", "domain": "EDTECH", "name": "SikshaSetu",
        "verdict": "A college portal that combines academic ops, live classes, and RAG-backed help in one role-aware system.",
        "signal": "RBAC across 3 roles · 10+ relational tables · virtual classroom · notes RAG via Qdrant",
        "stack": ["Spring Boot", "JWT", "React", "MySQL", "LangChain4j", "Qdrant", "ZEGOCLOUD"],
        "role": "Java backend + AI/RAG", "repo": "https://github.com/Shravan157/sikshasetu", "accent": "#315b78",
        "problem": "Most college systems split academic work into separate tools — attendance somewhere, notes elsewhere, video links in chat. SikshaSetu needed to feel like one operating system for a college, especially where admin capacity is thin.",
        "decision": "Spring Boot for permission-heavy domain work — typed services, layered controllers, DTOs, predictable security filters. JWT for a stateless React client. MySQL fit the academic schema. LangChain4j + Qdrant so uploaded notes became searchable context instead of generic chatbot answers.",
        "challenge": "Permission design for the AI layer. A student asking about portal navigation is harmless. A student asking for all users or faculty lists is not. The assistant had to be useful while respecting the same role boundaries as the normal APIs.",
        "outcome": "Role dashboards, attendance, timetable, assignments, notes, results, events, notifications, streaming AI responses, document insight chat, Qdrant-backed RAG, and live virtual classrooms — all in one system.",
        "differently": "Split AI tooling into a separate service boundary. Add background indexing jobs for notes instead of request-time indexing. Define richer integration tests around role leakage.",
    },
    {
        "id": "03", "domain": "FINTECH DATA", "name": "PhonePe Insights",
        "verdict": "A public fintech data pipeline that turns raw transaction files into a queryable regional dashboard.",
        "signal": "50K+ records · 36 states · 9 raw datasets → 5 relational tables · 10+ interactive charts",
        "stack": ["Python", "Pandas", "MySQL", "SQLAlchemy", "Streamlit", "Plotly"],
        "role": "Data engineering + dashboard", "repo": "https://github.com/Shravan157/phonepe-insights", "accent": "#b88a2f",
        "problem": "The PhonePe dataset is valuable, but raw transaction files don't explain regional behaviour by themselves. The dashboard needed to answer: where volume is moving, which categories dominate, and how state-level adoption changes over time.",
        "decision": "Pandas for transformation — source files needed cleaning before SQL. MySQL gave a durable analytical layer. SQLAlchemy + PyMySQL kept queries parameterised. Streamlit + Plotly made exploration fast enough for a reviewer to use without setup friction.",
        "challenge": "Data shape. Transaction, user, and geography files carried related but differently structured information. The value came from normalising them into tables that made filters and joins predictable.",
        "outcome": "Ad-hoc analysis collapsed into a dashboard path: choose state, year, quarter, category — then inspect transaction trends, regional distribution, and payment behaviour visually.",
        "differently": "A reproducible data validation layer. Cache expensive dashboard queries. Define dbt-style transformation checks before loading data into MySQL.",
    },
    {
        "id": "04", "domain": "HEALTHTECH", "name": "MedoraX",
        "verdict": "A multilingual clinical assistant that accepts voice, image, and text while staying below the line of medical authority.",
        "signal": "English + Hindi + Marathi · voice, image, text · hospital search · AQI context · TTS output",
        "stack": ["Python", "Gradio", "Groq Whisper", "Llama", "Google Maps API", "Edge TTS"],
        "role": "AI pipeline + product workflow", "repo": "https://github.com/Shravan157/MedX-AI-Clinical-Assistant", "accent": "#637d69",
        "problem": "Healthcare discovery breaks down when the user can't type symptoms comfortably, can't explain an image, or needs help in a local language. MedoraX is a triage assistant — not a doctor replacement.",
        "decision": "Gradio for the demo surface — multimodal inputs are easier to ship there than in a heavier frontend. Groq Whisper for speech-to-text. Llama models for structured medical responses and image reasoning. Google Maps closes the loop when the answer should be: find care near you now.",
        "challenge": "Orchestration. Voice, image, text, map lookup, AQI, emergency keywords, and TTS all have different latency and failure modes. The app needed to keep the user moving even when one external service was slow.",
        "outcome": "Full GenAI care-assistance pipeline with multilingual interaction, hospital discovery, and audio feedback for users who aren't comfortable with English-only interfaces.",
        "differently": "Stronger clinical guardrails. Source-grounded medical retrieval. Offline fallback language packs. Red-team tests for unsafe medical advice.",
    },
    {
        "id": "05", "domain": "ENV DATA", "name": "Bird Observation",
        "verdict": "A conservation-data dashboard comparing forest and grassland observation patterns.",
        "signal": "Forest + grassland datasets · temporal, spatial, species-diversity, and environmental analysis",
        "stack": ["Python", "Pandas", "NumPy", "SQLite", "Plotly", "Streamlit"],
        "role": "Data cleaning + SQLite + dashboarding", "repo": "https://github.com/Shravan157/bird_project", "accent": "#4a7c59",
        "problem": "Observation datasets are easy to collect and hard to reason about. The goal was to compare habitat patterns without forcing the viewer to inspect spreadsheets.",
        "decision": "Pandas + NumPy for cleaning. SQLite to keep analysis lightweight and portable. Plotly + Streamlit for interactive filters across habitat, time, species, and environmental conditions.",
        "challenge": "Making two ecosystem datasets comparable. Forest and grassland observations need shared fields, consistent cleaning, and clear filters before the dashboard can say anything meaningful.",
        "outcome": "Raw observation files become conservation-oriented views across time, geography, species diversity, and environmental conditions.",
        "differently": "Data provenance notes. Automated schema checks for incoming Excel files. More explicit statistical confidence around conservation conclusions.",
    },
]

NOTES = [
    {"label": "RAG", "text": "Moving from loaders and splitters into retrieval quality — chunk size, metadata design, vector store choice, and when an agent should call a backend tool instead of answering from memory."},
    {"label": "SYSTEMS", "text": "The next version of my work needs more background jobs, logs, test fixtures, model decision records, and deployment notes. The product idea is only half the work."},
    {"label": "STACK", "text": "Spring Boot gives me discipline for business systems. Python gives me speed for AI and data workflows. The interesting part is designing the boundary between them."},
]

# Hide all streamlit chrome
st.markdown("""
<style>
#root > div:nth-child(1) > div > div > div > div > section > div {padding: 0 !important;}
[data-testid="stHeader"],[data-testid="stToolbar"],[data-testid="stDecoration"],
footer,.css-18e3th9,.css-1d391kg {display:none !important;}
.main .block-container {padding:0 !important; max-width:100% !important;}
iframe {display:block;}
</style>
""", unsafe_allow_html=True)

cases_json = json.dumps(CASES)
notes_json = json.dumps(NOTES)

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0;}}
:root{{
  --bg:#0c0d0c;--surf:#111311;--surf2:#171a17;
  --b1:rgba(255,255,255,0.06);--b2:rgba(255,255,255,0.12);
  --ink:#e4e8e2;--muted:#6e7a6c;--dim:#3e4a3c;
  --teal:#4ecba0;--indigo:#7b9fd4;
  --mono:'JetBrains Mono',monospace;--sans:'Inter',sans-serif;
}}
html,body{{background:var(--bg);color:var(--ink);font-family:var(--mono);height:100%;overflow-x:hidden;}}

/* sidebar */
.sidebar{{
  position:fixed;left:0;top:0;bottom:0;width:42px;
  background:var(--surf);border-right:1px solid var(--b1);
  display:flex;flex-direction:column;align-items:center;
  padding:1.2rem 0 1.6rem;z-index:100;
}}
.stamp{{
  writing-mode:vertical-rl;transform:rotate(180deg);
  font-size:8.5px;letter-spacing:0.22em;text-transform:uppercase;
  color:var(--dim);margin-bottom:auto;padding-top:0.4rem;
}}
.stamp b{{color:var(--muted);font-weight:400;}}
.icons{{display:flex;flex-direction:column;align-items:center;gap:1.2rem;}}
.ic-wrap{{position:relative;display:flex;align-items:center;}}
.ic{{
  width:26px;height:26px;display:flex;align-items:center;justify-content:center;
  color:var(--dim);text-decoration:none;font-size:9px;font-weight:700;
  letter-spacing:0.05em;transition:color 0.15s;
}}
.ic:hover{{color:var(--teal);}}
.tip{{
  position:absolute;left:36px;
  background:var(--surf2);border:1px solid var(--b2);
  color:var(--ink);font-size:9.5px;letter-spacing:0.1em;
  text-transform:uppercase;padding:3px 9px;
  white-space:nowrap;pointer-events:none;
  opacity:0;transition:opacity 0.15s;z-index:200;
}}
.ic-wrap:hover .tip{{opacity:1;}}

/* main */
.main{{margin-left:42px;display:flex;flex-direction:column;min-height:100vh;}}

/* masthead */
.mast{{
  display:flex;justify-content:space-between;align-items:center;
  padding:0.75rem 1.6rem;border-bottom:1px solid var(--b1);
  background:var(--surf);flex-shrink:0;gap:1rem;
}}
.mast-l{{font-size:9.5px;letter-spacing:0.18em;text-transform:uppercase;color:var(--muted);}}
.mast-l b{{color:var(--ink);font-weight:500;}}
.mast-r{{font-size:9px;letter-spacing:0.1em;color:var(--dim);text-align:right;}}

/* board */
.board{{padding:1.2rem 1.4rem 0;}}
.grid{{display:grid;grid-template-columns:2fr 1fr 1fr;gap:7px;}}
.col{{display:flex;flex-direction:column;gap:7px;}}

/* case file */
.file{{
  background:var(--surf);border:1px solid var(--b1);
  padding:1rem 1.1rem 0.95rem;position:relative;
  overflow:hidden;cursor:pointer;
  transition:border-color 0.18s,background 0.18s;
}}
.file:hover{{border-color:var(--b2);background:var(--surf2);}}
.file.open{{border-color:var(--b2);background:var(--surf2);}}
.file.feat{{cursor:default;}}
.tbar{{position:absolute;top:0;left:0;right:0;height:2px;transition:height 0.18s;}}
.file:hover .tbar,.file.open .tbar{{height:3px;}}

.cid{{display:flex;justify-content:space-between;align-items:center;margin-bottom:0.65rem;gap:0.5rem;}}
.cid-l{{display:flex;align-items:center;gap:6px;font-size:9px;letter-spacing:0.2em;text-transform:uppercase;color:var(--dim);}}
.dot{{width:5px;height:5px;border-radius:50%;flex-shrink:0;}}
.badge{{font-size:8.5px;letter-spacing:0.14em;text-transform:uppercase;color:var(--dim);border:1px solid var(--b1);padding:2px 5px;flex-shrink:0;}}
.badge.on{{color:var(--teal);border-color:rgba(78,203,160,0.22);}}

.verdict{{font-size:14px;font-weight:500;color:var(--ink);line-height:1.35;margin-bottom:0.45rem;font-family:var(--sans);}}
.file.feat .verdict{{font-size:17px;line-height:1.22;margin-bottom:0.75rem;}}
.sig{{font-size:11px;line-height:1.7;color:var(--muted);}}

.chips{{display:flex;flex-wrap:wrap;gap:4px;margin-top:0.8rem;}}
.chip{{font-size:9px;letter-spacing:0.05em;border:1px solid var(--b1);padding:2px 7px;color:var(--dim);transition:color 0.15s,border-color 0.15s;}}
.file:hover .chip,.file.open .chip{{color:var(--muted);border-color:var(--b2);}}

.cfoot{{margin-top:0.9rem;padding-top:0.7rem;border-top:1px solid var(--b1);display:flex;justify-content:space-between;align-items:center;}}
.crole{{font-size:9px;text-transform:uppercase;letter-spacing:0.13em;color:var(--dim);}}
.arr{{font-size:12px;color:var(--dim);transition:color 0.15s,transform 0.15s;}}
.file:hover .arr,.file.open .arr{{color:var(--teal);}}
.file.open .arr{{transform:rotate(90deg);}}

/* detail */
.detail{{
  margin:7px 1.4rem 0;background:var(--surf);
  border:1px solid var(--b2);position:relative;overflow:hidden;
  display:none;
}}
.detail.show{{display:block;}}
.dtbar{{height:2px;}}
.din{{padding:1.5rem 1.8rem 1.7rem;}}
.dhead{{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:1.3rem;padding-bottom:0.9rem;border-bottom:1px solid var(--b1);gap:1rem;}}
.dname{{font-size:20px;font-weight:500;color:var(--ink);font-family:var(--sans);line-height:1;}}
.dmeta{{font-size:9px;letter-spacing:0.14em;text-transform:uppercase;color:var(--dim);margin-top:0.35rem;}}
.drepo a{{
  font-size:9.5px;letter-spacing:0.13em;text-transform:uppercase;
  color:var(--indigo);text-decoration:none;
  border:1px solid rgba(123,159,212,0.22);padding:5px 11px;
  transition:border-color 0.15s;display:inline-block;white-space:nowrap;
}}
.drepo a:hover{{border-color:rgba(123,159,212,0.55);}}
.dgrid{{display:grid;grid-template-columns:1fr 1fr;}}
.dblock{{padding:1rem 1.3rem 1rem 0;border-bottom:1px solid var(--b1);}}
.dblock:nth-child(even){{padding-left:1.3rem;padding-right:0;border-left:1px solid var(--b1);}}
.dblock.full{{grid-column:1/-1;padding-right:0;border-left:none;}}
.dblock:nth-last-child(-n+2){{border-bottom:none;}}
.dblock.full:last-child{{border-bottom:none;}}
.dlabel{{font-size:8.5px;letter-spacing:0.22em;text-transform:uppercase;color:var(--dim);margin-bottom:0.4rem;}}
.dtext{{font-size:12px;line-height:1.8;color:var(--muted);font-family:var(--sans);}}

/* notes */
.notes{{display:grid;grid-template-columns:repeat(3,1fr);gap:7px;margin:7px 1.4rem 0;}}
.note{{background:var(--surf);border:1px solid var(--b1);padding:0.9rem 1rem;position:relative;}}
.note::after{{content:'';position:absolute;bottom:0;left:0;right:0;height:1px;background:linear-gradient(90deg,rgba(201,162,74,0.35),transparent 55%);}}
.nlabel{{font-size:8.5px;letter-spacing:0.22em;text-transform:uppercase;color:rgba(201,162,74,0.65);margin-bottom:0.45rem;}}
.ntext{{font-size:11px;line-height:1.78;color:var(--muted);font-family:var(--sans);}}

/* footer */
.foot{{
  margin:7px 1.4rem 1.8rem;border:1px solid var(--b1);
  background:var(--surf);padding:0.9rem 1.3rem;
  display:flex;justify-content:space-between;align-items:center;gap:1rem;
}}
.fl{{font-size:9px;letter-spacing:0.13em;color:var(--dim);text-transform:uppercase;}}
.fl b{{color:var(--muted);font-weight:400;}}
.fr{{font-size:9.5px;letter-spacing:0.09em;color:var(--dim);}}
</style>
</head>
<body>

<div class="sidebar">
  <div class="stamp"><b>Shravan Parthe</b> · backend + ai</div>
  <div class="icons">
    <div class="ic-wrap">
      <a class="ic" href="https://github.com/Shravan157" target="_blank">GH</a>
      <div class="tip">github</div>
    </div>
    <div class="ic-wrap">
      <a class="ic" href="https://www.linkedin.com/in/shravan-parthe-00946b2ab/" target="_blank">IN</a>
      <div class="tip">linkedin</div>
    </div>
    <div class="ic-wrap">
      <a class="ic" href="mailto:shravanparthe@gmail.com?subject=Role" target="_blank">@</a>
      <div class="tip">email</div>
    </div>
    <div class="ic-wrap">
      <a class="ic" href="mailto:shravanparthe@gmail.com?subject=Collaboration" target="_blank">✉</a>
      <div class="tip">collaborate</div>
    </div>
  </div>
</div>

<div class="main">
  <div class="mast">
    <div class="mast-l"><b>Field journal</b> · AI backend engineering · Mumbai, India</div>
    <div class="mast-r">5 case files · B.Tech AI/ML · ViMEET · Intern @ Innovexis</div>
  </div>

  <div class="board">
    <div class="grid" id="grid"></div>
  </div>

  <div class="detail" id="detail">
    <div class="dtbar" id="dtbar"></div>
    <div class="din">
      <div class="dhead">
        <div>
          <div class="dname" id="d-name"></div>
          <div class="dmeta" id="d-meta"></div>
        </div>
        <div class="drepo"><a id="d-repo" href="#" target="_blank">Open repository ↗</a></div>
      </div>
      <div class="dgrid">
        <div class="dblock"><div class="dlabel">Problem I was actually solving</div><div class="dtext" id="d-prob"></div></div>
        <div class="dblock"><div class="dlabel">Engineering decision</div><div class="dtext" id="d-dec"></div></div>
        <div class="dblock"><div class="dlabel">Core technical challenge</div><div class="dtext" id="d-chal"></div></div>
        <div class="dblock"><div class="dlabel">Outcome</div><div class="dtext" id="d-out"></div></div>
        <div class="dblock full"><div class="dlabel">What I would do differently</div><div class="dtext" id="d-diff"></div></div>
      </div>
    </div>
  </div>

  <div class="notes" id="notes"></div>
  <div class="foot">
    <div class="fl">B.Tech CSE (AI/ML) · <b>University of Mumbai</b> · Expected 2027 &nbsp;·&nbsp; Data Science + GenAI Intern · <b>Innovexis</b></div>
    <div class="fr">shravanparthe@gmail.com</div>
  </div>
</div>

<script>
const CASES = {cases_json};
const NOTES = {notes_json};

let active = null;

function esc(s) {{
  return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}}

function buildGrid() {{
  const grid = document.getElementById('grid');

  // featured col
  const colFeat = document.createElement('div');
  colFeat.className = 'col';
  colFeat.appendChild(makeFile(CASES[0], true));
  grid.appendChild(colFeat);

  // mid col
  const colMid = document.createElement('div');
  colMid.className = 'col';
  colMid.appendChild(makeFile(CASES[1]));
  colMid.appendChild(makeFile(CASES[3]));
  grid.appendChild(colMid);

  // right col
  const colRight = document.createElement('div');
  colRight.className = 'col';
  colRight.appendChild(makeFile(CASES[2]));
  colRight.appendChild(makeFile(CASES[4]));
  grid.appendChild(colRight);
}}

function makeFile(c, feat=false) {{
  const div = document.createElement('div');
  div.className = 'file' + (feat ? ' feat' : '');
  div.dataset.id = c.id;

  const chips = c.stack.slice(0,5).map(s => `<span class="chip">${{esc(s)}}</span>`).join('');
  const sig = feat ? `<div class="sig">${{esc(c.signal)}}</div>` : '';

  div.innerHTML = `
    <div class="tbar" style="background:${{esc(c.accent)}}"></div>
    <div class="cid">
      <div class="cid-l">
        <div class="dot" style="background:${{esc(c.accent)}}"></div>
        CASE ${{esc(c.id)}} · ${{esc(c.domain)}}
      </div>
      <div class="badge" id="badge-${{esc(c.id)}}">FILE</div>
    </div>
    <div class="verdict">${{esc(c.verdict)}}</div>
    ${{sig}}
    <div class="chips">${{chips}}</div>
    <div class="cfoot">
      <span class="crole">${{esc(c.name)}} · ${{esc(c.role)}}</span>
      <span class="arr" id="arr-${{esc(c.id)}}">→</span>
    </div>
  `;

  if (!feat) {{
    div.addEventListener('click', () => toggleDetail(c));
  }}
  return div;
}}

function toggleDetail(c) {{
  const detail = document.getElementById('detail');

  if (active === c.id) {{
    active = null;
    detail.classList.remove('show');
    resetBadge(c.id);
    return;
  }}

  if (active) resetBadge(active);
  active = c.id;

  document.getElementById('dtbar').style.background = `linear-gradient(90deg, ${{c.accent}}, transparent)`;
  document.getElementById('d-name').textContent = c.name;
  document.getElementById('d-meta').textContent = `CASE ${{c.id}} · ${{c.domain}} · ${{c.role}}`;
  document.getElementById('d-repo').href = c.repo;
  document.getElementById('d-prob').textContent = c.problem;
  document.getElementById('d-dec').textContent = c.decision;
  document.getElementById('d-chal').textContent = c.challenge;
  document.getElementById('d-out').textContent = c.outcome;
  document.getElementById('d-diff').textContent = c.differently;

  detail.classList.add('show');
  detail.scrollIntoView({{behavior:'smooth', block:'nearest'}});

  const badge = document.getElementById(`badge-${{c.id}}`);
  if (badge) {{ badge.textContent = 'OPEN'; badge.className = 'badge on'; }}
  const arr = document.getElementById(`arr-${{c.id}}`);
  if (arr) {{ arr.style.transform = 'rotate(90deg)'; arr.style.color = 'var(--teal)'; }}

  document.querySelectorAll('.file').forEach(f => {{
    if (f.dataset.id === c.id) f.classList.add('open');
    else f.classList.remove('open');
  }});
}}

function resetBadge(id) {{
  const badge = document.getElementById(`badge-${{id}}`);
  if (badge) {{ badge.textContent = 'FILE'; badge.className = 'badge'; }}
  const arr = document.getElementById(`arr-${{id}}`);
  if (arr) {{ arr.style.transform = ''; arr.style.color = ''; }}
  document.querySelectorAll('.file').forEach(f => f.classList.remove('open'));
}}

function buildNotes() {{
  const container = document.getElementById('notes');
  NOTES.forEach(n => {{
    const div = document.createElement('div');
    div.className = 'note';
    div.innerHTML = `<div class="nlabel">signal / ${{esc(n.label)}}</div><div class="ntext">${{esc(n.text)}}</div>`;
    container.appendChild(div);
  }});
}}

buildGrid();
buildNotes();
</script>
</body>
</html>"""

components.html(html, height=1100, scrolling=True)
