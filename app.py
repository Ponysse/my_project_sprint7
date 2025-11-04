import streamlit as st 
import pandas as pd
import plotly.express as px

st.header('Student Sleep Patterns and Habits')

sleep_df = pd.read_csv("notebooks\student_sleep_patterns.csv")# leer los datos
# Casillas de verificación
st.write("Select the chart(s) you want to create:")
show_hist = st.checkbox('Histogram: Sleep Duration')
show_scatter = st.checkbox('Scatter Plot: Study vs Sleep vs Caffeine')

# Si el usuario hace clic en el checkbox
if show_hist:
    st.write('This histogram will help you visualize the distribution of sleep duration.')
    fig = px.histogram(
        sleep_df, 
        x="Sleep_Duration", 
        color_discrete_sequence=["slateblue"]
    )
    fig.update_layout(
        xaxis_title="Sleep duration",
        yaxis_title="Students",
        title="Sleep duration distribution"
    )
    st.plotly_chart(fig, use_container_width=True)

if show_scatter:
    st.write('This scatter plot shows the correlation between study time, sleep duration, and caffeine consumption.')
    fig = px.scatter(
        sleep_df,
        x="Study_Hours",
        y="Sleep_Duration",
        color="Caffeine_Intake",
        color_continuous_scale="Viridis",
        title="Sleep vs. Study (color = caffeine)",
        labels={"Caffeine_Intake": "Caffeine intake"}
    )
    fig.update_layout(
        xaxis_title="Study Hours",
        yaxis_title="Sleep Duration",
    )
    st.plotly_chart(fig, use_container_width=True)

# Si no se seleccionó nada
if not show_hist and not show_scatter:
    st.warning("Please select at least one chart to create.")