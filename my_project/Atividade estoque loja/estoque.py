class Produtos:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def adicionar_estoque(self, quantidade):
        if quantidade <= 0:
            raise ValueError("Digite uma quantidade válida maior que zero.")
        self.quantidade += quantidade

    def remover_estoque(self, quantidade):
        if quantidade <= 0:
            raise ValueError("Digite uma quantidade válida maior que zero.")
        if quantidade > self.quantidade:
            raise ValueError("Quantidade a remover é maior que a disponível no estoque.")
        self.quantidade -= quantidade



produto1 = Produtos("Produto A", 10.0, 100)
produto2 = Produtos("Produto B", 20.0, 50)
produto3 = Produtos("Produto C", 30.0, 75)


lista_produtos = [produto1, produto2, produto3]



def listar_produtos(lista):
    if not lista:
        print("Nenhum produto no estoque.")
    else:
        print("\nProdutos em estoque:")
        for produto in lista:
            print(f"- {produto.nome} | Preço: R${produto.preco:.2f} | Quantidade: {produto.quantidade}")
