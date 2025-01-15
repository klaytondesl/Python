# Faça um Programa que peça a temperatura em graus Farenheit,
# transforme e mostre a temperatura em graus Celsius.

farenheit = float(input("Informe a temperatura em farenheit: ")) # Recebe um valor e atrbui à variável [farenheit]
celsius = 5/9*(farenheit-32) # Calcula a variável [farenheit] - 32 e multiplica pelo valor da divisão de 5/9

print("{}º graus farenheit é {}º graus celsius".format(farenheit,celsius)) # Exibe o resultado da conversão 
