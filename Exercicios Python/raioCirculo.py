# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

raio = float(input("Digite o valor do raio: ")) # Recebe o número e atribui à variável [raio]
area = 3.14 * (raio*raio) # Calcula a variável [raio] ao quadrado e multiplica pelo valor de Pi

print("Área: {:.2f}".format(area)) # Exibe o resultado da variável [area]
