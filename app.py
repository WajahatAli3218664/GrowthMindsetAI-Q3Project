import streamlit as st
import random
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime
from PIL import Image
import time

# Set page configuration
st.set_page_config(page_title="Elevate Mindset AI", page_icon="🚀", layout="wide")

# Custom Styling
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
        * { font-family: 'Inter', sans-serif; }
        body { background-color: #f8f9fa; color: #333; }
        .title { 
            font-size: 48px; 
            font-weight: 700; 
            text-align: center; 
            background: linear-gradient(90deg, #6A11CB, #2575FC);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 20px; 
            animation: fadeIn 2s ease-in-out; 
        }
        .subheader { 
            font-size: 28px; 
            font-weight: 600; 
            text-align: center; 
            color: #2575FC;
            margin-bottom: 15px; 
            border-bottom: 3px solid #6A11CB; 
            padding-bottom: 10px; 
            animation: slideIn 1.5s ease-in-out; 
        }
        .card { 
            border-radius: 15px; 
            padding: 20px; 
            text-align: center; 
            font-weight: 500; 
            margin-bottom: 20px; 
            animation: fadeIn 2s ease-in-out; 
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            background-color: #ffffff; 
            border-left: 8px solid #2575FC; 
            color: #444; 
        }
        .footer { 
            font-size: 16px; 
            color: white; 
            text-align: center; 
            padding: 20px;
            margin-top: 30px; 
            background: linear-gradient(90deg, #6A11CB, #2575FC);
            border-radius: 10px; 
            font-weight: 500; 
            animation: fadeIn 2s ease-in-out; 
        }
        .stButton>button { 
            background: linear-gradient(90deg, #6A11CB, #2575FC);
            color: white; 
            font-size: 16px; 
            font-weight: 600; 
            border: none; 
            border-radius: 8px; 
            padding: 12px 24px; 
            cursor: pointer; 
            transition: transform 0.3s ease, box-shadow 0.3s ease; 
            margin-top: 10px; 
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .stButton>button:hover { 
            transform: scale(1.05); 
            box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
        }
        .sidebar .sidebar-content {
            background: linear-gradient(180deg, #6A11CB, #2575FC);
            color: white;
            padding: 20px;
            border-radius: 15px;
        }
        @keyframes fadeIn { 
            from { opacity: 0; } 
            to { opacity: 1; } 
        }
        @keyframes slideIn { 
            from { transform: translateX(-100%); } 
            to { transform: translateX(0); } 
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: white;'>🚀 Elevate Mindset AI</h2>", unsafe_allow_html=True)
    st.markdown("---")
    user_name = st.text_input("Enter your name to personalize your experience:")
    if user_name:
        st.success(f"Welcome, **{user_name}**! Let's grow together. ☺")
    st.markdown("---")
    st.markdown("### Navigation")
    page = st.radio("Go to", ["Home", "Daily Inspiration", "Goal Setting", "Productivity Challenge", "Charts & Analytics", "Habit Tracker", "Mindfulness Exercises", "Resource Library", "Community Forum", "Daily Journal", "Progress Photos", "Meditation Timer", "Achievement Badges"])
    st.markdown("---")
    st.markdown("### Key Insights")
    st.markdown("- ✅ Small, consistent steps lead to big changes over time.")
    st.markdown("- 🟢 A growth mindset can increase your resilience and productivity.")
    st.markdown("- 🔍 Celebrate every win, no matter how small!")
    st.markdown("---")
    st.markdown("### Reach New Heights Together!")
    st.markdown("Empowering Growth with Elevate Mindset AI")

# Main Content
if page == "Home":
    st.markdown("<h1 class='title'>🌟 Welcome to Elevate Mindset AI</h1>", unsafe_allow_html=True)
    st.markdown("<h2 class='subheader'>Your personal growth companion for mindset elevation and productivity enhancement</h2>", unsafe_allow_html=True)
    st.markdown("<div class='card'>🚀 Start your journey today by exploring the features in the sidebar.</div>", unsafe_allow_html=True)

elif page == "Daily Inspiration":
    st.markdown("<h1 class='title'>💡 Daily Inspiration</h1>", unsafe_allow_html=True)
    quotes = [
        "Dream big and dare to fail. — Norman Vaughan",
        "Do what you can, with what you have, where you are. — Theodore Roosevelt",
        "Act as if what you do makes a difference. It does. — William James",
        "Happiness is not something ready-made. It comes from your own actions. — Dalai Lama",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. — Winston Churchill"
    ]
    if st.button("✨ Inspire Me!"):
        st.markdown(f"<div class='card'>{random.choice(quotes)}</div>", unsafe_allow_html=True)

elif page == "Goal Setting":
    st.markdown("<h1 class='title'>🎯 Goal Setting</h1>", unsafe_allow_html=True)
    goal = st.text_input("What is your goal for this week?")
    if goal:
        st.success(f"🚀 Goal Set: **{goal}**. Stay committed and keep moving forward!")

elif page == "Productivity Challenge":
    st.markdown("<h1 class='title'>🔥 Productivity Challenge</h1>", unsafe_allow_html=True)
    challenges = [
        "Learn something new today and teach it to someone.",
        "Step out of your comfort zone and try something different!",
        "Spend 15 minutes reflecting on your achievements.",
        "List three things you're grateful for today.",
        "Declutter your workspace and organize your thoughts."
    ]
    if st.button("💡 Get Challenge!"):
        st.info(f"💡 **Challenge:** {random.choice(challenges)}")

elif page == "Charts & Analytics":
    st.markdown("<h1 class='title'>📊 Charts & Analytics</h1>", unsafe_allow_html=True)
    st.markdown("<h2 class='subheader'>Track your progress with interactive charts</h2>", unsafe_allow_html=True)
    
    # Sample Data
    data = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "Goals Set": [5, 7, 10, 8, 12, 15],
        "Goals Achieved": [3, 5, 8, 7, 10, 12]
    })
    
    # Bar Chart
    st.markdown("### Goals Set vs Goals Achieved")
    fig = px.bar(data, x="Month", y=["Goals Set", "Goals Achieved"], barmode="group")
    st.plotly_chart(fig, use_container_width=True)
    
    # Line Chart
    st.markdown("### Progress Over Time")
    fig2 = px.line(data, x="Month", y=["Goals Set", "Goals Achieved"], markers=True)
    st.plotly_chart(fig2, use_container_width=True)
    
    # Pie Chart
    st.markdown("### Goal Completion Rate")
    completion_rate = (data["Goals Achieved"].sum() / data["Goals Set"].sum()) * 100
    fig3 = px.pie(values=[completion_rate, 100 - completion_rate], names=["Completed", "Pending"], title="Goal Completion Rate")
    st.plotly_chart(fig3, use_container_width=True)

elif page == "Habit Tracker":
    st.markdown("<h1 class='title'>📅 Habit Tracker</h1>", unsafe_allow_html=True)
    st.markdown("<h2 class='subheader'>Track your daily habits and build consistency</h2>", unsafe_allow_html=True)
    
    habits = ["Meditation", "Exercise", "Reading", "Journaling", "Learning"]
    selected_habits = st.multiselect("Select habits to track:", habits)
    
    if selected_habits:
        st.write("### Your Habits:")
        for habit in selected_habits:
            st.checkbox(f"{habit}", key=habit)

elif page == "Mindfulness Exercises":
    st.markdown("<h1 class='title'>🧘 Mindfulness Exercises</h1>", unsafe_allow_html=True)
    st.markdown("<h2 class='subheader'>Practice mindfulness to reduce stress and improve focus</h2>", unsafe_allow_html=True)
    
    exercises = [
        "5-Minute Breathing Exercise",
        "Body Scan Meditation",
        "Gratitude Journaling",
        "Mindful Walking",
        "Visualization Exercise"
    ]
    selected_exercise = st.selectbox("Choose an exercise:", exercises)
    
    if selected_exercise:
        st.info(f"🧘 **Exercise:** {selected_exercise}")
        st.write("Follow these steps:")
        st.write("1. Find a quiet place.")
        st.write("2. Set a timer for 5-10 minutes.")
        st.write("3. Focus on your breath or the exercise instructions.")
        st.write("4. Reflect on your experience afterward.")

elif page == "Resource Library":
    st.markdown("<h1 class='title'>📚 Resource Library</h1>", unsafe_allow_html=True)
    st.markdown("<h2 class='subheader'>Explore books, articles, and videos for personal growth</h2>", unsafe_allow_html=True)
    
    resources = {
        "Books": ["Atomic Habits by James Clear", "The Power of Now by Eckhart Tolle", "Mindset by Carol Dweck"],
        "Articles": ["The Science of Habit Formation", "How to Build a Growth Mindset", "10 Mindfulness Tips for Beginners"],
        "Videos": ["TED Talk: The Power of Vulnerability", "How to Stay Focused", "Mindfulness Meditation Guide"]
    }
    
    category = st.selectbox("Choose a category:", list(resources.keys()))
    if category:
        st.write(f"### {category}:")
        for item in resources[category]:
            st.write(f"- {item}")

elif page == "Community Forum":
    st.markdown("<h1 class='title'>💬 Community Forum</h1>", unsafe_allow_html=True)
    st.markdown("<h2 class='subheader'>Connect with others and share your journey</h2>", unsafe_allow_html=True)
    
    if "forum_posts" not in st.session_state:
        st.session_state.forum_posts = []
    
    post = st.text_area("Share your thoughts or ask a question:")
    if st.button("Post"):
        if post:
            st.session_state.forum_posts.append({"user": user_name, "post": post, "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
            st.success("Your post has been shared!")
    
    st.write("### Recent Posts:")
    for p in st.session_state.forum_posts:
        st.write(f"**{p['user']}** ({p['time']}): {p['post']}")
        st.write("---")

elif page == "Daily Journal":
    st.markdown("<h1 class='title'>📔 Daily Journal</h1>", unsafe_allow_html=True)
    st.markdown("<h2 class='subheader'>Write and reflect on your daily experiences</h2>", unsafe_allow_html=True)
    
    journal_entry = st.text_area("Write your journal entry:")
    if st.button("Save Entry"):
        if "journal_entries" not in st.session_state:
            st.session_state.journal_entries = []
        st.session_state.journal_entries.append({"date": datetime.now().strftime("%Y-%m-%d"), "entry": journal_entry})
        st.success("Journal entry saved!")
    
    if "journal_entries" in st.session_state:
        st.write("### Journal Entries:")
        for entry in st.session_state.journal_entries:
            st.write(f"**{entry['date']}:** {entry['entry']}")
            st.write("---")

elif page == "Progress Photos":
    st.markdown("<h1 class='title'>📸 Progress Photos</h1>", unsafe_allow_html=True)
    st.markdown("<h2 class='subheader'>Track your progress with photos</h2>", unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader("Upload a progress photo:", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Your Progress Photo", use_column_width=True)
        st.success("Photo uploaded successfully!")

elif page == "Meditation Timer":
    st.markdown("<h1 class='title'>⏳ Meditation Timer</h1>", unsafe_allow_html=True)
    st.markdown("<h2 class='subheader'>Practice mindfulness with a built-in timer</h2>", unsafe_allow_html=True)
    
    meditation_time = st.slider("Set meditation time (minutes):", 1, 30, 5)
    if st.button("Start Timer"):
        with st.spinner(f"Meditating for {meditation_time} minutes..."):
            time.sleep(meditation_time * 60)
        st.success("Meditation session complete! 🧘‍♂️")

elif page == "Achievement Badges":
    st.markdown("<h1 class='title'>🏅 Achievement Badges</h1>", unsafe_allow_html=True)
    st.markdown("<h2 class='subheader'>Earn badges for completing tasks and challenges</h2>", unsafe_allow_html=True)
    
    if "badges" not in st.session_state:
        st.session_state.badges = []
    
    tasks = ["Complete 5 Goals", "Meditate for 7 Days", "Write 10 Journal Entries"]
    for task in tasks:
        if st.button(f"Complete: {task}"):
            st.session_state.badges.append(task)
            st.success(f"🏅 You earned a badge for: {task}")
    
    if st.session_state.badges:
        st.write("### Your Badges:")
        for badge in st.session_state.badges:
            st.write(f"- {badge}")

# Footer
st.markdown("""
<div class='footer'>
🚀 Believe in yourself—every challenge you overcome, every step you take, and every lesson you learn shapes your incredible journey! ❤️🌟<br>
<strong>Created by Wajahat</strong>
</div>
""", unsafe_allow_html=True)
