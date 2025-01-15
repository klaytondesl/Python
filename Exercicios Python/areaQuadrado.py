# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

comprimento = int(input("Digite o comprimento do quadrado: ")) # Recebe o número e atribui á variável [comprimento]
area = comprimento **2 # Calcula o valor do comprimento ao quadrado
dobro = area*2 # Recebe o valor da área e multiplica por 2

print("A área do quadrado é: {}".format(area)) # Exibe o valor da área
print("O dobro da área do quadrado é: {}".format(dobro)) # Exibe o valor do dobro da área


