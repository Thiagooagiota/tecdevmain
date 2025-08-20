class Alunos:
    def __init__(self):
        self.alunos = {}

    def adicionar_aluno(self):
        while True:
            nome = input("Digite o nome do aluno: ")
            curso = input("Digite o curso do aluno: ")  
            matricula = input("Digite a matrícula do aluno: ")

            if not nome:
                    print("Nome não pode ser vazio. Tente novamente.")
                    continue  
            else:
                break  
            
        self.alunos[nome] = (curso, matricula)

        return f"Aluno {nome} cadastrado com sucesso!"

    def visualizar_alunos(self):
        if not self.alunos:
            return "Nenhum aluno cadastrado."

        resultado = "Alunos cadastrados:\n"
        for nome, (curso, matricula) in self.alunos.items():
            resultado += f"Nome: {nome}, Curso: {curso}, Matrícula: {matricula}\n"

        return resultado