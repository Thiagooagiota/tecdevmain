import funcionarios

def menu():
    print("Menu de Funcionario")
    print("1. Cadastrar Funcionario")
    print("2. Listar Funcionarios")
    
    opcao = input("Escolha uma opção: ")
    
    return opcao

if __name__ == "__main__":
    while True:
        opcao = menu()
        
        if opcao == '1':
            print("Cadastrar Funcionario")

            funcionarios.Funcionario.adicionar_funcionario()
            
        elif opcao == '2':
            
            print("Listar Funcionarios")
            
            funcionarios.Funcionario.listar_funcionarios()

    
        else:
            print("Opção inválida. Tente novamente.")
        
        continuar = input("Deseja continuar? (s/n): ")
        if continuar.lower() != 's':
            break