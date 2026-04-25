from flask import Flask, render_template
from urllib.parse import quote

app = Flask(__name__)

@app.route("/")
def inicio():
    numero = "5493329692776"

    menu = {
        "Pastas": [
            {
                "nombre": "Ravioles caseros",
                "precio": 7000,
                "whatsapp": f"https://wa.me/{numero}?text={quote('Hola quiero pedir Ravioles caseros')}"
            },
            {
                "nombre": "Spaghetti",
                "precio": 6500,
                "whatsapp": f"https://wa.me/{numero}?text={quote('Hola quiero pedir Spaghetti')}"
            }
        ],
        "Carnes": [
            {
                "nombre": "Milanesa con papas",
                "precio": 8000,
                "whatsapp": f"https://wa.me/{numero}?text={quote('Hola quiero pedir Milanesa con papas')}"
            },
            {
                "nombre": "Asado",
                "precio": 12000,
                "whatsapp": f"https://wa.me/{numero}?text={quote('Hola quiero pedir Asado')}"
            }
        ],
        "Bebidas": [
            {
                "nombre": "Coca Cola",
                "precio": 2000,
                "whatsapp": f"https://wa.me/{numero}?text={quote('Hola quiero pedir Coca Cola')}"
            },
            {
                "nombre": "Vino de la casa",
                "precio": 5000,
                "whatsapp": f"https://wa.me/{numero}?text={quote('Hola quiero pedir Vino de la casa')}"
            }
        ]
    }

    return render_template("index.html", menu=menu)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
