print("Bem vindo a loja de gelados do Victor!")

total = 0 #declara e limpa a variável acumuladora

while True: #repete todo o código

    print("-" * 25, "Cardápio", "-" * 25)
    print("-" * 60)
    print("-" * 3, " | ",  " Tamanho " , " | ", "Cupuaçú (CP) " , " | ", " Açaí (AC) " , " | ", "-" * 3)
    print("-" * 3, " | ",  "    P   " , "  | ", "  R$ 9,00 " , "    | ", "  R$ 11,00 " , " | ", "-" * 3)
    print("-" * 3, " | ",  "    M   " , "  | ", "  R$ 14,00 " , "   | ", "  R$ 16,00 " , " | ", "-" * 3)
    print("-" * 3, " | ",  "    G   " , "  | ", "  R$ 18,00 " , "   | ", "  R$ 20,00 " , " | ", "-" * 3)
    print("-"* 60)

    sabor = str(input("Qual sabor deseja comprar? \n \n"))
    if sabor == "cp" or sabor == "ac": #primeira testagem, se for cp ou ac, caso contrario mostra invalido e reinicia
        #inicia a compra de cupuacu
        if sabor == "cp":
            tam = str(input("Qual o tamanho de Cupuaçú desejado?: \n \n"))
            if tam == "p" or tam == "m" or tam == "g": #testa os tamanhos dos potes de cupuacu
                if tam == "p":
                    total += 9
                    opcao = str(input("Deseja continuar comprando? (S/N) \n")) #repete o menu
                    if opcao == "s":
                        True
                    else:
                        print(f"Valor total da compra: {total} \n")
                        break
                elif tam == "m":
                    total += 14
                    opcao = str(input("Deseja continuar comprando? (S/N) \n"))
                    if opcao == "s":
                        True
                    else:
                        print(f"Valor total da compra: {total} \n")
                        break
                elif tam == "g":
                    total += 18
                    opcao = str(input("Deseja continuar comprando? (S/N) \n"))
                    if opcao == "s":
                        True
                    else:
                        print(f"Valor total da compra: {total} \n")
                        break
                   
            else:
                print("Tamanho inválido. Tente novamente")
        else: #caso contrario, assume que será acai
            tam = str(input("Qual o tamanho de Açaí desejado? \n"))
            if tam == "p":
                total += 11
                opcao = str(input("Deseja continuar comprando? (S/N) \n"))
                if opcao == "s":
                    True
                else:
                    print(f"Valor total da compra: {total} \n")
                    break
            elif tam == "m":
                total += 16
                opcao = str(input("Deseja continuar comprando? (S/N) \n"))
                if opcao == "s":
                    True
                else:
                    print(f"Valor total da compra: {total} \n")
                    break
            elif tam == "g":
                total += 20
                opcao = str(input("Deseja continuar comprando? (S/N) \n"))
                if opcao == "s":
                    True
                else:
                    print(f"Valor total da compra: {total} \n")
                    break
            else:
                print("Tamanho inválido. Tente novamente \n")
    else:
        print("Sabor inválido. Tente novamente")
    
        