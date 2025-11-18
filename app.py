from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = "supersecretkey"

USER = "admin"
PASS = "1234"

def login_required(f):
    def wrapper(*args, **kwargs):
        if "user" not in session:
            return redirect("/login")
        return f(*args, **kwargs)
    wrapper.__name__ = f.__name__
    return wrapper


@app.route("/")
def home():
    return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if request.form["user"] == USER and request.form["pass"] == PASS:
            session["user"] = USER
            return redirect("/dashboard")
        else:
            error = "Usuário ou senha incorretos"
    return render_template("login.html", error=error)


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")


# ---------------------- CONSULTAS FAKE ---------------------- #

@app.route("/cpf", methods=["GET", "POST"])
@login_required
def cpf():
    data = None
    if request.method == "POST":
        data = {
            "nome": "João da Silva",
            "nascimento": "12/03/1990",
            "mae": "Maria da Silva"
        }
    return render_template("cpf.html", data=data)


@app.route("/cnpj", methods=["GET", "POST"])
@login_required
def cnpj():
    data = None
    if request.method == "POST":
        data = {
            "empresa": "Tech Solutions LTDA",
            "abertura": "2012",
            "status": "Ativa"
        }
    return render_template("cnpj.html", data=data)


@app.route("/email", methods=["GET", "POST"])
@login_required
def email():
    data = None
    if request.method == "POST":
        data = {
            "dono": "Roberto Lima",
            "desde": "2017",
            "vazamentos": 4
        }
    return render_template("email.html", data=data)


@app.route("/telefone", methods=["GET", "POST"])
@login_required
def telefone():
    data = None
    if request.method == "POST":
        data = {
            "dono": "Carlos Pereira",
            "operadora": "Vivo",
            "estado": "SP"
        }
    return render_template("telefone.html", data=data)


@app.route("/nome", methods=["GET", "POST"])
@login_required
def nome():
    data = None
    if request.method == "POST"]:
        data = {
            "nome": request.form["nome"],
            "registros": 3,
            "possiveis_docs": ["CPF listado", "RG registrado"]
        }
    return render_template("nome.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
