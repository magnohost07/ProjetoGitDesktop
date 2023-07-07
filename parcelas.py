# entrada de dados
produto = input('Produto: ')            # entrada de string
preco = float(input('Preço R$: '))      # entrada de float

'''
comentário de várias linhas
aqui dentro, tudo é comentário
'''

print('Formas de Pagto: {}'.format(produto))
print('-'*40)

for i in range(10):
    parcela = preco / (i+1)
    print('{0:2d}x de R$ {1:9.2f}'.format(i+1, parcela))

print('-'*40)