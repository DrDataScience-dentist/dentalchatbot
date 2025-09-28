import streamlit as st

# ------------------------------
# Decision tree
# ------------------------------
chat_flow = {
    "start": {
        "message": "Hi 👋 I’m TOOTH RESCUE. Tell me what happened:",
        "options": [
            "🦷 Tooth knocked out (Avulsion)",
            "↔️ Tooth moved (Extrusive luxation)",
            "⬇️ Tooth pushed in (Intrusive luxation)",
            "🌀 Tooth loosened",
            "💥 Tooth broken/chipped",
            "👄 Gum/lip/face injury",
            "😬 Jaw/joint injury",
        ],
    },
    "🦷 Tooth knocked out (Avulsion)": {
        "message": "Is it a permanent tooth or a milk tooth?",
        "options": ["Permanent tooth", "Milk tooth"],
    },
    "🦷 Tooth knocked out (Avulsion) - Permanent tooth": {
        "message": "⚠️ Act fast!\n- Pick tooth by crown, not root\n- Rinse with milk/saline (not water)\n- Put back in socket if possible, bite gauze\n- If not possible → store in milk/saline/saliva\n🚨 Go to dentist immediately!",
        "options": [],
    },
    "🦷 Tooth knocked out (Avulsion) - Milk tooth": {
        "message": "❗ Do NOT put milk teeth back in.\n- Control bleeding with gauze\n- Keep child comfortable\n- Dentist check soon",
        "options": [],
    },
    "↔️ Tooth moved (Extrusive luxation)": {
        "message": "⚠️ Handle gently:\n- Avoid pushing it further\n- Soft diet\n- See dentist within 24h",
        "options": [],
    },
    "⬇️ Tooth pushed in (Intrusive luxation)": {
        "message": "⚠️ Do not try to pull it out yourself.\n- Soft diet\n- See dentist ASAP",
        "options": [],
    },
    "🌀 Tooth loosened": {
        "message": "⚠️ Stabilize the tooth:\n- Avoid biting hard\n- Soft diet\n- See dentist soon",
        "options": [],
    },
    "💥 Tooth broken/chipped": {
        "message": "⚠️ Rinse mouth with water\n- Save broken pieces if possible\n- Avoid eating hard foods\n- See dentist",
        "options": [],
    },
    "👄 Gum/lip/face injury": {
        "message": "🩸 Clean wound\n- Apply pressure to stop bleeding\n- Seek medical/dental care if deep or uncontrolled",
        "options": [],
    },
    "😬 Jaw/joint injury": {
        "message": "🚨 Emergency!\n- Call emergency services if unconscious\n- Support jaw gently\n- Go to hospital immediately",
        "options": [],
    },
}

# ------------------------------
# Session state
# ------------------------------
if "current" not in st.session_state:
    st.session_state.current = "start"

if "history" not in st.session_state:
    st.session_state.history = []

# ------------------------------
# Show conversation history
# ------------------------------
for msg in st.session_state.history:
    if msg["role"] == "bot":
        st.text(f"Bot: {msg['content']}")
    else:
        st.text(f"You: {msg['content']}")

# ------------------------------
# Show current bot message (once)
# ------------------------------
if not st.session_state.history or st.session_state.history[-1]["role"] != "bot":
    bot_msg = chat_flow[st.session_state.current]["message"]
    st.session_state.history.append({"role": "bot", "content": bot_msg})
    st.text(f"Bot: {bot_msg}")

# ------------------------------
# Show clickable options
# ------------------------------
options = chat_flow[st.session_state.current]["options"]
clicked_option = None

if options:
    for i, opt in enumerate(options):
        if st.button(opt, key=f"{st.session_state.current}_{i}"):
            clicked_option = opt
            break

# ------------------------------
# Process click
# ------------------------------
if clicked_option:
    # Record user click
    st.session_state.history.append({"role": "user", "content": clicked_option})

    # Determine next node
    next_key = f"{st.session_state.current} - {clicked_option}" \
        if f"{st.session_state.current} - {clicked_option}" in chat_flow else clicked_option

    st.session_state.current = next_key if next_key in chat_flow else "start"

# ------------------------------
# Restart button for leaf nodes
# ------------------------------
elif not options:
    if st.button("🔄 Restart"):
        st.session_state.current = "start"
        st.session_state.history = []
