# Faça um Programa que converta metros para centímetros.

metro = float(input("Digite o metro a ser convertido: ")) # Recebe o número e atribui à variável [metro]
cm = metro * 100 # Multiplica o metro

print("{} Metros é {:.0f} centímetros".format(metro, cm)) # Exibe o resultado convertido