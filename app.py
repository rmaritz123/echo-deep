
import streamlit as st

st.set_page_config(page_title="Echo Deep", layout="centered")

# --- Custom CSS Styling with Background Image ---
st.markdown("""
<style>
body {
    background-image: url('campfire_background.png');
    background-size: cover;
    background-position: center;
    color: #f4ecd8;
    font-family: 'Georgia', serif;
}
h1 {
    color: #f4ecd8;
    text-align: center;
    font-size: 3em;
    margin-top: 0.5em;
}
label, .stSelectbox label, .stTextArea label {
    font-size: 1.2em;
    color: #f4ecd8;
}
.stButton>button {
    background-color: #6b4f3b;
    color: #f4ecd8;
    font-weight: bold;
    border-radius: 10px;
    padding: 10px 24px;
    margin-top: 20px;
}
.stTextArea textarea {
    background-color: #f4ecd8;
    color: #1c1f26;
    border-radius: 10px;
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>ECHO DEEP</h1>", unsafe_allow_html=True)

# --- Settings ---
setting = st.selectbox("Setting:", ["Campfire", "Boardroom", "Council Room", "Spaceship"])

# --- Archetypes ---
archetypes = [
    "The Wise Headmaster",
    "The Billionaire Investor",
    "The Shadow Self",
    "The Joker",
    "The Serial Entrepreneur"
]
selected = st.multiselect("Choose your archetypes:", archetypes, default=archetypes[:3])

# --- Journal Input ---
st.subheader("Start your conversation:")
entry = st.text_area("Enter your message...")

# --- Simulate Council Response ---
if st.button("Reflect with the Council"):
    if not entry or not selected:
        st.warning("Please provide a journal entry and select at least one archetype.")
    else:
        st.markdown("---")
        st.subheader("Council Responses")
        for a in selected:
            st.markdown(f"### {a}")
            st.write(f"*(Placeholder response)* "{entry}"")
        st.markdown("---")
        st.subheader("Council Challenge")
        st.write("Which voice irritated you the most — and why might that be the one you need to listen to?")
