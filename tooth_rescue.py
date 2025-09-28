import streamlit as st

st.set_page_config(page_title="🦷 Tooth Rescue WhatsApp Bot", page_icon="🟢")

st.markdown(
    """
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
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------------------
# Decision tree
# ------------------------------
chat_flow = {
    "start": {
        "message": "Hi 👋 I’m *TOOTH RESCUE*. Tell me what happened:",
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
        "message": """⚠️ Act fast!  
- Pick tooth by crown, not root  
- Rinse with milk/saline (not water)  
- Put back in socket if possible, bite gauze  
- If not possible → store in milk/saline/saliva  
🚨 Go to dentist immediately!""",
        "options": [],
    },
    "🦷 Tooth knocked out (Avulsion) - Milk tooth": {
        "message": """❗ Do NOT put milk teeth back in.  
- Control bleeding with gauze  
- Keep child comfortable  
- Dentist check soon""",
        "options": [],
    },
    "👄 Gum/lip/face injury": {
        "message": """🩸 Clean wound  
- Apply pressure to stop bleeding  
- Seek medical/dental care if deep or uncontrolled""",
        "options": [],
    },
    "😬 Jaw/joint injury": {
        "message": """🚨 Emergency!  
- Call emergency services if unconscious  
- Support jaw gently  
- Go to hospital immediately""",
        "options": [],
    },
}

# ------------------------------
# State
# ------------------------------
if "current" not in st.session_state:
    st.session_state.current = "start"
if "history" not in st.session_state:
    st.session_state.history = []

def show_message(role, text):
    if role == "user":
        st.markdown(f"<div class='user-msg'>{text}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='bot-msg'>{text}</div>", unsafe_allow_html=True)

# ------------------------------
# Render conversation
# ------------------------------
for msg in st.session_state.history:
    show_message(msg["role"], msg["content"])

# Current node
node = chat_flow[st.session_state.current]
show_message("bot", node["message"])

# Options (auto advance)
if node["options"]:
    choice = st.radio("Select:", node["options"], key="opt_" + st.session_state.current)
    if choice:
        # Add user reply
        st.session_state.history.append({"role": "user", "content": choice})

        # Next key
        next_key = f"{st.session_state.current} - {choice}" if f"{st.session_state.current} - {choice}" in chat_flow else choice
        if next_key in chat_flow:
            st.session_state.current = next_key
        else:
            st.session_state.current = "start"

        # Add bot reply
        st.session_state.history.append({"role": "bot", "content": chat_flow[st.session_state.current]["message"]})

        st.rerun()
else:
    if st.button("🔄 Restart"):
        st.session_state.current = "start"
        st.session_state.history = []
        st.rerun()
