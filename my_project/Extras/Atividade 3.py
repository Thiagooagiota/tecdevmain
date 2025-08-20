print("Sistema RH xyz")

cargahoraria = int(input("carga horaria do funcionario em horas:"))
valorhora = float(input("digite o valor da hora do funcionario"))

resultado = cargahoraria * valorhora

print(f"o valor total a ser pago é R$ {resultado:.2f}")