from pathlib import Path

import streamlit as st


BASE_DIR = Path(__file__).parent
RESUME_PATH = BASE_DIR / "assets" / "shravan_resume.pdf"


st.set_page_config(
    page_title="Shravan Parthe | Backend + AI Case Archive",
    page_icon="SP",
    layout="wide",
    initial_sidebar_state="collapsed",
)


CARD_COLOR_CLASS = {
    "SAHAY": "color-clay",
    "SikshaSetu": "color-blue",
    "PhonePe Insights": "color-gold",
    "MedoraX": "color-sage",
    "Bird Observation Analysis": "color-forest",
}


CASES = {
    "SAHAY": {
        "code": "01",
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
        "code": "02",
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
        "code": "03",
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
        "code": "04",
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
        "code": "05",
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
        @import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Inter:wght@400;500;600;700;800&display=swap');

        :root {
            --ink: #17211d;
            --muted: #5d6963;
            --paper: #fbfaf6;
            --panel: #ffffff;
            --line: #d9ddd3;
            --sage: #637d69;
            --clay: #b75533;
            --blue: #315b78;
            --gold: #b88a2f;
            --forest: #4a7c59;
        }

        .stApp {
            background:
                radial-gradient(ellipse 80% 50% at 15% -10%, rgba(183, 85, 51, 0.08) 0%, transparent 62%),
                radial-gradient(ellipse 65% 42% at 90% 110%, rgba(49, 91, 120, 0.07) 0%, transparent 60%),
                linear-gradient(90deg, rgba(23, 33, 29, 0.04) 1px, transparent 1px),
                linear-gradient(0deg, rgba(23, 33, 29, 0.03) 1px, transparent 1px),
                var(--paper);
            background-size: auto, auto, 32px 32px, 32px 32px, auto;
            color: var(--ink);
        }

        [data-testid="stHeader"],
        [data-testid="stToolbar"] {
            display: none;
        }

        [data-testid="stAppViewContainer"] > .main .block-container {
            max-width: 1220px;
            padding: 2rem 1.15rem 4rem;
        }

        h1, h2, h3, p, li, div, span {
            letter-spacing: 0;
        }

        h2 {
            font-family: 'DM Serif Display', Georgia, "Times New Roman", serif;
            font-size: clamp(1.55rem, 3.5vw, 3rem);
            line-height: 1.05;
            color: var(--ink);
        }

        h3 {
            font-size: 1.02rem;
            line-height: 1.28;
            color: var(--ink);
        }

        p, li {
            font-size: 1rem;
            line-height: 1.72;
            color: var(--muted);
        }

        a {
            color: var(--blue) !important;
            text-decoration: none;
            border-bottom: 1px solid rgba(49, 91, 120, 0.28);
            transition: border-color 0.18s ease;
        }

        a:hover {
            border-color: var(--blue);
        }

        /* MAIN ARCHIVE LANDING */

        .casefile-landing {
            min-height: 78vh;
            display: grid;
            grid-template-columns: 0.9fr 1.65fr;
            border: 1px solid var(--line);
            background: rgba(255, 255, 255, 0.82);
            margin-bottom: 2.4rem;
            overflow: hidden;
        }

        .casefile-left {
            border-right: 1px solid var(--line);
            padding: clamp(1.2rem, 3vw, 2.2rem);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            background:
                linear-gradient(180deg, rgba(23, 33, 29, 0.04), transparent),
                rgba(251, 250, 246, 0.92);
        }

        .casefile-right {
            padding: clamp(1.4rem, 4vw, 3.6rem);
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        .small-label {
            text-transform: uppercase;
            font-size: 0.78rem;
            font-weight: 800;
            letter-spacing: 0.11em;
            color: var(--clay);
            font-family: Inter, system-ui, sans-serif;
        }

        .archive-code {
            font-family: 'DM Serif Display', Georgia, serif;
            font-size: clamp(3rem, 8vw, 7.5rem);
            line-height: 0.9;
            color: var(--ink);
            margin: 3rem 0 1rem;
        }

        .archive-text {
            max-width: 390px;
            color: var(--muted);
            font-size: 1rem;
            line-height: 1.75;
        }

        .mini-index {
            display: grid;
            gap: 0.75rem;
            margin-top: 2rem;
            border-top: 1px solid var(--line);
            padding-top: 1rem;
        }

        .mini-index div {
            display: flex;
            gap: 0.8rem;
            align-items: center;
            font-size: 0.9rem;
            color: var(--ink);
            font-weight: 600;
            font-family: Inter, system-ui, sans-serif;
        }

        .mini-index span {
            color: var(--clay);
            font-size: 0.78rem;
            font-weight: 800;
        }

        .case-stamp {
            width: fit-content;
            border: 1px solid var(--ink);
            padding: 0.35rem 0.7rem;
            text-transform: uppercase;
            font-size: 0.72rem;
            font-weight: 800;
            letter-spacing: 0.09em;
            margin-bottom: 1.2rem;
            color: var(--ink);
            font-family: Inter, system-ui, sans-serif;
        }

        .casefile-right h1 {
            font-family: 'DM Serif Display', Georgia, serif;
            font-size: clamp(2.2rem, 5.7vw, 5.75rem);
            line-height: 0.95;
            max-width: 920px;
            margin: 0;
            color: var(--ink);
        }

        .evidence-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 0;
            border-top: 1px solid var(--line);
            border-left: 1px solid var(--line);
            margin-top: 2.3rem;
        }

        .evidence-grid > div {
            border-right: 1px solid var(--line);
            border-bottom: 1px solid var(--line);
            padding: 1rem;
        }

        .evidence-grid strong {
            display: block;
            color: var(--ink);
            font-size: 0.84rem;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            margin-bottom: 0.4rem;
            font-family: Inter, system-ui, sans-serif;
        }

        .evidence-grid p {
            margin: 0;
            font-size: 0.92rem;
            line-height: 1.55;
        }

        /* CASE SWITCHBOARD */

        .switchboard {
            border: 1px solid var(--line);
            background: rgba(255, 255, 255, 0.78);
            padding: 1rem;
            margin-bottom: 1.5rem;
        }

        .switchboard-top {
            display: flex;
            justify-content: space-between;
            gap: 1rem;
            align-items: center;
            border-bottom: 1px solid var(--line);
            padding-bottom: 0.8rem;
            margin-bottom: 0.8rem;
        }

        .switchboard-title {
            font-weight: 800;
            text-transform: uppercase;
            color: var(--ink);
            letter-spacing: 0.08em;
            font-size: 0.82rem;
            font-family: Inter, system-ui, sans-serif;
        }

        .switchboard-subtitle {
            color: var(--muted);
            font-size: 0.85rem;
        }

        [data-testid="stRadio"] {
            background: transparent;
        }

        [data-testid="stRadio"] label p {
            color: var(--ink);
            font-weight: 700;
            font-size: 0.9rem;
        }

        /* SECTION HEAD */

        .section-head {
            display: flex;
            align-items: center;
            gap: 1rem;
            margin: 2.6rem 0 1.4rem;
        }

        .section-head h2 {
            margin: 0;
            white-space: nowrap;
        }

        .section-head-line {
            flex: 1;
            height: 1px;
            background: linear-gradient(90deg, var(--line) 0%, transparent 100%);
        }

        /* CASE DETAIL */

        .case-detail-shell {
            border: 1px solid var(--line);
            background: rgba(255, 255, 255, 0.86);
            padding: clamp(1rem, 2.2vw, 1.5rem);
            margin-bottom: 2rem;
        }

        .case-title {
            display: grid;
            grid-template-columns: 4.5rem 1fr;
            gap: 1rem;
            border-bottom: 1px solid var(--line);
            padding-bottom: 1.2rem;
            margin-bottom: 1.1rem;
        }

        .case-number {
            width: 4.1rem;
            height: 4.1rem;
            border: 1px solid var(--ink);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.4rem;
            color: var(--ink);
            font-weight: 800;
            font-family: Inter, system-ui, sans-serif;
        }

        .case-title h2 {
            margin: 0 0 0.35rem;
        }

        .case-title p {
            margin: 0;
        }

        .kicker {
            text-transform: uppercase;
            font-weight: 800;
            color: var(--clay);
            font-size: 0.76rem;
            letter-spacing: 0.1em;
            display: inline-flex;
            align-items: center;
            gap: 0.48rem;
            font-family: Inter, system-ui, sans-serif;
            margin-bottom: 0.55rem;
        }

        .kicker-dot {
            width: 7px;
            height: 7px;
            background: var(--clay);
            border-radius: 50%;
            display: inline-block;
            flex-shrink: 0;
            animation: pulse-dot 2.2s ease-in-out infinite;
        }

        @keyframes pulse-dot {
            0%, 100% {
                transform: scale(1);
                opacity: 1;
            }

            50% {
                transform: scale(1.55);
                opacity: 0.55;
            }
        }

        .tag-row {
            display: flex;
            flex-wrap: wrap;
            gap: 0.38rem;
            margin: 0.9rem 0 0;
        }

        .tag {
            background: rgba(23, 33, 29, 0.05);
            border: 1px solid rgba(23, 33, 29, 0.1);
            padding: 0.2rem 0.62rem;
            font-size: 0.74rem;
            color: var(--ink);
            border-radius: 100px;
            font-weight: 500;
            letter-spacing: 0.02em;
            font-family: Inter, system-ui, sans-serif;
            transition: background 0.15s ease, border-color 0.15s ease;
        }

        .tag:hover {
            background: rgba(23, 33, 29, 0.1);
            border-color: rgba(23, 33, 29, 0.22);
        }

        .narrative-block {
            border-bottom: 1px solid var(--line);
            padding: 1.1rem 0;
            display: grid;
            grid-template-columns: 2.4rem 1fr;
            gap: 1rem;
            align-items: start;
        }

        .narrative-block:last-child {
            border-bottom: 0;
        }

        .narrative-step {
            width: 2.4rem;
            height: 2.4rem;
            background: var(--ink);
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.67rem;
            font-weight: 800;
            flex-shrink: 0;
            margin-top: 0.1rem;
            letter-spacing: 0.04em;
            font-family: Inter, system-ui, sans-serif;
            transition: background 0.2s ease;
        }

        .narrative-block:hover .narrative-step {
            background: var(--clay);
        }

        .narrative-block .label {
            color: var(--clay);
            font-weight: 800;
            text-transform: uppercase;
            font-size: 0.72rem;
            margin-bottom: 0.3rem;
            letter-spacing: 0.09em;
            font-family: Inter, system-ui, sans-serif;
        }

        .bench-card {
            border: 1px solid var(--line);
            background: linear-gradient(155deg, rgba(255,255,255,0.96) 0%, rgba(99, 125, 105, 0.08) 100%);
            padding: 1.2rem 1rem;
            position: relative;
            margin-bottom: 1rem;
        }

        .bench-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            bottom: 0;
            width: 3px;
            background: var(--sage);
        }

        .bench-card strong,
        .case-card strong,
        .note-card strong,
        .contact-card strong {
            display: block;
            margin-bottom: 0.42rem;
            color: var(--ink);
            font-size: 0.94rem;
        }

        .bench-card p,
        .case-card p,
        .note-card p,
        .contact-card p {
            margin-bottom: 0;
        }

        /* EVIDENCE BOARD */

        .case-card {
            border: 1px solid var(--line);
            background: var(--panel);
            padding: 1.2rem 1rem 1.1rem;
            min-height: 100%;
            position: relative;
            overflow: hidden;
            transition: transform 0.22s ease, box-shadow 0.22s ease, border-color 0.22s ease;
        }

        .case-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 10px 30px rgba(23, 33, 29, 0.09);
            border-color: rgba(23, 33, 29, 0.22);
        }

        .case-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
        }

        .color-clay::before {
            background: var(--clay);
        }

        .color-blue::before {
            background: var(--blue);
        }

        .color-gold::before {
            background: var(--gold);
        }

        .color-sage::before {
            background: var(--sage);
        }

        .color-forest::before {
            background: var(--forest);
        }

        .meta {
            color: var(--muted);
            font-size: 0.86rem;
        }

        /* NOTES + CONTACT */

        .note-card,
        .contact-card {
            border: 1px solid var(--line);
            background: var(--panel);
            padding: 1.2rem 1rem;
            min-height: 100%;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }

        .note-card:hover,
        .contact-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 22px rgba(23, 33, 29, 0.08);
        }

        .note-card {
            position: relative;
            overflow: hidden;
        }

        .note-card::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            height: 2px;
            background: linear-gradient(90deg, var(--gold) 0%, transparent 65%);
        }

        /* BUTTONS */

        .stButton > button,
        .stDownloadButton > button {
            border-radius: 0;
            border: 1.5px solid var(--ink);
            background: transparent;
            color: var(--ink);
            min-height: 2.8rem;
            font-weight: 800;
            letter-spacing: 0.06em;
            font-size: 0.82rem;
            text-transform: uppercase;
            transition: background 0.22s ease, color 0.22s ease, border-color 0.22s ease;
            font-family: Inter, system-ui, sans-serif;
        }

        .stButton > button:hover,
        .stDownloadButton > button:hover {
            border-color: var(--clay);
            background: var(--clay);
            color: white;
        }

        @media (max-width: 820px) {
            [data-testid="stAppViewContainer"] > .main .block-container {
                padding-top: 1rem;
            }

            .casefile-landing {
                grid-template-columns: 1fr;
                min-height: auto;
            }

            .casefile-left {
                border-right: 0;
                border-bottom: 1px solid var(--line);
            }

            .evidence-grid {
                grid-template-columns: 1fr;
            }

            .switchboard-top {
                display: block;
            }

            .case-title {
                grid-template-columns: 1fr;
            }

            .case-number {
                width: 3.5rem;
                height: 3.5rem;
            }

            .narrative-block {
                grid-template-columns: 1fr;
            }

            .narrative-step {
                display: none;
            }

            .section-head h2 {
                font-size: 1.55rem;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def tags(items: list[str]) -> str:
    return (
        "<div class='tag-row'>"
        + "".join(f"<span class='tag'>{item}</span>" for item in items)
        + "</div>"
    )


def section_header(title: str) -> None:
    st.markdown(
        f"""
        <div class="section-head">
            <h2>{title}</h2>
            <div class="section-head-line"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def narrative_block(label: str, text: str, step: int) -> None:
    st.markdown(
        f"""
        <div class="narrative-block">
            <div class="narrative-step">{str(step).zfill(2)}</div>
            <div class="narrative-content">
                <div class="label">{label}</div>
                <p>{text}</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def header() -> None:
    st.markdown(
        """
        <div class="casefile-landing">
            <div class="casefile-left">
                <div>
                    <div class="small-label">Case Archive / Backend + AI Systems</div>
                    <div class="archive-code">SP-2027</div>
                    <p class="archive-text">
                        A collection of systems built across lending, education, healthcare,
                        public data, and retrieval-based AI. This is not arranged as a resume.
                        It is arranged as evidence.
                    </p>
                </div>

                <div class="mini-index">
                    <div><span>01</span> Credit workflows</div>
                    <div><span>02</span> College systems</div>
                    <div><span>03</span> Public data pipelines</div>
                    <div><span>04</span> Multilingual AI assistance</div>
                    <div><span>05</span> Environmental dashboards</div>
                </div>
            </div>

            <div class="casefile-right">
                <div class="case-stamp">Backend systems / AI only where useful</div>

                <h1>
                    Systems where the backend carries the product,
                    and AI is only added when it improves the workflow.
                </h1>

                <div class="evidence-grid">
                    <div>
                        <strong>Primary stack</strong>
                        <p>Java, Spring Boot, Python, FastAPI, MySQL, Streamlit, RAG</p>
                    </div>
                    <div>
                        <strong>Working style</strong>
                        <p>Build the workflow first. Add AI only where retrieval, prediction, or automation helps.</p>
                    </div>
                    <div>
                        <strong>Best signal</strong>
                        <p>Projects are written as decisions, tradeoffs, and outcomes instead of only feature lists.</p>
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def case_selector() -> str:
    st.markdown(
        """
        <div class="switchboard">
            <div class="switchboard-top">
                <div class="switchboard-title">Open a case file</div>
                <div class="switchboard-subtitle">Select one system and inspect the problem, decision, challenge, outcome, and future improvement.</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    names = list(CASES.keys())

    return st.radio(
        "Case files",
        names,
        horizontal=True,
        label_visibility="collapsed",
    )


def render_case(name: str) -> None:
    case = CASES[name]

    st.markdown('<div class="case-detail-shell">', unsafe_allow_html=True)

    st.markdown(
        f"""
        <div class="case-title">
            <div class="case-number">{case["code"]}</div>
            <div>
                <span class="kicker"><span class="kicker-dot"></span>{case["market"]}</span>
                <h2>{name}</h2>
                <p>{case["deck"]}</p>
                {tags(case["stack"])}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    left, right = st.columns([1.55, 0.85], gap="large")

    with left:
        narrative_block("Problem I was actually solving", case["problem"], 1)
        narrative_block("Engineering decision", case["decision"], 2)
        narrative_block("Core technical challenge", case["challenge"], 3)
        narrative_block("Measurable outcome", case["outcome"], 4)
        narrative_block("What I would do differently now", case["differently"], 5)

    with right:
        st.markdown(
            f"""
            <div class="bench-card">
                <strong>Reviewer signal</strong>
                <p>{case["signal"]}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
            <div class="bench-card">
                <strong>Role in this build</strong>
                <p>{case["role"]}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.link_button("Open repository", case["repo"], use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)


def case_summary_grid() -> None:
    section_header("Evidence Board")

    cols = st.columns(3)

    for idx, (name, case) in enumerate(CASES.items()):
        color_cls = CARD_COLOR_CLASS.get(name, "color-clay")

        with cols[idx % 3]:
            st.markdown(
                f"""
                <div class="case-card {color_cls}">
                    <strong>{case["code"]} / {name}</strong>
                    <p>{case["deck"]}</p>
                    <p class="meta">{case["market"]}</p>
                    {tags(case["stack"][:4])}
                </div>
                """,
                unsafe_allow_html=True,
            )


def render_learning() -> None:
    section_header("Engineering Notes")

    st.markdown(
        """
        <p>
            This section is intentionally not a skill trophy shelf. It tracks the parts of the system that still need
            stronger engineering: retrieval quality, service boundaries, logging, testing, deployment notes, and model decision records.
        </p>
        """,
        unsafe_allow_html=True,
    )

    cols = st.columns(3)

    for idx, note in enumerate(NOTES):
        with cols[idx]:
            st.markdown(
                f"""
                <div class="note-card">
                    <strong>{note["title"]}</strong>
                    <p>{note["body"]}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )


def render_profile_strip() -> None:
    section_header("Context")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="contact-card">
                <strong>Education pointer</strong>
                <p>B.Tech in Computer Science Engineering, AI and ML specialization, University of Mumbai. Expected graduation: 2027.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="contact-card">
                <strong>Current work signal</strong>
                <p>Data Science with GenAI Intern at Innovexis, working with Python, data preprocessing, applied ML evaluation, and GenAI workflow components.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
            <div class="contact-card">
                <strong>Best-fit teams</strong>
                <p>Early-stage startups, AI-forward product companies, and engineering-led teams hiring for backend plus GenAI roles in India or remotely.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_contact() -> None:
    section_header("Contact")

    recruiter, collaborator = st.columns(2, gap="large")

    with recruiter:
        st.markdown(
            """
            <div class="contact-card">
                <strong>For recruiters</strong>
                <p>
                    If your role needs someone who can own Python or Java backend work and connect it to practical AI systems,
                    send the role context and the problems the team is solving.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.link_button(
            "Email for roles",
            "mailto:shravanparthe@gmail.com?subject=Backend%20%2B%20GenAI%20role",
            use_container_width=True,
        )

    with collaborator:
        st.markdown(
            """
            <div class="contact-card">
                <strong>For collaborators</strong>
                <p>
                    If you are building in fintech, healthtech, edtech, public data, or GenAI tooling for Indian users,
                    send the workflow and where the system currently breaks.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.link_button(
            "Email for collaboration",
            "mailto:shravanparthe@gmail.com?subject=Collaboration%20idea",
            use_container_width=True,
        )

    st.markdown("<div style='height:0.6rem'></div>", unsafe_allow_html=True)

    social1, social2, social3 = st.columns(3)

    social1.link_button(
        "LinkedIn",
        "https://www.linkedin.com/in/shravan-parthe-00946b2ab/",
        use_container_width=True,
    )

    social2.link_button(
        "GitHub",
        "https://github.com/Shravan157",
        use_container_width=True,
    )

    if RESUME_PATH.exists():
        with RESUME_PATH.open("rb") as resume_file:
            social3.download_button(
                "Download resume",
                data=resume_file,
                file_name="shravan_resume.pdf",
                mime="application/pdf",
                use_container_width=True,
            )
    else:
        social3.caption("Resume file is not available in this deployment.")


def main() -> None:
    inject_css()
    header()

    selected = case_selector()
    render_case(selected)

    case_summary_grid()
    render_learning()
    render_profile_strip()
    render_contact()


if __name__ == "__main__":
    main()
