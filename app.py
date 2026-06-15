from pathlib import Path
from html import escape

import streamlit as st


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
        "id": "01",
        "domain": "FINTECH",
        "name": "SAHAY",
        "verdict": "Micro-credit underwriting for borrowers who shouldn't need to understand banking software.",
        "signal": "RF credit scoring · 76% accuracy · 19 features · 3-role loan state machine · Aadhaar + PAN OCR",
        "stack": ["FastAPI", "Flutter", "Firebase", "Scikit-learn", "Tesseract OCR", "Stripe"],
        "role": "Full-stack backend + ML",
        "repo": "https://github.com/Shravan157/Sahay-Loan",
        "accent": "#b75533",
        "problem": "Small borrowers lose time and confidence when loan systems assume paperwork, branch visits, and manual screening. The product needed to treat credit, identity, repayment, and provider review as one workflow instead of disconnected screens.",
        "decision": "Flutter for the mobile-first client — one codebase for phone and web demos. FastAPI for the decision-heavy backend because Python made ML, OCR, and payment services easier to compose. Firebase Auth + Firestore gave real-time status updates without a separate auth and notification stack. Random Forest for scoring because explainability mattered more than chasing a black-box model.",
        "challenge": "Making the loan state machine honest. KYC extraction, model scoring, admin review, provider decisions, repayment schedules, and notifications all had to agree on the same borrower state. A single inconsistency breaks trust in a credit product.",
        "outcome": "Three-role lending platform. A borrower applies up to ₹1,00,000, completes Aadhaar and PAN extraction through OCR, and moves through approval and EMI repayment without manual KYC entry.",
        "differently": "Stronger audit trail for every model-assisted credit decision. Separate risk-service versioning from the main API. Build a fairness report before calling the model production-ready.",
    },
    {
        "id": "02",
        "domain": "EDTECH",
        "name": "SikshaSetu",
        "verdict": "A college portal that combines academic ops, live classes, and RAG-backed help in one role-aware system.",
        "signal": "RBAC across 3 roles · 10+ relational tables · virtual classroom · notes RAG via Qdrant",
        "stack": ["Spring Boot", "Spring Security", "JWT", "React", "MySQL", "LangChain4j", "Qdrant", "ZEGOCLOUD"],
        "role": "Java backend + AI/RAG integration",
        "repo": "https://github.com/Shravan157/sikshasetu",
        "accent": "#315b78",
        "problem": "Most college systems split academic work into separate tools — attendance somewhere, notes elsewhere, video links in chat, help requests handled manually. SikshaSetu needed to feel like one operating system for a college, especially where admin capacity is thin.",
        "decision": "Spring Boot for permission-heavy domain work — typed services, layered controllers, DTOs, predictable security filters. JWT for a stateless React client. MySQL fit the academic schema. LangChain4j + Qdrant so uploaded notes became searchable context instead of generic chatbot answers. ZEGOCLOUD tokens generated server-side so classroom secrets never sit in the browser.",
        "challenge": "Permission design for the AI layer. A student asking about portal navigation is harmless. A student asking for all users or faculty lists is not. The assistant had to be useful while respecting the same role boundaries as the normal APIs.",
        "outcome": "Role dashboards, attendance, timetable, assignments, notes, results, events, notifications, streaming AI responses, document insight chat, Qdrant-backed RAG, and live virtual classrooms — all in one system.",
        "differently": "Split AI tooling into a separate service boundary. Add background indexing jobs for notes instead of request-time indexing. Define richer integration tests around role leakage.",
    },
    {
        "id": "03",
        "domain": "FINTECH DATA",
        "name": "PhonePe Insights",
        "verdict": "A public fintech data pipeline that turns raw transaction files into a queryable regional dashboard.",
        "signal": "50K+ records · 36 states · 9 raw datasets → 5 relational tables · 10+ interactive charts",
        "stack": ["Python", "Pandas", "MySQL", "SQLAlchemy", "PyMySQL", "Streamlit", "Plotly"],
        "role": "Data engineering + dashboard",
        "repo": "https://github.com/Shravan157/phonepe-insights",
        "accent": "#b88a2f",
        "problem": "The PhonePe dataset is valuable, but raw transaction files don't explain regional behaviour by themselves. The dashboard needed to answer practical questions: where transaction volume is moving, which categories dominate, and how state-level adoption changes over time.",
        "decision": "Pandas for transformation — source files needed cleaning and reshaping before SQL. MySQL gave the dashboard a durable analytical layer instead of repeatedly scanning files. SQLAlchemy + PyMySQL kept queries parameterised. Streamlit + Plotly made exploration fast enough for a reviewer to use without setup friction.",
        "challenge": "Data shape. Transaction, user, and geography files carried related but differently structured information. The value came from normalising them into tables that made filters and joins predictable.",
        "outcome": "Ad-hoc analysis collapsed into a dashboard path: choose state, year, quarter, category — then inspect transaction trends, regional distribution, and payment behaviour visually.",
        "differently": "A reproducible data validation layer. Cache expensive dashboard queries. Define dbt-style transformation checks before loading data into MySQL.",
    },
    {
        "id": "04",
        "domain": "HEALTHTECH",
        "name": "MedoraX",
        "verdict": "A multilingual clinical assistant that accepts voice, image, and text while staying below the line of medical authority.",
        "signal": "English + Hindi + Marathi · voice, image, text input · hospital search · AQI context · TTS output",
        "stack": ["Python", "Gradio", "Groq Whisper", "Llama models", "Google Maps API", "Google Air Quality API", "Edge TTS"],
        "role": "AI pipeline + product workflow",
        "repo": "https://github.com/Shravan157/MedX-AI-Clinical-Assistant",
        "accent": "#637d69",
        "problem": "Healthcare discovery breaks down when the user can't type symptoms comfortably, can't explain an image, or needs help in a local language. MedoraX is a triage assistant — not a doctor replacement.",
        "decision": "Gradio for the demo surface — multimodal inputs are easier to ship there than in a heavier frontend. Groq Whisper for speech-to-text. Llama models for structured medical responses and image reasoning. Google Maps/Places closes the loop when the answer should be: find care near you now.",
        "challenge": "Orchestration. Voice, image, text, map lookup, AQI, emergency keywords, and TTS all have different latency and failure modes. The app needed to keep the user moving even when one external service was slow.",
        "outcome": "Full GenAI care-assistance pipeline with multilingual interaction, hospital discovery, and audio feedback for users who aren't comfortable with English-only text interfaces.",
        "differently": "Stronger clinical guardrails. Source-grounded medical retrieval. Offline fallback language packs. Red-team tests for unsafe medical advice.",
    },
    {
        "id": "05",
        "domain": "ENV DATA",
        "name": "Bird Observation",
        "verdict": "A conservation-data dashboard comparing forest and grassland observation patterns.",
        "signal": "Forest + grassland datasets · temporal, spatial, species-diversity, and environmental analysis",
        "stack": ["Python", "Pandas", "NumPy", "SQLite", "Plotly", "Streamlit"],
        "role": "Data cleaning + SQLite + dashboarding",
        "repo": "https://github.com/Shravan157/bird_project",
        "accent": "#4a7c59",
        "problem": "Observation datasets are easy to collect and hard to reason about. The goal was to compare habitat patterns without forcing the viewer to inspect spreadsheets.",
        "decision": "Pandas + NumPy for cleaning. SQLite to keep analysis lightweight and portable. Plotly + Streamlit for interactive filters across habitat, time, species, and environmental conditions — without turning a data project into a web engineering project.",
        "challenge": "Making two ecosystem datasets comparable. Forest and grassland observations need shared fields, consistent cleaning, and clear filters before the dashboard can say anything meaningful.",
        "outcome": "Raw observation files become conservation-oriented views across time, geography, species diversity, and environmental conditions.",
        "differently": "Data provenance notes. Automated schema checks for incoming Excel files. More explicit statistical confidence around conservation conclusions.",
    },
]


NOTES = [
    {
        "label": "RAG",
        "text": "Moving from loaders and splitters into retrieval quality — chunk size, metadata design, vector store choice, and when an agent should call a backend tool instead of answering from memory.",
    },
    {
        "label": "SYSTEMS",
        "text": "The next version of my work needs more background jobs, logs, test fixtures, model decision records, and deployment notes. The product idea is only half the work.",
    },
    {
        "label": "STACK",
        "text": "Spring Boot gives me discipline for business systems. Python gives me speed for AI and data workflows. The interesting part is designing the boundary between them.",
    },
]


def inject_css():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;700&family=Inter:wght@400;500;600&display=swap');

        :root {
            --bg:       #0e0f0e;
            --surface:  #141614;
            --surface2: #1a1d1a;
            --border:   rgba(255,255,255,0.07);
            --border2:  rgba(255,255,255,0.13);
            --ink:      #e8ebe6;
            --muted:    #7a8478;
            --dim:      #4a5248;
            --teal:     #4ecba0;
            --indigo:   #7b9fd4;
            --clay:     #c4704a;
            --gold:     #c9a24a;
            --sage:     #7ab090;
            --forest:   #5a9e6a;
            --mono: 'JetBrains Mono', 'Courier New', monospace;
            --sans: 'Inter', system-ui, sans-serif;
        }

        html, body, .stApp {
            background: var(--bg) !important;
            color: var(--ink);
        }

        [data-testid="stHeader"],
        [data-testid="stToolbar"],
        [data-testid="stDecoration"],
        footer {
            display: none !important;
        }

        [data-testid="stAppViewContainer"] > .main .block-container {
            max-width: 100%;
            padding: 0 !important;
            margin: 0 !important;
        }

        section[data-testid="stMain"] > div {
            padding: 0 !important;
        }

        * {
            font-family: var(--mono);
            letter-spacing: 0;
        }

        .sidebar-strip {
            width: 44px;
            min-height: 100vh;
            background: var(--surface);
            border-right: 1px solid var(--border);
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 1.4rem 0 2rem;
            position: fixed;
            left: 0;
            top: 0;
            bottom: 0;
            z-index: 100;
        }

        .sidebar-stamp {
            writing-mode: vertical-rl;
            text-orientation: mixed;
            transform: rotate(180deg);
            font-size: 9px;
            letter-spacing: 0.22em;
            text-transform: uppercase;
            color: var(--dim);
            margin-bottom: auto;
            user-select: none;
            padding-top: 0.5rem;
        }

        .sidebar-stamp strong {
            color: var(--muted);
            font-weight: 400;
        }

        .sidebar-icons {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 1.4rem;
        }

        .sidebar-icon-wrap {
            position: relative;
            display: flex;
            align-items: center;
        }

        .sidebar-icon {
            width: 28px;
            height: 28px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--dim);
            cursor: pointer;
            transition: color 0.18s;
            text-decoration: none !important;
            border: none;
        }

        .sidebar-icon:hover {
            color: var(--teal);
        }

        .sidebar-icon svg {
            width: 16px;
            height: 16px;
            stroke: currentColor;
            fill: none;
            stroke-width: 1.5;
            stroke-linecap: round;
            stroke-linejoin: round;
        }

        .sidebar-tooltip {
            position: absolute;
            left: 38px;
            background: var(--surface2);
            border: 1px solid var(--border2);
            color: var(--ink);
            font-size: 10px;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            padding: 4px 10px;
            white-space: nowrap;
            pointer-events: none;
            opacity: 0;
            transition: opacity 0.15s;
            z-index: 200;
        }

        .sidebar-icon-wrap:hover .sidebar-tooltip {
            opacity: 1;
        }

        .main-content {
            margin-left: 44px;
            min-height: 100vh;
        }

        .masthead {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0.85rem 2rem 0.85rem 1.6rem;
            border-bottom: 1px solid var(--border);
            background: var(--surface);
            gap: 1rem;
        }

        .masthead-left {
            font-size: 10px;
            letter-spacing: 0.2em;
            text-transform: uppercase;
            color: var(--muted);
        }

        .masthead-left strong {
            color: var(--ink);
            font-weight: 500;
        }

        .masthead-right {
            font-size: 10px;
            letter-spacing: 0.12em;
            color: var(--dim);
            text-align: right;
        }

        .board {
            padding: 1.4rem 1.6rem 0 1.6rem;
        }

        .case-file {
            background: var(--surface);
            border: 1px solid var(--border);
            padding: 1.1rem 1.15rem 1rem;
            position: relative;
            overflow: hidden;
            transition: border-color 0.2s, background 0.2s;
            min-height: 100%;
        }

        .case-file:hover {
            border-color: var(--border2);
            background: var(--surface2);
        }

        .case-file.selected {
            border-color: var(--border2);
            background: var(--surface2);
        }

        .case-file .top-bar {
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 2px;
            transition: height 0.2s;
        }

        .case-file:hover .top-bar,
        .case-file.selected .top-bar {
            height: 3px;
        }

        .case-id-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 0.75rem;
            gap: 0.75rem;
        }

        .case-id-left {
            display: flex;
            align-items: center;
            gap: 7px;
            font-size: 9.5px;
            letter-spacing: 0.2em;
            text-transform: uppercase;
            color: var(--dim);
        }

        .dot {
            width: 6px;
            height: 6px;
            border-radius: 50%;
            flex-shrink: 0;
        }

        .case-status {
            font-size: 9px;
            letter-spacing: 0.15em;
            text-transform: uppercase;
            color: var(--dim);
            border: 1px solid var(--border);
            padding: 2px 6px;
            flex-shrink: 0;
        }

        .case-status.open {
            color: var(--teal);
            border-color: rgba(78,203,160,0.25);
        }

        .case-verdict {
            font-size: 14.5px;
            font-weight: 500;
            color: var(--ink);
            line-height: 1.35;
            margin-bottom: 0.55rem;
            font-family: var(--sans);
        }

        .case-file.featured .case-verdict {
            font-size: 18px;
            line-height: 1.25;
            margin-bottom: 0.8rem;
        }

        .case-signal {
            font-size: 11px;
            line-height: 1.7;
            color: var(--muted);
        }

        .case-file.featured .case-signal {
            font-size: 12px;
        }

        .chip-row {
            display: flex;
            flex-wrap: wrap;
            gap: 5px;
            margin-top: 0.9rem;
        }

        .chip {
            font-size: 9.5px;
            letter-spacing: 0.06em;
            border: 1px solid var(--border);
            padding: 2px 8px;
            color: var(--dim);
            transition: color 0.15s, border-color 0.15s;
        }

        .case-file:hover .chip,
        .case-file.selected .chip {
            color: var(--muted);
            border-color: var(--border2);
        }

        .case-footer {
            margin-top: 1rem;
            padding-top: 0.75rem;
            border-top: 1px solid var(--border);
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 0.8rem;
        }

        .case-role {
            font-size: 9.5px;
            text-transform: uppercase;
            letter-spacing: 0.14em;
            color: var(--dim);
        }

        .case-arrow {
            font-size: 13px;
            color: var(--dim);
            transition: color 0.15s, transform 0.15s;
        }

        .case-file:hover .case-arrow,
        .case-file.selected .case-arrow {
            color: var(--teal);
            transform: translateX(2px);
        }

        .detail-panel {
            margin: 8px 1.6rem 0;
            background: var(--surface);
            border: 1px solid var(--border2);
            position: relative;
            overflow: hidden;
        }

        .detail-top-bar {
            height: 2px;
            width: 100%;
        }

        .detail-inner {
            padding: 1.6rem 2rem 1.8rem;
        }

        .detail-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 1.5rem;
            padding-bottom: 1rem;
            border-bottom: 1px solid var(--border);
            gap: 1rem;
        }

        .detail-name {
            font-size: 22px;
            font-weight: 500;
            color: var(--ink);
            font-family: var(--sans);
            line-height: 1;
        }

        .detail-meta {
            font-size: 10px;
            letter-spacing: 0.14em;
            text-transform: uppercase;
            color: var(--dim);
            margin-top: 0.4rem;
        }

        .detail-repo a {
            font-size: 10px;
            letter-spacing: 0.14em;
            text-transform: uppercase;
            color: var(--indigo);
            text-decoration: none;
            border: 1px solid rgba(123,159,212,0.25);
            padding: 5px 12px;
            transition: border-color 0.15s;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            white-space: nowrap;
        }

        .detail-repo a:hover {
            border-color: rgba(123,159,212,0.6);
            color: var(--indigo);
        }

        .detail-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 0;
        }

        .detail-block {
            padding: 1.1rem 1.4rem 1.1rem 0;
            border-bottom: 1px solid var(--border);
        }

        .detail-block:nth-child(even) {
            padding-left: 1.4rem;
            padding-right: 0;
            border-left: 1px solid var(--border);
        }

        .detail-block:nth-last-child(-n+2) {
            border-bottom: none;
        }

        .detail-block.full-width {
            grid-column: 1 / -1;
            padding-right: 0;
            border-left: none;
        }

        .detail-label {
            font-size: 9px;
            letter-spacing: 0.22em;
            text-transform: uppercase;
            color: var(--dim);
            margin-bottom: 0.5rem;
        }

        .detail-text {
            font-size: 12.5px;
            line-height: 1.75;
            color: var(--muted);
            font-family: var(--sans);
        }

        .notes-row {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 8px;
            margin: 8px 1.6rem 0;
        }

        .note-file {
            background: var(--surface);
            border: 1px solid var(--border);
            padding: 1rem 1.1rem;
            position: relative;
        }

        .note-file::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            height: 1px;
            background: linear-gradient(90deg, var(--gold) 0%, transparent 55%);
            opacity: 0.4;
        }

        .note-label {
            font-size: 9px;
            letter-spacing: 0.22em;
            text-transform: uppercase;
            color: var(--gold);
            opacity: 0.7;
            margin-bottom: 0.55rem;
        }

        .note-text {
            font-size: 11.5px;
            line-height: 1.75;
            color: var(--muted);
            font-family: var(--sans);
        }

        .footer-strip {
            margin: 8px 1.6rem 2rem;
            border: 1px solid var(--border);
            background: var(--surface);
            padding: 1rem 1.4rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 1rem;
        }

        .footer-left {
            font-size: 9.5px;
            letter-spacing: 0.14em;
            color: var(--dim);
            text-transform: uppercase;
        }

        .footer-left strong {
            color: var(--muted);
            font-weight: 400;
        }

        .footer-right {
            font-size: 10px;
            letter-spacing: 0.1em;
            color: var(--dim);
        }

        .stButton > button {
            background: transparent !important;
            border: 1px solid var(--border2) !important;
            color: var(--muted) !important;
            font-family: var(--mono) !important;
            font-size: 9.5px !important;
            letter-spacing: 0.14em !important;
            text-transform: uppercase !important;
            border-radius: 0 !important;
            padding: 8px 14px !important;
            min-height: 34px !important;
            width: 100% !important;
            margin: 0.35rem 0 0.8rem !important;
            transition: color 0.15s, border-color 0.15s, background 0.15s !important;
        }

        .stButton > button:hover {
            color: var(--teal) !important;
            border-color: rgba(78,203,160,0.45) !important;
            background: rgba(78,203,160,0.04) !important;
        }

        @media (max-width: 900px) {
            .masthead {
                flex-direction: column;
                align-items: flex-start;
            }

            .masthead-right {
                text-align: left;
            }

            .detail-grid {
                grid-template-columns: 1fr;
            }

            .detail-block,
            .detail-block:nth-child(even) {
                padding-left: 0;
                padding-right: 0;
                border-left: none;
            }

            .detail-block:nth-last-child(-n+2) {
                border-bottom: 1px solid var(--border);
            }

            .detail-block:last-child {
                border-bottom: none;
            }

            .notes-row {
                grid-template-columns: 1fr;
            }

            .footer-strip {
                flex-direction: column;
                align-items: flex-start;
            }
        }

        @media (max-width: 640px) {
            .sidebar-strip {
                display: none;
            }

            .main-content {
                margin-left: 0;
            }

            .board,
            .detail-panel,
            .notes-row,
            .footer-strip {
                margin-left: 1rem;
                margin-right: 1rem;
            }

            .board {
                padding-left: 0;
                padding-right: 0;
            }

            .detail-inner {
                padding: 1.2rem;
            }

            .detail-header {
                flex-direction: column;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def sidebar_strip():
    st.markdown(
        """
        <div class="sidebar-strip">
            <div class="sidebar-stamp"><strong>Shravan Parthe</strong> &nbsp;·&nbsp; backend + ai</div>
            <div class="sidebar-icons">

                <div class="sidebar-icon-wrap">
                    <a class="sidebar-icon" href="https://github.com/Shravan157" target="_blank">
                        <svg viewBox="0 0 24 24"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/></svg>
                    </a>
                    <div class="sidebar-tooltip">github</div>
                </div>

                <div class="sidebar-icon-wrap">
                    <a class="sidebar-icon" href="https://www.linkedin.com/in/shravan-parthe-00946b2ab/" target="_blank">
                        <svg viewBox="0 0 24 24"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/></svg>
                    </a>
                    <div class="sidebar-tooltip">linkedin</div>
                </div>

                <div class="sidebar-icon-wrap">
                    <a class="sidebar-icon" href="mailto:shravanparthe@gmail.com?subject=Backend%20%2B%20GenAI%20role" target="_blank">
                        <svg viewBox="0 0 24 24"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
                    </a>
                    <div class="sidebar-tooltip">email</div>
                </div>

                <div class="sidebar-icon-wrap">
                    <a class="sidebar-icon" href="mailto:shravanparthe@gmail.com?subject=Collaboration%20idea" target="_blank">
                        <svg viewBox="0 0 24 24"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
                    </a>
                    <div class="sidebar-tooltip">collaborate</div>
                </div>

            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def masthead():
    st.markdown(
        """
        <div class="masthead">
            <div class="masthead-left">
                <strong>Field journal</strong> &nbsp;·&nbsp; AI backend engineering &nbsp;·&nbsp; Mumbai, India
            </div>
            <div class="masthead-right">
                5 case files &nbsp;·&nbsp; B.Tech AI/ML · ViMEET, University of Mumbai &nbsp;·&nbsp; Intern @ Innovexis
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def case_file_html(case, featured=False, selected=False):
    featured_cls = "featured" if featured else ""
    selected_cls = "selected" if selected else ""
    status_cls = "open" if selected else ""
    status_txt = "OPEN" if selected else "FILE"

    chips = "".join(
        f"<span class='chip'>{escape(stack_item)}</span>"
        for stack_item in case["stack"][:5]
    )

    signal_html = ""
    if featured:
        signal_html = f"<div class='case-signal'>{escape(case['signal'])}</div>"

    return f"""
    <div class="case-file {featured_cls} {selected_cls}">
        <div class="top-bar" style="background:{escape(case['accent'])}"></div>

        <div class="case-id-row">
            <div class="case-id-left">
                <div class="dot" style="background:{escape(case['accent'])}"></div>
                CASE {escape(case['id'])} &nbsp;/&nbsp; {escape(case['domain'])}
            </div>
            <div class="case-status {status_cls}">{status_txt}</div>
        </div>

        <div class="case-verdict">{escape(case['verdict'])}</div>
        {signal_html}

        <div class="chip-row">{chips}</div>

        <div class="case-footer">
            <span class="case-role">{escape(case['name'])} &nbsp;·&nbsp; {escape(case['role'])}</span>
            <span class="case-arrow">{"↓" if selected else "→"}</span>
        </div>
    </div>
    """


def detail_panel_html(case):
    return f"""
    <div class="detail-panel">
        <div class="detail-top-bar" style="background: linear-gradient(90deg, {escape(case['accent'])}, transparent)"></div>

        <div class="detail-inner">
            <div class="detail-header">
                <div>
                    <div class="detail-name">{escape(case['name'])}</div>
                    <div class="detail-meta">
                        CASE {escape(case['id'])} &nbsp;·&nbsp; {escape(case['domain'])} &nbsp;·&nbsp; {escape(case['role'])}
                    </div>
                </div>

                <div class="detail-repo">
                    <a href="{escape(case['repo'])}" target="_blank">
                        Open repository
                    </a>
                </div>
            </div>

            <div class="detail-grid">
                <div class="detail-block">
                    <div class="detail-label">Problem I was actually solving</div>
                    <div class="detail-text">{escape(case['problem'])}</div>
                </div>

                <div class="detail-block">
                    <div class="detail-label">Engineering decision</div>
                    <div class="detail-text">{escape(case['decision'])}</div>
                </div>

                <div class="detail-block">
                    <div class="detail-label">Core technical challenge</div>
                    <div class="detail-text">{escape(case['challenge'])}</div>
                </div>

                <div class="detail-block">
                    <div class="detail-label">Outcome</div>
                    <div class="detail-text">{escape(case['outcome'])}</div>
                </div>

                <div class="detail-block full-width">
                    <div class="detail-label">What I would do differently</div>
                    <div class="detail-text">{escape(case['differently'])}</div>
                </div>
            </div>
        </div>
    </div>
    """


def notes_row():
    notes_html = ""

    for note in NOTES:
        notes_html += f"""
        <div class="note-file">
            <div class="note-label">signal &nbsp;/&nbsp; {escape(note['label'])}</div>
            <div class="note-text">{escape(note['text'])}</div>
        </div>
        """

    st.markdown(f"<div class='notes-row'>{notes_html}</div>", unsafe_allow_html=True)


def footer():
    st.markdown(
        """
        <div class="footer-strip">
            <div class="footer-left">
                B.Tech CSE (AI/ML) &nbsp;·&nbsp; <strong>University of Mumbai</strong> &nbsp;·&nbsp; Expected 2027
                &nbsp;&nbsp;·&nbsp;&nbsp;
                Data Science + GenAI Intern &nbsp;·&nbsp; <strong>Innovexis</strong>
            </div>
            <div class="footer-right">
                shravanparthe@gmail.com
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_case_button(case):
    selected = st.session_state.selected == case["id"]
    button_text = "Close case" if selected else f"Open {case['name']}"

    if st.button(button_text, key=f"btn_{case['id']}", use_container_width=True):
        st.session_state.selected = None if selected else case["id"]
        st.rerun()


def render_case_column(case_list, featured_first=False):
    for index, case in enumerate(case_list):
        selected = st.session_state.selected == case["id"]
        featured = featured_first and index == 0

        st.markdown(
            case_file_html(case, featured=featured, selected=selected),
            unsafe_allow_html=True,
        )

        render_case_button(case)


def main():
    inject_css()

    if "selected" not in st.session_state:
        st.session_state.selected = None

    sidebar_strip()

    st.markdown('<div class="main-content">', unsafe_allow_html=True)

    masthead()

    st.markdown('<div class="board">', unsafe_allow_html=True)

    col_feat, col_mid, col_right = st.columns([2, 1, 1], gap="small")

    with col_feat:
        render_case_column([CASES[0]], featured_first=True)

    with col_mid:
        render_case_column([CASES[1], CASES[3]])

    with col_right:
        render_case_column([CASES[2], CASES[4]])

    st.markdown("</div>", unsafe_allow_html=True)

    if st.session_state.selected:
        active = next(
            (case for case in CASES if case["id"] == st.session_state.selected),
            None,
        )

        if active:
            st.markdown(detail_panel_html(active), unsafe_allow_html=True)

    notes_row()
    footer()

    st.markdown("</div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
