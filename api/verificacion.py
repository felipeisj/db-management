from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>¡Hola Mundo!</h1> <p>Bienvenido a nuestra aplicación web básica en Python</p>"

if __name__ == "__main__":
    app.run(debug=False,port=1234)
