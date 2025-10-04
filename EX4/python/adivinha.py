import random

numero_int = random.randint(1, 10)
print(f"Número aleatório: {numero_int}")

tentativa = int(input("Digite um número de 1 a 10\n"))

contador = 1

while tentativa != numero_int:
  contador+=1
  tentativa = int(input("Errado, tente novamente \n"))
print("parabens, voce acertou com ", contador, "tentativa(s)") 
  


