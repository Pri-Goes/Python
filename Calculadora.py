n1= float(input("insira o primeiro numero: "))
n2= float(input("insira o segundo numero: "))
sinal = str(input("operacoes disponiveis: +, -, /, *: "))

if sinal == "+":
    calculo = n1 + n2
    print("a soma dos numeros e ", calculo)
elif sinal == "-":
    calculo = n1-n2
    print("a diferenca dos numeros e ", calculo)
elif sinal == "/":
    calculo = n1/n2
    print("a divisao dos numeros e " , calculo)
elif sinal == "*":
    calculo = n1*n2
    print("a multiplicacao dos numeros e " ,calculo)
    

