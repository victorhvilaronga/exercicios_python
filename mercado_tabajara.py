def compra_cartao_tabajara(opcao, qtd, valor_total):
    print("Tabajara")
    file_duplo = 'Filé Duplo'
    alcatra = 'Alcatra'
    picanha = 'Picanha'
    desconto = 0.05
    if opcao == 1:
        opcao = file_duplo
        if qtd <= 5:
            valor_total = qtd * (4.90 - (4.90 * desconto))
        elif qtd > 5:
            valor_total = qtd * (5.80 - (5.80 * desconto))
    elif opcao == 2:
        opcao = alcatra 
        if qtd <= 5:
            valor_total = qtd * (5.90 - (5.90 * desconto))
        elif qtd > 5:
            valor_total = qtd * (6.80 - (6.80 * desconto))
    else:
        opcao = picanha
        if qtd <= 5:
            valor_total = qtd * (6.90 - (6.90 * desconto))
        elif qtd > 5:
            valor_total = qtd * (6.80 - (7.80 * desconto))
    print(f'{opcao} | Peso: {qtd}kg| Valor Total: R${valor_total + (valor_total * desconto):.2f} Desconto: R$ {valor_total * desconto:.2f}|Valor Total com desconto: {valor_total} | Forma de pagamento: Cartão Tabajara')
    

def compra_normal(opcao, qtd, valor_total):
    print("Normal")
    file_duplo = 'Filé Duplo'
    alcatra = 'Alcatra'
    picanha = 'Picanha'
    if opcao == 1:
        opcao = file_duplo
        if qtd <= 5:
            valor_total = qtd * 4.90
        elif qtd > 5:
            valor_total = qtd * 5.80 
    elif opcao == 2:
        opcao = alcatra
        if qtd <= 5:
            valor_total = qtd * 5.90 
        elif qtd > 5:
            valor_total = qtd * 6.80 
    else:
        opcao = picanha
        if qtd <= 5:
            valor_total = qtd * 6.90 
        elif qtd > 5:
            valor_total = qtd * 6.80 
    print(f'{opcao} | Peso: {qtd} | Total: R$ {valor_total} | Forma de pagamento: X')
  

#Programa principal
forma_pgmto = int(input("Vai utilizar cartão Tabajara no pagamento? 1. Sim; 2. Não \n"))

opcao = 0
valor_total = 0

print(" "*10 + "         Até 5 Kg " + " "* 10 + "  Acima de 5 Kg \n"
"1. File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg \n"
"2. Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg \n"
"3. Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg \n")
if forma_pgmto == 1:
    opcao = int(input("Qual o produto? \n"))
    qtd = float(input("Qual a quantidade? \n"))
    compra_cartao_tabajara(opcao, qtd, valor_total)
else:
    opcao = int(input("Qual o produto? \n"))
    qtd = float(input("Qual a quantidade? \n"))
    compra_normal(opcao, qtd, valor_total)
        
                
            