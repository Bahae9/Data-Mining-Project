"""
DataMine Studio — Fouille de Données Interface
Mini-Projet FD1 · Faculté d'Informatique · 2025-2026
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

st.set_page_config(
    page_title="DataMine Studio",
    page_icon="⬡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ══════════════════════════════════════════════════════════════════════════════
#  GLOBAL CSS  — light editorial theme (Nunito + clean cards, purple accent)
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@300;400;600;700;800;900&family=Fira+Code:wght@400;500&display=swap');

:root {
  --bg:        #f8f7ff;
  --surface:   #f0eeff;
  --card:      #ffffff;
  --border:    #e2deff;
  --accent:    #6c47ff;
  --a2:        #ff6b6b;
  --a3:        #22c55e;
  --a4:        #f59e0b;
  --text:      #1e1b3a;
  --muted:     #7c7a9e;
  --shadow:    0 4px 20px rgba(108,71,255,0.08);
  --shadow-lg: 0 8px 40px rgba(108,71,255,0.14);
}

/* ── Base ── */
html, body, [data-testid="stAppViewContainer"] {
    background: var(--bg) !important;
    color: var(--text) !important;
    font-family: 'Nunito', sans-serif !important;
}
[data-testid="stHeader"] { background: transparent !important; }
[data-testid="stSidebar"] { display: none !important; }
.block-container { padding: 0 2rem 4rem !important; max-width: 1280px !important; margin: 0 auto !important; }
[data-testid="stAppViewContainer"] > .main { padding-top: 0 !important; }

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: var(--surface); }
::-webkit-scrollbar-thumb { background: var(--border); border-radius: 4px; }

/* ── Buttons ── */
.stButton > button {
    background: var(--accent) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 50px !important;
    font-family: 'Nunito', sans-serif !important;
    font-weight: 800 !important;
    font-size: .88rem !important;
    padding: .55rem 1.6rem !important;
    transition: all .2s !important;
    box-shadow: 0 4px 14px rgba(108,71,255,.28) !important;
    letter-spacing: .01em !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 22px rgba(108,71,255,.42) !important;
}
.stButton > button:active { transform: translateY(0) !important; }

/* ── Form widgets ── */
.stTextInput > div > div > input,
.stTextArea textarea,
.stNumberInput > div > div > input {
    background: var(--card) !important;
    color: var(--text) !important;
    border: 1.5px solid var(--border) !important;
    border-radius: 12px !important;
    font-family: 'Nunito', sans-serif !important;
    font-weight: 600 !important;
}
.stTextInput > div > div > input:focus { border-color: var(--accent) !important; box-shadow: 0 0 0 3px rgba(108,71,255,.1) !important; }

/* Selectbox + dropdown text */
.stSelectbox > div > div,
.stMultiSelect > div > div {
    background: var(--card) !important;
    border: 1.5px solid var(--border) !important;
    border-radius: 12px !important;
    color: var(--text) !important;
    font-family: 'Nunito', sans-serif !important;
}
/* Dropdown selected value text */
.stSelectbox [data-baseweb="select"] > div,
.stSelectbox [data-baseweb="select"] span,
.stMultiSelect [data-baseweb="select"] > div,
.stMultiSelect [data-baseweb="select"] span { color: var(--text) !important; font-family: 'Nunito', sans-serif !important; }
/* Dropdown popup list items */
[data-baseweb="popover"] li,
[data-baseweb="popover"] [role="option"],
[data-baseweb="menu"] li,
[data-baseweb="menu"] [role="option"],
ul[data-baseweb="menu"] li { color: var(--text) !important; background: var(--card) !important; font-family: 'Nunito', sans-serif !important; font-weight: 600 !important; }
[data-baseweb="popover"] li:hover,
[data-baseweb="menu"] li:hover { background: var(--surface) !important; }
/* Dropdown popup container */
[data-baseweb="popover"],
[data-baseweb="popover"] > div { background: var(--card) !important; border: 1.5px solid var(--border) !important; border-radius: 12px !important; }
/* Multiselect tags */
.stMultiSelect [data-baseweb="tag"] { background: rgba(108,71,255,.12) !important; color: var(--accent) !important; border-radius: 50px !important; }
.stMultiSelect [data-baseweb="tag"] span { color: var(--accent) !important; }
/* Number input arrows */
.stNumberInput button { color: var(--text) !important; background: var(--surface) !important; border-color: var(--border) !important; }

/* Slider */
.stSlider [data-baseweb="slider"] { color: var(--accent) !important; }
.stSlider [data-testid="stTickBar"] > div { color: var(--muted) !important; font-size: .75rem !important; }
/* Slider value label */
.stSlider [role="slider"] { background: var(--accent) !important; }

/* Radio + Checkbox */
.stRadio label, .stCheckbox label { font-family: 'Nunito', sans-serif !important; font-weight: 700 !important; color: var(--text) !important; }
.stRadio > div > div > label > div:first-child > div { border-color: var(--border) !important; }
.stRadio > div > div > label > div:first-child > div[aria-checked="true"] { background: var(--accent) !important; border-color: var(--accent) !important; }

/* Tabs */
[data-baseweb="tab-list"] { background: var(--surface) !important; border-radius: 10px !important; padding: 3px !important; }
[data-baseweb="tab"] { color: var(--muted) !important; font-family: 'Nunito', sans-serif !important; font-weight: 700 !important; border-radius: 8px !important; }
[data-baseweb="tab"][aria-selected="true"] { color: var(--accent) !important; background: var(--card) !important; }
[data-baseweb="tab-highlight"] { background: var(--card) !important; }
[data-baseweb="tab-border"] { background: transparent !important; }

/* Expander */
[data-testid="stExpander"] { background: var(--card) !important; border: 1.5px solid var(--border) !important; border-radius: 12px !important; }
[data-testid="stExpander"] summary { color: var(--text) !important; font-weight: 700 !important; font-family: 'Nunito', sans-serif !important; }
[data-testid="stExpander"] summary:hover { color: var(--accent) !important; }

/* File uploader */
[data-testid="stFileUploader"] { background: var(--card) !important; border: 2px dashed var(--border) !important; border-radius: 12px !important; }
[data-testid="stFileUploader"] label, [data-testid="stFileUploader"] span, [data-testid="stFileUploader"] p { color: var(--muted) !important; font-family: 'Nunito', sans-serif !important; }
[data-testid="stFileUploaderFileName"] { color: var(--text) !important; font-weight: 700 !important; }

/* Spinner */
[data-testid="stSpinner"] > div { color: var(--accent) !important; }

/* General text catch-all for any missed elements */
.stMarkdown p, .stMarkdown li, .stMarkdown span { color: var(--text) !important; }
label[data-testid="stWidgetLabel"] { color: var(--text) !important; font-weight: 700 !important; font-family: 'Nunito', sans-serif !important; font-size: .88rem !important; }

/* ── NUCLEAR TEXT FIX: force ALL text to be readable ── */
/* Scope to Streamlit's main app container only — avoids touching browser chrome */
[data-testid="stAppViewContainer"] { color: var(--text) !important; }
[data-testid="stMain"] p,
[data-testid="stMain"] span:not([data-baseweb="tag"] span),
[data-testid="stMain"] label,
[data-testid="stMain"] li,
[data-testid="stMain"] td,
[data-testid="stMain"] th { color: var(--text) !important; }
/* Specific overrides for elements that still escape */
[data-testid="stMarkdownContainer"] * { color: var(--text) !important; }
[data-testid="stMarkdownContainer"] strong { color: var(--text) !important; font-weight: 800 !important; }
[data-testid="stMarkdownContainer"] a { color: var(--accent) !important; }
/* All widget labels */
[data-testid="stWidgetLabel"] p { color: var(--text) !important; font-weight: 700 !important; }
[data-testid="stWidgetLabel"] span { color: var(--text) !important; }
/* Selectbox: all inner text */
[data-baseweb="select"] * { color: var(--text) !important; }
[data-baseweb="select"] [data-baseweb="input"] { color: var(--text) !important; }
/* Dropdown list items — both light and any forced-dark */
[role="listbox"] { background: var(--card) !important; border: 1.5px solid var(--border) !important; border-radius: 12px !important; }
[role="option"] { color: var(--text) !important; background: var(--card) !important; }
[role="option"] * { color: var(--text) !important; }
[role="option"]:hover { background: var(--surface) !important; }
[aria-selected="true"][role="option"] { background: rgba(108,71,255,.08) !important; color: var(--accent) !important; }
/* Multiselect tags */
[data-baseweb="tag"] { background: rgba(108,71,255,.12) !important; border-radius: 50px !important; }
[data-baseweb="tag"] span { color: var(--accent) !important; font-weight: 700 !important; }
/* Number input text */
input[type="number"] { color: var(--text) !important; background: var(--card) !important; }
/* Sliders — only color the text labels, never touch internal div backgrounds */
[data-testid="stSlider"] [data-testid="stTickBarMin"],
[data-testid="stSlider"] [data-testid="stTickBarMax"] { color: var(--muted) !important; font-size: .75rem !important; }
[data-testid="stSlider"] [role="slider"] { background: var(--accent) !important; border-color: var(--accent) !important; }
[data-testid="stSlider"] [data-baseweb="slider"] [class*="Track"] > div:first-child { background: var(--accent) !important; }
/* Slider tooltip value */
[data-testid="stSlider"] [role="slider"] + div { background: var(--accent) !important; color: #fff !important; border-radius: 6px !important; font-weight: 700 !important; }
/* Radio items */
[data-testid="stRadio"] p { color: var(--text) !important; font-weight: 700 !important; }
[data-testid="stRadio"] label { color: var(--text) !important; }
/* Checkbox */
[data-testid="stCheckbox"] p { color: var(--text) !important; font-weight: 700 !important; }
[data-testid="stCheckbox"] label { color: var(--text) !important; }
/* Tabs */
[data-baseweb="tab-list"] { background: var(--surface) !important; border-radius: 10px !important; padding: 3px !important; border: 1.5px solid var(--border) !important; }
[data-baseweb="tab"] { color: var(--muted) !important; font-weight: 700 !important; border-radius: 8px !important; }
[data-baseweb="tab"][aria-selected="true"] { color: var(--accent) !important; background: var(--card) !important; box-shadow: var(--shadow) !important; }
[data-baseweb="tab"] p { color: inherit !important; }
/* Expander */
details { background: var(--card) !important; border: 1.5px solid var(--border) !important; border-radius: 12px !important; padding: .5rem !important; }
details summary { color: var(--text) !important; font-weight: 800 !important; cursor: pointer !important; padding: .5rem !important; }
details summary:hover { color: var(--accent) !important; }
details summary p { color: inherit !important; font-weight: inherit !important; }
details > div { padding: .5rem !important; }
/* File uploader */
[data-testid="stFileUploader"] section { background: var(--card) !important; border: 2px dashed var(--border) !important; border-radius: 12px !important; }
[data-testid="stFileUploader"] * { color: var(--muted) !important; }
[data-testid="stFileUploaderFileName"] { color: var(--text) !important; font-weight: 700 !important; }
[data-testid="stFileUploadDropzone"] button { background: var(--surface) !important; color: var(--accent) !important; border: 1.5px solid var(--accent) !important; border-radius: 50px !important; }
/* Spinner text */
[data-testid="stSpinner"] p { color: var(--muted) !important; }
/* DataFrame / table */
.stDataFrame { border: 1.5px solid var(--border) !important; border-radius: 12px !important; overflow: hidden !important; }
.stDataFrame * { color: var(--text) !important; }
/* Code blocks */
.stCode, .stCode * { color: var(--accent) !important; background: var(--surface) !important; }
pre code { color: var(--text) !important; }
/* Toast / alerts from streamlit */
[data-testid="stAlert"] { border-radius: 12px !important; }
[data-testid="stAlert"] p { color: inherit !important; }
/* Info/success/warning/error boxes */
.stSuccess, .stInfo, .stWarning, .stError { border-radius: 12px !important; }
/* Sidebar (hidden but just in case) */
section[data-testid="stSidebar"] { display: none !important; }

/* ── DataFrames ── */
.stDataFrame { border: 1.5px solid var(--border) !important; border-radius: 12px !important; overflow: hidden; }

/* ── Metrics ── */
[data-testid="metric-container"] {
    background: var(--card) !important;
    border: 1.5px solid var(--border) !important;
    border-radius: 14px !important;
    padding: 1rem 1.2rem !important;
    box-shadow: var(--shadow) !important;
}
[data-testid="metric-container"] label { color: var(--muted) !important; font-size: .78rem !important; font-weight: 700 !important; text-transform: uppercase; letter-spacing: .06em; }
[data-testid="metric-container"] [data-testid="metric-value"] { color: var(--accent) !important; font-weight: 900 !important; font-size: 1.5rem !important; }

/* ── Typography ── */
h1,h2,h3,h4,h5 { font-family: 'Nunito', sans-serif !important; font-weight: 900 !important; color: var(--text) !important; }
p, li, span, div { font-family: 'Nunito', sans-serif !important; }
code { font-family: 'Fira Code', monospace !important; background: var(--surface) !important; color: var(--accent) !important; padding: 2px 6px !important; border-radius: 5px !important; }

/* ══════════════════════════════════════════
   CUSTOM COMPONENTS
   ══════════════════════════════════════════ */

/* Top nav */
.dn-nav {
    background: var(--card);
    border-bottom: 2px solid var(--border);
    padding: 1rem 2.5rem;
    display: flex; align-items: center; justify-content: space-between;
    position: sticky; top: 0; z-index: 999;
}
.dn-brand { font-size: 1.3rem; font-weight: 900; color: var(--accent); letter-spacing: -0.5px; display:flex; align-items:center; gap:.4rem; }
.dn-brand .slash { color: var(--a2); }
.dn-tabs { display:flex; gap:.2rem; }
.dn-tab {
    padding: .45rem 1.1rem; border-radius: 50px;
    font-weight: 800; font-size: .84rem; color: var(--muted);
    border: 1.5px solid transparent; cursor: pointer; transition: all .15s;
    text-decoration: none !important;
}
.dn-tab.active { color: var(--accent); border-color: var(--accent); background: rgba(108,71,255,.08); }
.dn-tab:hover:not(.active) { color: var(--text); background: var(--surface); }

/* Page hero */
.dn-hero {
    background: linear-gradient(135deg, var(--accent) 0%, #9b71ff 60%, #c084fc 100%);
    border-radius: 20px;
    padding: 2rem 2.8rem;
    margin: 1.5rem 0 2rem;
    color: white;
    position: relative; overflow: hidden;
}
.dn-hero::before {
    content:''; position:absolute; top:-50%; right:-5%;
    width: 350px; height: 350px;
    background: rgba(255,255,255,.06); border-radius: 50%;
}
.dn-hero h2 { color: white !important; font-size: 1.7rem; margin: 0 0 .25rem; }
.dn-hero p  { color: rgba(255,255,255,.8) !important; margin: 0; font-size: .92rem; }
.dn-hero-tag {
    display: inline-block; background: rgba(255,255,255,.18);
    border: 1px solid rgba(255,255,255,.3);
    border-radius: 50px; padding: 3px 12px;
    font-size: .76rem; font-weight: 800; color: white !important;
    margin-bottom: .6rem; letter-spacing: .04em;
}

/* Section header */
.dn-section {
    display: flex; align-items: center; gap: .7rem;
    font-size: .72rem; font-weight: 900; text-transform: uppercase;
    letter-spacing: .1em; color: var(--muted);
    margin: 2rem 0 1rem; padding-bottom: .6rem;
    border-bottom: 2px solid var(--border);
}
.dn-section .pip {
    width: 8px; height: 8px; border-radius: 50%;
    background: var(--accent); display: inline-block; flex-shrink: 0;
}

/* Card */
.dn-card {
    background: var(--card);
    border: 1.5px solid var(--border);
    border-radius: 16px;
    padding: 1.4rem 1.6rem;
    box-shadow: var(--shadow);
    margin-bottom: 1rem;
}
.dn-card-sm { padding: 1rem 1.2rem; border-radius: 12px; }

/* Pill badges */
.dn-badge {
    display: inline-block; padding: 3px 11px; border-radius: 50px;
    font-size: .73rem; font-weight: 800; letter-spacing: .03em;
}
.dn-blue   { background: rgba(108,71,255,.1); color: var(--accent); border: 1.5px solid rgba(108,71,255,.25); }
.dn-green  { background: rgba(34,197,94,.1);  color: #15803d;       border: 1.5px solid rgba(34,197,94,.25); }
.dn-red    { background: rgba(255,107,107,.1); color: #c0392b;      border: 1.5px solid rgba(255,107,107,.25); }
.dn-yellow { background: rgba(245,158,11,.1); color: #92400e;       border: 1.5px solid rgba(245,158,11,.25); }

/* Alert boxes */
.dn-alert {
    border-radius: 12px; padding: .9rem 1.2rem;
    font-size: .88rem; font-weight: 700; margin: .4rem 0;
    border-left: 4px solid;
}
.dn-alert-ok  { background: rgba(34,197,94,.08);  border-color: #22c55e; color: #15803d; }
.dn-alert-warn{ background: rgba(245,158,11,.08);  border-color: #f59e0b; color: #92400e; }
.dn-alert-err { background: rgba(255,107,107,.08); border-color: #ff6b6b; color: #c0392b; }
.dn-alert-info{ background: rgba(108,71,255,.06);  border-color: var(--accent); color: var(--accent); }

/* Pipeline bar */
.dn-pipeline {
    display: flex; align-items: center; gap: .5rem;
    background: var(--surface); border: 1.5px solid var(--border);
    border-radius: 50px; padding: .5rem 1.2rem;
    margin-bottom: 1.2rem; flex-wrap: wrap;
}
.dn-step {
    font-size: .76rem; font-weight: 800;
    padding: 3px 10px; border-radius: 50px;
}
.dn-step-done { background: rgba(34,197,94,.15); color: #15803d; }
.dn-step-todo { background: rgba(124,122,158,.12); color: var(--muted); }
.dn-arr { color: var(--border); font-size: .8rem; }

/* Algo selector cards */
.dn-algo {
    background: var(--card); border: 2px solid var(--border);
    border-radius: 14px; padding: 1rem 1.2rem;
    text-align: center; cursor: default;
    transition: all .18s;
}
.dn-algo:hover { border-color: var(--accent); box-shadow: 0 4px 18px rgba(108,71,255,.12); }
.dn-algo.sel   { border-color: var(--accent); background: rgba(108,71,255,.04); }
.dn-algo .ico  { font-size: 1.8rem; margin-bottom: .3rem; }
.dn-algo .nm   { font-weight: 900; font-size: .88rem; color: var(--text); }
.dn-algo .ds   { font-size: .74rem; color: var(--muted); margin-top: .1rem; }

/* Footer */
.dn-footer {
    text-align: center; color: var(--muted); font-size: .78rem;
    padding: 2rem 0 1rem; margin-top: 3rem;
    border-top: 2px solid var(--border);
}
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  SESSION STATE
# ══════════════════════════════════════════════════════════════════════════════
_defaults = dict(
    page="preprocessing",
    df=None,
    df_clean=None,
    file_id=None,
    clean_done=False,
    norm_done=False,
)
for k, v in _defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

def nav(p): st.session_state.page = p

# ══════════════════════════════════════════════════════════════════════════════
#  TOP NAV
# ══════════════════════════════════════════════════════════════════════════════
PAGE = st.session_state.page
PAGES = [("preprocessing","🔧 Prétraitement"), ("clustering","🔵 Clustering"), ("classification","🎯 Classification")]

tabs_html = "".join(
    f'<span class="dn-tab {"active" if PAGE==pid else ""}">{lbl}</span>'
    for pid, lbl in PAGES
)
st.markdown(f"""
<div class="dn-nav">
  <div class="dn-brand">⬡ DataMine<span class="slash">/</span>Studio</div>
  <div class="dn-tabs">{tabs_html}</div>
  <div style="font-size:.78rem;color:var(--muted);font-weight:700">FD1 · 2025-26</div>
</div>
""", unsafe_allow_html=True)

nb1, nb2, nb3, _ = st.columns([1,1,1,7])
with nb1:
    if st.button("🔧 Prétraitement", key="n1", use_container_width=True): nav("preprocessing"); st.rerun()
with nb2:
    if st.button("🔵 Clustering",    key="n2", use_container_width=True): nav("clustering");   st.rerun()
with nb3:
    if st.button("🎯 Classification",key="n3", use_container_width=True): nav("classification");st.rerun()

st.markdown("<div style='height:.4rem'></div>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  MATPLOTLIB THEME HELPER
# ══════════════════════════════════════════════════════════════════════════════
PALETTE = ["#6c47ff","#ff6b6b","#22c55e","#f59e0b","#06b6d4","#ec4899","#84cc16","#f97316"]

def _fig(w=8, h=4.5):
    fig, ax = plt.subplots(figsize=(w, h), facecolor="#ffffff")
    ax.set_facecolor("#f8f7ff")
    for sp in ax.spines.values(): sp.set_color("#e2deff")
    ax.tick_params(colors="#7c7a9e", labelsize=8)
    ax.grid(alpha=0.35, color="#e2deff", linestyle="--")
    return fig, ax

def _style_ax(ax, title="", xlabel="", ylabel=""):
    ax.set_title(title, color="#1e1b3a", fontsize=12, fontweight="bold", pad=10)
    ax.set_xlabel(xlabel, color="#7c7a9e", fontsize=9)
    ax.set_ylabel(ylabel, color="#7c7a9e", fontsize=9)

def section(label):
    st.markdown(f'<div class="dn-section"><span class="pip"></span>{label}</div>', unsafe_allow_html=True)

def alert(msg, kind="info"):
    cls = {"ok":"dn-alert-ok","warn":"dn-alert-warn","err":"dn-alert-err","info":"dn-alert-info"}.get(kind,"dn-alert-info")
    st.markdown(f'<div class="dn-alert {cls}">{msg}</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  PAGE 1 — PRÉTRAITEMENT
# ══════════════════════════════════════════════════════════════════════════════
if PAGE == "preprocessing":
    st.markdown("""
    <div class="dn-hero">
      <div class="dn-hero-tag">VOLET 01</div>
      <h2>🔧 Prétraitement des Données</h2>
      <p>Chargement · Exploration · Valeurs manquantes · Outliers · Normalisation · Visualisation</p>
    </div>""", unsafe_allow_html=True)

    # ── Pipeline status ────────────────────────────────────────────────────────
    loaded  = st.session_state.df_clean is not None
    cleaned = st.session_state.clean_done
    normed  = st.session_state.norm_done

    def _step(done, lbl):
        cls = "dn-step-done" if done else "dn-step-todo"
        ico = "✓ " if done else "○ "
        return f'<span class="dn-step {cls}">{ico}{lbl}</span>'

    no_missing = loaded and int(st.session_state.df_clean.isnull().sum().sum()) == 0
    st.markdown(f"""
    <div class="dn-pipeline">
      <span style="font-size:.72rem;font-weight:900;color:var(--muted);letter-spacing:.08em">PIPELINE</span>
      {_step(loaded,"Chargé")}
      <span class="dn-arr">›</span>
      {_step(cleaned or no_missing,"Nettoyé")}
      <span class="dn-arr">›</span>
      {_step(normed,"Normalisé")}
    </div>""", unsafe_allow_html=True)

    # ── 01. Import ─────────────────────────────────────────────────────────────
    section("01 — Importation du Dataset")

    uploaded = st.file_uploader(
        "Fichier CSV, Excel, TSV, Parquet…",
        type=["csv","xlsx","xls","tsv","parquet","json"],
        label_visibility="collapsed"
    )

    if uploaded:
        fid = f"{uploaded.name}_{uploaded.size}"
        if fid != st.session_state.file_id:
            try:
                ext = uploaded.name.rsplit(".",1)[-1].lower()
                readers = {"csv": pd.read_csv, "tsv": lambda f: pd.read_csv(f, sep="\t"),
                           "xlsx": pd.read_excel, "xls": pd.read_excel,
                           "parquet": pd.read_parquet, "json": pd.read_json}
                df_raw = readers.get(ext, pd.read_csv)(uploaded)
                st.session_state.df = df_raw
                st.session_state.df_clean = df_raw.copy()
                st.session_state.file_id = fid
                st.session_state.clean_done = False
                st.session_state.norm_done = False
                alert(f"✅ <b>{uploaded.name}</b> chargé — {df_raw.shape[0]} lignes × {df_raw.shape[1]} colonnes", "ok")
            except Exception as e:
                alert(f"❌ Erreur de chargement : {e}", "err")
        else:
            alert(f"✅ Dataset actif : <b>{uploaded.name}</b> — {st.session_state.df_clean.shape[0]} lignes × {st.session_state.df_clean.shape[1]} colonnes", "ok")

    df = st.session_state.df_clean

    if df is not None:
        r1c1, r1c2 = st.columns([1,1])
        if r1c1.button("🔄 Réinitialiser le dataset"):
            st.session_state.df_clean = st.session_state.df.copy()
            st.session_state.clean_done = False
            st.session_state.norm_done = False
            st.session_state.file_id = None
            st.rerun()

        # ── 02. Exploration ───────────────────────────────────────────────────
        section("02 — Exploration & Statistiques Descriptives")

        m1,m2,m3,m4 = st.columns(4)
        m1.metric("Lignes",             df.shape[0])
        m2.metric("Colonnes",           df.shape[1])
        m3.metric("Valeurs manquantes", int(df.isnull().sum().sum()))
        m4.metric("Colonnes num.",      int(df.select_dtypes(include=np.number).shape[1]))

        t1,t2,t3 = st.tabs(["📋 Aperçu des données","📊 Statistiques","🔤 Types & Nulls"])
        with t1:
            st.dataframe(df.head(50), use_container_width=True)
        with t2:
            st.dataframe(df.describe(include="all").T, use_container_width=True)
        with t3:
            tdf = pd.DataFrame({
                "Colonne": df.columns,
                "Type": df.dtypes.astype(str).values,
                "Non-nuls": df.count().values,
                "Nuls": df.isnull().sum().values,
                "% Nuls": (df.isnull().mean()*100).round(2).values,
                "Uniques": df.nunique().values,
            })
            st.dataframe(tdf.set_index("Colonne"), use_container_width=True)

        # ── 03. Visualisation valeurs manquantes ──────────────────────────────
        section("03 — Visualisation des Valeurs Manquantes")

        null_counts = df.isnull().sum()
        null_counts = null_counts[null_counts > 0]

        if len(null_counts) == 0:
            alert("✅ Aucune valeur manquante dans le dataset", "ok")
        else:
            alert(f"⚠️ <b>{int(null_counts.sum())}</b> valeur(s) manquante(s) dans <b>{len(null_counts)}</b> colonne(s)", "warn")
            if st.button("📊 Afficher graphique des valeurs manquantes"):
                fig, ax = _fig(10, max(3, len(null_counts)*0.45))
                pcts = (null_counts / len(df) * 100)
                colors_bar = [PALETTE[0] if p < 10 else PALETTE[1] if p < 30 else PALETTE[2] for p in pcts]
                bars = ax.barh(null_counts.index, pcts, color=colors_bar, edgecolor="white", linewidth=0.5, height=0.6)
                for bar, cnt, pct in zip(bars, null_counts, pcts):
                    ax.text(pct + 0.3, bar.get_y() + bar.get_height()/2,
                            f"{cnt} ({pct:.1f}%)", va="center", fontsize=8, fontweight="bold", color="#1e1b3a")
                _style_ax(ax, "Valeurs Manquantes par Colonne", "% de valeurs manquantes", "")
                ax.set_xlim(0, max(pcts)*1.2)
                ax.invert_yaxis()
                st.pyplot(fig); plt.close(fig)

        # ── 04. Nettoyage ─────────────────────────────────────────────────────
        section("04 — Traitement des Valeurs Manquantes")

        if st.session_state.clean_done:
            alert("✅ Nettoyage déjà appliqué", "ok")

        null_cols = df.columns[df.isnull().any()].tolist()
        if null_cols:
            c_s, c_b = st.columns([4,1])
            with c_s:
                strategy = st.radio(
                    "Stratégie",
                    ["Supprimer les lignes","Moyenne","Médiane","Mode","Valeur fixe"],
                    horizontal=True, label_visibility="collapsed"
                )
                fill_val = None
                if strategy == "Valeur fixe":
                    fill_val = st.number_input("Valeur de remplacement", value=0.0, key="fill_val")
            with c_b:
                st.markdown("<div style='height:2px'></div>", unsafe_allow_html=True)
                do_clean = st.button("Nettoyer ✓", key="clean_btn")

            if do_clean:
                df_c = st.session_state.df_clean.copy()
                num_c = df_c.select_dtypes(include=np.number).columns.tolist()
                cat_c = df_c.select_dtypes(exclude=np.number).columns.tolist()
                if strategy == "Supprimer les lignes":
                    df_c = df_c.dropna()
                elif strategy == "Moyenne":
                    if num_c: df_c[num_c] = df_c[num_c].fillna(df_c[num_c].mean())
                    for col in cat_c:
                        m = df_c[col].mode(); df_c[col] = df_c[col].fillna(m[0] if not m.empty else "Unknown")
                elif strategy == "Médiane":
                    if num_c: df_c[num_c] = df_c[num_c].fillna(df_c[num_c].median())
                    for col in cat_c:
                        m = df_c[col].mode(); df_c[col] = df_c[col].fillna(m[0] if not m.empty else "Unknown")
                elif strategy == "Mode":
                    for col in df_c.columns:
                        m = df_c[col].mode()
                        if not m.empty: df_c[col] = df_c[col].fillna(m[0])
                else:
                    for col in num_c: df_c[col] = df_c[col].fillna(fill_val)
                    for col in cat_c: df_c[col] = df_c[col].fillna(str(fill_val))
                rem = int(df_c.isnull().sum().sum())
                st.session_state.df_clean = df_c
                st.session_state.clean_done = True
                st.session_state.norm_done = False
                alert(f"✅ Nettoyage appliqué ({strategy}). Valeurs manquantes restantes : <b>{rem}</b>", "ok")
                st.rerun()
        else:
            alert("✅ Aucune valeur manquante — nettoyage non requis", "ok")

        df = st.session_state.df_clean
        num_cols_all = df.select_dtypes(include=np.number).columns.tolist()

        # ── 05. Outliers ──────────────────────────────────────────────────────
        section("05 — Détection & Traitement des Valeurs Aberrantes (IQR)")

        if num_cols_all:
            c_oc1, c_oc2 = st.columns([3,1])
            with c_oc1:
                out_cols = st.multiselect("Colonnes à analyser", num_cols_all, default=num_cols_all[:min(6,len(num_cols_all))], key="out_cols")
            with c_oc2:
                iqr_mult = st.number_input("Multiplicateur IQR", value=1.5, min_value=0.5, max_value=5.0, step=0.5, key="iqr_m")

            if out_cols:
                outlier_report = []
                for col in out_cols:
                    Q1, Q3 = df[col].quantile(0.25), df[col].quantile(0.75)
                    IQR = Q3 - Q1
                    lb, ub = Q1 - iqr_mult*IQR, Q3 + iqr_mult*IQR
                    n_out = int(((df[col] < lb) | (df[col] > ub)).sum())
                    outlier_report.append({"Colonne": col, "Q1": round(Q1,3), "Q3": round(Q3,3),
                                           "IQR": round(IQR,3), "Borne inf.": round(lb,3),
                                           "Borne sup.": round(ub,3), "Outliers": n_out,
                                           "% Outliers": round(n_out/len(df)*100,2)})
                out_df = pd.DataFrame(outlier_report)
                total_out = out_df["Outliers"].sum()
                alert(f"🔍 <b>{int(total_out)}</b> outlier(s) détecté(s) sur {len(out_cols)} colonne(s)", "warn" if total_out>0 else "ok")
                st.dataframe(out_df.set_index("Colonne"), use_container_width=True)

                c_os1, c_os2 = st.columns([3,1])
                with c_os1:
                    out_strategy = st.radio("Traitement des outliers",
                        ["Aucun (conserver)","Supprimer les lignes outliers","Remplacer par les bornes (capping)"],
                        horizontal=True, key="out_strat", label_visibility="collapsed")
                with c_os2:
                    if st.button("Appliquer", key="out_btn") and out_strategy != "Aucun (conserver)":
                        df_c = st.session_state.df_clean.copy()
                        for col in out_cols:
                            Q1, Q3 = df_c[col].quantile(0.25), df_c[col].quantile(0.75)
                            IQR = Q3 - Q1
                            lb, ub = Q1 - iqr_mult*IQR, Q3 + iqr_mult*IQR
                            if out_strategy == "Supprimer les lignes outliers":
                                df_c = df_c[(df_c[col] >= lb) & (df_c[col] <= ub)]
                            else:
                                df_c[col] = df_c[col].clip(lb, ub)
                        st.session_state.df_clean = df_c
                        alert(f"✅ Outliers traités ({out_strategy}). Nouvelles dimensions : {df_c.shape[0]} × {df_c.shape[1]}", "ok")
                        st.rerun()

        df = st.session_state.df_clean
        num_cols_all = df.select_dtypes(include=np.number).columns.tolist()

        # ── 06. Normalisation ──────────────────────────────────────────────────
        section("06 — Normalisation")

        if st.session_state.norm_done:
            alert("✅ Normalisation déjà appliquée", "ok")

        nan_remain = int(df[num_cols_all].isnull().sum().sum()) if num_cols_all else 0
        if nan_remain > 0:
            alert(f"⚠️ <b>{nan_remain}</b> valeur(s) manquante(s) détectée(s) dans les colonnes numériques — effectuez le nettoyage d'abord", "warn")

        if num_cols_all:
            cn1, cn2 = st.columns([4,1])
            with cn1:
                norm_method = st.selectbox("Méthode", ["Min-Max Scaling [0,1]","Standardisation Z-score"], key="norm_meth")
                cols_to_norm = st.multiselect("Colonnes à normaliser", num_cols_all, default=num_cols_all, key="cols_norm")
            with cn2:
                st.markdown("<div style='height:2.8rem'></div>", unsafe_allow_html=True)
                do_norm = st.button("Normaliser ✓", key="norm_btn")

            if do_norm:
                if not cols_to_norm:
                    alert("⚠️ Sélectionnez au moins une colonne", "warn")
                elif nan_remain > 0:
                    alert("❌ Impossible : des valeurs manquantes sont présentes — nettoyez d'abord", "err")
                else:
                    df_c = st.session_state.df_clean.copy()
                    if norm_method.startswith("Min-Max"):
                        from sklearn.preprocessing import MinMaxScaler
                        sc = MinMaxScaler()
                    else:
                        from sklearn.preprocessing import StandardScaler
                        sc = StandardScaler()
                    df_c[cols_to_norm] = sc.fit_transform(df_c[cols_to_norm])
                    st.session_state.df_clean = df_c
                    st.session_state.norm_done = True
                    alert(f"✅ Normalisation <b>{norm_method}</b> appliquée sur <b>{len(cols_to_norm)}</b> colonne(s)", "ok")
                    st.rerun()

        df = st.session_state.df_clean
        num_cols_all = df.select_dtypes(include=np.number).columns.tolist()

        # ── 07. Visualisation ──────────────────────────────────────────────────
        section("07 — Visualisation")

        if len(num_cols_all) >= 1:
            vt1, vt2 = st.tabs(["📦 Boxplots","🔵 Scatter Plot"])

            with vt1:
                bv1, bv2 = st.columns([3,1])
                with bv1:
                    box_cols = st.multiselect("Colonnes pour boxplot", num_cols_all,
                                              default=num_cols_all[:min(5,len(num_cols_all))], key="box_cols")
                with bv2:
                    st.markdown("<div style='height:1.8rem'></div>", unsafe_allow_html=True)
                    show_box = st.button("📦 Afficher", key="box_btn")
                if show_box and box_cols:
                    n_cols_plot = min(3, len(box_cols))
                    n_rows_plot = (len(box_cols) + n_cols_plot - 1) // n_cols_plot
                    fig, axes = plt.subplots(n_rows_plot, n_cols_plot,
                                             figsize=(n_cols_plot*4, n_rows_plot*3.5),
                                             facecolor="#ffffff")
                    axes = np.array(axes).flatten()
                    for i, col in enumerate(box_cols):
                        ax = axes[i]
                        ax.set_facecolor("#f8f7ff")
                        bp = ax.boxplot(df[col].dropna(), patch_artist=True, widths=0.5,
                                        medianprops=dict(color=PALETTE[0], linewidth=2.5),
                                        boxprops=dict(facecolor=f"{PALETTE[0]}22", color=PALETTE[0]),
                                        whiskerprops=dict(color=PALETTE[0], linewidth=1.5),
                                        capprops=dict(color=PALETTE[0], linewidth=1.5),
                                        flierprops=dict(color=PALETTE[1], marker='o', markersize=4, alpha=0.6))
                        ax.set_title(col, color="#1e1b3a", fontsize=10, fontweight="bold")
                        ax.tick_params(colors="#7c7a9e", labelsize=8)
                        for sp in ax.spines.values(): sp.set_color("#e2deff")
                    for j in range(i+1, len(axes)): axes[j].set_visible(False)
                    plt.tight_layout()
                    st.pyplot(fig); plt.close(fig)

            with vt2:
                sv1, sv2, sv3 = st.columns(3)
                with sv1: sc_x = st.selectbox("Axe X", num_cols_all, key="sc_x")
                with sv2: sc_y = st.selectbox("Axe Y", num_cols_all, key="sc_y", index=min(1, len(num_cols_all)-1))
                with sv3:
                    cat_c = df.select_dtypes(exclude=np.number).columns.tolist()
                    color_by = st.selectbox("Couleur par", ["Aucun"]+cat_c, key="sc_col")
                if st.button("🔵 Afficher Scatter", key="sc_btn"):
                    fig, ax = _fig(9, 5)
                    if color_by != "Aucun" and color_by in df.columns:
                        cats = df[color_by].astype(str).unique()
                        for idx, cat in enumerate(cats):
                            mask = df[color_by].astype(str) == cat
                            ax.scatter(df.loc[mask, sc_x], df.loc[mask, sc_y],
                                       color=PALETTE[idx % len(PALETTE)], alpha=0.65, s=28,
                                       label=str(cat), edgecolors="white", linewidths=0.4)
                        ax.legend(fontsize=8, framealpha=0.9)
                    else:
                        ax.scatter(df[sc_x], df[sc_y], color=PALETTE[0], alpha=0.6, s=25,
                                   edgecolors="white", linewidths=0.4)
                    _style_ax(ax, f"Scatter : {sc_x} vs {sc_y}", sc_x, sc_y)
                    st.pyplot(fig); plt.close(fig)
    else:
        st.markdown("""
        <div class="dn-card" style="text-align:center;padding:3.5rem 2rem">
          <div style="font-size:3rem;margin-bottom:.8rem">📂</div>
          <div style="font-weight:900;font-size:1.1rem;color:var(--text)">Aucun dataset chargé</div>
          <div style="color:var(--muted);margin-top:.3rem;font-size:.88rem">Chargez un fichier CSV, Excel ou autre format tabulaire ci-dessus</div>
        </div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  PAGE 2 — CLUSTERING
# ══════════════════════════════════════════════════════════════════════════════
elif PAGE == "clustering":
    st.markdown("""
    <div class="dn-hero">
      <div class="dn-hero-tag">VOLET 02</div>
      <h2>🔵 Clustering Non Supervisé</h2>
      <p>K-Means · K-Medoids · DBSCAN · AGNES · DIANA — Silhouette · PCA 2D</p>
    </div>""", unsafe_allow_html=True)

    df = st.session_state.df_clean
    if df is None:
        alert("⚠️ Veuillez d'abord charger un dataset dans l'onglet <b>Prétraitement</b>", "warn"); st.stop()

    num_cols = df.select_dtypes(include=np.number).columns.tolist()
    if not num_cols:
        alert("❌ Aucune colonne numérique disponible.", "err"); st.stop()

    # ── Config ─────────────────────────────────────────────────────────────────
    section("Configuration")
    cf1, cf2 = st.columns(2)
    with cf1:
        feat_cols = st.multiselect("Features", num_cols, default=num_cols[:min(len(num_cols),8)], key="cl_feats")
    with cf2:
        pre_norm  = st.selectbox("Normalisation préalable",
                                  ["Aucune (déjà normalisé)","Min-Max [0,1]","Standardisation Z-score"], key="cl_pre")
    if not feat_cols: alert("Sélectionnez au moins une feature","warn"); st.stop()

    X_raw = df[feat_cols].dropna().values
    from sklearn.preprocessing import MinMaxScaler, StandardScaler
    if pre_norm.startswith("Min-Max"):
        X = MinMaxScaler().fit_transform(X_raw)
    elif pre_norm.startswith("Std"):
        X = StandardScaler().fit_transform(X_raw)
    else:
        X = X_raw.copy()
    N = len(X)

    from sklearn.decomposition import PCA
    from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score

    def get_2d(X):
        if X.shape[1] == 1: return np.hstack([X, np.zeros((len(X),1))])
        if X.shape[1] == 2: return X
        return PCA(n_components=2).fit_transform(X)

    def sil_safe(X, labels):
        u = [l for l in set(labels) if l >= 0]
        if len(u) < 2: return 0.0
        m = labels >= 0
        if m.sum() < 2: return 0.0
        try: return float(silhouette_score(X[m], labels[m]))
        except: return 0.0

    def db_safe(X, labels):
        u = [l for l in set(labels) if l >= 0]
        if len(u) < 2: return float("nan")
        m = labels >= 0
        try: return float(davies_bouldin_score(X[m], labels[m]))
        except: return float("nan")

    def ch_safe(X, labels):
        u = [l for l in set(labels) if l >= 0]
        if len(u) < 2: return float("nan")
        m = labels >= 0
        try: return float(calinski_harabasz_score(X[m], labels[m]))
        except: return float("nan")

    X_2d = get_2d(X)

    def plot_clusters(X_2d, labels, title, markers=None):
        fig, ax = _fig(9, 5.5)
        unique = sorted(set(labels))
        for i, lab in enumerate(unique):
            mask = labels == lab
            if lab == -1:
                ax.scatter(X_2d[mask,0], X_2d[mask,1], c="#cccccc", marker="x",
                           s=18, alpha=0.5, linewidths=1, label="Bruit")
            else:
                ax.scatter(X_2d[mask,0], X_2d[mask,1], color=PALETTE[i % len(PALETTE)],
                           s=22, alpha=0.72, edgecolors="white", linewidths=0.4,
                           label=f"Cluster {lab}")
        if markers is not None:
            ax.scatter(markers[:,0], markers[:,1], marker="*", s=280,
                       color="#f59e0b", zorder=10, edgecolors="white", linewidths=0.8, label="Centre")
        _style_ax(ax, title, "PCA 1", "PCA 2")
        ax.legend(fontsize=7.5, framealpha=0.9, loc="best",
                  markerscale=1.2, borderpad=0.7, handlelength=1.5)
        return fig

    def show_metrics(labels, k_label=""):
        sil = sil_safe(X, labels)
        db  = db_safe(X, labels)
        ch  = ch_safe(X, labels)
        n_cl = len([l for l in set(labels) if l >= 0])
        n_noise = int((labels == -1).sum())
        m1,m2,m3,m4,m5 = st.columns(5)
        m1.metric("Clusters", n_cl)
        m2.metric("Bruit", n_noise)
        m3.metric("Silhouette ↑", f"{sil:.4f}")
        m4.metric("Davies-Bouldin ↓", f"{db:.4f}" if not np.isnan(db) else "N/A")
        m5.metric("Calinski-Harabasz ↑", f"{ch:.1f}" if not np.isnan(ch) else "N/A")

    # ── Algo selector ─────────────────────────────────────────────────────────
    section("Choix de l'Algorithme")

    ALGOS = [
        ("K-Means",   "⚙️",  "Centroïdes, Elbow"),
        ("K-Medoids", "🎯",  "PAM, médoïdes"),
        ("DBSCAN",    "🌐",  "Densité, bruit"),
        ("AGNES",     "⬆️",  "Agglomératif"),
        ("DIANA",     "⬇️",  "Divisif"),
    ]
    algo = st.radio("", [a[0] for a in ALGOS], horizontal=True, key="cl_algo", label_visibility="collapsed")

    acols = st.columns(len(ALGOS))
    for (nm, ico, ds), col in zip(ALGOS, acols):
        with col:
            sel_class = " sel" if nm == algo else ""
            st.markdown(f"""<div class="dn-algo{sel_class}">
              <div class="ico">{ico}</div>
              <div class="nm">{nm}</div>
              <div class="ds">{ds}</div>
            </div>""", unsafe_allow_html=True)

    # ── Elbow (partition algos) ───────────────────────────────────────────────
    if algo in ["K-Means","K-Medoids","AGNES","DIANA"]:
        section("Courbe d'Elbow")
        el1, el2 = st.columns([4,1])
        with el2:
            k_max = st.slider("K max", 2, 20, 10, key="elbow_k")
            do_elbow = st.button("📈 Calculer", key="elbow_btn")
        with el1:
            if do_elbow:
                from sklearn.cluster import KMeans as SKM
                inertias, sils = [], []
                with st.spinner("Calcul Elbow…"):
                    for k in range(1, k_max+1):
                        km = SKM(n_clusters=k, random_state=42, n_init=10).fit(X)
                        inertias.append(km.inertia_)
                        if k >= 2:
                            sils.append(sil_safe(X, km.labels_))
                fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4), facecolor="#ffffff")
                for ax in [ax1, ax2]:
                    ax.set_facecolor("#f8f7ff")
                    for sp in ax.spines.values(): sp.set_color("#e2deff")
                    ax.tick_params(colors="#7c7a9e", labelsize=8)
                    ax.grid(alpha=0.3, color="#e2deff", linestyle="--")
                ax1.plot(range(1, k_max+1), inertias, "o-", color=PALETTE[0], lw=2.5, ms=7)
                _style_ax(ax1, "Courbe d'Elbow (Inertie)", "k", "WCSS")
                ax2.plot(range(2, k_max+1), sils, "o-", color=PALETTE[2], lw=2.5, ms=7)
                _style_ax(ax2, "Silhouette par k", "k", "Score Silhouette")
                plt.tight_layout()
                st.pyplot(fig); plt.close(fig)

    # ══ Individual algo UIs ═══════════════════════════════════════════════════

    # ── K-MEANS ───────────────────────────────────────────────────────────────
    if algo == "K-Means":
        section("Paramètres K-Means")
        p1,p2,p3 = st.columns(3)
        with p1: k_km = st.slider("k", 2, 20, 3, key="km_k")
        with p2: max_it= st.slider("Max itérations", 50, 500, 300, 50, key="km_it")
        with p3: init_km = st.selectbox("Init", ["k-means++","random"], key="km_init")
        if st.button("▶ Lancer K-Means", key="run_km"):
            from sklearn.cluster import KMeans as SKM
            with st.spinner("K-Means…"):
                km = SKM(n_clusters=k_km, max_iter=max_it, init=init_km, random_state=42, n_init=10)
                labels = km.fit_predict(X)
            section("Résultats K-Means")
            show_metrics(labels)
            centers_2d = PCA(n_components=2).fit(X).transform(km.cluster_centers_) if X.shape[1]>2 else km.cluster_centers_[:,:2]
            fig = plot_clusters(X_2d, labels, f"K-Means — k={k_km}", markers=centers_2d)
            st.pyplot(fig); plt.close(fig)

    # ── K-MEDOIDS ─────────────────────────────────────────────────────────────
    elif algo == "K-Medoids":
        section("Paramètres K-Medoids")
        p1,p2 = st.columns(2)
        with p1: k_km = st.slider("k", 2, 15, 3, key="kmed_k")
        with p2: kmed_m = st.selectbox("Méthode", ["pam","alternate"], key="kmed_m")
        if st.button("▶ Lancer K-Medoids", key="run_kmed"):
            with st.spinner("K-Medoids…"):
                try:
                    from sklearn_extra.cluster import KMedoids
                    kmed = KMedoids(n_clusters=k_km, method=kmed_m, random_state=42)
                    labels = kmed.fit_predict(X)
                    med_idx = kmed.medoid_indices_
                except ImportError:
                    # PAM from scratch (TP4)
                    from sklearn.metrics import pairwise_distances
                    D = pairwise_distances(X)
                    med_idx = np.random.choice(N, k_km, replace=False)
                    for _ in range(100):
                        labels = np.argmin(D[:, med_idx], axis=1)
                        new_meds = []
                        for c in range(k_km):
                            mask = labels == c
                            if mask.sum() == 0: new_meds.append(med_idx[c]); continue
                            sub = D[np.ix_(np.where(mask)[0], np.where(mask)[0])]
                            best = np.where(mask)[0][sub.sum(1).argmin()]
                            new_meds.append(best)
                        if sorted(new_meds) == sorted(med_idx.tolist()): break
                        med_idx = np.array(new_meds)
                    labels = np.argmin(D[:, med_idx], axis=1)
            section("Résultats K-Medoids")
            show_metrics(labels)
            meds_2d = X_2d[med_idx]
            fig = plot_clusters(X_2d, labels, f"K-Medoids — k={k_km}", markers=meds_2d)
            st.pyplot(fig); plt.close(fig)

    # ── DBSCAN ────────────────────────────────────────────────────────────────
    elif algo == "DBSCAN":
        section("Paramètres DBSCAN")
        alert("💡 Utilisez le graphique k-distance pour choisir ε optimal (prendre la valeur au coude)", "info")
        p1,p2,p3 = st.columns(3)
        with p1: eps_v = st.number_input("ε (epsilon)", 0.01, 20.0, 0.5, 0.05, key="db_eps")
        with p2: minpts = st.slider("MinPts", 2, 30, 5, key="db_mp")
        with p3: db_impl = st.selectbox("Implémentation", ["Sklearn (rapide)","From Scratch (TP3)"], key="db_impl")

        if st.button("📊 Graphique k-distance", key="kdist"):
            from sklearn.neighbors import NearestNeighbors
            nbrs = NearestNeighbors(n_neighbors=minpts).fit(X)
            dists, _ = nbrs.kneighbors(X)
            kd = np.sort(dists[:,-1])[::-1]
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4), facecolor="#ffffff")
            for ax in [ax1, ax2]:
                ax.set_facecolor("#f8f7ff")
                for sp in ax.spines.values(): sp.set_color("#e2deff")
                ax.tick_params(colors="#7c7a9e", labelsize=8)
                ax.grid(alpha=0.3, color="#e2deff", linestyle="--")
            ax1.plot(kd, color=PALETTE[0], lw=2)
            ax1.axhline(eps_v, color=PALETTE[1], ls="--", lw=1.8, label=f"ε={eps_v}")
            ax1.legend(fontsize=8); _style_ax(ax1, f"k-distance complète (k={minpts})", "Points", "Distance")
            ax2.plot(kd[:min(50,len(kd))], color=PALETTE[2], lw=2)
            ax2.axhline(eps_v, color=PALETTE[1], ls="--", lw=1.8)
            _style_ax(ax2, "Zoom — 50 premiers points (zone coude)", "Points", "Distance")
            plt.tight_layout(); st.pyplot(fig); plt.close(fig)

        if st.button("▶ Lancer DBSCAN", key="run_db"):
            with st.spinner("DBSCAN…"):
                if db_impl.startswith("Sklearn"):
                    from sklearn.cluster import DBSCAN as SKDB
                    labels = SKDB(eps=eps_v, min_samples=minpts).fit_predict(X)
                else:
                    # From scratch — corrected TP3 implementation
                    DIST_mat = np.zeros((N, N))
                    for i in range(N):
                        diff = X[i+1:] - X[i]
                        DIST_mat[i, i+1:] = np.sqrt((diff**2).sum(axis=1))
                        DIST_mat[i+1:, i] = DIST_mat[i, i+1:]
                    UNVISITED = -2; NOISE = -1
                    labels = np.full(N, UNVISITED, dtype=int)
                    def region_query(idx):
                        return list(np.where(DIST_mat[idx] <= eps_v)[0])
                    cid = 0
                    for i in range(N):
                        if labels[i] != UNVISITED: continue
                        neighbours = region_query(i)
                        if len(neighbours) < minpts:
                            labels[i] = NOISE; continue
                        labels[i] = cid
                        seed_set = set(neighbours) - {i}
                        while seed_set:
                            j = seed_set.pop()
                            if labels[j] == NOISE: labels[j] = cid
                            if labels[j] != UNVISITED: continue
                            labels[j] = cid
                            nb2 = region_query(j)
                            if len(nb2) >= minpts: seed_set.update(nb2)
                        cid += 1
            section("Résultats DBSCAN")
            show_metrics(labels)
            fig = plot_clusters(X_2d, labels, f"DBSCAN — ε={eps_v}, MinPts={minpts}")
            st.pyplot(fig); plt.close(fig)

    # ── AGNES ─────────────────────────────────────────────────────────────────
    elif algo == "AGNES":
        section("Paramètres AGNES")
        p1,p2,p3 = st.columns(3)
        with p1: k_ag = st.slider("k", 2, 15, 3, key="ag_k")
        with p2: link_ag = st.selectbox("Linkage", ["ward","complete","average","single"], key="ag_link")
        with p3: ag_impl = st.selectbox("Implémentation", ["Sklearn","From Scratch (TP3)"], key="ag_impl")

        if st.button("🌲 Dendrogramme", key="ag_dend"):
            from scipy.cluster.hierarchy import dendrogram, linkage as sp_link
            Xs = X[:min(500,N)]
            Z = sp_link(Xs, method=link_ag)
            fig, ax = _fig(11, 4.5)
            dendrogram(Z, ax=ax, truncate_mode="lastp", p=30,
                       leaf_rotation=90, leaf_font_size=8, show_contracted=True,
                       color_threshold=0.6*Z[:,2].max(),
                       above_threshold_color="#ccc")
            _style_ax(ax, f"Dendrogramme AGNES ({link_ag})", "Observations", "Distance")
            plt.tight_layout(); st.pyplot(fig); plt.close(fig)

        if st.button("▶ Lancer AGNES", key="run_ag"):
            with st.spinner("AGNES…"):
                if ag_impl == "Sklearn":
                    from sklearn.cluster import AgglomerativeClustering
                    labels = AgglomerativeClustering(n_clusters=k_ag, linkage=link_ag).fit_predict(X)
                else:
                    # From scratch — TP3
                    DIST_mat = np.zeros((N,N))
                    for i in range(N):
                        diff = X[i+1:] - X[i]
                        DIST_mat[i,i+1:] = np.sqrt((diff**2).sum(axis=1))
                        DIST_mat[i+1:,i] = DIST_mat[i,i+1:]
                    def cl_dist(ci, cj, mode):
                        rows = DIST_mat[np.ix_(list(ci),list(cj))].ravel()
                        if mode=="single": return rows.min()
                        if mode=="complete": return rows.max()
                        return rows.mean()
                    mode_map = {"ward":"complete","complete":"complete","average":"average","single":"single"}
                    mode = mode_map[link_ag]
                    clusters = [frozenset([i]) for i in range(N)]
                    while len(clusters) > k_ag:
                        best_d, best_ij = np.inf, (0,1)
                        for i in range(len(clusters)):
                            for j in range(i+1, len(clusters)):
                                d = cl_dist(clusters[i], clusters[j], mode)
                                if d < best_d: best_d=d; best_ij=(i,j)
                        i,j = best_ij
                        clusters[i] = clusters[i]|clusters[j]; clusters.pop(j)
                    labels = np.zeros(N, dtype=int)
                    for ci,c in enumerate(clusters):
                        for idx in c: labels[idx] = ci
            section("Résultats AGNES")
            show_metrics(labels)
            fig = plot_clusters(X_2d, labels, f"AGNES — k={k_ag}, {link_ag}")
            st.pyplot(fig); plt.close(fig)

    # ── DIANA ─────────────────────────────────────────────────────────────────
    elif algo == "DIANA":
        section("Paramètres DIANA")
        p1,p2 = st.columns(2)
        with p1: k_di = st.slider("k", 2, 10, 3, key="di_k")
        with p2: di_impl = st.selectbox("Implémentation", ["Scipy (complete linkage)","From Scratch (TP3)"], key="di_impl")

        if st.button("🌲 Dendrogramme", key="di_dend"):
            from scipy.cluster.hierarchy import dendrogram, linkage as sp_link
            Xs = X[:min(500,N)]
            Z = sp_link(Xs, method="complete")
            fig, ax = _fig(11, 4.5)
            dendrogram(Z, ax=ax, truncate_mode="lastp", p=30,
                       leaf_rotation=90, leaf_font_size=8, show_contracted=True,
                       above_threshold_color="#ccc")
            _style_ax(ax, "Dendrogramme DIANA (complete linkage — divisif)", "Observations", "Distance")
            plt.tight_layout(); st.pyplot(fig); plt.close(fig)

        if st.button("▶ Lancer DIANA", key="run_di"):
            with st.spinner("DIANA…"):
                if di_impl.startswith("Scipy"):
                    from scipy.cluster.hierarchy import linkage as sp_link, fcluster
                    Z = sp_link(X, method="complete")
                    labels = fcluster(Z, t=k_di, criterion="maxclust") - 1
                else:
                    # From scratch — TP3
                    DIST_mat = np.zeros((N,N))
                    for i in range(N):
                        diff = X[i+1:] - X[i]
                        DIST_mat[i,i+1:] = np.sqrt((diff**2).sum(axis=1))
                        DIST_mat[i+1:,i] = DIST_mat[i,i+1:]
                    def diameter(c):
                        c=list(c)
                        if len(c)<2: return 0.0
                        return DIST_mat[np.ix_(c,c)].max()
                    def split_cluster(c):
                        c=list(c)
                        if len(c)<2: return c,[]
                        sub=DIST_mat[np.ix_(c,c)]
                        avg=sub.sum(axis=1)/(len(c)-1)
                        splinter=c[int(avg.argmax())]
                        main=[x for x in c if x!=splinter]; spl_g=[splinter]
                        changed=True
                        while changed:
                            changed=False; new_main=[]
                            for pt in main:
                                d_m=DIST_mat[pt][main].mean() if len(main)>1 else 0.0
                                d_s=DIST_mat[pt][spl_g].mean()
                                if d_s<d_m: spl_g.append(pt); changed=True
                                else: new_main.append(pt)
                            main=new_main
                        return main, spl_g
                    clusters=[list(range(N))]
                    while len(clusters)<k_di:
                        diams=[diameter(c) for c in clusters]
                        worst=int(np.argmax(diams))
                        to_split=clusters.pop(worst)
                        main,spl=split_cluster(to_split)
                        if main: clusters.append(main)
                        if spl:  clusters.append(spl)
                    labels=np.zeros(N,dtype=int)
                    for ci,c in enumerate(clusters):
                        for idx in c: labels[idx]=ci
            section("Résultats DIANA")
            show_metrics(labels)
            fig = plot_clusters(X_2d, labels, f"DIANA — k={k_di}")
            st.pyplot(fig); plt.close(fig)

    # ── Comparaison de tous les algos ─────────────────────────────────────────
    section("Comparaison de Tous les Algorithmes")
    k_cmp = st.slider("k pour la comparaison", 2, 10, 3, key="cmp_k")
    if st.button("📊 Comparer tous les algorithmes", key="cmp_all"):
        from sklearn.cluster import KMeans as SKM, DBSCAN as SKDB, AgglomerativeClustering
        from scipy.cluster.hierarchy import linkage as sp_link, fcluster
        results = []
        with st.spinner("Comparaison en cours…"):
            # K-Means
            km = SKM(n_clusters=k_cmp, random_state=42, n_init=10).fit(X)
            lkm = km.labels_
            results.append({"Algorithme":"K-Means","k":k_cmp,
                "Silhouette":round(sil_safe(X,lkm),4),"DB":round(db_safe(X,lkm),4),
                "Bruit":0,"Inertie":round(km.inertia_,2)})
            # K-Medoids
            try:
                from sklearn_extra.cluster import KMedoids
                lkmed = KMedoids(n_clusters=k_cmp, random_state=42).fit_predict(X)
            except:
                lkmed = lkm
            def _inertia(X, labels):
                total = 0.0
                for c in set(labels):
                    if c < 0: continue
                    pts = X[labels == c]
                    if len(pts) == 0: continue
                    total += float(np.sum((pts - pts.mean(axis=0))**2))
                return round(total, 2)
            results.append({"Algorithme":"K-Medoids","k":k_cmp,
                "Silhouette":round(sil_safe(X,lkmed),4),"DB":round(db_safe(X,lkmed),4),
                "Bruit":0,"Inertie":_inertia(X,lkmed)})
            # DBSCAN — use the eps/minpts the user already configured on this page
            _eps  = float(st.session_state.get("db_eps", 0.5))
            _mpts = int(st.session_state.get("db_mp",  5))
            ldb = SKDB(eps=_eps, min_samples=_mpts).fit_predict(X)
            nc = len([l for l in set(ldb) if l >= 0])
            results.append({"Algorithme":"DBSCAN","k":nc,
                "Silhouette":round(sil_safe(X,ldb),4),"DB":round(db_safe(X,ldb),4),
                "Bruit":int((ldb==-1).sum()),"Inertie":float("nan")})
            # AGNES
            lag = AgglomerativeClustering(n_clusters=k_cmp, linkage="ward").fit_predict(X)
            results.append({"Algorithme":"AGNES","k":k_cmp,
                "Silhouette":round(sil_safe(X,lag),4),"DB":round(db_safe(X,lag),4),
                "Bruit":0,"Inertie":float("nan")})
            # DIANA
            Z = sp_link(X, method="complete")
            ldi = fcluster(Z, t=k_cmp, criterion="maxclust") - 1
            results.append({"Algorithme":"DIANA","k":k_cmp,
                "Silhouette":round(sil_safe(X,ldi),4),"DB":round(db_safe(X,ldi),4),
                "Bruit":0,"Inertie":float("nan")})

        cmp_df = pd.DataFrame(results).set_index("Algorithme")
        # Keep Inertie as numeric (nan for algos that don't compute it)
        cmp_df["Inertie"] = pd.to_numeric(cmp_df["Inertie"], errors="coerce")
        st.dataframe(cmp_df, use_container_width=True)

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.5), facecolor="#ffffff")
        for ax in [ax1, ax2]:
            ax.set_facecolor("#f8f7ff")
            for sp in ax.spines.values(): sp.set_color("#e2deff")
            ax.tick_params(colors="#7c7a9e", labelsize=8)
            ax.grid(axis="y", alpha=0.3, color="#e2deff", linestyle="--")
        names = [r["Algorithme"] for r in results]
        sils  = [r["Silhouette"] for r in results]
        dbs   = [r["DB"] if isinstance(r["DB"], float) else 0 for r in results]
        bars1 = ax1.bar(names, sils, color=PALETTE[:5], edgecolor="white", linewidth=0.5, width=0.6)
        for b,v in zip(bars1,sils): ax1.text(b.get_x()+b.get_width()/2, b.get_height()+0.005, f"{v:.3f}", ha="center", va="bottom", fontsize=8, fontweight="bold", color="#1e1b3a")
        _style_ax(ax1, "Silhouette ↑ (plus élevé = meilleur)", "", "Score")
        bars2 = ax2.bar(names, dbs, color=PALETTE[:5], edgecolor="white", linewidth=0.5, width=0.6)
        for b,v in zip(bars2,dbs): ax2.text(b.get_x()+b.get_width()/2, b.get_height()+0.005, f"{v:.3f}", ha="center", va="bottom", fontsize=8, fontweight="bold", color="#1e1b3a")
        _style_ax(ax2, "Davies-Bouldin ↓ (plus bas = meilleur)", "", "Score")
        plt.tight_layout(); st.pyplot(fig); plt.close(fig)

# ══════════════════════════════════════════════════════════════════════════════
#  PAGE 3 — CLASSIFICATION
# ══════════════════════════════════════════════════════════════════════════════
elif PAGE == "classification":
    st.markdown("""
    <div class="dn-hero">
      <div class="dn-hero-tag">VOLET 03</div>
      <h2>🎯 Apprentissage Supervisé</h2>
      <p>K-Fold · Decision Tree · Random Forest · SVM · XGBoost · LGBM · CatBoost · Matrice de confusion</p>
    </div>""", unsafe_allow_html=True)

    df = st.session_state.df_clean
    if df is None:
        alert("⚠️ Veuillez d'abord charger un dataset dans l'onglet <b>Prétraitement</b>", "warn"); st.stop()

    all_cols = df.columns.tolist()
    num_cols = df.select_dtypes(include=np.number).columns.tolist()

    # ── Config ─────────────────────────────────────────────────────────────────
    section("Configuration")
    cfg1, cfg2, cfg3 = st.columns(3)
    with cfg1: target_col = st.selectbox("Variable cible (y)", all_cols, index=len(all_cols)-1, key="cls_tgt")
    with cfg2:
        feat_cands = [c for c in num_cols if c != target_col]
        feat_cols = st.multiselect("Features (X)", feat_cands, default=feat_cands[:min(len(feat_cands),10)], key="cls_feats")
    with cfg3:
        n_folds = st.slider("Nombre de folds (K-Fold)", 2, 10, 5, key="cls_folds")

    if not feat_cols: alert("⚠️ Sélectionnez au moins une feature", "warn"); st.stop()

    # Detect task type
    df_cls = df[feat_cols + [target_col]].dropna()
    y_unique = df_cls[target_col].nunique()
    is_binary = y_unique == 2
    task_lbl = "Classification Binaire" if is_binary else f"Classification Multi-classes ({y_unique} classes)"
    badge_cls = "dn-green" if is_binary else "dn-blue"
    alert(f"📌 Tâche détectée : <b>{task_lbl}</b> — {len(df_cls)} exemples", "info")

    n_total = len(df_cls)
    m1,m2,m3 = st.columns(3)
    m1.metric("Total exemples", n_total)
    m2.metric("K folds", n_folds)
    m3.metric("Taille fold test ~", f"{n_total//n_folds}")

    # ── Modèles disponibles ────────────────────────────────────────────────────
    section("Sélection des Modèles")

    MODEL_LIST = [
        ("Decision Tree",     "dt",       "🌳"),
        ("Random Forest",     "rf",       "🌲"),
        ("SVM (RBF)",         "svm",      "🔵"),
        ("K-Nearest Neighbors","knn",     "🔍"),
        ("Naive Bayes",       "nb",       "📐"),
    ]
    if is_binary:
        MODEL_LIST.insert(0, ("Logistic Regression","lr","📈"))

    BOOST_LIST = [
        ("XGBoost",  "xgb",  "⚡"),
        ("LightGBM", "lgbm", "💡"),
        ("CatBoost", "cat",  "🐱"),
    ]

    st.markdown("**Modèles classiques**")
    mcols = st.columns(len(MODEL_LIST))
    selected_models = []
    for (nm, key, ico), col in zip(MODEL_LIST, mcols):
        with col:
            if st.checkbox(f"{ico} {nm}", key=f"chk_{key}", value=(key in ["dt","rf","svm"])):
                selected_models.append((nm, key))

    st.markdown("**Boosting**")
    bcols = st.columns(len(BOOST_LIST))
    for (nm, key, ico), col in zip(BOOST_LIST, bcols):
        with col:
            if st.checkbox(f"{ico} {nm}", key=f"chk_{key}"):
                selected_models.append((nm, key))

    # ── Hyperparams ────────────────────────────────────────────────────────────
    with st.expander("⚙️ Hyperparamètres"):
        hp1,hp2,hp3,hp4,hp5 = st.columns(5)
        with hp1: dt_depth = st.slider("DT max_depth", 1, 30, 6, key="hp_dt")
        with hp2: rf_trees = st.slider("RF estimateurs", 10, 300, 100, 10, key="hp_rf")
        with hp3: knn_k   = st.slider("KNN k", 1, 30, 5, key="hp_knn")
        with hp4: svm_c   = st.number_input("SVM C", 0.01, 100.0, 1.0, key="hp_svc")
        with hp5: xgb_lr  = st.number_input("XGB/LGBM lr", 0.001, 1.0, 0.1, key="hp_xgb")

    # ── Train & Evaluate ────────────────────────────────────────────────────────
    if not selected_models:
        alert("Sélectionnez au moins un modèle", "warn"); st.stop()

    if st.button("🚀 Lancer l'entraînement K-Fold", key="run_cls"):
        from sklearn.model_selection import StratifiedKFold, cross_val_predict
        from sklearn.preprocessing import LabelEncoder, StandardScaler
        from sklearn.metrics import (confusion_matrix, accuracy_score,
                                     precision_score, recall_score, f1_score,
                                     roc_auc_score, classification_report)
        from sklearn.tree import DecisionTreeClassifier
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.neighbors import KNeighborsClassifier
        from sklearn.linear_model import LogisticRegression
        from sklearn.svm import SVC
        from sklearn.naive_bayes import GaussianNB

        # Prepare
        X_cls = df_cls[feat_cols].values
        y_raw = df_cls[target_col].values
        le = LabelEncoder(); y_cls = le.fit_transform(y_raw)
        class_names = le.classes_.astype(str)
        sc = StandardScaler(); X_cls = sc.fit_transform(X_cls)

        skf = StratifiedKFold(n_splits=n_folds, shuffle=True, random_state=42)
        avg_mode = "binary" if is_binary else "weighted"

        def build_model(key):
            m = {"dt": DecisionTreeClassifier(max_depth=dt_depth, random_state=42),
                 "rf": RandomForestClassifier(n_estimators=rf_trees, random_state=42, n_jobs=-1),
                 "svm": SVC(C=svm_c, kernel="rbf", probability=True, random_state=42),
                 "knn": KNeighborsClassifier(n_neighbors=knn_k, n_jobs=-1),
                 "nb":  GaussianNB(),
                 "lr":  LogisticRegression(max_iter=1000, random_state=42),
                 "xgb": None, "lgbm": None, "cat": None}
            if key == "xgb":
                try:
                    from xgboost import XGBClassifier
                    return XGBClassifier(learning_rate=xgb_lr, n_estimators=100, objective="binary:logistic" if is_binary else "multi:softprob",
                                        random_state=42, eval_metric="logloss", verbosity=0)
                except: return DecisionTreeClassifier(max_depth=dt_depth, random_state=42)
            if key == "lgbm":
                try:
                    from lightgbm import LGBMClassifier
                    return LGBMClassifier(learning_rate=xgb_lr, n_estimators=100, random_state=42, verbose=-1)
                except: return RandomForestClassifier(n_estimators=50, random_state=42)
            if key == "cat":
                try:
                    from catboost import CatBoostClassifier
                    return CatBoostClassifier(learning_rate=xgb_lr, iterations=100, random_seed=42, verbose=0)
                except: return RandomForestClassifier(n_estimators=50, random_state=42)
            return m[key]

        all_results = []
        section("Résultats par Modèle")

        for nm, key in selected_models:
            model = build_model(key)
            with st.spinner(f"Entraînement {nm} ({n_folds}-Fold)…"):
                # Manual K-Fold to avoid nested-parallelism issues and have
                # full control over predictions (fixes "Expected [0,1] got [0,2]")
                y_pred_all  = np.zeros(len(y_cls), dtype=int)
                y_proba_all = np.zeros((len(y_cls), len(class_names)))
                has_proba   = hasattr(model, "predict_proba")
                for train_idx, test_idx in skf.split(X_cls, y_cls):
                    Xtr, Xte = X_cls[train_idx], X_cls[test_idx]
                    ytr       = y_cls[train_idx]
                    fold_encoder = LabelEncoder()
                    ytr_encoded = fold_encoder.fit_transform(ytr)
                    model.fit(Xtr, ytr_encoded)
                    pred_encoded = model.predict(Xte)
                    y_pred_fold = fold_encoder.inverse_transform(pred_encoded)

                    y_pred_all[test_idx] = y_pred_fold
                    if has_proba:
                        proba = model.predict_proba(Xte)

                        # align probabilities toXG global class indices
                        fold_classes = fold_encoder.inverse_transform(model.classes_)

                        for ci, cl in enumerate(fold_classes):
                            y_proba_all[test_idx, cl] = proba[:, ci]
            y_pred = y_pred_all

            acc  = accuracy_score(y_cls, y_pred)
            prec = precision_score(y_cls, y_pred, average=avg_mode, zero_division=0)
            rec  = recall_score(y_cls, y_pred, average=avg_mode, zero_division=0)
            f1   = f1_score(y_cls, y_pred, average=avg_mode, zero_division=0)
            try:
                if is_binary:
                    if has_proba:
                        auc = roc_auc_score(y_cls, y_proba_all[:, 1])
                    else:
                        auc = roc_auc_score(y_cls, y_pred)
                else:
                    if has_proba:
                        auc = roc_auc_score(y_cls, y_proba_all, average="weighted", multi_class="ovr")
                    else:
                        auc = float("nan")
            except: auc = float("nan")

            all_results.append({"Modèle": nm, "Accuracy": round(acc,4),
                                 "Precision": round(prec,4), "Recall": round(rec,4),
                                 "F1-Score": round(f1,4), "AUC-ROC": round(auc,4) if not np.isnan(auc) else "N/A"})

            with st.expander(f"📊 {nm}  —  Acc: {acc:.4f}  |  F1: {f1:.4f}", expanded=len(selected_models)==1):
                r1,r2,r3,r4 = st.columns(4)
                r1.metric("Accuracy",  f"{acc:.4f}")
                r2.metric("Precision", f"{prec:.4f}")
                r3.metric("Recall",    f"{rec:.4f}")
                r4.metric("F1-Score",  f"{f1:.4f}")

                # Confusion matrix
                cm = confusion_matrix(y_cls, y_pred)
                fig, ax = _fig(max(6, len(class_names)*1.5), max(4.5, len(class_names)*1.2))
                im = ax.imshow(cm, cmap="BuPu", aspect="auto")
                plt.colorbar(im, ax=ax, shrink=0.8)
                ticks = np.arange(len(class_names))
                ax.set_xticks(ticks); ax.set_yticks(ticks)
                ax.set_xticklabels(class_names, rotation=45, ha="right", fontsize=8, color="#7c7a9e")
                ax.set_yticklabels(class_names, fontsize=8, color="#7c7a9e")
                thresh = cm.max() / 2
                for ii in range(cm.shape[0]):
                    for jj in range(cm.shape[1]):
                        ax.text(jj, ii, str(cm[ii,jj]), ha="center", va="center", fontsize=9,
                                fontweight="bold",
                                color="white" if cm[ii,jj] > thresh else PALETTE[0])
                _style_ax(ax, f"Matrice de Confusion — {nm}", "Prédit", "Réel")
                plt.tight_layout(); st.pyplot(fig); plt.close(fig)

                with st.expander("📄 Rapport de classification complet"):
                    rep = classification_report(y_cls, y_pred, target_names=class_names, zero_division=0)
                    st.code(rep, language="text")

        # ── Résumé comparatif ─────────────────────────────────────────────────
        if len(all_results) > 1:
            section("Tableau Comparatif Global")
            res_df = pd.DataFrame(all_results).set_index("Modèle")
            num_res = res_df.select_dtypes(include=np.number)
            st.dataframe(num_res.style.highlight_max(axis=0, color="rgba(108,71,255,0.15)")
                                      .highlight_min(axis=0, color="rgba(255,107,107,0.12)")
                                      .format("{:.4f}"),
                         use_container_width=True)

            # Bar chart
            metrics_to_plot = ["Accuracy","Precision","Recall","F1-Score"]
            x = np.arange(len(all_results)); w = 0.2
            fig, ax = _fig(max(10, len(all_results)*2.5), 5)
            for i, (met, col) in enumerate(zip(metrics_to_plot, PALETTE)):
                vals = [r[met] for r in all_results]
                bars = ax.bar(x + i*w, vals, w, label=met, color=col, edgecolor="white", linewidth=0.3, alpha=0.9)
            ax.set_xticks(x + w*1.5)
            ax.set_xticklabels([r["Modèle"] for r in all_results], rotation=20, ha="right", fontsize=8)
            ax.set_ylim(0, 1.12)
            _style_ax(ax, f"Comparaison des modèles ({n_folds}-Fold Cross-Validation)", "", "Score")
            ax.legend(fontsize=8, framealpha=0.9, loc="upper right")
            plt.tight_layout(); st.pyplot(fig); plt.close(fig)

            # Best model highlight
            best_idx = max(range(len(all_results)), key=lambda i: all_results[i]["F1-Score"])
            best = all_results[best_idx]
            alert(f"🏆 Meilleur modèle : <b>{best['Modèle']}</b> — F1-Score : <b>{best['F1-Score']:.4f}</b>  |  Accuracy : <b>{best['Accuracy']:.4f}</b>", "ok")

# ══════════════════════════════════════════════════════════════════════════════
#  FOOTER
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="dn-footer">
  ⬡ DataMine Studio &nbsp;·&nbsp; Mini-Projet Fouille de Données 1 &nbsp;·&nbsp; Faculté d'Informatique &nbsp;·&nbsp; 2025-2026
</div>""", unsafe_allow_html=True)