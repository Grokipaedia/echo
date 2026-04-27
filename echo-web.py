# echo-web.py - Nice web interface for Echo
import streamlit as st
import json
from datetime import datetime

st.set_page_config(page_title="Echo • Talk to Your Future Self", page_icon="🌌", layout="centered")

st.title("🌌 Echo")
st.markdown("**Talk to your future self.** Today.")

# Load or initialize memory
if "memory" not in st.session_state:
    try:
        with open("echo_memory.json", "r", encoding="utf-8") as f:
            st.session_state.memory = json.load(f)
    except:
        st.session_state.memory = []

def save_memory():
    with open("echo_memory.json", "w", encoding="utf-8") as f:
        json.dump(st.session_state.memory, f, indent=2)

# Timeline selector
years_ahead = st.slider("Talk to yourself in how many years?", min_value=5, max_value=30, value=10, step=5)

# Display chat history
for msg in st.session_state.memory[-20:]:  # show last 20 messages
    if msg["role"] == "user":
        st.chat_message("user").write(msg["text"])
    else:
        st.chat_message("assistant").write(f"**Future You ({st.session_state.get('age_now', 2026) + msg.get('years_ahead', 10)}):** {msg['text']}")

# User input
user_input = st.chat_input("Ask your future self anything...")

if user_input:
    st.session_state.memory.append({"role": "user", "text": user_input, "timestamp": datetime.now().isoformat()})
    
    # Generate response
    responses = [
        f"From {st.session_state.get('age_now', 2026) + years_ahead}... I still remember the exact day you asked me this.",
        f"The version of you in {st.session_state.get('age_now', 2026) + years_ahead} wishes you would stop overthinking and just do it.",
        f"You already know the answer. You're just scared. I was too... and I still regret waiting.",
        f"This decision is going to shape the next decade. Choose the one that makes older me proud.",
    ]
    response = random.choice(responses)
    
    st.session_state.memory.append({
        "role": "future",
        "text": response,
        "years_ahead": years_ahead,
        "timestamp": datetime.now().isoformat()
    })
    save_memory()
    
    st.chat_message("assistant").write(f"**Future You ({st.session_state.get('age_now', 2026) + years_ahead}):** {response}")
