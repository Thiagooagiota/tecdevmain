from biblioteca import Livros
import biblioteca

def menu():
    while True:
        print("\033c")
        print("escolha uma opção:\n")
        print("1 - emprestar livro\n")
        print("2 - devolver livro\n")
        print("3 - checar disponibilidade de livros\n\n")
        print("4 - sair\n")

        escolha = int(input("Digite sua escolha: "))

        if escolha == 1:
            ver = int(input(f"Qual livro você quer emprestar? (1, 2 ou 3): \n (1), {biblioteca.livro1.titulo} (2), {biblioteca.livro2.titulo} (3), {biblioteca.livro3.titulo}\n"))

            if ver < 1 or ver > 3:
                
                print("Opção inválida. Tente novamente.")
                return menu()
            else:
                print("\033c")
                if ver == 1:
                    ver = biblioteca.livro1
                elif ver == 2:
                    ver = biblioteca.livro2
                elif ver == 3:
                    ver = biblioteca.livro3
                
                Livros.emprestar(ver)

        if escolha == 2:
            ver = int(input(f"Qual livro você quer devolver? (1, 2 ou 3): \n (1), {biblioteca.livro1.titulo} (2), {biblioteca.livro2.titulo} (3), {biblioteca.livro3.titulo}\n"))

            if ver < 1 or ver > 3:
                print("Opção inválida. Tente novamente.")
                return menu()
            else:
                if ver == 1:
                    ver = biblioteca.livro1
                elif ver == 2:
                    ver = biblioteca.livro2
                elif ver == 3:
                    ver = biblioteca.livro3
                Livros.devolver(ver)

        if escolha == 3:
            print("\033c")
            print(biblioteca.livro1.exibir_info())
            print(biblioteca.livro2.exibir_info())
            print(biblioteca.livro3.exibir_info())
            input("Pressione Enter para continuar...")

        if escolha == 4:
            print("\033c")
            print("Saindo do sistema...")
            input("Pressione Enter para continuar...")
            break








menu()