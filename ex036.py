print('Vamos calcular a condição do seu empréstimo?')
casa = float(input('Qual o valor da casa que pretende comprar? R$'))
salario = float(input('Qual é o seu salário? R$'))
tempo = int(input('Em quantos anos pretende pagar o empréstimo?'))
prestacao = casa/(tempo * 12)
minimo = salario * 30 / 100
if prestacao >= minimo:
    print('A prestação mensal do empréstimo é de R${:.2f} reais.\nA prestação excede 30% do seu salário, logo o empréstimo foi NEGADO'.format(prestacao))
else:
    print('A prestação mensal do empréstimo será de R${:.2f} reais e não excede 30% do seu salário.'.format(prestacao))
    print('\033[7mEmpréstimo realizado com sucesso\033[m')