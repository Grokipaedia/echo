import streamlit as st
import json
import random
from datetime import datetime

st.set_page_config(page_title="Echo • Talk to Your Future Self", page_icon="🌌", layout="centered")

st.title("🌌 Echo")
st.markdown("**Talk to your future self.** Today.")

mode = st.radio("Choose your future self mode:", 
                ["General Conversation", "Legacy & Family", "Therapy & Reflection", "Leadership & Strategy"],
                horizontal=True)

years_ahead = st.slider("Talk to yourself in how many years?", 5, 30, 10, 5)

if "memory" not in st.session_state:
    try:
        with open("echo_memory.json", "r", encoding="utf-8") as f:
            st.session_state.memory = json.load(f)
    except:
        st.session_state.memory = []

for msg in st.session_state.memory[-12:]:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["text"])
    else:
        st.chat_message("assistant").write(f"**Future You ({2026 + msg.get('years_ahead', 10)}):** {msg['text']}")

user_input = st.chat_input("Ask your future self anything...")

if user_input:
    st.session_state.memory.append({"role": "user", "text": user_input})
    
    if mode == "Legacy & Family":
        reply = random.choice(["Your children will ask about this moment one day...", "I left this message for them..."])
    elif mode == "Therapy & Reflection":
        reply = random.choice(["I still carry that pain sometimes...", "This is the kind of thing we used to avoid..."])
    elif mode == "Leadership & Strategy":
        reply = random.choice(["This decision will define the next decade...", "Future teams will judge you by how you handled this..."])
    else:
        reply = random.choice(["I remember when you asked me this...", "You're overthinking it again..."])
    
    st.session_state.memory.append({"role": "future", "text": reply, "years_ahead": years_ahead})
    
    with open("echo_memory.json", "w", encoding="utf-8") as f:
        json.dump(st.session_state.memory, f, indent=2)
    
    st.chat_message("assistant").write(f"**Future You ({2026 + years_ahead}):** {reply}")
