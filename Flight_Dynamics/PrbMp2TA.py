import math 

Mpinp = float(input("Inserisci Anomalia Parabolica: "))

addendo = 3*Mpinp + (9*(Mpinp**2)+1)**(1/2)
result = 2*math.atan((addendo)**(1/3)-(addendo)**(-1/3))

print("Anomalia vera = ",result)



