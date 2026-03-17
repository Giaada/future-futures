import os
import json
from flask import Flask, render_template, request, Response, stream_with_context
import anthropic

app = Flask(__name__)
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

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


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    messages = data.get("messages", [])

    def generate():
        with client.messages.stream(
            model="claude-opus-4-6",
            max_tokens=1024,
            system=SYSTEM_PROMPT,
            messages=messages,
            thinking={"type": "adaptive"},
        ) as stream:
            for text in stream.text_stream:
                yield f"data: {json.dumps({'text': text})}\n\n"
        yield "data: [DONE]\n\n"

    return Response(
        stream_with_context(generate()),
        mimetype="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
        },
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
