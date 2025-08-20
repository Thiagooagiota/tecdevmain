from cadastro import Alunos

def menu():
    
    cadastro = Alunos()
    
    while True:
        print("Menu:")
        print("1. Cadastrar aluno")
        print("2. Visualizar alunos cadastrados")
        print("3. Sair")
    
        try:
            user = int(input("Escolha uma opção: "))

            if user == 1:
                
                print(cadastro.adicionar_aluno())
            elif user == 2:
                
                print(cadastro.visualizar_alunos())
                
            elif user == 3:
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")
        
        except ValueError:
            print("Opção inválida. Por favor, insira um número.")


menu()