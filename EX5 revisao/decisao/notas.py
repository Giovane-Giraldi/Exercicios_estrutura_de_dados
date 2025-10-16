nome = input("Digite seu nome:\n")
media = float(input("Digite sua nota de prova:\n"))

if media < 5:
    print(f"Lamento, {nome}, você reprovou.")

elif media < 6:
    print(f"Foi por pouco, {nome}, você ficou de recuperação.")

else:
    print(f"Parabéns, {nome}, você foi aprovado!")

print(f"Sua média foi: {media}")