import math 

##This code returns the time elapsed since passage from the pericenter 

##True Anomaly :- Elliptic Anomaly :- Mean Elliptic Anomaly :- Time 

##INPUT
theta = float(input("True Anomaly (rad): "))
e = float(input("Eccentricity: "))
T = float(input("Orbit period (s): "))
##ELABORATION 

##STEP 1: obtain Elliptic Anomaly

E = 2*math.atan(math.sqrt((e-1)/(e+1))*math.tan(theta/2))

##STEP 2: obtain Mean Elliptic Anomaly

Me = E - e * math.sin(E)

##STEP 3: obtain time elapsed 

t = (Me*T)/(2*math.pi)

print("Time elapsed: ",t)


