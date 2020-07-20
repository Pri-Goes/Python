vendamensal=float(input("valor das vendas mensal "))

if vendamensal >= 20.000 and vendamensal <= 23.999:
    calculo = (vendamensal/100)*4 
    print("comissao", calculo)
elif vendamensal >= 24.000 and vendamensal <= 29.999:
    calculo = (vendamensal/100)*5
    print("comissao" , calculo)
elif vendamensal >= 30.000:
    calculo = (vendamensal/100)*6
    print("comissao" , calculo)
else:
    print("sem comissao")


