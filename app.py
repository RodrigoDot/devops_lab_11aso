from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Oi, vc que está aí do outro lado, v1"

if __name__ == '__main__':
    app.run()