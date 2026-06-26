from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

BASE_DIR = Path(__file__).parent
RESUME_PATH = BASE_DIR / "assets" / "shravan_resume.pdf"

st.set_page_config(
    page_title="Shravan Parthe | AI Backend Case Journal",
    page_icon="SP",
    layout="wide",
    initial_sidebar_state="collapsed",
)

CASES = {
    "SAHAY": {
        "deck": "Micro-credit underwriting for people who should not need to understand banking software to access small loans.",
        "market": "Fintech · Micro-credit",
        "stack": ["FastAPI", "Flutter", "Firebase", "Scikit-learn", "Tesseract OCR", "Stripe"],
        "repo": "https://github.com/Shravan157/Sahay-Loan",
        "signal": "Random Forest credit scoring reached 76% test accuracy over 19 selected borrower features. The loan workflow supports borrower, admin, and provider roles with digital KYC and EMI repayment.",
        "problem": "I built SAHAY around a blunt problem: small borrowers lose time and confidence when loan systems assume paperwork, branch visits, and manual screening. The product needed to treat credit, identity, repayment, and provider review as one workflow instead of disconnected screens.",
        "decision": "I kept the mobile client in Flutter because the same codebase could cover phone-first usage and web demos. FastAPI handled the decision-heavy backend because Python made the ML, OCR, and payment services easier to compose. Firebase Auth and Firestore gave me real-time status updates without building a separate auth and notification stack. The scoring model used a Random Forest because explainability and stable tabular performance mattered more than chasing a black-box model.",
        "challenge": "The hard part was not a single API. It was making the loan state machine honest: KYC extraction, model scoring, admin review, provider decisions, repayment schedules, and notifications all had to agree on the same borrower state.",
        "outcome": "The result is a three-role lending platform where a borrower can apply up to INR 1,00,000, complete Aadhaar and PAN extraction through OCR, and move through approval and EMI repayment without manual KYC entry.",
        "differently": "I would now add a stronger audit trail for every model-assisted credit decision, separate risk-service versioning from the main API, and build a fairness report before showing the model as production-ready.",
    },
    "SikshaSetu": {
        "deck": "A college portal that combines academic operations, live classes, and RAG-backed help inside one role-aware system.",
        "market": "Edtech · College portal",
        "stack": ["Spring Boot", "Spring Security", "JWT", "React", "MySQL", "LangChain4j", "Qdrant", "ZEGOCLOUD"],
        "repo": "https://github.com/Shravan157/sikshasetu",
        "signal": "Built RBAC across student, faculty, and admin roles, modeled 10+ relational tables, and added virtual classroom plus notes RAG search.",
        "problem": "Most college systems split academic work into separate tools: attendance somewhere, notes somewhere else, video class links in chat, and help requests handled manually. I wanted SikshaSetu to feel like one operating system for a college, especially where admin capacity is thin.",
        "decision": "I chose Spring Boot because the domain is permission-heavy and benefits from typed services, layered controllers, DTOs, and predictable security filters. JWT made the React client stateless. MySQL fit the academic schema. For AI, I used LangChain4j and Qdrant so uploaded notes could become searchable context instead of generic chatbot answers. ZEGOCLOUD tokens are generated server-side so classroom secrets never sit in the browser.",
        "challenge": "The core challenge was permission design. A student asking the assistant about portal navigation is harmless; a student asking for all users or faculty lists is not. The assistant had to be useful while respecting the same role boundaries as the normal APIs.",
        "outcome": "The portal now supports role dashboards, attendance, timetable, assignments, notes, results, events, notifications, streaming AI responses, document insight chat, Qdrant-backed notes RAG, and live virtual classrooms.",
        "differently": "I would split AI tooling into a separate service boundary, add background indexing jobs for notes instead of direct request-time indexing, and define richer integration tests around role leakage.",
    },
    "PhonePe Insights": {
        "deck": "A public fintech data pipeline that turns transaction files into a queryable regional dashboard.",
        "market": "Public data · Fintech analytics",
        "stack": ["Python", "Pandas", "MySQL", "SQLAlchemy", "PyMySQL", "Streamlit", "Plotly"],
        "repo": "https://github.com/Shravan157/phonepe-insights",
        "signal": "Processed 50,000+ PhonePe transaction records across 36 states, normalized 9 raw datasets into 5 relational tables, and delivered 10+ interactive charts.",
        "problem": "The PhonePe dataset is valuable, but raw transaction files do not explain regional behavior by themselves. I wanted the dashboard to answer practical questions: where transaction volume is moving, which categories dominate, and how state-level adoption changes over time.",
        "decision": "I used Pandas for transformation because the source files needed cleaning and reshaping before SQL. MySQL gave the dashboard a durable analytical layer instead of repeatedly scanning files. SQLAlchemy and PyMySQL kept queries parameterized, while Streamlit and Plotly made the exploration fast enough for a reviewer to use without setup friction.",
        "challenge": "The main engineering problem was data shape. Transaction, user, and geography files carried related but differently structured information. The value came from normalizing them into tables that made filters and joins predictable.",
        "outcome": "The finished app reduced ad-hoc analysis into a dashboard path: choose state, year, quarter, and category, then inspect transaction trends, regional distribution, and payment behavior visually.",
        "differently": "I would now add a reproducible data validation layer, cache expensive dashboard queries, and define dbt-style transformation checks before loading data into MySQL.",
    },
    "MedoraX": {
        "deck": "A multilingual clinical assistant that accepts voice, image, and text while clearly staying below the line of medical authority.",
        "market": "Healthtech · Multilingual AI",
        "stack": ["Python", "Gradio", "Groq Whisper", "Llama models", "Google Maps API", "Google Air Quality API", "Edge TTS"],
        "repo": "https://github.com/Shravan157/MedX-AI-Clinical-Assistant",
        "signal": "Supports English, Hindi, and Marathi input/output, image analysis, nearby hospital search, AQI context, emergency detection, and text-to-speech responses.",
        "problem": "Healthcare discovery breaks down quickly when the user cannot type symptoms comfortably, cannot explain an image, or needs help in a local language. I treated MedoraX as a triage assistant, not a doctor replacement.",
        "decision": "Gradio was the right demo surface because multimodal inputs are easier to ship there than in a heavier frontend. Groq Whisper handles speech-to-text, Llama models handle structured medical responses and image reasoning, and Google Maps/Places closes the loop when the answer should be: find care near you now.",
        "challenge": "The challenge was orchestration. Voice, image, text, map lookup, AQI, emergency keywords, and TTS all have different latency and failure modes. The app needed to keep the user moving even when one external service was slow.",
        "outcome": "The project demonstrates a full GenAI care-assistance pipeline with multilingual interaction, hospital discovery, and audio feedback for users who may not be comfortable with English-only text interfaces.",
        "differently": "I would add stronger clinical guardrails, source-grounded medical retrieval, offline fallback language packs, and red-team tests for unsafe medical advice.",
    },
    "Bird Observation Analysis": {
        "deck": "A conservation-data dashboard for comparing forest and grassland observation patterns.",
        "market": "Environmental · Public data",
        "stack": ["Python", "Pandas", "NumPy", "SQLite", "Plotly", "Streamlit"],
        "repo": "https://github.com/Shravan157/bird_project",
        "signal": "Combines forest and grassland datasets into a Streamlit dashboard with temporal, spatial, species-diversity, and environmental analysis.",
        "problem": "Observation datasets are easy to collect and hard to reason about. I built this project to compare habitat patterns without forcing the viewer to inspect spreadsheets.",
        "decision": "Pandas and NumPy handled cleaning. SQLite kept the analysis lightweight and portable. Plotly and Streamlit were enough to make habitat, time, species, and environmental filters interactive without turning a data project into a web engineering project.",
        "challenge": "The technical challenge was making two ecosystem datasets comparable. Forest and grassland observations need shared fields, consistent cleaning, and clear filters before the dashboard can say anything useful.",
        "outcome": "The app turns raw observation files into conservation-oriented views across time, geography, species diversity, and environmental conditions.",
        "differently": "I would add data provenance notes, automated schema checks for incoming Excel files, and more explicit statistical confidence around conservation conclusions.",
    },
}

NOTES = [
    {
        "title": "RAG is becoming an engineering problem for me, not just a LangChain topic.",
        "body": "I am moving from loaders and splitters into retrieval quality: chunk size, metadata design, vector store choice, and when an agent should call a backend tool instead of answering from memory.",
    },
    {
        "title": "I am cleaning up the line between demos and systems.",
        "body": "The next version of my work needs more background jobs, logs, test fixtures, model decision records, and deployment notes. The product idea is only half the work; operational truth is the other half.",
    },
    {
        "title": "Java and Python are becoming complementary in my stack.",
        "body": "Spring Boot gives me discipline for business systems. Python gives me speed for AI and data workflows. The interesting part is designing the boundary between them.",
    },
]

STACK_GROUPS = {
    "Backend": ["Spring Boot + Spring Security", "FastAPI", "JWT + RBAC", "REST API design"],
    "AI / ML": ["Scikit-learn", "LangChain4j", "Qdrant", "Groq / Llama", "Tesseract OCR"],
    "Data": ["MySQL · SQLite · Firestore", "Pandas · NumPy", "SQLAlchemy", "Plotly · Streamlit"],
    "Frontend": ["React", "Flutter", "Gradio"],
    "Cloud / DevOps": ["AWS", "Firebase", "Vercel · Streamlit Cloud", "Docker (learning)"],
    "Languages": ["Python", "Java", "JavaScript", "Dart", "SQL"],
}

if "selected_case" not in st.session_state:
    st.session_state.selected_case = "SAHAY"


def inject_css() -> None:
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=DM+Sans:wght@300;400;500;600;700&display=swap');

        :root {
            --bg: #111110;
            --surface: #171615;
            --surface-2: #1d1c1b;
            --surface-off: #222120;
            --border: rgba(255,255,255,0.07);
            --text: #e8e6e2;
            --text-muted: #888580;
            --text-faint: #4e4c49;
            --primary: #4a9fa8;
            --primary-h: #2d8a94;
            --primary-hl: #1c3438;
            --accent: #e06540;
            --gold: #c49a32;
            --shadow-sm: 0 1px 3px rgba(0,0,0,.25), 0 1px 2px rgba(0,0,0,.2);
            --shadow-md: 0 4px 16px rgba(0,0,0,.35), 0 2px 4px rgba(0,0,0,.2);
            --shadow-lg: 0 16px 48px rgba(0,0,0,.5), 0 4px 12px rgba(0,0,0,.3);
        }

        .stApp {
            background:
                radial-gradient(circle at 70% 20%, rgba(74,159,168,0.10), transparent 24%),
                radial-gradient(circle at 12% 82%, rgba(224,101,64,0.08), transparent 20%),
                linear-gradient(var(--border) 1px, transparent 1px),
                linear-gradient(90deg, var(--border) 1px, transparent 1px),
                var(--bg);
            background-size: auto, auto, 48px 48px, 48px 48px, auto;
            color: var(--text);
            font-family: 'DM Sans', sans-serif;
        }

        #MainMenu, header, footer, [data-testid="stToolbar"], [data-testid="stDecoration"], [data-testid="stStatusWidget"] {
            visibility: hidden !important;
            display: none !important;
        }

        [data-testid="stAppViewContainer"] > .main {
            background: transparent;
        }

        [data-testid="stAppViewContainer"] > .main .block-container {
            max-width: 1180px;
            padding: 1.2rem 1rem 4rem;
        }

        div[data-testid="column"] { width: 100% !important; }

        .shell {
            position: relative;
            z-index: 1;
        }

        .glass-nav {
            position: sticky;
            top: 0.8rem;
            z-index: 50;
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 1rem;
            padding: 0.95rem 1.15rem;
            background: rgba(17,17,16,0.68);
            border: 1px solid var(--border);
            border-radius: 999px;
            backdrop-filter: blur(14px);
            margin-bottom: 2rem;
            box-shadow: var(--shadow-sm);
        }

        .nav-brand {
            font-family: 'Instrument Serif', serif;
            font-size: 1.4rem;
            color: var(--text);
            font-style: italic;
        }

        .nav-meta {
            color: var(--text-muted);
            font-size: 0.92rem;
        }

        .hero {
            min-height: 88vh;
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            padding: 3rem 0 2rem;
        }

        .eyebrow {
            display: inline-flex;
            align-items: center;
            gap: 0.6rem;
            color: var(--accent);
            font-size: 0.74rem;
            text-transform: uppercase;
            letter-spacing: 0.16em;
            font-weight: 700;
            margin-bottom: 1rem;
        }

        .eyebrow::before {
            content: '';
            width: 28px;
            height: 1px;
            background: var(--accent);
            display: inline-block;
        }

        .hero h1 {
            font-family: 'Instrument Serif', serif;
            color: var(--text);
            font-size: clamp(3rem, 8vw, 7rem);
            line-height: 0.92;
            margin: 0 0 1.4rem;
            max-width: 13ch;
        }

        .hero h1 em {
            color: var(--primary);
            font-style: italic;
        }

        .hero-copy {
            font-size: clamp(1.08rem, 2vw, 1.35rem);
            color: var(--text-muted);
            line-height: 1.7;
            max-width: 58ch;
            margin-bottom: 1.8rem;
        }

        .stat-row {
            display: grid;
            grid-template-columns: repeat(4, minmax(0, 1fr));
            gap: 1rem;
            margin-top: 2rem;
            padding-top: 1.5rem;
            border-top: 1px solid var(--border);
        }

        .stat-card {
            padding: 1rem 1rem 0.85rem;
            background: rgba(23,22,21,0.75);
            border: 1px solid var(--border);
            border-radius: 1rem;
            backdrop-filter: blur(10px);
        }

        .stat-num {
            display: block;
            font-family: 'Instrument Serif', serif;
            color: var(--text);
            font-size: 2rem;
            line-height: 1;
            margin-bottom: 0.35rem;
        }

        .stat-label {
            color: var(--text-muted);
            font-size: 0.74rem;
            text-transform: uppercase;
            letter-spacing: 0.12em;
        }

        .section-kicker {
            display: inline-flex;
            align-items: center;
            gap: 0.55rem;
            color: var(--text-faint);
            text-transform: uppercase;
            letter-spacing: 0.14em;
            font-size: 0.72rem;
            font-weight: 700;
            margin-bottom: 0.85rem;
        }

        .section-kicker::before {
            content: '';
            width: 18px;
            height: 1px;
            background: var(--text-faint);
            display: inline-block;
        }

        .section-title {
            font-family: 'Instrument Serif', serif;
            font-size: clamp(2rem, 4vw, 3.5rem);
            color: var(--text);
            line-height: 1.06;
            margin-bottom: 0.6rem;
            max-width: 18ch;
        }

        .section-copy {
            color: var(--text-muted);
            font-size: 1rem;
            line-height: 1.75;
            max-width: 54ch;
            margin-bottom: 2rem;
        }

        .bento-grid {
            display: grid;
            grid-template-columns: repeat(12, minmax(0, 1fr));
            gap: 1rem;
            margin-top: 1rem;
        }

        .case-card {
            position: relative;
            background: linear-gradient(180deg, rgba(29,28,27,0.96), rgba(23,22,21,0.92));
            border: 1px solid var(--border);
            border-radius: 1.25rem;
            padding: 1.25rem;
            min-height: 100%;
            box-shadow: var(--shadow-sm);
            transition: transform .22s ease, border-color .22s ease, box-shadow .22s ease;
        }

        .case-card:hover {
            transform: translateY(-2px);
            border-color: rgba(74,159,168,0.28);
            box-shadow: var(--shadow-md);
        }

        .span-7 { grid-column: span 7; }
        .span-5 { grid-column: span 5; }
        .span-4 { grid-column: span 4; }

        .case-market {
            color: var(--accent);
            font-size: 0.72rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.12em;
            margin-bottom: 0.7rem;
        }

        .case-name {
            font-family: 'Instrument Serif', serif;
            font-size: 2rem;
            line-height: 1.05;
            color: var(--text);
            margin-bottom: 0.55rem;
        }

        .case-deck {
            color: var(--text-muted);
            font-size: 0.95rem;
            line-height: 1.72;
            margin-bottom: 1rem;
        }

        .signal-box {
            border: 1px solid var(--border);
            background: rgba(255,255,255,0.02);
            border-radius: 0.9rem;
            padding: 0.9rem 1rem;
            color: var(--text-muted);
            font-size: 0.8rem;
            line-height: 1.65;
            margin-bottom: 1rem;
        }

        .tag-row {
            display: flex;
            flex-wrap: wrap;
            gap: 0.45rem;
            margin-top: auto;
        }

        .tag {
            padding: 0.3rem 0.65rem;
            border-radius: 999px;
            border: 1px solid var(--border);
            background: rgba(255,255,255,0.03);
            color: var(--text-muted);
            font-size: 0.75rem;
        }

        .detail-shell {
            margin-top: 1.25rem;
            background: linear-gradient(180deg, rgba(23,22,21,0.98), rgba(17,17,16,0.96));
            border: 1px solid var(--border);
            border-radius: 1.35rem;
            overflow: hidden;
            box-shadow: var(--shadow-lg);
        }

        .detail-head {
            padding: 1.5rem 1.5rem 1.2rem;
            border-bottom: 1px solid var(--border);
        }

        .detail-title {
            font-family: 'Instrument Serif', serif;
            font-size: clamp(2rem, 4vw, 3rem);
            color: var(--text);
            margin: 0.15rem 0 0.35rem;
            line-height: 1.05;
        }

        .detail-deck {
            color: var(--text-muted);
            font-size: 1rem;
            line-height: 1.75;
            max-width: 62ch;
        }

        .detail-body {
            padding: 1.35rem 1.5rem 1.6rem;
        }

        .signal-banner {
            border: 1px solid rgba(196,154,50,0.22);
            background: rgba(196,154,50,0.08);
            border-radius: 1rem;
            padding: 1rem 1.1rem;
            margin-bottom: 1rem;
        }

        .signal-label {
            color: var(--gold);
            font-size: 0.72rem;
            text-transform: uppercase;
            letter-spacing: 0.12em;
            font-weight: 700;
            margin-bottom: 0.4rem;
        }

        .signal-text {
            color: var(--text-muted);
            font-size: 0.93rem;
            line-height: 1.7;
        }

        .n-block {
            padding: 1rem 0;
            border-top: 1px solid var(--border);
        }

        .n-block:first-of-type { border-top: 0; }

        .n-label {
            color: var(--accent);
            font-size: 0.72rem;
            text-transform: uppercase;
            letter-spacing: 0.14em;
            font-weight: 800;
            margin-bottom: 0.45rem;
        }

        .n-text {
            color: var(--text-muted);
            font-size: 0.96rem;
            line-height: 1.8;
            max-width: 68ch;
        }

        .note-card, .context-card, .stack-card {
            background: rgba(23,22,21,0.9);
            border: 1px solid var(--border);
            border-radius: 1.1rem;
            padding: 1.15rem;
            min-height: 100%;
            box-shadow: var(--shadow-sm);
        }

        .note-num {
            font-family: 'Instrument Serif', serif;
            color: var(--text-faint);
            font-size: 2rem;
            margin-bottom: 0.5rem;
            font-style: italic;
        }

        .card-title {
            color: var(--text);
            font-size: 1rem;
            font-weight: 700;
            line-height: 1.4;
            margin-bottom: 0.45rem;
        }

        .card-copy {
            color: var(--text-muted);
            font-size: 0.94rem;
            line-height: 1.72;
            margin-bottom: 0;
        }

        .stack-group {
            margin-bottom: 1rem;
        }

        .stack-group:last-child { margin-bottom: 0; }

        .stack-head {
            color: var(--text-faint);
            text-transform: uppercase;
            font-weight: 700;
            letter-spacing: 0.11em;
            font-size: 0.72rem;
            margin-bottom: 0.7rem;
            padding-bottom: 0.45rem;
            border-bottom: 1px solid var(--border);
        }

        .stack-item {
            color: var(--text-muted);
            font-size: 0.9rem;
            line-height: 1.7;
            display: flex;
            align-items: center;
            gap: 0.55rem;
            margin-bottom: 0.35rem;
        }

        .stack-item::before {
            content: '';
            width: 6px;
            height: 6px;
            border-radius: 999px;
            background: var(--primary);
            display: inline-block;
            flex-shrink: 0;
        }

        .contact-shell {
            display: grid;
            grid-template-columns: 1.1fr 0.9fr;
            gap: 1.1rem;
            background: rgba(23,22,21,0.92);
            border: 1px solid var(--border);
            border-radius: 1.35rem;
            padding: 1.4rem;
            box-shadow: var(--shadow-md);
        }

        .contact-title {
            font-family: 'Instrument Serif', serif;
            font-size: clamp(2rem, 4vw, 3rem);
            color: var(--text);
            line-height: 1.08;
            margin-bottom: 0.6rem;
        }

        .contact-copy {
            color: var(--text-muted);
            line-height: 1.8;
            font-size: 0.98rem;
            max-width: 48ch;
            margin-bottom: 1rem;
        }

        .cta-card {
            background: rgba(255,255,255,0.02);
            border: 1px solid var(--border);
            border-radius: 1rem;
            padding: 1rem;
            margin-bottom: 0.85rem;
        }

        .btn-row a, .repo-btn a {
            text-decoration: none !important;
        }

        .stButton > button,
        .stDownloadButton > button,
        .repo-btn a,
        .ghost-link {
            border-radius: 999px !important;
            min-height: 2.8rem !important;
            padding: 0.62rem 1.1rem !important;
            font-weight: 700 !important;
            border: 1px solid var(--border) !important;
            background: rgba(255,255,255,0.03) !important;
            color: var(--text) !important;
            transition: all .2s ease !important;
            display: inline-flex !important;
            align-items: center !important;
            justify-content: center !important;
        }

        .stButton > button:hover,
        .stDownloadButton > button:hover,
        .repo-btn a:hover,
        .ghost-link:hover {
            border-color: rgba(74,159,168,0.32) !important;
            background: rgba(74,159,168,0.12) !important;
            color: var(--text) !important;
        }

        .primary-pill {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            min-height: 2.8rem;
            padding: 0.7rem 1.15rem;
            border-radius: 999px;
            background: var(--primary);
            color: #091011 !important;
            font-weight: 800;
            text-decoration: none !important;
            border: 1px solid transparent;
        }

        .primary-pill:hover {
            background: var(--primary-h);
            color: white !important;
        }

        .footer-line {
            margin-top: 2rem;
            padding-top: 1rem;
            border-top: 1px solid var(--border);
            display: flex;
            justify-content: space-between;
            gap: 1rem;
            flex-wrap: wrap;
            color: var(--text-faint);
            font-size: 0.8rem;
        }

        @media (max-width: 980px) {
            .span-7, .span-5, .span-4 { grid-column: span 12; }
            .stat-row, .contact-shell { grid-template-columns: 1fr; }
        }

        @media (max-width: 720px) {
            .glass-nav {
                border-radius: 1rem;
                padding: 0.9rem 1rem;
                display: block;
            }
            .nav-meta { margin-top: 0.3rem; display: block; }
            .hero { min-height: auto; padding-top: 1rem; }
            .detail-head, .detail-body, .contact-shell { padding: 1rem; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def tags(items: list[str]) -> str:
    return "<div class='tag-row'>" + "".join(f"<span class='tag'>{item}</span>" for item in items) + "</div>"


def top_nav() -> None:
    st.markdown(
        """
        <div class="glass-nav">
            <div class="nav-brand">SP</div>
            <span class="nav-meta">AI backend engineer · Python, Java, Spring Boot, FastAPI, GenAI systems</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


def hero() -> None:
    st.markdown(
        """
        <section class="hero">
            <div class="eyebrow">AI Backend Engineer</div>
            <h1>I build backend systems where <em>AI has to earn its place.</em></h1>
            <p class="hero-copy">
                Final-year CS student at University of Mumbai. I work at the seam of Python and Java — FastAPI and Spring Boot,
                ML pipelines and relational schemas, GenAI tooling and the production discipline it takes to trust a model in a real workflow.
            </p>
        </section>
        """,
        unsafe_allow_html=True,
    )

    stats = [
        ("5", "Case studies"),
        ("76–81%", "ML model accuracy"),
        ("50k+", "Records processed"),
        ("3", "Languages in MedoraX"),
    ]
    cols = st.columns(4)
    for col, (num, label) in zip(cols, stats):
        with col:
            st.markdown(
                f"""
                <div class="stat-card">
                    <span class="stat-num">{num}</span>
                    <span class="stat-label">{label}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )


def work_bento() -> None:
    st.markdown(
        """
        <div class="section-kicker">Selected Work</div>
        <div class="section-title">Five systems, each with a real decision trail.</div>
        <p class="section-copy">These are not demos. Each entry covers the problem I actually solved, why I made the choices I made, and what I would do differently now.</p>
        """,
        unsafe_allow_html=True,
    )

    layout = [
        ("SAHAY", "span-7"),
        ("SikshaSetu", "span-5"),
        ("PhonePe Insights", "span-4"),
        ("MedoraX", "span-4"),
        ("Bird Observation Analysis", "span-4"),
    ]

    st.markdown("<div class='bento-grid'>", unsafe_allow_html=True)
    for name, span in layout:
        case = CASES[name]
        st.markdown(
            f"""
            <div class="case-card {span}">
                <div class="case-market">{case['market']}</div>
                <div class="case-name">{name}</div>
                <div class="case-deck">{case['deck']}</div>
                {f"<div class='signal-box'>{case['signal']}</div>" if name in ['SAHAY', 'SikshaSetu'] else ''}
                {tags(case['stack'][:5 if name == 'SAHAY' else 4])}
            </div>
            """,
            unsafe_allow_html=True,
        )
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)
    selected = st.radio(
        "Case file",
        list(CASES.keys()),
        index=list(CASES.keys()).index(st.session_state.selected_case),
        horizontal=True,
        label_visibility="collapsed",
        key="case_selector_radio",
    )
    st.session_state.selected_case = selected


def selected_case_detail() -> None:
    case = CASES[st.session_state.selected_case]
    st.markdown(
        f"""
        <div class="detail-shell">
            <div class="detail-head">
                <div class="case-market">{case['market']}</div>
                <div class="detail-title">{st.session_state.selected_case}</div>
                <div class="detail-deck">{case['deck']}</div>
            </div>
            <div class="detail-body">
                <div class="signal-banner">
                    <div class="signal-label">Reviewer signal</div>
                    <div class="signal-text">{case['signal']}</div>
                </div>
                <div class="n-block">
                    <div class="n-label">Problem I was actually solving</div>
                    <div class="n-text">{case['problem']}</div>
                </div>
                <div class="n-block">
                    <div class="n-label">Engineering decision</div>
                    <div class="n-text">{case['decision']}</div>
                </div>
                <div class="n-block">
                    <div class="n-label">Core technical challenge</div>
                    <div class="n-text">{case['challenge']}</div>
                </div>
                <div class="n-block">
                    <div class="n-label">Measurable outcome</div>
                    <div class="n-text">{case['outcome']}</div>
                </div>
                <div class="n-block">
                    <div class="n-label">What I would do differently now</div>
                    <div class="n-text">{case['differently']}</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(f"<div class='repo-btn'><a href='{case['repo']}' target='_blank'>Open repository</a></div>", unsafe_allow_html=True)


def learning() -> None:
    st.markdown(
        """
        <div class="section-kicker">Learning In Progress</div>
        <div class="section-title">Not a trophy shelf.</div>
        <p class="section-copy">This is the part of the journal where the system is still wet paint — useful, unfinished, and honest about what has to become stronger before it deserves production trust.</p>
        """,
        unsafe_allow_html=True,
    )
    cols = st.columns(3)
    for idx, note in enumerate(NOTES):
        with cols[idx]:
            st.markdown(
                f"""
                <div class="note-card">
                    <div class="note-num">0{idx + 1}.</div>
                    <div class="card-title">{note['title']}</div>
                    <p class="card-copy">{note['body']}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )


def stack_section() -> None:
    st.markdown(
        """
        <div class="section-kicker">Technology</div>
        <div class="section-title">What I actually reach for.</div>
        <p class="section-copy">Grouped by the kind of problem, not by language.</p>
        """,
        unsafe_allow_html=True,
    )
    cols = st.columns(3)
    groups = list(STACK_GROUPS.items())
    for i, col in enumerate(cols):
        with col:
            for title, items in groups[i::3]:
                items_html = "".join(f"<div class='stack-item'>{item}</div>" for item in items)
                st.markdown(
                    f"""
                    <div class="stack-card stack-group">
                        <div class="stack-head">{title}</div>
                        {items_html}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )


def context_section() -> None:
    st.markdown(
        """
        <div class="section-kicker">Useful Context</div>
        <div class="section-title">Where I fit best.</div>
        <p class="section-copy">The work makes more sense with a little context around education, current internship experience, and the teams I can help most.</p>
        """,
        unsafe_allow_html=True,
    )
    col1, col2, col3 = st.columns(3)
    cards = [
        ("Education", "B.Tech in Computer Science Engineering, AI and ML specialization, University of Mumbai. Expected graduation: 2027."),
        ("Current role", "Data Science with GenAI Intern at Innovexis — Python, data preprocessing, applied ML evaluation, and GenAI workflow components."),
        ("Best-fit teams", "Early-stage startups, AI-forward product companies, and engineering-led teams hiring for backend plus GenAI roles in India or remotely."),
    ]
    for col, (title, body) in zip((col1, col2, col3), cards):
        with col:
            st.markdown(
                f"""
                <div class="context-card">
                    <div class="card-title">{title}</div>
                    <p class="card-copy">{body}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )


def contact_section() -> None:
    st.markdown(
        """
        <div class="section-kicker">Contact</div>
        <div class="contact-shell">
            <div>
                <div class="contact-title">Start the right conversation.</div>
                <p class="contact-copy">
                    If your role needs someone who can own Python or Java backend work and connect it to practical AI systems,
                    send the role context and the problems the team is actually solving. I care about the engineering surface, not just the title.
                </p>
                <div style="display:flex; gap:0.7rem; flex-wrap:wrap; margin-top:1rem;">
                    <a class="primary-pill" href="mailto:shravanparthe@gmail.com?subject=Backend%20%2B%20GenAI%20role">Email for roles</a>
                    <a class="ghost-link" href="https://www.linkedin.com/in/shravan-parthe-00946b2ab/" target="_blank">LinkedIn</a>
                    <a class="ghost-link" href="https://github.com/Shravan157" target="_blank">GitHub</a>
                </div>
            </div>
            <div>
                <div class="cta-card">
                    <div class="card-title">For recruiters</div>
                    <p class="card-copy">Backend plus GenAI roles where ownership matters more than buzzwords.</p>
                </div>
                <div class="cta-card">
                    <div class="card-title">For collaborators</div>
                    <p class="card-copy">Fintech, healthtech, edtech, public data, or GenAI tooling for Indian users — especially where the workflow is messy and real.</p>
                </div>
                <div class="cta-card">
                    <div class="card-title">Resume</div>
                    <p class="card-copy">Available directly in this deployment when the PDF is present in assets/shravan_resume.pdf.</p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    cols = st.columns(3)
    with cols[0]:
        st.link_button("Email", "mailto:shravanparthe@gmail.com?subject=Hello%20Shravan", use_container_width=True)
    with cols[1]:
        st.link_button("LinkedIn", "https://www.linkedin.com/in/shravan-parthe-00946b2ab/", use_container_width=True)
    with cols[2]:
        if RESUME_PATH.exists():
            with RESUME_PATH.open("rb") as resume_file:
                st.download_button(
                    "Download resume",
                    data=resume_file,
                    file_name="shravan_resume.pdf",
                    mime="application/pdf",
                    use_container_width=True,
                )
        else:
            st.link_button("GitHub", "https://github.com/Shravan157", use_container_width=True)


def footer() -> None:
    st.markdown(
        """
        <div class="footer-line">
            <span>Shravan Parthe</span>
            <span>Mumbai, India · Remote-ready · 2026</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


def app() -> None:
    inject_css()
    top_nav()
    hero()
    st.markdown("<div style='height:2.5rem'></div>", unsafe_allow_html=True)
    work_bento()
    selected_case_detail()
    st.markdown("<div style='height:3rem'></div>", unsafe_allow_html=True)
    learning()
    st.markdown("<div style='height:3rem'></div>", unsafe_allow_html=True)
    stack_section()
    st.markdown("<div style='height:3rem'></div>", unsafe_allow_html=True)
    context_section()
    st.markdown("<div style='height:3rem'></div>", unsafe_allow_html=True)
    contact_section()
    footer()


if __name__ == "__main__":
    app()
