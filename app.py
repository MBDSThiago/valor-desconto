# Programa que calcula o desconto de uma compra com base no valor informado pelo usuário.
valor = float(input("Digite o valor da compra: "))

# Condições de desconto:
# Aqui o programa verifica o valor da compra e aplica o desconto correspondente.
# Começando com a primeira condição, usando o if para verificar se o valor é menor que 200.
if valor < 200:
    desconto = valor * 0.05
    print(f"O desconto aplicado foi de 5%, total do desconto: R$ {desconto:.2f}, e o valor final da compra é R$ {valor - desconto:.2f}.")

# O elif é usado para verificar a segunda condição, que é se o valor da compra é menor que 300.
elif valor < 300:
       desconto = valor * 0.10
       print(f"O desconto aplicado foi de 10%, total do desconto: R$ {desconto:.2f}, e o valor final da compra é R$ {valor - desconto:.2f}.")

# O else é usado para lidar com qualquer valor que não se encaixe nas condições anteriores, ou seja, valores iguais ou superiores a 300.
else:
        desconto = valor * 0.15
        print(f"O desconto aplicado foi de 15%, total do desconto: R$ {desconto:.2f}, e o valor final da compra é R$ {valor - desconto:.2f}.")