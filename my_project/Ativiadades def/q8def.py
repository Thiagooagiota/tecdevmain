def idmeses(idade):
    total = idade * 12

    return total

anos = int(input("digite sua idade: "))
idade = idmeses(anos)
print(f"sua idade em meses é: {idade}")