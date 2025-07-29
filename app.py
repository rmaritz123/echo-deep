
import streamlit as st
import openai

st.set_page_config(page_title="Echo Deep", layout="wide")

# --- Settings ---
st.title("🔥 Echo Deep – Inner Dialogue Engine")

settings = {
    "campfire": "🔥 Campfire (Self-Reflection)",
    "council": "🏛️ Council Room (Wisdom & Guidance)",
    "boardroom": "🏢 Boardroom (Career & Business)",
    "spaceship": "🚀 Spaceship (Futuristic Brainstorming)"
}

archetypes = {
    "headmaster": "🧙 The Headmaster – The Sage",
    "investor": "💼 The Investor – The Executive Strategist",
    "shadow": "🩸 The Shadow Self – The Inner Opposite",
    "joker": "🎭 The Trickster – The Joker",
    "builder": "🚀 The Builder – The Serial Entrepreneur"
}

archetype_prompts = {
    "headmaster": "Wise, calm, long-term thinker. Asks reflective questions. Speaks in metaphors and stories.",
    "investor": "Direct, pragmatic, and focused on ROI. Pushes for strategic thinking and results.",
    "shadow": "Provocative, unsettling, exposes hidden fears and blind spots. Challenges core beliefs.",
    "joker": "Witty, chaotic, breaks patterns. Uses humor and absurdity to challenge seriousness.",
    "builder": "Energetic, optimistic, and always hunting for opportunity. Wants fast results and MVPs."
}

# --- UI ---
st.subheader("Choose Your Setting:")
setting = st.selectbox("Scene:", list(settings.keys()), format_func=lambda x: settings[x])

st.subheader("Choose Up to 5 Archetypes:")
selected_archetypes = st.multiselect(
    "Archetypes:", list(archetypes.keys()), default=list(archetypes.keys())[:3],
    format_func=lambda x: archetypes[x]
)

st.subheader("Write Your Journal Entry:")
journal = st.text_area("What’s on your mind today?", height=200)

if st.button("Reflect with the Council") and selected_archetypes and journal:
    st.markdown("---")
    st.subheader("Responses:")
    for key in selected_archetypes:
        st.markdown(f"### {archetypes[key]}")
        st.markdown(f"_{archetype_prompts[key]}_")
        st.write(f'Response to your journal: "{journal}"\n(This is where the GPT response would go.)')


    st.markdown("---")
    st.subheader("🔍 Council Challenge:")
    st.write("Which voice irritated you the most — and why might that be the one you need to listen to?")
