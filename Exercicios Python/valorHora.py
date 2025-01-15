# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

mes = str(input("Digite o mês: ")).upper() # Recebe uma string e atribui à variável [mes] transformando o texto em maiúsculo.
valor = float(input("Digite o valor das suas horas: ")) # Recebe um valor e atribui à variável [valor]
hora = float(input("Digite a quantidade de horas trabalhadas: ")) # Recebe um valor e atribui à variável [hora]
calcHoras = valor * hora # Multiplica a variável [valor] com a variável [hora]

print("-----------------------------------") # Exibe caracteres na tela 
print("{}:\n\nValor Hora: {}\nHoras Trabalhadas: {}\nSalário: R$ {:.2f}".format(mes,valor,hora,calcHoras)) # Exibe o resultado
print("-----------------------------------") # Exibe caracteres na tela
