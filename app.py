
import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="Echo Deep", layout="centered")

# Settings and archetypes
settings = {
    "Campfire": "background_campfire.png",
    "Boardroom": "background_boardroom.png",
    "Spaceship": "background_spaceship.png"
}

archetypes = {
    "The Wise Headmaster": "characters/headmaster.png",
    "The Billionaire Investor": "characters/investor.png",
    "The Shadow Self": "characters/shadow_self.png",
    "The Joker": "characters/joker.png",
    "The Serial Entrepreneur": "characters/entrepreneur.png"
}

# Select setting
setting = st.selectbox("Choose Setting:", list(settings.keys()))
bg_image = settings[setting]

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url('{bg_image}');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center; color: #f4ecd8;'>ECHO DEEP</h1>", unsafe_allow_html=True)

# Select archetypes
selected_archetypes = st.multiselect("Choose Your Archetypes:", list(archetypes.keys()), default=list(archetypes.keys())[:3])

# Show characters
cols = st.columns(5)
for i, archetype in enumerate(selected_archetypes):
    with cols[i]:
        st.image(archetypes[archetype], caption=archetype, use_column_width=True)

# Journal Entry
st.subheader("Start your conversation:")
entry = st.text_area("Enter your message...", height=150)

if st.button("Reflect with the Council"):
    if not selected_archetypes or not entry.strip():
        st.warning("Please select archetypes and enter a message.")
    else:
        st.markdown("---")
        st.subheader("Council Responses")
        for name in selected_archetypes:
            st.markdown(f"### {name}")
            st.write(f'*(Placeholder response)* "{entry}"')
        st.markdown("---")
        st.subheader("Council Challenge")
        st.write("Which voice irritated you the most — and why might that be the one you need to listen to?")
