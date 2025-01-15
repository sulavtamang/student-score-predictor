import streamlit as st
import numpy as np
import joblib 

model = joblib.load('../models/student_score_prediction_model.pkl')

import streamlit as st

st.set_page_config(
    page_title="Student Score Predictor",
    page_icon="../assets/images/report-card_2893763.png",
    layout="centered",
    initial_sidebar_state="expanded",
)


st.title("Student Score Predictor")
st.write("A simple app to predict a student's score based on study hours.")

study_hours = st.number_input("Enter the number of study hours (e.g., 5.5)", min_value=0.0, max_value=24.0, step=0.1)

if st.button("Predict Score"):
    try:
        predicted_score = model.predict([[study_hours]])
        st.success(f"You are likely to score {float(predicted_score):.2f}.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

st.markdown("---")
st.markdown("### Connect with Me:")
st.markdown("""
- [GitHub](https://github.com/sulavtamang)
- [LinkedIn](https://www.linkedin.com/in/sulav-man-sing-tamang-269bb5190/)
""")

st.markdown(
    """
    <hr style='border:1px solid #333;'>
    <p style='text-align:center;'>
        Made with ❤️ by Sulav Man Sing Tamang
    </p>
    """, 
    unsafe_allow_html=True
)

# Add custom CSS for styling (Optional)
st.markdown("""
<style>
body {
    font-family: 'Arial', sans-serif;
    background-color: #eef7f8;
    color: #333;
}
.stButton>button {
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 5px;
    padding: 10px 20px;
    cursor: pointer;
}
.stButton>button:hover {
    background-color: #45a049;
}
</style>
""", unsafe_allow_html=True)
