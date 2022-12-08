from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')

@app.route('/sobre')
def sobre():
  return render_template('sobre.html')

@app.route('/edital')
def edital():
  return render_template('edital.html')

@app.route('/equipe')
def equipe():
  return render_template('equipe.html')

@app.route('/avaliacao')
def avaliacoes():
  clientes = [
    {'nome': 'Caio', 'nota': 3},
	  {'nome': 'Melissa', 'nota': 1},
	  {'nome': 'Bianca', 'nota': 4},
	  {'nome': 'Ana', 'nota': 5},
	  {'nome': 'Diogo', 'nota': 3},  
  ]
  return render_template('avaliacao.html', clientes=clientes)

@app.route('/sobre/<id>')
def about(id):
  if id == "projeto":
    return render_template('sobre.html')
  elif id == "equipe":
    return render_template('equipe.html')


app.run(host='0.0.0.0', port=81)
