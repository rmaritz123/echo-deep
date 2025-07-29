import streamlit as st

st.set_page_config(page_title="Echo Deep", layout="centered")

# Config
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

# User Input
setting = st.selectbox("Choose Setting:", list(settings.keys()))
selected_archetypes = st.multiselect("Choose Your Archetypes:", list(archetypes.keys()), default=list(archetypes.keys())[:3])

# Background CSS (Streamlit static path fix)
bg_path = f"/{settings[setting]}"
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url('{bg_path}');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        background-repeat: no-repeat;
        color: #f4ecd8;
        font-family: 'Georgia', serif;
    }}
    .block-container {{
        background-color: rgba(0, 0, 0, 0.6);
        padding: 2em;
        border-radius: 10px;
    }}
    h1 {{
        text-align: center;
        font-size: 3em;
        color: #f4ecd8;
        margin-bottom: 1em;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Header
st.markdown("<h1>ECHO DEEP</h1>", unsafe_allow_html=True)

# Display Characters
if selected_archetypes:
    st.markdown("### Your Council:")
    cols = st.columns(len(selected_archetypes))
    for i, name in enumerate(selected_archetypes):
        with cols[i]:
            st.image(archetypes[name], caption=name, use_container_width=True)

# Journal Input
st.markdown("### Start Your Conversation")
entry = st.text_area("Enter your message here...", height=150)

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
