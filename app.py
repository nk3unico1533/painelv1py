from flask import Flask, render_template, request, redirect, session
import os

app = Flask(__name__)
app.secret_key = "segredo123"

ADMIN_USER = "admin"
ADMIN_PASS = "1234"

@app.route("/")
def home():
    return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form.get("username")
        password = request.form.get("password")

        if user == ADMIN_USER and password == ADMIN_PASS:
            session["user"] = user
            return redirect("/dashboard")
        else:
            return render_template("login.html", error="Usuário ou senha incorretos")

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/login")
    return render_template("dashboard.html")

@app.route("/cpf", methods=["GET", "POST"])
def cpf():
    if "user" not in session:
        return redirect("/login")

    result = None
    if request.method == "POST":
        cpf_value = request.form.get("cpf")
        result = f"Resultado fictício para CPF: {cpf_value}"

    return render_template("cpf.html", result=result)

@app.route("/cnpj", methods=["GET", "POST"])
def cnpj():
    if "user" not in session:
        return redirect("/login")

    result = None
    if request.method == "POST":
        cnpj_value = request.form.get("cnpj")
        result = f"Resultado fictício para CNPJ: {cnpj_value}"

    return render_template("cnpj.html", result=result)

@app.route("/email", methods=["GET", "POST"])
def email():
    if "user" not in session:
        return redirect("/login")

    result = None
    if request.method == "POST":
        email_value = request.form.get("email")
        result = f"Resultado fictício para Email: {email_value}"

    return render_template("email.html", result=result)

@app.route("/telefone", methods=["GET", "POST"])
def telefone():
    if "user" not in session:
        return redirect("/login")

    result = None
    if request.method == "POST":
        phone_value = request.form.get("telefone")
        result = f"Resultado fictício para Telefone: {phone_value}"

    return render_template("telefone.html", result=result)

@app.route("/nome", methods=["GET", "POST"])
def nome():
    if "user" not in session:
        return redirect("/login")

    result = None
    if request.method == "POST":
        nome_value = request.form.get("nome")
        result = f"Resultado fictício para Nome: {nome_value}"

    return render_template("nome.html", result=result)

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)