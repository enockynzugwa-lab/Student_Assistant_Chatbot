import html
import streamlit as st
from chatbot import chatbot_response


# ==============================
# PAGE CONFIGURATION
# ==============================

st.set_page_config(
    page_title="KennyLee SmartBot",
    page_icon="🎓",
    layout="centered"
)


# ==============================
# CUSTOM CSS
# ==============================

st.markdown("""
<style>
.stApp {
    background-color: #f0f2f5;
}
.chat-header {
    background-color: #075e54;
    padding: 15px;
    border-radius: 10px 10px 0px 0px;
    color: white;
    margin-bottom: 10px;
}
.chat-header h2 {
    margin: 0;
    font-size: 22px;
}
.chat-header p {
    margin: 3px 0px 0px 0px;
    font-size: 13px;
}
.chat-container {
    padding: 10px;
}
.user-message {
    background-color: #dcf8c6;
    padding: 10px 14px;
    border-radius: 12px 12px 2px 12px;
    margin: 8px 0px 8px 20%;
    text-align: left;
}
.bot-message {
    background-color: white;
    padding: 10px 14px;
    border-radius: 12px 12px 12px 2px;
    margin: 8px 20% 8px 0px;
    text-align: left;
}
.sender {
    font-size: 12px;
    font-weight: bold;
    margin-bottom: 4px;
}
</style>
""", unsafe_allow_html=True)


# ==============================
# HEADER
# ==============================

st.markdown(
    '<div class="chat-header">'
    '<h2>🎓 KennyLee SmartBot</h2>'
    '<p>🟢 Online • Ask me anything you wish to know</p>'
    '</div>',
    unsafe_allow_html=True
)


# ==============================
# STUDENT NAME
# ==============================

student_name = st.text_input(
    "Your name",
    placeholder="Enter your name...",
    key="student_name_input"
)


# ==============================
# CHAT HISTORY
# ==============================

if "messages" not in st.session_state:
    st.session_state.messages = []


# ==============================
# WELCOME MESSAGE
# ==============================

if len(st.session_state.messages) == 0:
    st.markdown(
        '<div class="bot-message">'
        '<div class="sender">🤖 KennyLee SmartBot</div>'
        'Hello! 👋<br>'
        'Welcome to myAssistant Chatbot.<br><br>'
        'How can I help you today?'
        '</div>',
        unsafe_allow_html=True
    )


# ==============================
# DISPLAY CHAT HISTORY
# ==============================

for message in st.session_state.messages:

    # Escape user/bot text so it can't break the layout or inject HTML
    safe_content = html.escape(message["content"]).replace("\n", "<br>")

    if message["role"] == "user":
        sender_name = html.escape(student_name) if student_name else "You"
        st.markdown(
            f'<div class="user-message">'
            f'<div class="sender">👤 {sender_name}</div>'
            f'{safe_content}'
            f'</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f'<div class="bot-message">'
            f'<div class="sender">🤖 KennyLee SmartBot</div>'
            f'{safe_content}'
            f'</div>',
            unsafe_allow_html=True
        )


# ==============================
# CHAT INPUT
# ==============================

user_input = st.chat_input("Type a message here...")


# ==============================
# PROCESS USER MESSAGE
# ==============================

if user_input:

    if not student_name:
        st.warning("⚠️ Please enter your name first.")

    else:
        # Save user message
        st.session_state.messages.append(
            {"role": "user", "content": user_input}
        )

        # Get chatbot response
        response = chatbot_response(user_input)

        # Save bot response
        st.session_state.messages.append(
            {"role": "assistant", "content": response}
        )

        st.rerun()


# ==============================
# CLEAR CHAT
# ==============================

if st.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()
