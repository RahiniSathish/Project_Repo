# app.py
import streamlit as st
from db import SessionLocal, init_db
from models import User, Conversation
from chat_engine import get_answer
import uuid

# Initialize DB and session
init_db()
db = SessionLocal()

# Streamlit setup
st.set_page_config(page_title="Chat Logger", layout="wide")
st.title("📜 User-based Chat Bot")

# Sidebar: User Selection
st.sidebar.title("👤 Select User")
users = db.query(User).all()
user_map = {f"{user.name} ({user.user_id})": user.user_id for user in users}
selected_user = st.sidebar.selectbox("Select User", list(user_map.keys()))

if selected_user:
    user_id = user_map[selected_user]
    st.sidebar.success(f"User: {selected_user}")
else:
    st.warning("Please select a user to continue.")
    st.stop()

# Setup session and conversation ID
if "user_sessions" not in st.session_state:
    st.session_state["user_sessions"] = {}

if user_id not in st.session_state["user_sessions"]:
    st.session_state["user_sessions"][user_id] = {
        "session_id": str(uuid.uuid4()),
        "conversation_id": str(uuid.uuid4())
    }

user_session = st.session_state["user_sessions"][user_id]

# Top-right button for new session
top_left, top_right = st.columns([6, 1])
with top_right:
    if st.button("➕ Start New Session"):
        st.session_state["user_sessions"][user_id] = {
            "session_id": str(uuid.uuid4()),
            "conversation_id": str(uuid.uuid4())
        }
        st.success("🔁 New session started!")

# Ask a question
question = st.text_input("Ask a question:")

if st.button("Submit") and question.strip():
    answer = get_answer(question)

    convo = Conversation(
        user_id=user_id,
        session_id=user_session["session_id"],
        conversation_id=user_session["conversation_id"],
        question=question,
        answer=answer
    )
    db.add(convo)
    db.commit()

    st.success("✅ Answer:")
    st.markdown(answer)

# Display conversation history
st.divider()
st.subheader(f"🧾 Conversation History for {selected_user}")

history = db.query(Conversation).filter_by(user_id=user_id).order_by(Conversation.id.desc()).all()

for entry in history:
    with st.expander(f"Q: {entry.question}"):
        st.markdown(f"**A:** {entry.answer}")
        st.caption(f"🧑‍💻 User ID: {entry.user_id} | 💬 Session: {entry.session_id} | 📌 Conversation: {entry.conversation_id}")
