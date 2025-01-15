# Faça um Programa que peça a 4 notas bimestrais e mostre a média.

nota1 = float(input("Digite a primeira nota: ")) # Recebe a nota dentro da variável [nota1]
nota2 = float(input("Digite a segunda nota: ")) # Recebe a nota dentro da variável [nota2]
nota3 = float(input("Digite a terceira nota: ")) # Recebe a nota dentro da variável [nota3]
nota4 = float(input("Digite a quarta nota: ")) # Recebe a nota dentro da variável [nota4]
media = (nota1 + nota2 + nota3 + nota4)/4 # Soma as 4 notas e divide por 4 

# Imprime as notas digitadas e sua média.
print("As notas digitadas foi:\n{}, {}, {}, {}\nE sua média é: {:.2f}".format(nota1, nota2, nota3, nota4, media))


