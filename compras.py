# declara uma variável (vetor) global, ou seja, que pode
# ser acessado em qualquer módulo (function) do sistema
produtos = []

def incluir():
    print('Inclusão de Produtos')
    print('-'*30)
    item = input('Produto: ')
    produtos.append(item)      # adiciona o item ao vetor
    print('Ok! Produto cadastrado')

def listar():
    print('Listagem dos Produtos Cadastrados')
    print('-'*30)

    # percorre o vetor, elemento por elemento
    #for prod in produtos:
    #    print(prod)

    # outra forma, acessando pelo índice
    for i in range(len(produtos)):
        print('{}. {}'.format(i+1, produtos[i]))

def excluir():
    listar()

    num = int(input('Qual número do produto excluir? '))

    if num <= 0 or num > len(produtos):
        print('Ops... número inválido')
        return            # retorna ao módulo principal

    produtos.pop(num-1)
    print('Ok! Produto excluído da lista de compras')

######################### programa principal
while True:
    print()
    print('1. Incluir Produto')
    print('2. Listar Produtos')
    print('3. Excluir Produto')
    print('4. Sair')
    opcao = int(input('Opção: '))
    if opcao == 1:
        incluir()
    elif opcao == 2:
        listar()
    elif opcao == 3:
        excluir()
    else:
        break    # sai da repetição

