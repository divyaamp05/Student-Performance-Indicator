import streamlit as st
import requests
import time

# Set Page Config
st.set_page_config(page_title="Student Performance Predictor", page_icon="🎓", layout="wide")

# Custom CSS Styling
st.markdown("""
    <style>
        .big-font { font-size: 28px !important; font-weight: bold; color: #4A90E2; text-align: center; }
        .stButton>button { background-color: #4CAF50; color: white; font-size: 18px; border-radius: 10px; padding: 10px; width: 100%; }
        .stButton>button:hover { background-color: #45a049; }
        .stSelectbox, .stNumberInput, .stTextInput { border-radius: 10px !important; }
        .result-box { border: 2px solid #4A90E2; padding: 15px; border-radius: 10px; text-align: center; background-color: #f9f9f9; }
    </style>
""", unsafe_allow_html=True)

# 🎓 Title & Description
st.markdown('<p class="big-font">🎓 Student Performance Predictor 🎯</p>', unsafe_allow_html=True)
st.write("Fill in the details below to **predict the student's Math Score** using machine learning.")

# 📝 SIDEBAR - Information Section
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2965/2965879.png", width=120)  # 🎓 Student Graduate Icon
st.sidebar.header("ℹ️ About this App")
st.sidebar.write("This app predicts a **student's math score** based on their profile using a trained ML model.")

# 🛠️ How It Works
st.sidebar.subheader("🛠️ Steps to Use")
st.sidebar.write("""
1️⃣ Enter student details  
2️⃣ Click **Predict**  
3️⃣ The model analyzes the data  
4️⃣ View the **predicted math score**  
""")

# 📊 Dataset Insights
st.sidebar.subheader("📊 Dataset Insights")
st.sidebar.write("""
- Data from **high school students**
- Features include:
  - **Parental Education**  
  - **Reading & Writing Scores**  
  - **Test Preparation**  
""")

# 🔗 Useful Links
st.sidebar.subheader("🔗 Useful Links")
st.sidebar.markdown("[📖 Learn More](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)")
st.sidebar.markdown("[📝 View Source Code](https://github.com/)")

# 📝 Input Fields
st.markdown("### 📝 Enter Student Details:")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("👤 Gender", ["Male", "Female"])
    race_ethnicity = st.selectbox("🌍 Race/Ethnicity", ["Group A", "Group B", "Group C", "Group D", "Group E"])
    parental_education = st.selectbox("🎓 Parental Education", [
        "Associate's Degree", "Bachelor's Degree", "High School", "Master's Degree", "Some College", "Some High School"
    ])

with col2:
    lunch = st.selectbox("🍽️ Lunch Type", ["Standard", "Free/Reduced"])
    test_prep = st.selectbox("📖 Test Preparation Course", ["None", "Completed"])
    reading_score = st.number_input("📕 Reading Score (0-100)", min_value=0, max_value=100, step=1)
    writing_score = st.number_input("✍️ Writing Score (0-100)", min_value=0, max_value=100, step=1)

# 🚀 Predict Button
if st.button("🚀 Predict Math Score"):  
    with st.spinner("🔄 Processing your data..."):
        time.sleep(2)  # Simulate processing delay

    # Prepare data for API request
    data = {
        "gender": gender,
        "race_ethnicity": race_ethnicity,
        "parental_level_of_education": parental_education,
        "lunch": lunch,
        "test_preparation_course": test_prep,
        "reading_score": reading_score,
        "writing_score": writing_score
    }

    # Call Flask API
    api_url = "http://127.0.0.1:5001/predictdata"  # Ensure Flask is running
    response = requests.post(api_url, json=data)

    # Display Prediction Result
    if response.status_code == 200:
        prediction = response.json().get("prediction", "Error")

        # Show Result
        st.success("✅ Prediction Complete!")
        with st.expander("📊 View Prediction"):
            st.markdown(f'<div class="result-box"><h2>🎯 Predicted Math Score: <span style="color: #FF5733;">{prediction}</span></h2></div>', unsafe_allow_html=True)
    
    else:
        st.error("⚠️ Failed to fetch prediction. Please check if the API is running.")

# Footer
st.markdown("---")
st.markdown("💡 **Created with ❤️ by a Data Enthusiast! 🚀**")