# 🔮 Futuri Possibili

Un'interfaccia conversazionale con un agente AI che ti aiuta a esplorare i tuoi futuri possibili.

![screenshot](https://via.placeholder.com/800x500/0d0d1a/7c6af5?text=Futuri+Possibili)

## Funzionalità

- Chat in streaming con Claude Opus 4.6
- Agente specializzato nell'esplorazione dei futuri personali
- Tecniche di futures thinking: scenari What-If, backcasting, wild cards
- UI moderna con tema cosmico
- Suggerimenti di conversazione per iniziare

## Installazione

```bash
# Clona il repository
git clone https://github.com/TUO_USERNAME/future-futures.git
cd future-futures

# Crea un ambiente virtuale
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Installa le dipendenze
pip install -r requirements.txt

# Configura la chiave API
cp .env.example .env
# Modifica .env e inserisci la tua ANTHROPIC_API_KEY
```

## Avvio

```bash
# Con variabile d'ambiente
ANTHROPIC_API_KEY=sk-ant-... python app.py

# Oppure con file .env (installa python-dotenv)
pip install python-dotenv
python app.py
```

Apri il browser su [http://localhost:5000](http://localhost:5000)

## Struttura

```
future-futures/
├── app.py              # Backend Flask + integrazione Claude
├── templates/
│   └── index.html      # Frontend (UI + logica chat)
├── requirements.txt
├── .env.example
└── README.md
```

## Come funziona

L'agente usa Claude Opus 4.6 con adaptive thinking e un system prompt progettato per:
- Fare domande aperte e stimolanti
- Esplorare scenari futuri multipli
- Usare tecniche di futures thinking
- Connettere i desideri ai valori profondi dell'utente

## Requisiti

- Python 3.9+
- Chiave API Anthropic ([ottienila qui](https://console.anthropic.com))
