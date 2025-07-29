
import streamlit as st
import openai

st.set_page_config(page_title="Echo Deep", layout="centered")

# --- Header ---
st.markdown("""
<style>
body {
    background-color: #1c1f26;
    color: #f4ecd8;
    font-family: 'Georgia', serif;
}
h1 {
    color: #f4ecd8;
    text-align: center;
}
select, textarea, input[type="text"] {
    background-color: #f4ecd8;
    color: #000000;
    border-radius: 5px;
    padding: 0.5em;
}
.stButton>button {
    background-color: #6b4f3b;
    color: #f4ecd8;
    font-weight: bold;
    border-radius: 10px;
    padding: 10px 24px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>ECHO DEEP</h1>", unsafe_allow_html=True)

# --- Choose Setting ---
st.subheader("Choose Setting")
setting = st.selectbox("Select your setting", ["Campfire", "Boardroom", "Council Room", "Spaceship"])

# --- Choose Archetypes ---
st.subheader("Choose Your Archetypes (Max 5)")
archetypes = [
    "The Wise Headmaster",
    "The Billionaire Investor",
    "The Shadow Self",
    "The Joker",
    "The Serial Entrepreneur"
]
selected_archetypes = st.multiselect("Select Archetypes", archetypes, default=archetypes[:3])

# --- Journal Entry ---
st.subheader("Journal Entry")
journal_entry = st.text_area("Write your thoughts here...", height=200)

# --- Submit Button ---
if st.button("Reflect with the Council"):
    if not selected_archetypes or not journal_entry:
        st.warning("Please select at least one archetype and enter a journal entry.")
    else:
        st.markdown("---")
        st.subheader("Council Responses")
        for archetype in selected_archetypes:
            st.markdown(f"### {archetype}")
            st.write(f"*(Placeholder)* Insightful response to your journal entry: "{journal_entry}"")
        st.markdown("---")
        st.subheader("🔍 Council Challenge")
        st.write("Which voice irritated you the most — and why might that be the one you need to listen to?")
