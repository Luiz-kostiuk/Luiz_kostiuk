primeiro_numero = input("digite o primeiro numero: ")
escolha = input("digite a operação desejada: ")
segundo_numero = input("digite o segundo numero: ")

if escolha == "+":
   resultado = int(primeiro_numero) + int(segundo_numero)
elif escolha == "-":
    resultado = int(primeiro_numero) - int(segundo_numero)
elif escolha == "*":
    resultado = int(primeiro_numero) * int(segundo_numero)
elif escolha == "/":
    resultado = int(primeiro_numero) / int(segundo_numero)
else:
    resultado = "Operação inválida esolha entre +, -, * ou /"


calculadora = print (f"{primeiro_numero} {escolha} {segundo_numero} = {resultado}")