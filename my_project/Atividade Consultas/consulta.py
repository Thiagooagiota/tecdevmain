import datetime

class Consultas:
    def __init__(self,nome_paciente,nome_medico,data, horario):
        self.nome_paciente = nome_paciente
        self.nome_medico = nome_medico
        self.data = data
        self.horario = horario

    def exibir_agendamentos(self):
        print(f"Paciente: {self.nome_paciente}")
        print(f"Médico: {self.nome_medico}")
        print(f"Data: {self.data.strftime('%d/%m/%Y')}")
        print(f"Horário: {self.horario.strftime('%H:%M')}")
        print("-----------------------------")

infos = []