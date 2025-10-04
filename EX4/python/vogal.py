palavra =str(input("digite uma palavra\n"))

vogal = "aeiouAEIOU"

contador = 0

for letra in palavra:
  if letra in vogal:
    contador +=1
print(f"A palavra '{palavra}' tem {contador} vogal(is).")
    
