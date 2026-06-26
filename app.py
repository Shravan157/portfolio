from pathlib import Path

import streamlit as st


BASE_DIR = Path(__file__).parent
RESUME_PATH = BASE_DIR / "assets" / "shravan_resume.pdf"


st.set_page_config(
    page_title="Shravan Parthe | Engineering Journal",
    page_icon="🜲",
    layout="wide",
    initial_sidebar_state="collapsed",
)


CASES = {
    "SAHAY": {
        "deck": "Micro-credit underwriting for people who should not need to understand banking software to access small loans.",
        "market": "Fintech for underserved Indian borrowers",
        "role": "Full-stack backend and ML engineering",
        "stack": ["FastAPI", "Flutter", "Firebase", "Scikit-learn", "Tesseract OCR", "Stripe"],
        "repo": "https://github.com/Shravan157/Sahay-Loan",
        "signal": "Random Forest credit scoring reached 76 percent test accuracy over 19 selected borrower features. The loan workflow supports borrower, admin, and provider roles with digital KYC and EMI repayment.",
        "problem": (
            "I built SAHAY around a blunt problem: small borrowers lose time and confidence when loan systems assume paperwork, branch visits, and manual screening. "
            "The product needed to treat credit, identity, repayment, and provider review as one workflow instead of disconnected screens."
        ),
        "decision": (
            "I kept the mobile client in Flutter because the same codebase could cover phone-first usage and web demos. "
            "FastAPI handled the decision-heavy backend because Python made the ML, OCR, and payment services easier to compose. "
            "Firebase Auth and Firestore gave me real-time status updates without building a separate auth and notification stack. "
            "The scoring model used a Random Forest because explainability and stable tabular performance mattered more than chasing a black-box model."
        ),
        "challenge": (
            "The hard part was not a single API. It was making the loan state machine honest: KYC extraction, model scoring, admin review, provider decisions, repayment schedules, and notifications all had to agree on the same borrower state."
        ),
        "outcome": (
            "The result is a three-role lending platform where a borrower can apply up to INR 1,00,000, complete Aadhaar and PAN extraction through OCR, and move through approval and EMI repayment without manual KYC entry."
        ),
        "differently": (
            "I would now add a stronger audit trail for every model-assisted credit decision, separate risk-service versioning from the main API, and build a fairness report before showing the model as production-ready."
        ),
    },
    "SikshaSetu": {
        "deck": "A college portal that combines academic operations, live classes, and RAG-backed help inside one role-aware system.",
        "market": "Edtech for rural and underserved institutions",
        "role": "Java backend, React frontend, AI/RAG integration",
        "stack": ["Spring Boot", "Spring Security", "JWT", "React", "MySQL", "LangChain4j", "Qdrant", "ZEGOCLOUD"],
        "repo": "https://github.com/Shravan157/sikshasetu",
        "signal": "Built RBAC across student, faculty, and admin roles, modeled 10+ relational tables, and added virtual classroom plus notes RAG search.",
        "problem": (
            "Most college systems split academic work into separate tools: attendance somewhere, notes somewhere else, video class links in chat, and help requests handled manually. "
            "I wanted SikshaSetu to feel like one operating system for a college, especially where admin capacity is thin."
        ),
        "decision": (
            "I chose Spring Boot because the domain is permission-heavy and benefits from typed services, layered controllers, DTOs, and predictable security filters. "
            "JWT made the React client stateless. MySQL fit the academic schema. "
            "For AI, I used LangChain4j and Qdrant so uploaded notes could become searchable context instead of generic chatbot answers. "
            "ZEGOCLOUD tokens are generated server-side so classroom secrets never sit in the browser."
        ),
        "challenge": (
            "The core challenge was permission design. A student asking the assistant about portal navigation is harmless; a student asking for all users or faculty lists is not. "
            "The assistant had to be useful while respecting the same role boundaries as the normal APIs."
        ),
        "outcome": (
            "The portal now supports role dashboards, attendance, timetable, assignments, notes, results, events, notifications, streaming AI responses, document insight chat, Qdrant-backed notes RAG, and live virtual classrooms."
        ),
        "differently": (
            "I would split AI tooling into a separate service boundary, add background indexing jobs for notes instead of direct request-time indexing, and define richer integration tests around role leakage."
        ),
    },
    "PhonePe Insights": {
        "deck": "A public fintech data pipeline that turns transaction files into a queryable regional dashboard.",
        "market": "Public data and fintech analytics",
        "role": "Data engineering and dashboard development",
        "stack": ["Python", "Pandas", "MySQL", "SQLAlchemy", "PyMySQL", "Streamlit", "Plotly"],
        "repo": "https://github.com/Shravan157/phonepe-insights",
        "signal": "Processed 50,000+ PhonePe transaction records across 36 states, normalized 9 raw datasets into 5 relational tables, and delivered 10+ interactive charts.",
        "problem": (
            "The PhonePe dataset is valuable, but raw transaction files do not explain regional behavior by themselves. "
            "I wanted the dashboard to answer practical questions: where transaction volume is moving, which categories dominate, and how state-level adoption changes over time."
        ),
        "decision": (
            "I used Pandas for transformation because the source files needed cleaning and reshaping before SQL. "
            "MySQL gave the dashboard a durable analytical layer instead of repeatedly scanning files. "
            "SQLAlchemy and PyMySQL kept queries parameterized, while Streamlit and Plotly made the exploration fast enough for a reviewer to use without setup friction."
        ),
        "challenge": (
            "The main engineering problem was data shape. Transaction, user, and geography files carried related but differently structured information. "
            "The value came from normalizing them into tables that made filters and joins predictable."
        ),
        "outcome": (
            "The finished app reduced ad-hoc analysis into a dashboard path: choose state, year, quarter, and category, then inspect transaction trends, regional distribution, and payment behavior visually."
        ),
        "differently": (
            "I would now add a reproducible data validation layer, cache expensive dashboard queries, and define dbt-style transformation checks before loading data into MySQL."
        ),
    },
    "MedoraX": {
        "deck": "A multilingual clinical assistant that accepts voice, image, and text while clearly staying below the line of medical authority.",
        "market": "Healthtech access for non-English Indian users",
        "role": "AI pipeline and product workflow builder",
        "stack": ["Python", "Gradio", "Groq Whisper", "Llama models", "Google Maps API", "Google Air Quality API", "Edge TTS"],
        "repo": "https://github.com/Shravan157/MedX-AI-Clinical-Assistant",
        "signal": "Supports English, Hindi, and Marathi input/output, image analysis, nearby hospital search, AQI context, emergency detection, and text-to-speech responses.",
        "problem": (
            "Healthcare discovery breaks down quickly when the user cannot type symptoms comfortably, cannot explain an image, or needs help in a local language. "
            "I treated MedoraX as a triage assistant, not a doctor replacement."
        ),
        "decision": (
            "Gradio was the right demo surface because multimodal inputs are easier to ship there than in a heavier frontend. "
            "Groq Whisper handles speech-to-text, Llama models handle structured medical responses and image reasoning, and Google Maps/Places closes the loop when the answer should be: find care near you now."
        ),
        "challenge": (
            "The challenge was orchestration. Voice, image, text, map lookup, AQI, emergency keywords, and TTS all have different latency and failure modes. "
            "The app needed to keep the user moving even when one external service was slow."
        ),
        "outcome": (
            "The project demonstrates a full GenAI care-assistance pipeline with multilingual interaction, hospital discovery, and audio feedback for users who may not be comfortable with English-only text interfaces."
        ),
        "differently": (
            "I would add stronger clinical guardrails, source-grounded medical retrieval, offline fallback language packs, and red-team tests for unsafe medical advice."
        ),
    },
    "Bird Observation Analysis": {
        "deck": "A conservation-data dashboard for comparing forest and grassland observation patterns.",
        "market": "Environmental public data",
        "role": "Data cleaning, SQLite modeling, dashboarding",
        "stack": ["Python", "Pandas", "NumPy", "SQLite", "Plotly", "Streamlit"],
        "repo": "https://github.com/Shravan157/bird_project",
        "signal": "Combines forest and grassland datasets into a Streamlit dashboard with temporal, spatial, species-diversity, and environmental analysis.",
        "problem": (
            "Observation datasets are easy to collect and hard to reason about. "
            "I built this project to compare habitat patterns without forcing the viewer to inspect spreadsheets."
        ),
        "decision": (
            "Pandas and NumPy handled cleaning. SQLite kept the analysis lightweight and portable. "
            "Plotly and Streamlit were enough to make habitat, time, species, and environmental filters interactive without turning a data project into a web engineering project."
        ),
        "challenge": (
            "The technical challenge was making two ecosystem datasets comparable. Forest and grassland observations need shared fields, consistent cleaning, and clear filters before the dashboard can say anything useful."
        ),
        "outcome": (
            "The app turns raw observation files into conservation-oriented views across time, geography, species diversity, and environmental conditions."
        ),
        "differently": (
            "I would add data provenance notes, automated schema checks for incoming Excel files, and more explicit statistical confidence around conservation conclusions."
        ),
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


def inject_css() -> None:
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=IBM+Plex+Mono:wght@300;400;500&family=Inter:wght@300;400;500;600&display=swap');

        :root {
            --ink: #0c0c0c;
            --charcoal: #141414;
            --graphite: #1c1c1c;
            --stone: #2a2a2a;
            --muted: #7a7a7a;
            --silver: #b0b0b0;
            --paper: #e8e4df;
            --warm: #c4b5a0;
            --clay: #c17f59;
            --sage: #7d8f7a;
            --blue: #5a7a8c;
            --gold: #b8a070;
        }

        /* Hide Streamlit chrome */
        #MainMenu, header, footer, .stDeployButton { display: none !important; }
        [data-testid="stHeader"], [data-testid="stToolbar"] { display: none !important; }
        .stApp {
            background: var(--ink);
            color: var(--paper);
            font-family: 'Inter', sans-serif;
        }
        [data-testid="stAppViewContainer"] > .main .block-container {
            max-width: 1200px;
            padding: 0 3rem 4rem;
        }

        /* Typography */
        h1, h2, h3, h4, p, li, div, span { letter-spacing: 0; }
        h1 {
            font-family: 'Playfair Display', Georgia, serif;
            font-size: clamp(2.8rem, 6vw, 5.5rem);
            line-height: 0.95;
            font-weight: 400;
            color: var(--paper);
            margin: 0;
        }
        h2 {
            font-family: 'Playfair Display', Georgia, serif;
            font-size: clamp(1.8rem, 3.5vw, 3rem);
            line-height: 1.05;
            color: var(--paper);
            font-weight: 400;
            margin: 0 0 1rem 0;
        }
        h3 {
            font-family: 'Playfair Display', Georgia, serif;
            font-size: 1.6rem;
            line-height: 1.2;
            color: var(--paper);
            font-weight: 600;
            margin: 0 0 0.5rem 0;
        }
        h4 {
            font-family: 'Playfair Display', Georgia, serif;
            font-size: 1.15rem;
            line-height: 1.3;
            color: var(--paper);
            font-weight: 600;
            margin: 0 0 0.75rem 0;
        }
        p, li {
            font-size: 0.95rem;
            line-height: 1.75;
            color: var(--silver);
            font-weight: 300;
        }

        /* Kicker / Label */
        .kicker {
            font-family: 'IBM Plex Mono', monospace;
            font-size: 0.68rem;
            letter-spacing: 0.3em;
            text-transform: uppercase;
            color: var(--clay);
            margin-bottom: 1.5rem;
        }
        .section-label {
            font-family: 'IBM Plex Mono', monospace;
            font-size: 0.65rem;
            letter-spacing: 0.25em;
            text-transform: uppercase;
            color: var(--clay);
            margin-bottom: 1rem;
        }

        /* Hero */
        .hero-shell {
            min-height: 85vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            padding: 4rem 0 3rem;
            position: relative;
        }
        .hero-sub {
            font-size: clamp(1rem, 1.4vw, 1.2rem);
            line-height: 1.7;
            color: var(--silver);
            max-width: 620px;
            margin-top: 2rem;
            font-weight: 300;
        }
        .hero-meta-row {
            display: flex;
            gap: 4rem;
            margin-top: 4rem;
            flex-wrap: wrap;
        }
        .hero-meta-item {
            opacity: 0;
            animation: fadeUp 0.8s ease forwards;
        }
        .hero-meta-item:nth-child(1) { animation-delay: 0.6s; }
        .hero-meta-item:nth-child(2) { animation-delay: 0.75s; }
        .hero-meta-item:nth-child(3) { animation-delay: 0.9s; }
        .meta-label {
            font-family: 'IBM Plex Mono', monospace;
            font-size: 0.6rem;
            letter-spacing: 0.2em;
            text-transform: uppercase;
            color: var(--muted);
            margin-bottom: 0.4rem;
        }
        .meta-value {
            font-size: 0.85rem;
            color: var(--paper);
        }

        @keyframes fadeUp {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        @keyframes lineReveal {
            from { transform: translateY(100%); }
            to { transform: translateY(0); }
        }
        .line-wrap {
            overflow: hidden;
            display: block;
        }
        .line-inner {
            display: block;
            animation: lineReveal 1.2s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        }
        .line-wrap:nth-child(1) .line-inner { animation-delay: 0.1s; transform: translateY(100%); }
        .line-wrap:nth-child(2) .line-inner { animation-delay: 0.25s; transform: translateY(100%); }
        .line-wrap:nth-child(3) .line-inner { animation-delay: 0.4s; transform: translateY(100%); }

        /* Dividers */
        .divider {
            width: 100%;
            height: 1px;
            background: linear-gradient(90deg, var(--stone), transparent);
            margin: 0;
        }

        /* Case Selector Tabs */
        .stRadio > div {
            display: flex;
            gap: 0;
            border-bottom: 1px solid var(--stone);
            margin-bottom: 2.5rem;
            padding-bottom: 0;
        }
        .stRadio label {
            font-family: 'IBM Plex Mono', monospace !important;
            font-size: 0.75rem !important;
            letter-spacing: 0.15em !important;
            text-transform: uppercase !important;
            color: var(--muted) !important;
            padding: 1rem 1.5rem !important;
            border-bottom: 2px solid transparent !important;
            margin: 0 !important;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        .stRadio label:hover {
            color: var(--paper) !important;
        }
        .stRadio label[data-baseweb="radio"] p {
            color: inherit !important;
            font-weight: 400 !important;
        }
        .stRadio label span {
            display: none !important;
        }
        /* Active tab styling via Streamlit's checked state */
        .stRadio label:has(input:checked) {
            color: var(--clay) !important;
            border-bottom-color: var(--clay) !important;
            font-weight: 500 !important;
        }

        /* Case Card */
        .case-shell {
            border: 1px solid var(--stone);
            background: var(--charcoal);
            padding: 2.5rem;
            position: relative;
        }
        .case-shell::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 2px;
            background: linear-gradient(90deg, var(--clay), var(--sage));
        }
        .case-market {
            font-family: 'IBM Plex Mono', monospace;
            font-size: 0.7rem;
            letter-spacing: 0.15em;
            text-transform: uppercase;
            color: var(--muted);
            margin-bottom: 1.5rem;
            padding-bottom: 1.5rem;
            border-bottom: 1px solid var(--stone);
        }
        .case-deck {
            font-size: 1.1rem;
            line-height: 1.6;
            color: var(--silver);
            margin-bottom: 2.5rem;
            font-weight: 300;
        }

        /* Narrative Blocks */
        .narrative-block {
            margin-bottom: 2rem;
            padding-left: 1.5rem;
            border-left: 1px solid var(--stone);
            transition: border-color 0.3s ease;
        }
        .narrative-block:hover {
            border-left-color: var(--clay);
        }
        .narrative-label {
            font-family: 'IBM Plex Mono', monospace;
            font-size: 0.6rem;
            letter-spacing: 0.25em;
            text-transform: uppercase;
            color: var(--clay);
            margin-bottom: 0.6rem;
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }
        .narrative-label::before {
            content: '';
            display: inline-block;
            width: 16px;
            height: 1px;
            background: var(--clay);
        }
        .narrative-text {
            font-size: 0.92rem;
            line-height: 1.8;
            color: var(--silver);
            font-weight: 300;
        }

        /* Signal Box */
        .signal-box {
            background: var(--graphite);
            border: 1px solid var(--stone);
            padding: 1.8rem;
            margin-bottom: 1.5rem;
            position: relative;
        }
        .signal-box::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 2px;
            background: linear-gradient(90deg, var(--clay), var(--sage));
        }
        .signal-label {
            font-family: 'IBM Plex Mono', monospace;
            font-size: 0.6rem;
            letter-spacing: 0.2em;
            text-transform: uppercase;
            color: var(--clay);
            margin-bottom: 0.8rem;
        }
        .signal-text {
            font-family: 'Playfair Display', serif;
            font-size: 0.95rem;
            line-height: 1.6;
            color: var(--paper);
            font-style: italic;
        }

        /* Tags */
        .tag-row {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin: 1.2rem 0;
        }
        .tag {
            font-family: 'IBM Plex Mono', monospace;
            font-size: 0.65rem;
            padding: 0.35rem 0.75rem;
            border: 1px solid var(--stone);
            color: var(--silver);
            letter-spacing: 0.05em;
            transition: all 0.3s ease;
            background: transparent;
        }
        .tag:hover {
            border-color: var(--clay);
            color: var(--clay);
        }

        /* Buttons */
        .stButton > button, .stDownloadButton > button {
            border-radius: 0 !important;
            border: 1px solid var(--stone) !important;
            background: transparent !important;
            color: var(--paper) !important;
            min-height: 3rem !important;
            font-family: 'IBM Plex Mono', monospace !important;
            font-size: 0.75rem !important;
            letter-spacing: 0.15em !important;
            text-transform: uppercase !important;
            font-weight: 400 !important;
            transition: all 0.4s ease !important;
        }
        .stButton > button:hover, .stDownloadButton > button:hover {
            border-color: var(--clay) !important;
            background: var(--clay) !important;
            color: var(--ink) !important;
        }

        /* Link buttons */
        .stLinkButton > a {
            border-radius: 0 !important;
            border: 1px solid var(--stone) !important;
            background: transparent !important;
            color: var(--paper) !important;
            font-family: 'IBM Plex Mono', monospace !important;
            font-size: 0.75rem !important;
            letter-spacing: 0.15em !important;
            text-transform: uppercase !important;
            font-weight: 400 !important;
            transition: all 0.4s ease !important;
        }
        .stLinkButton > a:hover {
            border-color: var(--clay) !important;
            background: var(--clay) !important;
            color: var(--ink) !important;
        }

        /* Note Cards */
        .note-card {
            background: var(--charcoal);
            border: 1px solid var(--stone);
            padding: 2rem;
            height: 100%;
            transition: transform 0.4s ease, border-color 0.4s ease;
        }
        .note-card:hover {
            transform: translateY(-6px);
            border-color: var(--clay);
        }
        .note-number {
            font-family: 'IBM Plex Mono', monospace;
            font-size: 0.6rem;
            color: var(--clay);
            margin-bottom: 1.2rem;
            letter-spacing: 0.2em;
        }
        .note-title {
            font-family: 'Playfair Display', serif;
            font-size: 1.15rem;
            line-height: 1.35;
            margin-bottom: 0.75rem;
            color: var(--paper);
        }
        .note-body {
            font-size: 0.88rem;
            line-height: 1.7;
            color: var(--silver);
            font-weight: 300;
        }

        /* Context / Contact Cards */
        .context-card {
            position: relative;
            padding-top: 1.5rem;
        }
        .context-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 40px;
            height: 2px;
            background: var(--clay);
        }
        .context-label {
            font-family: 'IBM Plex Mono', monospace;
            font-size: 0.65rem;
            letter-spacing: 0.2em;
            text-transform: uppercase;
            color: var(--muted);
            margin-bottom: 0.8rem;
        }
        .context-text {
            font-size: 0.9rem;
            line-height: 1.7;
            color: var(--silver);
            font-weight: 300;
        }

        /* Contact block */
        .contact-block {
            position: relative;
            padding-top: 1.5rem;
        }
        .contact-block::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 50px;
            height: 2px;
            background: var(--clay);
        }
        .contact-title {
            font-family: 'Playfair Display', serif;
            font-size: 1.5rem;
            margin-bottom: 1rem;
            color: var(--paper);
        }
        .contact-text {
            font-size: 0.92rem;
            line-height: 1.8;
            color: var(--silver);
            margin-bottom: 1.5rem;
            font-weight: 300;
        }

        /* Social row */
        .social-row {
            display: flex;
            gap: 2rem;
            margin-top: 3rem;
            padding-top: 2rem;
            border-top: 1px solid var(--stone);
            flex-wrap: wrap;
        }

        /* Footer */
        .footer-line {
            width: 100%;
            height: 1px;
            background: var(--stone);
            margin: 2rem 0 1.5rem;
        }
        .footer-text {
            font-family: 'IBM Plex Mono', monospace;
            font-size: 0.65rem;
            color: var(--muted);
            letter-spacing: 0.1em;
        }

        /* Mobile */
        @media (max-width: 768px) {
            [data-testid="stAppViewContainer"] > .main .block-container {
                padding: 0 1.5rem 2rem;
            }
            .hero-meta-row { gap: 2rem; }
            .stRadio > div { flex-wrap: wrap; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def hero() -> None:
    st.markdown(
        """
        <div class="hero-shell">
            <div class="kicker">AI-Powered Backend Engineer — Mumbai, India</div>
            <h1>
                <span class="line-wrap"><span class="line-inner">I build backend systems</span></span>
                <span class="line-wrap"><span class="line-inner">where AI has to</span></span>
                <span class="line-wrap"><span class="line-inner" style="color: #c17f59;"><em>earn its place.</em></span></span>
            </h1>
            <p class="hero-sub">
                Final-year AI/ML engineering student. This is not a coursework list. 
                The useful signal is how I think through messy systems: credit decisions, 
                college workflows, public fintech data, medical triage, and retrieval boundaries.
            </p>
            <div class="hero-meta-row">
                <div class="hero-meta-item">
                    <div class="meta-label">Current</div>
                    <div class="meta-value">Data Science with GenAI Intern at Innovexis</div>
                </div>
                <div class="hero-meta-item">
                    <div class="meta-label">Stack</div>
                    <div class="meta-value">Python, Java, Spring Boot, FastAPI, GenAI, RAG</div>
                </div>
                <div class="hero-meta-item">
                    <div class="meta-label">Status</div>
                    <div class="meta-value">Remote-ready, graduating 2027</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def case_selector() -> str:
    st.markdown("<div class='section-label'>01 / Case Journal</div>", unsafe_allow_html=True)
    st.markdown("<h2 style='margin-bottom:2.5rem;'>The decision trail matters more than the shipped app.</h2>", unsafe_allow_html=True)

    names = list(CASES.keys())
    return st.radio(
        "Select case",
        names,
        horizontal=True,
        label_visibility="collapsed",
    )


def tags(items: list[str]) -> str:
    return "<div class='tag-row'>" + "".join(f"<span class='tag'>{item}</span>" for item in items) + "</div>"


def narrative_block(label: str, text: str) -> None:
    st.markdown(
        f"""
        <div class="narrative-block">
            <div class="narrative-label">{label}</div>
            <p class="narrative-text">{text}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_case(name: str) -> None:
    case = CASES[name]

    st.markdown(
        f"""
        <div class="case-shell">
            <div class="case-market">{case["market"]}</div>
            <h3>{name}</h3>
            <p class="case-deck">{case["deck"]}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    left, right = st.columns([1.6, 0.9], gap="large")

    with left:
        narrative_block("Problem I was actually solving", case["problem"])
        narrative_block("Engineering decision", case["decision"])
        narrative_block("Core technical challenge", case["challenge"])
        narrative_block("Measurable outcome", case["outcome"])
        narrative_block("What I would do differently now", case["differently"])

    with right:
        st.markdown(
            f"""
            <div class="signal-box">
                <div class="signal-label">Reviewer Signal</div>
                <p class="signal-text">{case["signal"]}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(f"<div class='narrative-label' style='margin-bottom:1rem;'>Stack</div>{tags(case['stack'])}", unsafe_allow_html=True)
        st.link_button("Open repository →", case["repo"], use_container_width=True)


def case_summary_grid() -> None:
    st.markdown("<div style='margin-top:4rem;'></div>", unsafe_allow_html=True)
    st.markdown("<div class='section-label'>Workbench</div>", unsafe_allow_html=True)
    st.markdown("<h2 style='margin-bottom:2rem;'>All threads, at a glance.</h2>", unsafe_allow_html=True)

    cols = st.columns(3)
    for idx, (name, case) in enumerate(CASES.items()):
        with cols[idx % 3]:
            st.markdown(
                f"""
                <div class="note-card" style="margin-bottom:1rem;">
                    <div class="note-number">CASE 0{idx + 1}</div>
                    <h4 style="font-size:1.1rem; margin-bottom:0.5rem;">{name}</h4>
                    <p style="font-size:0.85rem; color:#b0b0b0; margin-bottom:0.75rem; line-height:1.6;">{case["deck"]}</p>
                    <p style="font-family:'IBM Plex Mono',monospace; font-size:0.6rem; color:#7a7a7a; text-transform:uppercase; letter-spacing:0.1em; margin-bottom:1rem;">{case["market"]}</p>
                    {tags(case["stack"][:4])}
                </div>
                """,
                unsafe_allow_html=True,
            )


def render_learning() -> None:
    st.markdown("<div style='margin-top:5rem;'></div>", unsafe_allow_html=True)
    st.markdown("<div class='divider' style='margin-bottom:3rem;'></div>", unsafe_allow_html=True)
    st.markdown("<div class='section-label'>02 / Field Notes</div>", unsafe_allow_html=True)
    st.markdown("<h2 style='margin-bottom:2.5rem;'>Learning in progress.<br>Wet paint, honest gaps.</h2>", unsafe_allow_html=True)

    cols = st.columns(3)
    for idx, note in enumerate(NOTES):
        with cols[idx]:
            st.markdown(
                f"""
                <div class="note-card" style="{'margin-top:2rem;' if idx == 1 else ('margin-top:1rem;' if idx == 2 else '')}">
                    <div class="note-number">NOTE 0{idx + 1}</div>
                    <div class="note-title">{note["title"]}</div>
                    <p class="note-body">{note["body"]}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )


def render_context() -> None:
    st.markdown("<div style='margin-top:5rem;'></div>", unsafe_allow_html=True)
    st.markdown("<div class='divider' style='margin-bottom:3rem;'></div>", unsafe_allow_html=True)
    st.markdown("<div class='section-label'>03 / Context</div>", unsafe_allow_html=True)
    st.markdown("<h2 style='margin-bottom:2.5rem;'>Useful background for the right conversation.</h2>", unsafe_allow_html=True)

    cols = st.columns(3)
    contexts = [
        ("Education", "B.Tech in Computer Science Engineering, AI and ML specialization, University of Mumbai. Expected graduation: 2027."),
        ("Current Signal", "Data Science with GenAI Intern at Innovexis, working with Python, data preprocessing, applied ML evaluation, and GenAI workflow components."),
        ("Best-Fit Teams", "Early-stage startups, AI-forward product companies, and engineering-led teams hiring for backend plus GenAI roles in India or remotely."),
    ]
    for idx, (label, text) in enumerate(contexts):
        with cols[idx]:
            st.markdown(
                f"""
                <div class="context-card">
                    <div class="context-label">{label}</div>
                    <p class="context-text">{text}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )


def render_contact() -> None:
    st.markdown("<div style='margin-top:5rem;'></div>", unsafe_allow_html=True)
    st.markdown("<div class='divider' style='margin-bottom:3rem;'></div>", unsafe_allow_html=True)
    st.markdown("<div class='section-label'>04 / Contact</div>", unsafe_allow_html=True)
    st.markdown("<h2 style='margin-bottom:2.5rem;'>Start the right conversation.</h2>", unsafe_allow_html=True)

    recruiter, collaborator = st.columns(2, gap="large")

    with recruiter:
        st.markdown(
            """
            <div class="contact-block">
                <h3 class="contact-title">For Recruiters</h3>
                <p class="contact-text">
                If your role needs someone who can own Python or Java backend work and connect it to practical AI systems, send the role context and the problems the team is solving. I care about the engineering surface, not just the title.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.link_button("Email for roles →", "mailto:shravanparthe@gmail.com?subject=Backend%20%2B%20GenAI%20role", use_container_width=True)

    with collaborator:
        st.markdown(
            """
            <div class="contact-block">
                <h3 class="contact-title">For Collaborators</h3>
                <p class="contact-text">
                If you are building in fintech, healthtech, edtech, public data, or GenAI tooling for Indian users, send the workflow and where the system currently breaks. I am most useful when the problem is real.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.link_button("Email for collaboration →", "mailto:shravanparthe@gmail.com?subject=Collaboration%20idea", use_container_width=True)

    st.markdown("<div class='social-row'>", unsafe_allow_html=True)
    soc1, soc2, soc3 = st.columns(3)
    with soc1:
        st.link_button("LinkedIn", "https://www.linkedin.com/in/shravan-parthe-00946b2ab/", use_container_width=True)
    with soc2:
        st.link_button("GitHub", "https://github.com/Shravan157", use_container_width=True)
    with soc3:
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
            st.caption("Resume file not available in this deployment.")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="footer-line"></div>
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:1rem;">
            <span class="footer-text">SHRAVAN PARTHE — 2026</span>
            <span class="footer-text">BUILT WITH INTENT. NO TEMPLATES.</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


def main() -> None:
    inject_css()
    hero()
    st.markdown("<div class='divider' style='margin:2rem 0;'></div>", unsafe_allow_html=True)
    selected = case_selector()
    render_case(selected)
    case_summary_grid()
    render_learning()
    render_context()
    render_contact()


if __name__ == "__main__":
    main()
