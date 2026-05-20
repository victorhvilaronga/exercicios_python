print("Bem vindo à loja do Victor Hugo Vilaronga!")
valor_unitario = float(input("Digite o valor unitário do produto: \n")) #catches the product's price
qtd_produto = int(input("Digite a quantidade da compra: \n")) #catches the product's quantity
valor_total = valor_unitario * qtd_produto #calculates the product's final cost

#conditional test for the right discount
if valor_total < 2500:
    valor_total = valor_total
elif valor_total >= 2500 and valor_total < 6000:
    valor_total -= valor_total * 0.04
elif valor_total >= 6000 and valor_total < 10000:
    valor_total -= valor_total * 0.07
else:
    valor_total -= valor_total * 0.11

print(f"Valor total sem desconto {valor_unitario * qtd_produto}") #prints the full price without the discount
print(f"Valor total com desconto {valor_total}") #prints the full price with the discount

