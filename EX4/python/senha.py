senha = str(input("Digite uma senha\n"))

confirma = str(input("Digite a senha novamente\n"))

while senha != confirma:
  print("senha incorreta")
  confirma = str(input("Digite a senha novamente\n"))
print("senha certa")