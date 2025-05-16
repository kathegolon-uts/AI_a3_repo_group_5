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
    st.set_page_config(page_title="Melofy", layout="centered")
    st.markdown("<h1 style='text-align: center; font-family: Arial, sans-serif;'>Melofy</h1>",
    unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center;'>The AI Mood-Based Music Recommender 🎵 🎶</h2>", unsafe_allow_html=True)

    # Welcome Lottie BEFORE title
    welcome_lottie = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_3vbOcw.json")
    if welcome_lottie:
        st_lottie(welcome_lottie, height=250, key="welcome")

    # Title and description
    st.markdown("""
    <div style="font-size: 18px; line-height: 1.8; padding: 10px 20px; border-radius: 10px;">

    <h3 style="text-align: center;">👋 Welcome!</h3>

    <p style="text-align: center;">This app detects your mood from a selfie and recommends music to match — or uplift — your mood.</p>

    <h4>🎯 Here's how it works:</h4>
    <ul>
        <li>📸 <b>Upload a selfie</b> (jpg/jpeg/png)</li>
        <li>🤖 <b>We detect your mood</b> using AI facial recognition</li>
        <li>🎶 <b>Get a Spotify song</b> that fits your vibe</li>
    </ul>

    <p style="text-align: center; font-size: 25px;">Let’s find the perfect track for you! 🚀</p>

    </div>
    """, unsafe_allow_html=True)

    # Load the Moodify dataset
    moodify_df = load_moodify_dataset("data/278k_labelled_uri.csv")

    # --- User Consent Agreement ---
    st.markdown("""
    <div style="background-color:#f0f2f6; padding:15px; border-radius:10px;">
        <h4 style="text-align:center;">🛡️ User Consent</h4>
        <p style="text-align:center; font-size:16px;">
            By uploading or capturing a photo, you consent to the use of your image for mood detection within this session only. 
            No images are stored or shared. All processing happens in real-time and is fully anonymised.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Ask user to accept
    consent = st.checkbox("I consent to the processing of my uploaded image for this session.")

    if consent:
        # Display upload options only if consent is given
        st.markdown("<h6 style='text-align: center;'>📸 Choose how you'd like to upload your photo:</h4>", unsafe_allow_html=True)

        # Center the radio buttons
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            selfie_option = st.radio(
                "",  # No label here, it's in the header above
                ("Take a selfie (camera)", "Upload an image"),
                horizontal=True
            )

        # Display input based on selection
        if selfie_option == "Take a selfie (camera)":
            uploaded_file = st.camera_input("Take a selfie (camera)")
        elif selfie_option == "Upload an image":
            uploaded_file = st.file_uploader("Upload your picture (jpg/jpeg/png)", type=["jpg", "jpeg", "png"])
    else:
        uploaded_file = None

    if uploaded_file is not None:
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

        mood_emoji = {"happy": "😊", "sad": "😢", "calm": "😐", "energetic": "⚡"}
        st.success(f"Your detected mood is: **{mood.capitalize()}** {mood_emoji.get(mood, '')}")


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

            # --- Separator line between songs ---
            st.markdown("<hr style='margin-top: 30px; margin-bottom: 30px;'>", unsafe_allow_html=True)

            # --- Subtitle for uplifting song ---
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
            
        st.markdown("<h3 style='text-align: center;'>🎶 Did you enjoy your song recommendation?</h3>", unsafe_allow_html=True)
            
        # Create columns
        col1, col2, col3, col4 = st.columns([8, 1, 1, 10])

        # Initialize feedback state
        feedback = None

        # Buttons in narrow columns
        with col2:
            if st.button("👍"):
                feedback = "positive"
        with col4:
            if st.button("👎"):
                feedback = "negative"

        # Display feedback message outside the columns
        if feedback == "positive":
            st.success("Thanks for your feedback! 🎵")
        elif feedback == "negative":
            st.warning("Thanks for your feedback! We'll try better next time! 🎶")
    st.markdown(
    """
    <div style='position: fixed; bottom: 60px; right: 10px; text-align: right; font-size: 12px; color: gray;'>
        <b>Contributors:</b><br>
        Jaime Garcia y Garcia<br>
        Katherin Gomez Londono<br>
        Miguel Ramal<br>
        Spenser Gautama<br>
        Dipesh Shrestha
    </div>
    """,
    unsafe_allow_html=True)


if __name__ == "__main__":
    main()
