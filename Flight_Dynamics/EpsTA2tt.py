import math 

##This code returns the time elapsed since passage from the pericenter 

##True Anomaly :- Elliptic Anomaly :- Mean Elliptic Anomaly :- Time 

##INPUT
theta = float(input("T. Anomaly (rad): "))
e = float(input("Eccentricity: "))
T = float(input("Period (s): "))

##ELABORATION 

##STEP 1: obtain Elliptic Anomaly

E = 2*math.atan(math.sqrt((1-e)/(e+1))*math.tan(theta/2))
print("E: ",E)

##STEP 2: obtain Mean Elliptic Anomaly

Me = E - e * math.sin(E)
print("Me: ",Me)
##STEP 3: obtain time elapsed 

t = (Me*T)/(2*math.pi)

print("Time elapsed: ",t)


