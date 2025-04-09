import math

##INPUT
theta = float(input("T. Anomaly (rad): "))
e = float(input("Eccentricity: "))
h = float(input("Specific angular momentum (km^2/s): "))
mu = 398600


###ELABORATION
F = 2*math.atanh(math.sqrt((e-1)/(e+1))*math.tan(theta/2))
print("F: ",F)

Mh = e*math.sinh(F) - F
print("Mh: ",Mh)

t = (Mh * h**3) / (((e**2-1)**(3/2))*(mu**2))
print("Time elapsed: ",t)
