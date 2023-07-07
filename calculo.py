# entrada de dados
nome = input('Nome: ')
idade = int(input('Idade: '))
salario = float(input('Salário: '))

print('Nome: {} - Idade: {}'.format(nome, idade))

if idade >= 18:
    print('{} você é maior de idade'.format(nome))
else:
    print('Ops... {}, você é menor'.format(nome))

reajuste = salario * 1.10

print('{0:20s} seu novo salário é R$: {1:9.2f}'.format(nome, reajuste))