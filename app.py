import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Industrial AI | Engineering Portfolio", page_icon="⚙️", layout="wide", initial_sidebar_state="expanded")

NAME = "Udhayamoorthi Arachalakumar"
GITHUB = "https://github.com/udhayamoorthi99-collab"
CNC_REPO = "https://github.com/udhayamoorthi99-collab/DEEP-Koopman--MPC--Smart-CNC"
TENSILE_DEMO = "https://tensile-ml-dashboard-nvvzgywwmchambwrsnqj3i.streamlit.app/"

st.markdown('''<style>
.stApp {background: #0a1020; color: #e9eef8;}
[data-testid="stSidebar"] {background: #111a2e;}
.block-container {max-width: 1180px; padding-top: 2.5rem;}
h1,h2,h3 {letter-spacing: -.035em;}
.kicker {font-size:.8rem; letter-spacing:.19em; color:#77d7db; font-weight:700; margin-bottom:.7rem}
.hero {padding:2.1rem 2rem; border:1px solid #263b5a; border-radius:20px; background:linear-gradient(115deg,#132440,#111728); margin-bottom:1.5rem;}
.hero h1 {font-size:clamp(2rem,4vw,3.3rem);line-height:1.12;margin:.5rem 0;color:#f6f9ff}
.hero p {color:#c5d2e8;max-width:800px;font-size:1.07rem;line-height:1.6}
.tag {display:inline-block; padding:5px 11px; margin:6px 6px 0 0; background:#17364b; border:1px solid #266278; border-radius:999px; font-size:.77rem;color:#b9f2ee}
.project-box {background:#121d33;border:1px solid #293a53;border-radius:14px;padding:1rem 1.1rem;min-height:190px;margin-bottom:.5rem}
.project-box h3 {margin:0 0 .35rem 0;font-size:1.14rem;color:white}
.project-box p {font-size:.91rem;color:#bdcbe0;line-height:1.6}
.status {font-size:.74rem; color:#86e1d2;text-transform:uppercase;letter-spacing:.09em}
.small-note {font-size:.86rem;color:#a9b9d0}
</style>''', unsafe_allow_html=True)

sections = ["Overview", "CNC Digital Twin", "Materials AI", "Robotics & Analytics", "Research", "About & Contact"]
with st.sidebar:
    st.markdown("### ⚙️ INDUSTRIAL AI")
    st.caption("Engineering portfolio")
    page = st.radio("Explore", sections, label_visibility="collapsed")
    st.divider()
    st.markdown(f"**{NAME}**")
    st.caption("M.Sc. Intelligent Manufacturing | TU Clausthal")
    st.link_button("View GitHub ↗", GITHUB, use_container_width=True)

if page == "Overview":
    st.markdown('''<div class="hero"><div class="kicker">APPLIED ML · DIGITAL TWINS · INTELLIGENT CONTROL</div>
    <h1>Building AI systems for smarter manufacturing.</h1>
    <p>I am Udhayamoorthi Arachalakumar, an M.Sc. Intelligent Manufacturing student at TU Clausthal. I develop industrial machine-learning, process modeling, control, and robotics perception projects — from data to validated prototypes.</p>
    <span class="tag">PyTorch</span><span class="tag">CasADi / MPC</span><span class="tag">Computer Vision</span><span class="tag">Time-series ML</span><span class="tag">Streamlit</span></div>''', unsafe_allow_html=True)
    a,b = st.columns([1,1]);
    with a: st.link_button("⚙️ Explore CNC project", CNC_REPO, use_container_width=True)
    with b: st.link_button("🧪 Try Materials AI demo", TENSILE_DEMO, use_container_width=True)
    st.subheader("Selected engineering evidence")
    c1,c2,c3 = st.columns(3)
    c1.metric("Cutting force reduction", "44.46%", help="Simulated fixed-parameter CNC baseline vs Deep Koopman MPC")
    c2.metric("Test R² — tensile force", "0.944", help="Reported held-out test result for random forest max-force prediction")
    c3.metric("CNC modeled states", "7", help="Simulation-based digital twin")
    st.caption("CNC improvements are simulation-based and are not claims of industrial deployment. Tensile results refer to the project's held-out test evaluation.")
    st.subheader("Featured projects")
    col1,col2 = st.columns(2)
    with col1:
        st.markdown('''<div class="project-box"><div class="status">Simulation study</div><h3>Deep Koopman MPC for CNC Machining</h3><p>Seven-state digital twin, learned dynamics, and predictive control to regulate cutting force, temperature, and other process variables.</p></div>''', unsafe_allow_html=True)
    with col2:
        st.markdown('''<div class="project-box"><div class="status">Deployed web demo</div><h3>Tensile Strength Prediction</h3><p>Feature-based Random Forest prediction, evaluation metrics, and an interactive Streamlit dashboard for materials data.</p></div>''', unsafe_allow_html=True)
    with col1:
        st.markdown('''<div class="project-box"><div class="status">Computer vision prototype</div><h3>YOLOv8 AMR Perception</h3><p>Object detection workflow for autonomous mobile robots, including data preparation, training, and evaluation.</p></div>''', unsafe_allow_html=True)
    with col2:
        st.markdown('''<div class="project-box"><div class="status">Research in progress</div><h3>Interpretable Manufacturing Digital Twins</h3><p>Neural state-space models and symbolic equation discovery for explainable process modeling and control.</p></div>''', unsafe_allow_html=True)

elif page == "CNC Digital Twin":
    st.title("Deep Koopman MPC — CNC Digital Twin")
    st.caption("Simulation-based research prototype · PyTorch · CasADi · System Identification")
    st.write("Physics-based seven-state machining model, neural Koopman dynamics, and model predictive control. Compared against a fixed-parameter CNC simulation baseline.")
    improvements = {"Cutting force":44.46,"Temperature":7.28,"Power":6.64,"Vibration":5.06,"Surface roughness":3.99,"Tool wear":2.09}
    df = pd.DataFrame({"Metric":list(improvements),"Reduction (%)":list(improvements.values())})
    fig = go.Figure(go.Bar(x=df["Reduction (%)"], y=df["Metric"], orientation="h", marker_color="#69d5d4"))
    fig.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", yaxis=dict(autorange="reversed"), height=390, margin=dict(l=10,r=10,t=30,b=30))
    st.plotly_chart(fig, use_container_width=True)
    st.warning("These percentages are simulated improvements against the project baseline. They are not results from physical machining trials.")
    st.link_button("Source code and methodology ↗", CNC_REPO)

elif page == "Materials AI":
    st.title("Materials AI — Tensile Force Prediction")
    st.caption("Machine learning prototype · Random Forest · Streamlit deployment")
    a,b,c=st.columns(3)
    a.metric("Test MAE", "78.99 N"); b.metric("Test RMSE", "105.97 N"); c.metric("Test R²", "0.944")
    st.write("Predict maximum specimen force from specimen attributes and analyze model performance. These are previously reported test-set scores; generalization to other laboratories or materials has not yet been established.")
    st.link_button("Launch live dashboard ↗", TENSILE_DEMO)

elif page == "Robotics & Analytics":
    st.title("Robotics & Industrial Analytics")
    st.subheader("YOLOv8 for AMR Object Detection")
    st.write("Object detection training and evaluation workflow for autonomous mobile robot perception. Add qualitative predictions, sample images, dataset size, mAP, precision, and recall once verified.")
    st.subheader("Industrial Anomaly Detection")
    st.write("Exploratory anomaly detection with PCA, Isolation Forest, LOF, and clustering on industrial-style telemetry.")
    st.subheader("Time-Series Forecasting")
    st.write("Energy forecasting experiments with Prophet and SARIMAX, including seasonal and lag-based features.")

elif page == "Research":
    st.title("Research Direction")
    st.subheader("Interpretable Nonlinear Equation Discovery")
    st.write("Goal: learn nonlinear process dynamics from manufacturing datasets, discover explicit mathematical equations, validate them on unseen conditions, and ultimately support model predictive control.")
    st.code("Process data → Neural state-space model → Symbolic regression → Validation → Digital twin → MPC", language="text")
    st.info("Research in progress: no physical control validation is claimed.")

else:
    st.title("About & Contact")
    st.subheader(NAME)
    st.write("M.Sc. Intelligent Manufacturing, Technische Universität Clausthal, Germany")
    st.write("Focus: Applied Machine Learning, Industrial AI, Digital Twins, Robotics Perception, and Data-Driven Control.")
    st.markdown("**Technical stack:** Python, PyTorch, scikit-learn, CasADi, Streamlit, SQL, Plotly, YOLOv8, Git")
    st.link_button("GitHub ↗", GITHUB)
    st.caption("Add your verified email, LinkedIn profile, and a PDF resume before publishing this section.")

st.divider()
st.caption("© 2026 · Engineering portfolio · Results are labeled by validation context")
