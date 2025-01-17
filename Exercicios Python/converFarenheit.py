# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.

celsius = float(input("Informe a temperatura em Celsius: ")) # Recebe o valor e atribui à variável [celsius]
farenheit = (celsius*9/5) + 32 # Calcula 9/5, multiplica pela variável [celsius] e soma 32 

print("{}º graus celsius é {}º graus farenheit".format(celsius,farenheit)) # Exibe o resultado da conversão  