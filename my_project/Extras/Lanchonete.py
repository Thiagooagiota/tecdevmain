
opc = int(input(f"""selecione o numero do seu pedido
                #1 coca cola 1lt R$10,00
                #2 coca cola lata R$6,00
                #3 mc lanche feliz R$20,00
                #4 mc crispy chicken R$35,00
                #5 crispy chicken spicy R$30,00
                
                #6 pagamento 
                 """))

total = 0

while opc != 6:
    if opc == 1:
        qtd1 = int(input("quantidade \n"))

        total += qtd1 * 10
    elif opc == 2:
        qtd2 = int(input("quantidade \n"))
     
        total += qtd2 * 6
    elif opc == 3:
        qtd3 = int(input("quantidade \n"))

        total += qtd3 * 20
    
    elif opc == 4:
        qtd4 = int(input("quantidade \n"))

        total += qtd4 * 35
    
    elif opc == 5:
        qtd5 = int(input("quantidade \n"))

        total += qtd5 * 30
    
    else:
        print("invalido")
        continue


    mais = int(input(f"""deseja continuar seu pedido?
                      #1 sim
                      #2 nao
                      # """))
    
    if mais == 1:
        opc = int(input(f"""Selecione o número do seu pedido:
                        #1 Coca Cola 1lt R$10,00
                        #2 Coca Cola Lata R$6,00
                        #3 Mc Lanche Feliz R$20,00
                        #4 Mc Crispy Chicken R$35,00
                        #5 Crispy Chicken Spicy R$30,00
                        #6 Pagamento
                        """))
        
    elif mais == 2:
        break
    else:
        print("Opção inválida, tente novamente.")

print(f"""valor total: R${total}""")