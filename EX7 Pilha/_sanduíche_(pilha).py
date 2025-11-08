def exibir_menu():
    print("\n=== MENU - MONTAGEM DO SANDUÍCHE ===")
    print("1 - Adicionar ingrediente")
    print("2 - Remover ingrediente (do topo)")
    print("3 - Ver último ingrediente adicionado")
    print("4 - Mostrar sanduíche completo")
    print("5 - Finalizar pedido")

def main():
    pilha = []  

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        
        if opcao == "1":
            ingrediente = input("Digite o nome do ingrediente a adicionar: ").strip()
            if ingrediente:
                pilha.append(ingrediente)
                print(f"Ingrediente '{ingrediente}' adicionado ao sanduíche.")
            else:
                print("Nome de ingrediente inválido.")

       
        elif opcao == "2":
            if pilha:
                removido = pilha.pop()
                print(f"Ingrediente '{removido}' foi removido do topo do sanduíche.")
            else:
                print("O sanduíche está vazio! Não há nada para remover.")

        
        elif opcao == "3":
            if pilha:
                print(f"O último ingrediente adicionado é: '{pilha[-1]}'")
            else:
                print("O sanduíche está vazio!")

       
        elif opcao == "4":
            if pilha:
                print("\n--- Seu sanduíche ---")
                for i, ingrediente in enumerate(pilha):
                    if i == 0:
                        print(f"Pão de baixo → {ingrediente}")
                    else:
                        print(f"↑ {ingrediente}")
                print("↑ Pão de cima (topo)")
            else:
                print("Ainda não há ingredientes no sanduíche.")

        
        elif opcao == "5":
            print("\nPedido finalizado! Bom apetite! 🍔")
            break

        else:
            print("Opção inválida! Escolha entre 1 e 5.")

if __name__ == "__main__":
    main()
