import streamlit as st
import streamlit.components.v1 as components
from streamlit_lottie import st_lottie
import requests
import base64

from src.emotion_detection import detect_emotion
from src.music_recommender import (
    load_moodify_dataset,
    map_emotion_to_mood,
    recommend_song
)

# ----------------------------- Helper Functions ----------------------------- #

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def embed_spotify(uri: str):
    track_id = uri.split(":")[-1]

    st.markdown(
        f"""
        <div style="background-color:#f5f5f5; padding:15px; border-radius:15px; margin-bottom:30px; width: 400px; margin-left: auto; margin-right: auto;">
            <iframe src="https://open.spotify.com/embed/track/{track_id}" width="100%" height="80" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>
            <div style="text-align:center; margin-top:10px;">
                <a href="https://open.spotify.com/track/{track_id}" target="_blank" 
                   style="background-color:#1DB954; color:white; padding:8px 18px; 
                          border-radius:20px; text-decoration:none; font-weight:bold;">
                    🎵 Open in Spotify
                </a>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ----------------------------- Streamlit App ----------------------------- #

def main():
    st.set_page_config(page_title="AI Mood-Based Music Recommender 🎵", layout="centered")

    # Welcome Lottie BEFORE title
    welcome_lottie = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_3vbOcw.json")
    if welcome_lottie:
        st_lottie(welcome_lottie, height=250, key="welcome")

    # Title and description
    st.title("🎵 AI Mood-Based Music Recommender 🎶")
    st.markdown("""
Welcome! 👋  
This app detects your mood from a selfie and recommends music to match (or uplift) your mood.  
Here's how it works:
- 📸 Upload a selfie (jpg/jpeg/png).
- 🤖 We'll detect your mood using AI facial recognition.
- 🎶 Get a Spotify song that fits your vibe!

Let's find the perfect track for you! 🚀
""")

    # Load the Moodify dataset
    moodify_df = load_moodify_dataset("data/278k_labelled_uri.csv")

    # File uploader
    uploaded_file = st.file_uploader(
        "Upload a selfie (jpg/jpeg/png)",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file:
        # Center uploaded image manually
        img_data = uploaded_file.getvalue()
        b64 = base64.b64encode(img_data).decode()

        st.markdown(
            f"""
            <div style="text-align: center;">
                <img src="data:image/jpeg;base64,{b64}" alt="Uploaded Image" width="350">
            </div>
            """,
            unsafe_allow_html=True
        )

        with st.spinner("Analyzing your mood..."):
            emotion = detect_emotion(uploaded_file)
            mood = map_emotion_to_mood(emotion)

        st.success(f"Your detected mood is: **{mood.capitalize()}**")

        # ---Main Title ---
        st.markdown("""
            <h2 style='text-align: center;'>🎧 Recommended Track</h2>
        """, unsafe_allow_html=True)

        # ---Subtitle before first song ---
        st.markdown("""
                    <h3 style='text-align: center;'>🎵 Here's a song matching your current mood:</h3>
                    """, unsafe_allow_html=True)

        if mood == "sad":
            sad_uri = recommend_song(moodify_df, "sad")
            happy_uri = recommend_song(moodify_df, "happy")

            if sad_uri:
                embed_spotify(sad_uri)

            # ---Subtitle for happy uplifting song ---
            st.markdown("""
                        <h3 style='text-align: center;'>🌞 Here's a happy song to lift your spirit:</h3>
                        """, unsafe_allow_html=True)
            
            if happy_uri:
                embed_spotify(happy_uri)
        else:
            uri = recommend_song(moodify_df, mood)
            if uri:
                embed_spotify(uri)
            else:
                st.error("Sorry, no songs found for your mood.")

if __name__ == "__main__":
    main()
