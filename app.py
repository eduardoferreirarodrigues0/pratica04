from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Produtos disponíveis
produtos = [
    {'id': 1, 'nome': 'Chocolate Kit Kat ao Leite Nestlé - 41,5g', 'preco': 4.00},
    {'id': 2, 'nome': 'Chocolate Branco Lacta Laka Oreo 80g', 'preco': 6.50},
    {'id': 3, 'nome': 'Chocolate Bis Xtra ao Leite - 45g', 'preco': 3.50},
    {'id': 4, 'nome': 'Caixa Bombom Especialidades Nestlé 251g', 'preco': 15.50},
]

# Carrinho de compras
itens_carrinho = []

# Função para calcular o valor total do carrinho
def calcular_total():
    total = 0.0
    for item in itens_carrinho:
        produto = item['produto']
        quantidade = item['quantidade']
        total += produto['preco'] * quantidade
    return total


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/produtos')
def exibir_produtos():
    return render_template('produtos.html', produtos=produtos)


@app.route('/adicionar_produto', methods=['POST'])
def adicionar_produto():
    for produto in produtos:
        quantidade = int(request.form.get(str(produto['id'])))
        if quantidade > 0:
            itens_carrinho.append({'produto': produto, 'quantidade': quantidade})
    return redirect(url_for('exibir_carrinho'))

@app.route('/carrinho')
def exibir_carrinho():
    total = calcular_total()
    return render_template('carrinho.html', carrinho=itens_carrinho, total=total)

@app.route('/editar/<int:index>', methods=['GET', 'POST'])
def editar_produto(index):
    item = itens_carrinho[index]
    produto = item['produto']

    if request.method == 'POST':
        quantidade = int(request.form['quantidade'])
        itens_carrinho[index]['quantidade'] = quantidade
        return redirect(url_for('exibir_carrinho'))
    return render_template('editar.html', produto=produto, quantidade=item['quantidade'], index=index)

@app.route('/excluir/<int:index>')
def excluir_produto(index):
    if index < len(itens_carrinho):
        del itens_carrinho[index]

    return redirect(url_for('exibir_carrinho'))


if __name__ == '__main__':
    app.run(debug=True)



