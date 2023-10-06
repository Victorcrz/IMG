
from flask import Flask, request, render_template
import openai

app = Flask(__name__)

imagenr = []

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        descripcion = request.form.get("descripcion")
        imagen = int(request.form.get("imagen"))
        for _ in range(imagen):
            img = enviar_imagen(descripcion)
            imagenr.append(img)
    return render_template('index.html', imagenr=imagenr)

def enviar_imagen(descripcion):
    openai.api_key = "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"
    respuesta = openai.Image.create(
            prompt=descripcion,
            n=1,
            size="256x256"
        )
    return respuesta["data"][0]["url"]


if __name__ == "__main__":
    app.run(debug=True, port=5000)