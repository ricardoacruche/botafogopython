'''#Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto.
Exiba o valor do desconto e o preço a pagar.'''

# Solicita o preço da mercadoria e o percentual de desconto
preco = float(input("Digite o preço da mercadoria: R$ "))
percentual_desconto = float(input("Digite o percentual de desconto: "))

# Calcula o valor do desconto
valor_desconto = preco * (percentual_desconto / 100)

# Calcula o preço final
preco_final = preco - valor_desconto

# Exibe os resultados
print(f"Valor do desconto: R$ {valor_desconto:}")
print(f"Preço a pagar: R$ {preco_final:}")
