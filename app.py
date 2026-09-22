import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("software_effort_model.pkl")

st.set_page_config(
    page_title="AI Software Effort Estimation",
    page_icon="💻",
    layout="centered"
)

st.title("💻 AI-Based Software Effort Estimation")
st.write("Predict software development effort using project characteristics.")

st.subheader("Project Details")

team_exp = st.number_input(
    "Team Experience",
    min_value=0,
    max_value=10,
    value=3
)

manager_exp = st.number_input(
    "Manager Experience",
    min_value=0,
    max_value=10,
    value=4
)

year_end = st.number_input(
    "Year End",
    min_value=80,
    max_value=100,
    value=86
)

length = st.number_input(
    "Project Length",
    min_value=1,
    max_value=100,
    value=10
)

transactions = st.number_input(
    "Transactions",
    min_value=1,
    max_value=2000,
    value=150
)

entities = st.number_input(
    "Entities",
    min_value=1,
    max_value=1000,
    value=100
)

points_non_adjust = st.number_input(
    "Points Non-Adjusted",
    min_value=1,
    max_value=2000,
    value=300
)

adjustment = st.number_input(
    "Adjustment",
    min_value=0,
    max_value=100,
    value=25
)

points_adjust = st.number_input(
    "Points Adjusted",
    min_value=1,
    max_value=2000,
    value=280
)

language = st.selectbox(
    "Programming Language",
    [1, 2, 3],
    index=0
)

if st.button("Estimate Software Effort"):

    new_project = pd.DataFrame({
        "TeamExp": [team_exp],
        "ManagerExp": [manager_exp],
        "YearEnd": [year_end],
        "Length": [length],
        "Transactions": [transactions],
        "Entities": [entities],
        "PointsNonAdjust": [points_non_adjust],
        "Adjustment": [adjustment],
        "PointsAjust": [points_adjust],
        "Language": [language]
    })
    prediction = model.predict(new_project)[0]

    st.success(f"Estimated Software Effort: {prediction:.2f} person-hours")