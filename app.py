import streamlit as st
from pipeline import generate, NO_ANSWER

st.set_page_config(
    page_title="The Unofficial Haverford Guide",
    page_icon="🎓",
    layout="centered",
)

st.markdown("""
<style>
/* Header */
.hc-header {
    display: flex;
    align-items: center;
    gap: 18px;
    background: #111111;
    border: 2px solid #8B1A1A;
    border-radius: 14px;
    padding: 24px 28px;
    margin-bottom: 24px;
}
.hc-logo {
    font-family: Georgia, serif;
    font-size: 2.2em;
    font-weight: bold;
    color: white;
    background: #8B1A1A;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    border: 2px solid white;
}
.hc-title { font-family: Georgia, serif; font-size: 1.7em; color: white; margin: 0 0 4px 0; }
.hc-sub { font-family: Georgia, serif; font-size: 0.9em; color: #aaaaaa; margin: 0 0 8px 0; }
.hc-badge {
    background: #8B1A1A;
    color: white;
    font-size: 0.7em;
    padding: 2px 10px;
    border-radius: 20px;
    display: inline-block;
}
/* Hide streamlit default header/footer */
#MainMenu, footer, header { visibility: hidden; }
</style>

<div class="hc-header">
    <div class="hc-logo">HC</div>
    <div>
        <p class="hc-title">The Unofficial Haverford Guide</p>
        <p class="hc-sub">Real student perspectives on life at Haverford College</p>
        <span class="hc-badge">RAG · Student-written sources · Groq llama-3.3-70b</span>
    </div>
</div>
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    avatar = "🐿️" if msg["role"] == "assistant" else None
    with st.chat_message(msg["role"], avatar=avatar):
        st.markdown(msg["content"])
        if msg["role"] == "assistant" and msg.get("sources"):
            with st.expander("Sources"):
                st.markdown(msg["sources"])

if question := st.chat_input("Ask anything about Haverford..."):
    with st.chat_message("user"):
        st.markdown(question)
    st.session_state.messages.append({"role": "user", "content": question})

    with st.chat_message("assistant", avatar="🐿️"):
        with st.spinner("Searching documents..."):
            result = generate(question)

        st.markdown(result["answer"])

        sources_md = ""
        if result["answer"].strip() != NO_ANSWER and result["sources"]:
            sources_md = "\n\n".join(
                f"- [{s.split(' — ')[0]}]({s.split(' — ')[1]})"
                for s in result["sources"]
            )
            with st.expander("Sources"):
                st.markdown(sources_md)

    st.session_state.messages.append({
        "role": "assistant",
        "content": result["answer"],
        "sources": sources_md,
    })
