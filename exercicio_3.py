def desc_pag (valor_pag, num_pag):   
        if num_pag >20000:
            print("Não trabalhamos com essa quantidade de páginas")
            return None
    
        if num_pag < 20:
            return valor_pag * num_pag   
        elif num_pag >= 20 and num_pag < 200:
            return valor_pag * num_pag * 0.85   
        elif num_pag >= 200 and num_pag < 2000:
            return valor_pag * num_pag * 0.80     
        else:
            return valor_pag * num_pag * 0.75
        
# --------------------- PROGRAMA PRINCIPAL -------------------

print("-" * 30, "Bem vindo a loja de cópias do Victor", "-" * 30)

while True:
    print("DIG - Digitalização")
    print("ICO - Impressão colorida")
    print("IPB - Impressão preto e branco")
    print("FOT - Fotocópia \n")
    opcao_menu = str(input("Digite o serviço desejado: \n"))
    num_pag = int(input("\n Qual o número de páginas? \n"))

    if opcao_menu == "DIG":
        valor_total = desc_pag (1.10, num_pag)
        if valor_total is not None:
            print(f"O valor total é de {valor_total}")

    if opcao_menu == "ICO":
        valor_total = desc_pag (1, num_pag)
        if valor_total is not None:
            print(f"O valor total é de {valor_total}")

    if opcao_menu == "IPB":
        valor_total = desc_pag (0.40, num_pag)
        if valor_total is not None:
            print(f"O valor total é de {valor_total}")
    if opcao_menu == "FOT":
        valor_total = desc_pag (0.20, num_pag)
        if valor_total is not None:
            print(f"O valor total é de {valor_total}")            
    else:
        print("Serviço inexistente, tente novamente: \n")