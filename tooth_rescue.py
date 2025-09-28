import streamlit as st

st.set_page_config(page_title="🦷 Tooth Rescue Chatbot", page_icon="🦷")

st.title("🦷 Tooth Rescue – Dental Injury First Aid Chatbot")

# ===============================
# DECISION TREE STRUCTURE
# ===============================

chat_flow = {
    "start": {
        "message": "Hi, I’m TOOTH RESCUE – here to guide you through what to do right now for a dental injury.\n\nPlease select what happened:",
        "options": [
            "Tooth completely knocked out (Avulsion)",
            "Tooth moved slightly out (Extrusive luxation)",
            "Tooth pushed in (Intrusive luxation)",
            "Tooth loosened",
            "Tooth broken or chipped",
            "Injury to gums, lips or face (Soft tissue injury)",
            "Injured jaws and joints",
        ],
    },

    # -----------------------------
    # AVULSION
    # -----------------------------
    "Tooth completely knocked out (Avulsion)": {
        "message": "Is it a permanent tooth or a milk tooth?",
        "options": ["Permanent tooth", "Milk tooth"],
    },
    "Avulsion - Permanent tooth": {
        "message": "How long has it been since the tooth got knocked out?",
        "options": ["< 60 minutes", "> 60 minutes"],
    },
    "Avulsion - Permanent tooth - < 60 minutes": {
        "message": """✅ Instructions:
- Find the tooth and pick it up by the crown (white part). Avoid touching the root.  
- If dirty, rinse gently with milk or saline.  
- Immediately place the tooth back in its original place if possible.  
- Bite on gauze/napkin to hold it in place.  
- See a dentist immediately.  
⚠️ If unable to replant → store tooth in milk, saline, saliva, or water (last option) and visit dentist immediately.""",
        "options": [],
    },
    "Avulsion - Permanent tooth - > 60 minutes": {
        "message": """⚠️ Prognosis is poor but still:
- Rinse tooth gently if dirty.  
- Place back into socket if possible OR store in milk/saline/saliva/water.  
- Go to dentist immediately.""",
        "options": [],
    },
    "Avulsion - Milk tooth": {
        "message": """❗ Primary teeth should NOT be replanted.  
- Control bleeding with gauze.  
- Keep child comfortable.  
- Visit dentist soon to check gums and permanent tooth underneath.""",
        "options": [],
    },

    # -----------------------------
    # EXTRUSIVE LUXATION
    # -----------------------------
    "Tooth moved slightly out (Extrusive luxation)": {
        "message": "Is the injured tooth a permanent tooth or a milk tooth?",
        "options": ["Permanent tooth", "Milk tooth"],
    },
    "Extrusive - Milk tooth": {
        "message": """❗ Do NOT push it back.  
- Control bleeding with gentle pressure.  
- Visit a dentist soon (to avoid damage to permanent tooth underneath).""",
        "options": [],
    },
    "Extrusive - Permanent tooth": {
        "message": "Is the tooth very loose or only slightly displaced?",
        "options": ["Very loose", "Slightly displaced"],
    },
    "Extrusive - Permanent tooth - Very loose": {
        "message": """❗ Do not force it back.  
- Keep it in place gently with cloth or by biting lightly.  
- Go to a dentist immediately.""",
        "options": [],
    },
    "Extrusive - Permanent tooth - Slightly displaced": {
        "message": "Is there heavy bleeding from the site?",
        "options": ["Yes", "No"],
    },
    "Extrusive - Permanent tooth - Slightly displaced - Yes": {
        "message": "How long ago did the injury occur?",
        "options": ["< 60 mins", "> 60 mins"],
    },
    "Extrusive - Permanent tooth - Slightly displaced - No": {
        "message": "How long ago did the injury occur?",
        "options": ["< 60 mins", "> 60 mins"],
    },
    "Extrusive - Permanent tooth - Slightly displaced - < 60 mins": {
        "message": """✅ Instructions:  
- Emergency → see dentist ASAP.  
- Try to gently move teeth back to original position.  
- Bite on gauze between teeth.  
- Visit dentist immediately.""",
        "options": [],
    },
    "Extrusive - Permanent tooth - Slightly displaced - > 60 mins": {
        "message": """❗ Do not reposition tooth.  
- Keep stable, avoid biting with it.  
- See dentist immediately.""",
        "options": [],
    },

    # -----------------------------
    # INTRUSIVE LUXATION
    # -----------------------------
    "Tooth pushed in (Intrusive luxation)": {
        "message": "Is it a permanent tooth or a milk tooth?",
        "options": ["Permanent tooth", "Milk tooth"],
    },
    "Intrusive - Milk tooth": {
        "message": """❗ Do not reposition baby tooth.  
- Use cold compress for swelling.  
- Visit dentist soon (to protect permanent tooth underneath).""",
        "options": [],
    },
    "Intrusive - Permanent tooth": {
        "message": "Can you see the tooth or is it completely pushed inside gums?",
        "options": ["Partially visible", "Completely inside gums"],
    },
    "Intrusive - Permanent tooth - Completely inside gums": {
        "message": """❗ Severe intrusion → do NOT pull it out.  
- Go to dentist immediately.""",
        "options": [],
    },
    "Intrusive - Permanent tooth - Partially visible": {
        "message": "Is the tooth loose or firmly stuck?",
        "options": ["Loose", "Firmly locked"],
    },
    "Intrusive - Permanent tooth - Partially visible - Loose": {
        "message": """Avoid touching/wiggling.  
- Use cold compress.  
- Visit dentist immediately for stabilisation.""",
        "options": [],
    },
    "Intrusive - Permanent tooth - Partially visible - Firmly locked": {
        "message": "How long ago did the injury occur?",
        "options": ["< 60 mins", "> 60 mins"],
    },
    "Intrusive - Permanent tooth - Partially visible - < 60 mins": {
        "message": """Keep area clean.  
- Bite on gauze between teeth.  
- Avoid biting with tooth.  
- Go to dentist immediately.""",
        "options": [],
    },
    "Intrusive - Permanent tooth - Partially visible - > 60 mins": {
        "message": """⚠️ Do not delay further.  
- Keep clean, bite on gauze.  
- Avoid biting with tooth.  
- See dentist immediately.""",
        "options": [],
    },

    # -----------------------------
    # TOOTH LOOSENED
    # -----------------------------
    "Tooth loosened": {
        "message": "Is it a permanent tooth or a milk tooth?",
        "options": ["Permanent tooth", "Milk tooth"],
    },
    "Loosened - Milk tooth": {
        "message": """❗ Do not push it back.  
- Control bleeding with gauze.  
- Dentist will check for fractures and permanent successor.""",
        "options": [],
    },
    "Loosened - Permanent tooth": {
        "message": "Is the tooth slightly loose or very loose?",
        "options": ["Slightly loose", "Very loose"],
    },
    "Loosened - Permanent tooth - Very loose": {
        "message": """⚠️ High risk of displacement.  
- Try to gently move back to position.  
- Bite on gauze.  
- Dentist ASAP.""",
        "options": [],
    },
    "Loosened - Permanent tooth - Slightly loose": {
        "message": "Is there bleeding from gums?",
        "options": ["Yes", "No"],
    },
    "Loosened - Permanent tooth - Slightly loose - Yes": {
        "message": """Apply gentle pressure with gauze.  
Visit dentist immediately.""",
        "options": [],
    },
    "Loosened - Permanent tooth - Slightly loose - No": {
        "message": "Is tooth painful when biting?",
        "options": ["Yes", "No"],
    },
    "Loosened - Permanent tooth - Slightly loose - No - Yes": {
        "message": """Could be concussion or subluxation.  
- Reposition gently, bite on gauze.  
- Dentist ASAP.""",
        "options": [],
    },
    "Loosened - Permanent tooth - Slightly loose - No - No": {
        "message": """Avoid biting.  
- Eat soft foods.  
- Visit dentist for monitoring.""",
        "options": [],
    },

    # -----------------------------
    # BROKEN / CHIPPED
    # -----------------------------
    "Tooth broken or chipped": {
        "message": "Is it a permanent tooth or a milk tooth?",
        "options": ["Permanent tooth", "Milk tooth"],
    },
    "Broken - Permanent tooth": {
        "message": "Is it a small chip or larger fracture?",
        "options": ["Small chip", "Large fracture"],
    },
    "Broken - Permanent tooth - Small chip": {
        "message": """Not emergency, but treatment needed.  
- Find broken piece, store in milk/water.  
- Dentist may glue it back.  
- Visit dentist soon.""",
        "options": [],
    },
    "Broken - Permanent tooth - Large fracture": {
        "message": "Can you see red/pink spot (pulp)?",
        "options": ["Yes", "No"],
    },
    "Broken - Permanent tooth - Large fracture - Yes": {
        "message": """⚠️ Possible pulp exposure.  
- Cover tooth with clean gauze.  
- Dentist immediately.""",
        "options": [],
    },
    "Broken - Permanent tooth - Large fracture - No": {
        "message": "Is tooth sensitive to cold/hot/bite?",
        "options": ["Yes", "No"],
    },
    "Broken - Permanent tooth - Large fracture - No - Yes": {
        "message": """Not emergency, but treatment needed.  
- Store broken piece in milk/water.  
- Dentist can restore.  
- Visit dentist soon.""",
        "options": [],
    },
    "Broken - Permanent tooth - Large fracture - No - No": {
        "message": """Not emergency.  
- Visit dentist soon for treatment.""",
        "options": [],
    },
    "Broken - Milk tooth": {
        "message": """❗ Dentist check required.  
- Do not attempt home repair.  
- Visit dentist soon.""",
        "options": [],
    },

    # -----------------------------
    # SOFT TISSUE INJURY
    # -----------------------------
    "Injury to gums, lips or face (Soft tissue injury)": {
        "message": """Soft tissue injuries can be cuts or bruises.  
- Clean immediately.  
- Control bleeding with pressure.  
- Seek dental/medical care depending on severity.""",
        "options": [],
    },

    # -----------------------------
    # JAWS & JOINTS
    # -----------------------------
    "Injured jaws and joints": {
        "message": """🚨 Emergency!  
- Call emergency services if unconscious/disoriented.  
- Place patient in recovery position if unconscious.  
- Support jaw with hands/bandage (easy to remove if vomiting).  
- Go immediately to hospital/emergency care.""",
        "options": [],
    },
}

# ===============================
# CHATBOT ENGINE
# ===============================

if "current" not in st.session_state:
    st.session_state.current = "start"

# Display message
node = chat_flow[st.session_state.current]
with st.chat_message("assistant"):
    st.markdown(node["message"])

# Display options
if node["options"]:
    choice = st.radio("Choose:", node["options"], key="radio_" + st.session_state.current)

    if choice:  # auto-advance when user selects
        if st.session_state.current == "Tooth completely knocked out (Avulsion)":
            next_key = f"Avulsion - {choice}"
        elif st.session_state.current == "Tooth moved slightly out (Extrusive luxation)":
            next_key = f"Extrusive - {choice}"
        elif st.session_state.current == "Tooth pushed in (Intrusive luxation)":
            next_key = f"Intrusive - {choice}"
        elif st.session_state.current == "Tooth loosened":
            next_key = f"Loosened - {choice}"
        elif st.session_state.current == "Tooth broken or chipped":
            next_key = f"Broken - {choice}"
        else:
            next_key = f"{st.session_state.current} - {choice}"

        if next_key in chat_flow:
            st.session_state.current = next_key
            st.rerun()

else:
    if st.button("🔄 Restart", key="restart_" + st.session_state.current):
        st.session_state.current = "start"
        st.rerun()
