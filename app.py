#Importando as classes e funções necessárias do Flask.
from flask import Flask, render_template, request, redirect, url_for

#Criando uma instância do objeto Flask para a aplicação web.
app = Flask(__name__)

# Dicionário que armazenará os produtos e seus preços
produtos = {
    100: {'descricao': 'Cachorro-Quente', 'valor': 9.00},
    101: {'descricao': 'Cachorro-Quente Duplo', 'valor': 11.00},
    102: {'descricao': 'X-Egg', 'valor': 12.00},
    103: {'descricao': 'X-Salada', 'valor': 13.00},
    104: {'descricao': 'X-Bacon', 'valor': 14.00},
    105: {'descricao': 'X-Tudo', 'valor': 17.00},
    200: {'descricao': 'Refrigerante Lata', 'valor': 5.00},
    201: {'descricao': 'Chá Gelado', 'valor': 4.00}
}

# Variável criada para armazenar o valor total da compra
valor_total = 0
#Lista que armazena os produtos do pedido atual.
pedido = []

@app.route('/', methods=['GET', 'POST'])
def index():
    global valor_total
    global pedido

    if request.method == 'POST':
        # Obter o código do produto a partir do formulário
        codigo = int(request.form['codigo'])

        if codigo in produtos:
            # Adicionar o valor do produto ao valor total da compra
            valor_total += produtos[codigo]['valor']
            # Adicionar a descrição do produto ao pedido
            pedido.append(produtos[codigo]['descricao'])
            mensagem = f'{produtos[codigo]["descricao"]} adicionado ao pedido.'
        else:
            mensagem = 'Opção inválida.'

        return render_template('index.html', produtos=produtos, mensagem=mensagem, pedido=pedido)

    return render_template('index.html', produtos=produtos, pedido=pedido)

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    global valor_total
    global pedido

    if request.method == 'POST':
        if 'submit_button' in request.form:
            if request.form['submit_button'] == 'Voltar':
                # Redirecionar para a página de checkout
                return redirect(url_for('index'))
            elif request.form['submit_button'] == 'Encerrar':
                # Finalizar o pedido, reiniciando as variáveis
                valor_final = valor_total
                valor_total = 0
                pedido = []
                return render_template('encerramento.html', valor_final=valor_final)

    return render_template('checkout.html', valor_total=valor_total, pedido=pedido)

if __name__ == '__main__':
    app.run(debug=True)
