
import streamlit as st

st.set_page_config(page_title="Teacher Training Effectiveness Score", layout="centered")
st.title("📊 Teacher Training Effectiveness Score (TTES) Calculator")

st.header("1. Content Relevance")
curriculum_alignment = st.slider("Curriculum Alignment Score (0–100)", 0, 100, 80)
subject_relevance = st.slider("Subject Relevance (1–5)", 1, 5, 4)

st.header("2. Instructional Quality")
trainer_eval = st.slider("Trainer Evaluation Score (0–100)", 0, 100, 85)
interactive_methods = st.slider("Interactive Methods Score (0–100)", 0, 100, 75)

st.header("3. Engagement & Participation")
attendance_rate = st.slider("Attendance Rate (%)", 0, 100, 90)
completion_score = st.slider("Completion Score (%)", 0, 100, 95)

st.header("4. Skill Acquisition")
knowledge_gain = st.slider("Knowledge Gain (%)", 0, 100, 70)
confidence_score = st.slider("Practice Confidence Score (1–5)", 1, 5, 4)

st.header("5. Classroom Application")
implementation_score = st.slider("Implementation Score (0–100)", 0, 100, 60)
plc_integration = st.slider("PLC/Peer Coaching Score (0–100)", 0, 100, 50)

st.header("6. Long-Term Outcomes")
student_impact = st.slider("Student Impact Proxy (0–100)", 0, 100, 50)
feedback_followup = st.slider("Feedback Follow-Up Score (0–100)", 0, 100, 60)

# Convert scaled inputs
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

# Rating interpretation
if tt_score >= 90:
    rating = "🟢 Excellent"
elif tt_score >= 75:
    rating = "🟡 High"
elif tt_score >= 60:
    rating = "🟠 Moderate"
else:
    rating = "🔴 Low"

st.markdown("## Final TTES Score")
st.metric("Score", f"{tt_score:.2f}", label_visibility="visible")
st.markdown(f"### Rating: {rating}")
st.caption("This score helps assess and improve the quality of your teacher training programs.")
