import flask
from db import get_data

app = flask.Flask(__name__)

@app.route('/')
def home():
    return flask.render_template('index.html')

@app.route('/welcome', methods=['POST'])
def welcome():
    nome = flask.request.form['nome']
    email = flask.request.form['email']
    senha = flask.request.form['senha']
    get_data(nome, email, senha) 
    return flask.render_template('welcome.html', nome = nome, email = email, senha = senha)

if(__name__ == '__main__'):
    app.run(debug=True, host='0.0.0.0', port=5000)