import streamlit as st
from PIL import Image

st.set_page_config(page_title="Echo Deep", layout="centered")

# === CONFIG ===
settings = {
    "Campfire": "static/background_campfire.png",
    "Boardroom": "static/background_boardroom.png",
    "Spaceship": "static/background_spaceship.png"
}

archetypes = {
    "The Wise Headmaster": "static/characters/headmaster.png",
    "The Billionaire Investor": "static/characters/investor.png",
    "The Shadow Self": "static/characters/shadow_self.png",
    "The Joker": "static/characters/joker.png",
    "The Serial Entrepreneur": "static/characters/entrepreneur.png"
}

# === USER CHOICES ===
setting = st.selectbox("Choose Setting:", list(settings.keys()))
selected_archetypes = st.multiselect("Choose Your Archetypes:", list(archetypes.keys()), default=list(archetypes.keys())[:3])

# === DYNAMIC
