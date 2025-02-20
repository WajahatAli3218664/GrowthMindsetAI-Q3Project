import streamlit as st

# Set the page title and favicon
st.set_page_config(page_title="🌟Elevate Mindset AI 💡", page_icon="🌟")

# Custom CSS for a sleek UI
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Times+New+Roman&display=swap');
    
    .stApp {
        background-color: navy blue;
        font-family: 'Times New Roman', serif;
    }
    .title {
        font-size: 42px;
        font-weight: bold;
        background: linear-gradient(90deg, #4A90E2, #6A11CB);
        -webkit-background-clip: text;
        -webkit-text-fill-color: white;
        text-align: center;
        margin-bottom: 15px;
    }
    .subheader {
        font-size: 24px;
        color: black;
        font-weight: bold;
        border-bottom: 3px solid #6A11CB;
        padding-bottom: 5px;
        margin-bottom: 15px;
    }
    .quote-box {
        background-color: #FFF3CD;
        border-left: 5px solid #FFCC00;
        padding: 15px;
        font-size: 18px;
        font-style: italic;
        font-weight: bold;
        text-align: center;
        color: black;
        border-radius: 8px;
    }
    .footer {
    font-size: 14px;
    color: #FFD700; /* Light golden for better highlight */
    text-align: center;
    padding: 15px;
    margin-top: 20px;
    background-color: #007777; /* Slightly darker cyan for a professional look */
    border-radius: 8px;
    font-weight: bold;
}

    </style>
    """, unsafe_allow_html=True)

# Title with gradient color effect
st.markdown("<h1 class='title'>🌟Elevate Mindset AI💡</h1>", unsafe_allow_html=True)

# Introduction Section
st.markdown("<h2 class='subheader'>🚀Unlock Your Growth Potential!🌱</h2>", unsafe_allow_html=True)
st.write("""
    Overcome challenges, grow from failures, and **unlock your true potential**. 
    This AI-powered app empowers you with **reflection, challenges, and achievements!** 🌟
""")

# Growth Mindset Quote Section with Yellow Background
st.markdown("<h2 class='subheader'>🌟 Inspiring Words to Fuel Your Growth</h2>", unsafe_allow_html=True)
st.markdown("""
    <div class='quote-box'>
        "Your time is limited, so don’t waste it living someone else’s life."<br>
        — Steve Jobs
    </div>
""", unsafe_allow_html=True)

# Input for challenges
st.markdown("<h2 class='subheader'>🔧Step Up to Your Next Challenge!</h2>", unsafe_allow_html=True)
user_input = st.text_input("Describe a challenge you're facing:")

if user_input:
    st.success(f"💪 **You're facing:** {user_input}. Keep pushing forward! 🚀")
else:
    st.warning("Tell us about your challenge to get started!")

# Reflection section
st.markdown("<h2 class='subheader'>💭Deepen Your Insights & Reflections!</h2>", unsafe_allow_html=True)
st.write("Every experience holds a lesson. Share a recent insight that helped you grow! 💡")
reflection = st.text_area("Write your reflection here:")

if reflection:
    st.success(f"✨ **Great Insight!** Your reflection: {reflection}")
else:
    st.info("Reflecting on past experiences helps you grow. Share your thoughts!")

# Achievement section
st.markdown("<h2 class='subheader'>🥇 Honor Your Success!</h2>", unsafe_allow_html=True)
achievement = st.text_input("Share something you've recently accomplished:")

if achievement:
    st.success(f"🎉 **Amazing!** You achieved: {achievement}")
else:
    st.info("Big or small, every achievement counts! Share one now!")

# Motivation Button
if st.button("🔥 Need More Motivation?"):
    st.success("You're doing amazing! Every step counts. Keep growing and shining! 💫")

# Footer
st.markdown("""
    <div class='footer'>
        🚀 Believe in yourself—every challenge you overcome, every step you take, and every lesson you learn shapes the incredible journey of your growth!❤️🌟<br>
        <strong>Created by Wajahat Ali</strong>
    </div>
""", unsafe_allow_html=True)
