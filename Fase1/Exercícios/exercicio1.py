#CALCULADORA DO IMC
  
# Pedir o nome do usuário
nome= input("Digite o seu nome ---> ")

# Pedir o peso em kg (número decimal)
peso= float(input("Digite o seu peso em Kg ---> "))

# Pedir a altura em metros (número decimal)
altura= float(input("Digite a sua ALTURA --->"))

# Calcular o IMC: peso / (altura ** 2)
imc=peso/(altura**2)

# Exibir uma mensagem personalizada:
# IMC abaixo de 18.5 → "Abaixo do peso"
# IMC entre 18.5 e 24.9 → "Peso normal"
# IMC entre 25 e 29.9 → "Sobrepeso"
# IMC 30 ou acima → "Obesidade"
if imc<18.5:
    print(f"{nome}, você está abaixo do peso")
elif imc>=18.5 and imc<24.9:
    print(f"{nome}, você está no seu peso normal")
elif imc>=25 and imc<29.9:
    print(f"{nome}, você está sobrepeso")
else:
    print(f"{nome}, você está obeso")