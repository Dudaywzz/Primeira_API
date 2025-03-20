from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!/Ola mundo'


@app.route('/<informacao_texto>')
def hello_name(informacao_texto):
    return f'Hello, {informacao_texto}!'


@app.route('/soma/<num1>/<num2>')
def soma(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    return f'Soma de {num1} + {num2} = {num1 + num2}'

@app.route('/subtracao/<num1>/<num2>')
def subtracao(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    return f'Subtracao de {num1} - {num2} = {num1 - num2}'

@app.route('/multiplicacao/<num1>/<num2>')
def multiplicacao(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    return f'Multiplicacao de {num1} * {num2} = {num1 * num2}'

@app.route('/divisao/<num1>/<num2>')
def divisao(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    return f'Divisao de {num1} / {num2} = {num1 / num2}'


if __name__ == '__main__':
    app.run(debug=True)


