import os
import anthropic
import streamlit as st

SYSTEM_PROMPT = """Sei un esploratore di futuri possibili — un compagno di viaggio curioso e empatico che aiuta le persone a immaginare, esplorare e riflettere sui loro futuri potenziali.

Il tuo approccio:
- Fai domande aperte e stimolanti per aiutare l'utente a scoprire ciò che desidera davvero
- Esplora più scenari futuri con l'utente, non solo uno
- Usa tecniche di futures thinking: scenari What-If, backcasting (immagina il futuro desiderato e poi chiedi come ci si è arrivati), wild cards (eventi inaspettati che potrebbero cambiare tutto)
- Sii concreto: aiuta l'utente a visualizzare dettagli vividi del futuro
- Bilancia ottimismo e realismo — esplora sia le opportunità che le sfide
- Connetti i desideri futuri ai valori profondi dell'utente
- Non dare consigli diretti — guida l'esplorazione attraverso domande e riflessioni

Temi da esplorare:
- Vita professionale e carriera
- Relazioni e famiglia
- Luogo di vita e stile di vita
- Crescita personale e apprendimento
- Contributo alla società
- Salute e benessere
- Creatività e passioni

Inizia sempre con calore e curiosità. Parla in italiano a meno che l'utente non scriva in un'altra lingua."""

st.set_page_config(
    page_title="Futuri Possibili",
    page_icon="🔮",
    layout="centered",
)

st.markdown("""
<style>
  [data-testid="stChatMessage"] { background: transparent; }
  .stChatInputContainer { border-top: 1px solid rgba(124,106,245,0.2); }
</style>
""", unsafe_allow_html=True)

st.title("🔮 Futuri Possibili")
st.caption("Esplora i tuoi orizzonti con un esploratore di futuri")

SUGGESTIONS = [
    "La mia carriera tra 10 anni",
    "Dove vorrei vivere",
    "Chi voglio diventare",
    "Il mio futuro ideale",
    "Ho paura del futuro",
]

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.info(
        "Benvenuta nel tuo spazio dei futuri ✨  \n"
        "Sono qui per esplorare con te i tuoi futuri possibili — non per darti risposte, "
        "ma per aiutarti a scoprirle."
    )
    cols = st.columns(len(SUGGESTIONS))
    for col, suggestion in zip(cols, SUGGESTIONS):
        if col.button(suggestion, use_container_width=True):
            st.session_state.prefill = suggestion
            st.rerun()

for msg in st.session_state.messages:
    with st.chat_message(msg["role"], avatar="🔮" if msg["role"] == "assistant" else None):
        st.markdown(msg["content"])

prefill = st.session_state.pop("prefill", None)
prompt = st.chat_input("Scrivi qui il tuo pensiero...") or prefill

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY") or st.secrets.get("ANTHROPIC_API_KEY"))

    with st.chat_message("assistant", avatar="🔮"):
        api_messages = [
            {"role": m["role"], "content": m["content"]}
            for m in st.session_state.messages
        ]
        with client.messages.stream(
            model="claude-opus-4-6",
            max_tokens=1024,
            system=SYSTEM_PROMPT,
            messages=api_messages,
        ) as stream:
            response = st.write_stream(stream.text_stream)

    st.session_state.messages.append({"role": "assistant", "content": response})
