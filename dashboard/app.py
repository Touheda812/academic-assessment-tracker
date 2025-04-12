import pandas as pd
import streamlit as st

df = pd.read_csv("../output/cleaned_assessments.csv")

st.title("Academic Assessment Dashboard")

st.write("### Student Data")
st.dataframe(df)

st.write("### Intervention Needed")
st.dataframe(df[df["Intervention_Needed"] == True])

avg_scores = df.groupby("Grade")[["ELA_Score", "Math_Score"]].mean()
st.write("### Average Scores by Grade")
st.bar_chart(avg_scores)
