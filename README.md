# 🔮 Futuri Possibili

Un'interfaccia conversazionale con un agente AI che ti aiuta a esplorare i tuoi futuri possibili.

![screenshot](https://via.placeholder.com/800x500/0d0d1a/7c6af5?text=Futuri+Possibili)

## Funzionalità

- Chat in streaming con Claude Opus 4.6
- Agente specializzato nell'esplorazione dei futuri personali
- Tecniche di futures thinking: scenari What-If, backcasting, wild cards
- UI moderna con tema cosmico
- Suggerimenti di conversazione per iniziare

## Deploy su Streamlit Cloud

1. Forka o clona questo repo su GitHub
2. Vai su [share.streamlit.io](https://share.streamlit.io) e connetti il repo
3. In **Advanced settings → Secrets** aggiungi:
   ```toml
   ANTHROPIC_API_KEY = "sk-ant-..."
   ```
4. Clicca **Deploy**

## Avvio locale

```bash
git clone https://github.com/Giaada/future-futures.git
cd future-futures
pip install -r requirements.txt
ANTHROPIC_API_KEY=sk-ant-... streamlit run app.py
```

## Struttura

```
future-futures/
├── app.py          # App Streamlit + integrazione Claude
├── requirements.txt
├── .env.example
└── README.md
```

## Come funziona

L'agente usa Claude Opus 4.6 con un system prompt progettato per:
- Fare domande aperte e stimolanti
- Esplorare scenari futuri multipli
- Usare tecniche di futures thinking (What-If, backcasting, wild cards)
- Connettere i desideri ai valori profondi dell'utente

## Requisiti

- Python 3.9+
- Chiave API Anthropic ([ottienila qui](https://console.anthropic.com))
