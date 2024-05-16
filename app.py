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

    # Variável utilizada para saber qual e se algum campo não foi preenchido
    noneInputs = []

    for c, i in enumerate([nome, email, tipo]):
        # Verifica Se os campos NÃO foram preenchidos
        if not i:
            noneInputs.append(c)
            i = None

    # Verifica quais campos não foram preenchidos
    noneInputsRefinada = []
    for i in noneInputs:
        match i:
            case 0:
                noneInputsRefinada.append('nome')
            case 1:
                noneInputsRefinada.append('email')
            case 2:
                noneInputsRefinada.append('tipo')

    # Imprime os Campos Preenchidos
    print(f'Nome: {nome}')
    print(f'Email: {email}')
    print(f'Tipo da Empresa: {tipo}')

    # Caso todos os campos sejam preenchidos
    if len(noneInputsRefinada) == 0:
        return "Dados Recebidos Com Sucesso!"
    
    # Caso algum campo não seja preenchido
    errorString = 'Erro! Campos Não Preenchidos: '
    for i in noneInputsRefinada:
        errorString += i + ' '

    return errorString

# Inicializa a Aplicação
if __name__ == '__main__':
    app.run(debug=True)
