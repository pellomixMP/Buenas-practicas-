from flask import Flask
app= Flask(__name__)#iniciando una aplicacion 
@app.route("/")
def index():
    return "Susana la dejada"

if __name__ == "__main__":
    app.run()