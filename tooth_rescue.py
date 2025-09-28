import streamlit as st

# ------------------------------
# Page config and styles
# ------------------------------
st.set_page_config(page_title="🦷 Tooth Rescue Bot", page_icon="🟢")

st.markdown("""
<style>
.user-msg {
    background-color: #dcf8c6;
    padding: 10px;
    border-radius: 10px;
    margin: 5px 0;
    text-align: right;
}
.bot-msg {
    background-color: #ffffff;
    padding: 10px;
    border-radius: 10px;
    margin: 5px 0;
    border: 1px solid #ddd;
    text-align: left;
}
button {
    margin: 5px 5px 5px 0;
}
</style>
""", unsafe_allow_html=True)

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
# Helper to show messages
# ------------------------------
def show_message(role, text):
    if role == "user":
        st.markdown(f"<div class='user-msg'>{text}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='bot-msg'>{text}</div>", unsafe_allow_html=True)

# ------------------------------
# Render chat history
# ------------------------------
for msg in st.session_state.history:
    show_message(msg["role"], msg["content"])

# ------------------------------
# Show current bot message
# ------------------------------
node = chat_flow[st.session_state.current]
show_message("bot", node["message"])

# ------------------------------
# Show clickable options
# ------------------------------
clicked_option = None
if node["options"]:
    for option in node["options"]:
        if st.button(option, key=f"{st.session_state.current}_{option}"):
            clicked_option = option
            break

if clicked_option:
    st.session_state.history.append({"role": "user", "content": clicked_option})
    next_key = f"{st.session_state.current} - {clicked_option}" if f"{st.session_state.current} - {clicked_option}" in chat_flow else clicked_option
    st.session_state.current = next_key if next_key in chat_flow else "start"
    st.session_state.history.append({"role": "bot", "content": chat_flow[st.session_state.current]["message"]})
    st.experimental_rerun()
elif not node["options"]:
    if st.button("🔄 Restart"):
        st.session_state.current = "start"
        st.session_state.history = []
        st.experimental_rerun()
