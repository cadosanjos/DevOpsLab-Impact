from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Testando nova branch"

if __name__ == '__main__':
    app.run()