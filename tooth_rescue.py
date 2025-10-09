import streamlit as st

# Full decision flow for TOOTH RESCUE
chat_flow = {
    # --- Start ---
    "start": {
        "message": "👋 Hi! I’m **TOOTH RESCUE** — here to guide you through what to do for a dental injury.\n\nPlease select the option that best describes what happened:",
        "options": [
            "🦷 Tooth completely knocked out (Avulsion)",
            "↔️ Tooth moved slightly out (Extrusive luxation)",
            "⬇️ Tooth pushed in (Intrusive luxation)",
            "🌀 Tooth loosened",
            "💥 Tooth broken or chipped",
            "👄 Injury to gums, lips or face (soft tissue injury)",
            "😬 Injured jaws and joints"
        ]
    },

    # --- AVULSION ---
    "🦷 Tooth completely knocked out (Avulsion)": {
        "message": "Is it a **permanent tooth** or a **milk tooth**?",
        "options": ["Permanent tooth", "Milk tooth"]
    },

    # Permanent tooth
    "🦷 Tooth completely knocked out (Avulsion) - Permanent tooth": {
        "message": "How long has it been since the tooth got knocked out?",
        "options": ["< 60 minutes", "> 60 minutes"]
    },

    # Permanent tooth - < 60 mins
    "🦷 Tooth completely knocked out (Avulsion) - Permanent tooth - < 60 minutes": {
        "message": "Where is the tooth right now?",
        "options": ["On the ground (unwashed)", "In my hand"]
    },

    # Tooth found locations
    "🦷 Tooth completely knocked out (Avulsion) - Permanent tooth - < 60 minutes - On the ground (unwashed)": {
        "message": "⚠️ Follow these steps immediately:\n\n1️⃣ Pick the tooth up **by the crown** (white part), avoid touching the root.\n2️⃣ If dirty, rinse gently with **milk** or **saline**.\n3️⃣ Try to put it **back into the socket** gently.\n4️⃣ Bite on gauze to hold it in place.\n\nIf unable to replant, choose below:",
        "options": ["Tooth replanted into jaw", "Tooth not replanted into jaw"]
    },
    "🦷 Tooth completely knocked out (Avulsion) - Permanent tooth - < 60 minutes - In my hand": {
        "message": "⚠️ Follow these steps immediately:\n\n1️⃣ Hold tooth by **crown**, not the root.\n2️⃣ If dirty, rinse gently with **milk** or **saline**.\n3️⃣ Try to **reinsert tooth** into socket gently.\n4️⃣ Bite on gauze to stabilize.\n\nIf unable to replant, choose below:",
        "options": ["Tooth replanted into jaw", "Tooth not replanted into jaw"]
    },
    "Tooth replanted into jaw": {
        "message": "✅ Great job! Keep the tooth stable by biting on gauze. 🚑 See a dentist **immediately** for further stabilization and antibiotics.",
        "options": []
    },
    "Tooth not replanted into jaw": {
        "message": "🦷 If not replanted, place tooth in one of these:\n- 🥛 Milk\n- 💧 Saline\n- 😮 Your saliva (in a clean cup)\n- 🚫 Water (only if nothing else)\n\nThen go to a dentist **immediately**.",
        "options": []
    },

    # Permanent tooth - > 60 mins
    "🦷 Tooth completely knocked out (Avulsion) - Permanent tooth - > 60 minutes": {
        "message": "🕐 Since it’s been over an hour, the prognosis is poor, but replantation can still help preserve bone.\n\nKeep the tooth in **milk or saline** and visit a **dentist immediately**.",
        "options": []
    },

    # Milk tooth
    "🦷 Tooth completely knocked out (Avulsion) - Milk tooth": {
        "message": "What is the **age of the child**?",
        "options": ["0–6 years", "6–12 years", "> 12 years"]
    },
    "🦷 Tooth completely knocked out (Avulsion) - Milk tooth - 0–6 years": {
        "message": "Is the bleeding under control?",
        "options": ["Yes", "No"]
    },
    "🦷 Tooth completely knocked out (Avulsion) - Milk tooth - 6–12 years": {
        "message": "Is the bleeding under control?",
        "options": ["Yes", "No"]
    },
    "🦷 Tooth completely knocked out (Avulsion) - Milk tooth - > 12 years": {
        "message": "Is the bleeding under control?",
        "options": ["Yes", "No"]
    },
    "Yes": {
        "message": "✅ Guidance:\n- Do **not replant milk teeth**.\n- Keep the child calm and comfortable.\n- Visit a **dentist soon** to ensure no damage to the permanent tooth underneath.",
        "options": []
    },
    "No": {
        "message": "🩸 Apply gentle pressure with clean gauze or cotton for **5–10 minutes**.\nThen, visit a **dentist immediately**.",
        "options": []
    },

    # --- EXTRUSIVE LUXATION ---
    "↔️ Tooth moved slightly out (Extrusive luxation)": {
        "message": "Is the injured tooth **permanent** or a **milk tooth**?",
        "options": ["Permanent tooth", "Milk tooth"]
    },
    "↔️ Tooth moved slightly out (Extrusive luxation) - Milk tooth": {
        "message": "❗ Do not try to push it back.\n- Control bleeding gently.\n- Visit dentist soon.",
        "options": []
    },
    "↔️ Tooth moved slightly out (Extrusive luxation) - Permanent tooth": {
        "message": "Is the tooth **very loose** or **slightly displaced**?",
        "options": ["Very loose", "Slightly displaced"]
    },
    "↔️ Tooth moved slightly out (Extrusive luxation) - Permanent tooth - Very loose": {
        "message": "⚠️ Do not force it back. Gently keep it in place and go to dentist immediately.",
        "options": []
    },
    "↔️ Tooth moved slightly out (Extrusive luxation) - Permanent tooth - Slightly displaced": {
        "message": "Is there **heavy bleeding** from the site?",
        "options": ["Yes", "No"]
    },
    "↔️ Tooth moved slightly out (Extrusive luxation) - Permanent tooth - Slightly displaced - Yes": {
        "message": "Apply gentle pressure with gauze. How long ago did the injury occur?",
        "options": ["< 60 mins", "> 60 mins"]
    },
    "↔️ Tooth moved slightly out (Extrusive luxation) - Permanent tooth - Slightly displaced - No": {
        "message": "How long ago did the injury occur?",
        "options": ["< 60 mins", "> 60 mins"]
    },
    "↔️ Tooth moved slightly out (Extrusive luxation) - Permanent tooth - Slightly displaced - < 60 mins": {
        "message": "🚨 Emergency! Try to gently reposition it, close mouth with gauze, and go to dentist immediately.",
        "options": []
    },
    "↔️ Tooth moved slightly out (Extrusive luxation) - Permanent tooth - Slightly displaced - > 60 mins": {
        "message": "Do not reposition. Avoid biting with it and see a dentist immediately.",
        "options": []
    },

    # --- INTRUSIVE LUXATION ---
    "⬇️ Tooth pushed in (Intrusive luxation)": {
        "message": "Is the tooth **permanent** or a **milk tooth**?",
        "options": ["Permanent tooth", "Milk tooth"]
    },
    "⬇️ Tooth pushed in (Intrusive luxation) - Milk tooth": {
        "message": "Do not reposition. Use a **cold compress** and see a **dentist soon**.",
        "options": []
    },
    "⬇️ Tooth pushed in (Intrusive luxation) - Permanent tooth": {
        "message": "Can you still see part of the tooth or is it completely pushed in?",
        "options": ["Partially visible", "Completely inside the gums"]
    },
    "⬇️ Tooth pushed in (Intrusive luxation) - Permanent tooth - Completely inside the gums": {
        "message": "❗ Severe intrusion — do **not pull it out**. Visit a **dentist immediately**.",
        "options": []
    },
    "⬇️ Tooth pushed in (Intrusive luxation) - Permanent tooth - Partially visible": {
        "message": "Is the tooth **loose** or **firmly stuck**?",
        "options": ["Loose", "Firmly locked"]
    },
    "⬇️ Tooth pushed in (Intrusive luxation) - Permanent tooth - Partially visible - Loose": {
        "message": "Avoid touching or wiggling. Use cold compress and go to dentist immediately.",
        "options": []
    },
    "⬇️ Tooth pushed in (Intrusive luxation) - Permanent tooth - Partially visible - Firmly locked": {
        "message": "How long ago did the injury occur?",
        "options": ["< 60 mins", "> 60 mins"]
    },
    "⬇️ Tooth pushed in (Intrusive luxation) - Permanent tooth - Partially visible - < 60 mins": {
        "message": "Keep area clean, avoid biting. Dentist immediately.",
        "options": []
    },
    "⬇️ Tooth pushed in (Intrusive luxation) - Permanent tooth - Partially visible - > 60 mins": {
        "message": "Avoid delay. Keep area clean, go to dentist immediately.",
        "options": []
    },

    # --- TOOTH LOOSENED ---
    "🌀 Tooth loosened": {
        "message": "Is it a **permanent** or **milk tooth**?",
        "options": ["Permanent tooth", "Milk tooth"]
    },
    "🌀 Tooth loosened - Milk tooth": {
        "message": "❗ Do not push back. Control bleeding with gentle pressure. Visit dentist immediately.",
        "options": []
    },
    "🌀 Tooth loosened - Permanent tooth": {
        "message": "Is the tooth **slightly loose** or **very loose**?",
        "options": ["Slightly loose", "Very loose"]
    },
    "🌀 Tooth loosened - Permanent tooth - Slightly loose": {
        "message": "Is there bleeding from the gums?",
        "options": ["Yes", "No"]
    },
    "🌀 Tooth loosened - Permanent tooth - Very loose": {
        "message": "Try to gently reposition and close mouth with gauze. See dentist immediately.",
        "options": []
    },
    "🌀 Tooth loosened - Permanent tooth - Slightly loose - Yes": {
        "message": "Apply gentle pressure with gauze. Visit dentist soon.",
        "options": []
    },
    "🌀 Tooth loosened - Permanent tooth - Slightly loose - No": {
        "message": "Is the tooth painful when you bite?",
        "options": ["Yes", "No"]
    },
    "🌀 Tooth loosened - Permanent tooth - Slightly loose - No - Yes": {
        "message": "May be subluxation injury. See dentist as soon as possible.",
        "options": []
    },
    "🌀 Tooth loosened - Permanent tooth - Slightly loose - No - No": {
        "message": "Avoid biting with that tooth. Eat soft foods. Dentist check soon.",
        "options": []
    },

    # --- TOOTH BROKEN / CHIPPED ---
    "💥 Tooth broken or chipped": {
        "message": "Is it a **permanent tooth** or a **milk tooth**?",
        "options": ["Permanent tooth", "Milk tooth"]
    },
    "💥 Tooth broken or chipped - Permanent tooth": {
        "message": "Is it a **small chip** or a **larger break**?",
        "options": ["Small chip (enamel only)", "Larger fracture (enamel + dentin)"]
    },
    "💥 Tooth broken or chipped - Permanent tooth - Small chip (enamel only)": {
        "message": "🦷 Not an emergency but needs care.\n- Save broken piece in milk or water\n- Dentist can bond it back",
        "options": []
    },
    "💥 Tooth broken or chipped - Permanent tooth - Larger fracture (enamel + dentin)": {
        "message": "Can you see **red/pink spot or bleeding** inside the tooth?",
        "options": ["Yes", "No"]
    },
    "💥 Tooth broken or chipped - Permanent tooth - Larger fracture (enamel + dentin) - Yes": {
        "message": "🩸 Possible pulp exposure. Cover with gauze. Dentist immediately.",
        "options": []
    },
    "💥 Tooth broken or chipped - Permanent tooth - Larger fracture (enamel + dentin) - No": {
        "message": "Is it **sensitive to cold or biting**?",
        "options": ["Yes", "No"]
    },
    "💥 Tooth broken or chipped - Permanent tooth - Larger fracture (enamel + dentin) - No - Yes": {
        "message": "Likely dentin exposure. Visit dentist soon.",
        "options": []
    },
    "💥 Tooth broken or chipped - Permanent tooth - Larger fracture (enamel + dentin) - No - No": {
        "message": "Not an emergency but needs treatment soon.",
        "options": []
    },
    "💥 Tooth broken or chipped - Milk tooth": {
        "message": "Avoid hard foods, control pain if any, and visit a **dentist soon**.",
        "options": []
    },

    # --- SOFT TISSUE INJURY ---
    "👄 Injury to gums, lips or face (soft tissue injury)": {
        "message": "🩸 Clean wounds gently, apply pressure for bleeding.\nSeek dental/medical care based on severity.",
        "options": []
    },

    # --- JAW / JOINT INJURY ---
    "😬 Injured jaws and joints": {
        "message": "🚨 Emergency!\n- Call emergency services if severe or unconscious.\n- Support jaw gently with a loose bandage.\n- Go to nearest hospital immediately.",
        "options": []
    }
}

# --- Session state ---
if "current" not in st.session_state:
    st.session_state.current = "start"
if "history" not in st.session_state:
    st.session_state.history = []

# Display history
for msg in st.session_state.history:
    st.text(f"{msg['role'].capitalize()}: {msg['content']}")

# Current bot message
if not st.session_state.history or st.session_state.history[-1]["role"] != "bot" or \
        st.session_state.history[-1]["content"] != chat_flow[st.session_state.current]["message"]:
    bot_msg = chat_flow[st.session_state.current]["message"]
    st.session_state.history.append({"role": "bot", "content": bot_msg})
    st.text(f"Bot: {bot_msg}")

# Options
options = chat_flow[st.session_state.current]["options"]
clicked_option = None
if options:
    for i, opt in enumerate(options):
        if st.button(opt, key=f"{st.session_state.current}_{i}"):
            clicked_option = opt
            break

# Process response
if clicked_option:
    st.session_state.history.append({"role": "user", "content": clicked_option})
    next_key = f"{st.session_state.current} - {clicked_option}" \
        if f"{st.session_state.current} - {clicked_option}" in chat_flow else clicked_option
    st.session_state.current = next_key if next_key in chat_flow else "start"
    bot_msg = chat_flow[st.session_state.current]["message"]
    st.session_state.history.append({"role": "bot", "content": bot_msg})

# Restart
if not options:
    if st.button("🔄 Restart"):
        st.session_state.current = "start"
        st.session_state.history = []
