import streamlit as st
import pandas as pd
import plotly.express as px

# Title
st.title("Business Performance Dashboard")

# Upload CSV
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Data Preview", df.head())

    # Let user pick columns for visualization
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    if len(numeric_cols) >= 2:
        x_axis = st.selectbox("X-axis", numeric_cols)
        y_axis = st.selectbox("Y-axis", numeric_cols, index=1)

        fig = px.scatter(df, x=x_axis, y=y_axis, title=f"{x_axis} vs {y_axis}")
        st.plotly_chart(fig)
    else:
        st.warning("Please upload a dataset with at least 2 numeric columns.")
else:
    st.info("Upload a CSV file to see the dashboard.")
