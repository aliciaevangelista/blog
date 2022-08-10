from flask import Flask, render_template

app = Flask("hello")
nomeAula = "Aula Python para web"

@app.route("/usuario")
def usuario():
    usuario = [1, "Alícia Duarte Evangelista", "Estudante"]
    alunos = ["Andre Guedes", "Lucas Santos",  "Miguel Lima", "Ana Carolina"]
    return render_template("index.html", usuario=usuario, nome=nomeAula, alunos=alunos)

@app.route("/contatos")
def contato():
    return render_template("index.html", usuario=usuario, nome=nomeAula)