from flask import Flask, render_template
import plotly.express as px
import pandas as pd

app = Flask(__name__, static_folder='static')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/localizacao")
def localizacao():
    return render_template("localizacao.html")

@app.route("/redes")
def redes():
    return render_template("redes.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/mamiferos")
def mamiferos():
    return render_template("mamiferos.html")

@app.route("/repteis")
def repteis():
    return render_template("repteis.html")

@app.route("/aves")
def aves():
    return render_template("aves.html")


@app.route("/dashboard")
def dashboard():
    # Dados de exemplo
    df = pd.DataFrame({
        "Animal": ["Leão", "Tigre", "Arara", "Flamingo", "Cobra"],
        "Quantidade": [5, 3, 8, 12, 7]
    })

    # Gráfico de Barras com Plotly
    fig_bar = px.bar(df, x="Animal", y="Quantidade", title="Quantidade de Animais por Espécie")

    # Gráfico de Pizza com Plotly
    fig_pie = px.pie(df, names="Animal", values="Quantidade", title="Distribuição de Animais")

    # Converte os gráficos para HTML
    graph_bar_html = fig_bar.to_html(full_html=False)
    graph_pie_html = fig_pie.to_html(full_html=False)

    # Renderiza o template e passa os gráficos
    return render_template("dashboard.html", graph_bar_html=graph_bar_html, graph_pie_html=graph_pie_html)

if __name__ == "__main__":
    app.run(debug=True)