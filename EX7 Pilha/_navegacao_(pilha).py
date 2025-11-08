def exibir_menu():
    print("\n=== MENU - HISTÓRICO DE NAVEGAÇÃO ===")
    print("1 - Acessar novo site")
    print("2 - Voltar (remover último site)")
    print("3 - Ver site atual")
    print("4 - Mostrar histórico completo")
    print("5 - Sair")

def main():
    historico = [] 

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            site = input("Digite o endereço do site: ").strip()
            if site:
                historico.append(site)
                print(f"Você acessou: {site}")
            else:
                print("Endereço inválido!")

       
        elif opcao == "2":
            if historico:
                removido = historico.pop()
                print(f"Voltando... Você saiu de: {removido}")
                if historico:
                    print(f"Agora você está em: {historico[-1]}")
                else:
                    print("Você está na página inicial (sem histórico).")
            else:
                print("Nenhum site no histórico para voltar.")

       
        elif opcao == "3":
            if historico:
                print(f"Você está no site: {historico[-1]}")
            else:
                print("Você ainda não acessou nenhum site.")

        
        elif opcao == "4":
            if historico:
                print("\n--- Histórico de navegação ---")
                for site in reversed(historico):
                    print(f"- {site}")
            else:
                print("Histórico vazio.")
        
       
        elif opcao == "5":
            print("\nEncerrando o navegador... Até mais!")
            break

        else:
            print("Opção inválida! Escolha entre 1 e 5.")

if __name__ == "__main__":
    main()
