from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/consulta')
def consulta():
    return render_template('consulta.html')

@app.route('/marketplace')
def market():
    return render_template('marketplace.html')

@app.route('/processar', methods=['POST'])
def processar():
    # Perguntas "placeholder"
    nome = request.form['nome']
    email = request.form['email']
    tipo = request.form['tipo']

    # Tratamento dos Dados Recebidos
    print(f'Nome: {nome}')
    print(f'Email: {email}')
    print(f'Tipo da Empresa: {tipo}')

    return "Dados Recebidos Com Sucesso!"

if __name__ == '__main__':
    app.run(debug=True)
