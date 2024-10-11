from flask import Flask, render_template, request, flash, redirect
app = Flask(__name__)
from database import db
from flask_migrate import Migrate
from models import Planetas
app.config['SECRET_KEY'] = 'fdt435t4654756h3q3464756y'
conexao = 'mysql+pymysql://alunos:cefetmg@127.0.0.1/correcaog1'
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    dados = Planetas.query.all()
    return render_template('index.html', dados = dados)

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/save', methods=['POST'])
def save():
    nome = request.form.get('nome')
    distancia_sol = request.form.get('distancia_sol')
    numero_satelites = request.form.get('numero_satelites')
    if nome and distancia_sol and numero_satelites:
        planeta = Planetas(nome, distancia_sol, numero_satelites)
        db.session.add(planeta)
        db.session.commit()
        flash('Planeta salvo com sucesso!!!')
        return redirect('/')
    else:
        flash('Preencha todos os campos!!!')
        return redirect('/add')
    
if __name__ == '__main__':
    app.run()
