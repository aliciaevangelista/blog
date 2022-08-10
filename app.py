from flask import Flask

app = Flask("hello")

@app.route("/")
def hello():
    return "Hello World"

@app.route("/contatos")
def contato():
    return """<html>
                <head>
                    <title> Contatos </title>
                </head>
                <body>
                    <h1>Alícia Duarte Evangelista</h1>
                    <h2>aliciaevgt@gmail.com</h2>
                    <h3> (00) 0 0000-0000</h3>
                </body>
            </html>"""