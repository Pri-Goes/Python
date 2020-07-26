nome = str(input("Qual o nome do funcionario "))
horas = float(input("A quantidade de horas permitidas pela internte e "))
acesso = float(input("A quantidade de horas acessadas e "))

if acesso > horas:
    print("voce ultrapacou o limite" )
else:
    if acesso < horas:
        print("Abaixo do limite ")
    else:
        print("No limite")

    
               
