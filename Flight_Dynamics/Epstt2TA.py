import math
##This code returns the true anomaly given the time elapsed since the passage from the pericenter


##Since Keplero's equation is transcendent, It needs numeric approximation
def solve_kepler(M, e, tol=1e-6, max_iter=100):
    E = M  #starting point, generally good
    for _ in range(max_iter):
        f = E - e * math.sin(E) - M
        f_prime = 1 - e * math.cos(E)
        delta = -f / f_prime
        E += delta
        if abs(delta) < tol:
            return E
    raise ValueError("Newton-Raphson method doesn't converge")

##INPUT
T = float(input("Period (s): "))
t = float(input("Time elapsed (s): "))
e = float(input("Eccentricity: "))

##STEP 1: obtain Mean Elliptic Anomaly
Me = (2*math.pi*t)/T

##STEP 2: obtain Elliptic Anomaly
E = solve_kepler(Me,e)

##STEP 3: obtain True Anomaly
theta = 2*math.atan(math.sqrt((1+e)/(1-e))*math.tan(E/2))

##OUTPUT 
print("True Anomaly (rad): ",theta)

