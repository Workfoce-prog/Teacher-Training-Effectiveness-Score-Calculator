
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Teacher Training Effectiveness Score", layout="centered")
st.title("📊 Teacher Training Effectiveness Score (TTES) Calculator")

st.markdown("You can manually enter scores or upload a CSV file with your training evaluation data.")

# File upload section
uploaded_file = st.file_uploader("📁 Upload your CSV file (with matching column names)", type=["csv"])

# Default slider values
default_values = {
    "curriculum_alignment": 80,
    "subject_relevance": 4,
    "trainer_eval": 85,
    "interactive_methods": 75,
    "attendance_rate": 90,
    "completion_score": 95,
    "knowledge_gain": 70,
    "confidence_score": 4,
    "implementation_score": 60,
    "plc_integration": 50,
    "student_impact": 50,
    "feedback_followup": 60
}

data = {}

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("File uploaded successfully!")
        row = df.iloc[0]  # take first row of input
        for key in default_values:
            data[key] = row.get(key, default_values[key])
    except Exception as e:
        st.error(f"Error reading the file: {e}")
        data = default_values
else:
    data = default_values

st.header("1. Content Relevance")
curriculum_alignment = st.slider("Curriculum Alignment Score (0–100)", 0, 100, int(data["curriculum_alignment"]))
subject_relevance = st.slider("Subject Relevance (1–5)", 1, 5, int(data["subject_relevance"]))

st.header("2. Instructional Quality")
trainer_eval = st.slider("Trainer Evaluation Score (0–100)", 0, 100, int(data["trainer_eval"]))
interactive_methods = st.slider("Interactive Methods Score (0–100)", 0, 100, int(data["interactive_methods"]))

st.header("3. Engagement & Participation")
attendance_rate = st.slider("Attendance Rate (%)", 0, 100, int(data["attendance_rate"]))
completion_score = st.slider("Completion Score (%)", 0, 100, int(data["completion_score"]))

st.header("4. Skill Acquisition")
knowledge_gain = st.slider("Knowledge Gain (%)", 0, 100, int(data["knowledge_gain"]))
confidence_score = st.slider("Practice Confidence Score (1–5)", 1, 5, int(data["confidence_score"]))

st.header("5. Classroom Application")
implementation_score = st.slider("Implementation Score (0–100)", 0, 100, int(data["implementation_score"]))
plc_integration = st.slider("PLC/Peer Coaching Score (0–100)", 0, 100, int(data["plc_integration"]))

st.header("6. Long-Term Outcomes")
student_impact = st.slider("Student Impact Proxy (0–100)", 0, 100, int(data["student_impact"]))
feedback_followup = st.slider("Feedback Follow-Up Score (0–100)", 0, 100, int(data["feedback_followup"]))

# Scaled values
subject_relevance_scaled = (subject_relevance - 1) / 4 * 100
confidence_score_scaled = (confidence_score - 1) / 4 * 100

# Weighted score calculation
tt_score = (
    0.10 * (curriculum_alignment + subject_relevance_scaled) / 2 +
    0.075 * (trainer_eval + interactive_methods) / 2 +
    0.05 * (attendance_rate + completion_score) / 2 +
    0.10 * (knowledge_gain + confidence_score_scaled) / 2 +
    0.10 * (implementation_score + plc_integration) / 2 +
    0.05 * (student_impact + feedback_followup) / 2
)

# Rating
if tt_score >= 90:
    rating = "🟢 Excellent"
elif tt_score >= 75:
    rating = "🟡 High"
elif tt_score >= 60:
    rating = "🟠 Moderate"
else:
    rating = "🔴 Low"

st.markdown("## Final TTES Score")
st.metric("Score", f"{tt_score:.2f}")
st.markdown(f"### Rating: {rating}")
