from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def initial_page():
    return render_template('index.html')

@app.route("/test")
def test_page():
    return 'Rota de testes funcionando'

if __name__ == '__main__':
    app.run()
