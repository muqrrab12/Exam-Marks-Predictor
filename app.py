import streamlit as st
import joblib
import pandas as pd
import numpy as np
import plotly.express as px

# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="Student Exam Score Predictor",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# Load Machine Learning Model
# ==========================================

model = joblib.load("exam_predict_joblib")

# ==========================================
# Custom CSS
# ==========================================

st.markdown("""
<style>

/* Hide Streamlit Menu */

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

/* Main App */

.stApp{
background:#f4f7fb;
}

/* Hero Banner */

.hero{
background:linear-gradient(135deg,#2563eb,#4f46e5);
padding:40px;
border-radius:25px;
color:white;
text-align:center;
box-shadow:0px 10px 30px rgba(0,0,0,.20);
margin-bottom:30px;
}

/* Glass Card */

.card{
background:white;
padding:25px;
border-radius:20px;
box-shadow:0 10px 25px rgba(0,0,0,.08);
margin-bottom:20px;
transition:.3s;
}

.card:hover{
transform:translateY(-5px);
}

/* Big Score */

.score{
font-size:60px;
font-weight:bold;
color:#2563eb;
}

/* Footer */

.footer{
text-align:center;
padding:30px;
color:gray;
font-size:15px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# Hero Section
# ==========================================

st.markdown("""
<div class="hero">

<h1>🎓 Student Exam Score Predictor</h1>

<h4>Artificial Intelligence Powered Prediction System</h4>

<p>
Predict your expected exam score using a trained Machine Learning model.
Simply choose your study hours and let AI estimate your performance.
</p>

</div>
""", unsafe_allow_html=True)
# ==========================================================
# Dashboard Layout
# ==========================================================

left_col, right_col = st.columns([1, 1], gap="large")

# ==========================================================
# LEFT PANEL
# ==========================================================

with left_col:

    st.markdown("""
    <div class="card">
    <h2>📚 Student Input</h2>
    <p>Select the number of hours you studied.</p>
    </div>
    """, unsafe_allow_html=True)

    study_hours = st.slider(
        "Study Hours",
        min_value=0.0,
        max_value=12.0,
        value=5.0,
        step=0.5,
        help="Move the slider to choose study hours."
    )

    st.info(f"📖 Current Study Hours: **{study_hours:.1f} Hours**")

    predict = st.button(
        "🚀 Predict My Score",
        use_container_width=True,
        type="primary"
    )

# ==========================================================
# RIGHT PANEL
# ==========================================================

with right_col:

    st.markdown("""
    <div class="card">
    <h2>📊 Prediction Result</h2>
    <p>Your predicted exam score will appear here.</p>
    </div>
    """, unsafe_allow_html=True)

    if predict:

        prediction = model.predict([[study_hours]])[0]

        st.markdown(f"""
        <div class="card">

        <center>

        <h4>Predicted Exam Score</h4>

        <div class="score">
            {prediction:.2f}
        </div>

        <h4>/100</h4>

        </center>

        </div>
        """, unsafe_allow_html=True)

        st.progress(min(int(prediction), 100))

        if prediction >= 90:
            level = "🏆 Excellent"
            color = "success"

        elif prediction >= 75:
            level = "🥇 Very Good"
            color = "success"

        elif prediction >= 60:
            level = "📘 Average"
            color = "warning"

        else:
            level = "⚠ Needs Improvement"
            color = "error"

        if color == "success":
            st.success(level)
        elif color == "warning":
            st.warning(level)
        else:
            st.error(level)

        st.subheader("🤖 AI Study Advisor")

        if prediction >= 90:

            st.markdown("""
✅ Outstanding preparation.

✅ Continue your current study routine.

✅ Solve previous papers.

✅ Focus on revision rather than increasing study hours.
""")

        elif prediction >= 75:

            st.markdown("""
✅ You're doing well.

✅ Revise daily.

✅ Practice more numerical questions.

✅ Attempt mock tests every week.
""")

        elif prediction >= 60:

            st.markdown("""
📚 Increase your study time.

📚 Revise difficult topics.

📚 Solve practice questions.

📚 Create a daily timetable.
""")

        else:

            st.markdown("""
⚠ Your predicted score is low.

📖 Increase study time.

📖 Avoid distractions.

📖 Revise every day.

📖 Solve past papers.
""")