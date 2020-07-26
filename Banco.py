nome = str(input("Banco YZP "))
saldo = float(input("Qual o saldo medio em credito de cada cliente "))


if saldo >= 0 and saldo <= 500: 
    print("Sem credito disponivel ")
elif saldo >= 500.01 and saldo <= 1000:
    calculo = (saldo/100)*30
    print("Possui trinta por cento de credito ", calculo)
elif saldo >= 1000.01 and saldo <= 3000:
    calculo = (saldo/100)*40
    print("Possui quarenta por cento de credito " ,calculo)
else:
    calculo = (saldo /100)*50
    print("Possui cinquenta por cento de credito " ,calculo)
        
    
    
    
    


