from collections import deque

def menu():
    print("\n=== SISTEMA DE FILA DE JOGADORES ===")
    print("1 - Adicionar jogador à fila")
    print("2 - Iniciar partida manualmente (mínimo 5 jogadores)")
    print("3 - Mostrar fila de espera")
    print("4 - Sair")

def main():
    fila = deque()
    minimo_para_iniciar = 5
    maximo_fila = 20

    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            if len(fila) >= maximo_fila:
                print(f"A fila já está cheia ({maximo_fila} jogadores). Aguarde uma partida começar.")
                continue

            nome = input("Digite o nome do jogador: ").strip()
            if nome:
                fila.append(nome)
                print(f"{nome} entrou na fila.")
                print(f"Total de jogadores na fila: {len(fila)}/{maximo_fila}")

                # Início automático se atingir 20 jogadores
                if len(fila) == maximo_fila:
                    print("\nPartida iniciando automaticamente!")
                    print("Jogadores desta partida:")
                    while fila:
                        jogador = fila.popleft()
                        print(f"- {jogador}")
                    print("Partida iniciada com sucesso!")
            else:
                print("Nome inválido. Tente novamente.")

        elif opcao == "2":
            if len(fila) < minimo_para_iniciar:
                faltam = minimo_para_iniciar - len(fila)
                print(f"Não há jogadores suficientes para iniciar a partida. Faltam {faltam} jogador(es).")
            else:
                print("\nPartida manual iniciada!")
                print("Jogadores desta partida:")
                while fila:
                    jogador = fila.popleft()
                    print(f"- {jogador}")
                print("Partida iniciada com sucesso! A fila agora está vazia.")

        elif opcao == "3":
            if fila:
                print("\nJogadores na fila de espera:")
                for i, jogador in enumerate(fila, start=1):
                    print(f"{i}. {jogador}")
                print(f"\nTotal na fila: {len(fila)}/{maximo_fila}")
            else:
                print("Nenhum jogador na fila no momento.")

        elif opcao == "4":
            print("Encerrando o sistema... Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()