import streamlit as st
import pandas as pd
import altair as alt
from wordcloud import WordCloud
import plotly.express as px

# Sidebar setup
st.sidebar.title("Navigation")
option = st.sidebar.selectbox("Go to", ["About Me", "Projects", "Contact"])

# Page navigation logic
if option == "About Me":
    st.title("About Me")
    st.write("Hi! I'm [Your Name], a data enthusiast passionate about solving real-world problems through analytics and machine learning.")

elif option == "Projects":
    st.title("My Projects")
    
    # Project 1: Customer Segmentation
    st.subheader("Project 1: Customer Segmentation")
    st.write("Segment customers based on their purchasing behaviors using clustering techniques.")
    st.write("Features:")
    st.write("- Visualizations of customer demographics using bar and pie charts.")
    st.write("- Interactive sliders to adjust cluster numbers dynamically.")

    # Project 2: Sentiment Analysis of Tweets
    st.subheader("Project 2: Sentiment Analysis of Tweets")
    st.write("Analyze Twitter data to classify sentiments (positive, neutral, negative).")
    st.write("Features:")
    st.write("- Word clouds for common words by sentiment.")
    st.write("- Dynamic keyword search for tweets with real-time sentiment classification.")

    # Generate a word cloud (dummy example)
    text = "positive neutral negative sentiment"
    wordcloud = WordCloud().generate(text)
    st.image(wordcloud.to_array(), caption="Sentiment Word Cloud", use_column_width=True)

    # Project 3: Sales Forecasting Dashboard
    st.subheader("Project 3: Sales Forecasting Dashboard")
    st.write("Predict future sales trends using historical data with machine learning models.")
    st.write("Features:")
    st.write("- Time-series data visualization with forecast overlay.")
    st.write("- Parameters for tweaking forecasting (e.g., duration).")

    # Project 4: COVID-19 Analysis
    st.subheader("Project 4: COVID-19 Analysis")
    st.write("Visualize and track COVID-19 cases globally or regionally.")
    st.write("Features:")
    st.write("- Map visualizations of cases by country.")
    st.write("- Date filter to view cases at different times.")

    # Dummy map example
    covid_data = pd.DataFrame({
        'Country': ['USA', 'India', 'Brazil'],
        'Cases': [100000, 50000, 30000],
        'Latitude': [37.0902, 20.5937, -14.2350],
        'Longitude': [-95.7129, 78.9629, -51.9253]
    })
    st.map(covid_data)

    # Project 5: Resume Keyword Extraction
    st.subheader("Project 5: Resume Keyword Extraction")
    st.write("Extract skills and keywords from resumes using Natural Language Processing.")
    st.write("Features:")
    st.write("- Upload feature for resumes in PDF format.")
    st.write("- Display a word cloud of extracted keywords.")

elif option == "Contact":
    st.title("Contact")
    st.write("Connect with me on LinkedIn or email me at [your email]")

    # Contact form
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit = st.form_submit_button("Submit")

        if submit:
            st.write(f"Thank you for reaching out, {name}! I'll get back to you shortly.")
