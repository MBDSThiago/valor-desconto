#if,else,elif
# desconto <= RS 200,00 5%
# desconto >= RS 200,00 e < RS 300,00 10% 
# desconto >= RS 300,00 15%

valor = float(input("Digite o valor da compra: "))

if valor < 200:
    desconto = valor * 0.05
elif valor < 300:
    desconto = valor * 0.10
else:
    desconto = valor * 0.15

print(f"O desconto é de: R$ {desconto:.2f}")