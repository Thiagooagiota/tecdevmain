import estoque

def menu():
    while True:
        print("\nEscolha uma opção:")
        print("1 - Adicionar produto (não implementado)")
        print("2 - Remover produto (não implementado)")
        print("3 - Listar produtos")
        print("4 - Sair")

        escolha = input("Digite sua opção: ")

        if escolha == "1":
            produto = input("Digite o nome do produto: ")
            try:
                preco = float(input("Digite o preço do produto: "))
                quantidade = int(input("Digite a quantidade do produto: "))

                novo_produto = estoque.Produtos(produto, preco, quantidade)
                estoque.lista_produtos.append(novo_produto)
            except ValueError:
                print("Preço ou quantidade inválido. Tente novamente.")
                continue

        elif escolha == "2":
            
            produto = input("Digite o nome do produto a remover: ")
            quantidade = int(input("Digite a quantidade a remover: "))
            for p in estoque.lista_produtos:
                if p.nome == produto:
                    try:
                        p.remover_estoque(quantidade)
                        print(f"Quantidade de {produto} atualizada para {p.quantidade}.")
                    except ValueError as e:
                        print(e)
                    break
            else:
                print("Produto não encontrado.")

        elif escolha == "3":
            estoque.listar_produtos(estoque.lista_produtos)
        elif escolha == "4":
            print("Saindo...")
            break
        else:
            print("Função inexistente ou inválida. Tente novamente.")
            continue

menu()