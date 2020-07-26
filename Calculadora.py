n1= float(input("insira o primeiro numero: "))
sinal = str(input(" "))
n2= float(input("insira o segundo numero: "))

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
elif sinal == "**":
    calculo = n1**n2
    print ("a potencia dos numeros e " ,calculo)


