import math

def solve_kepler(M, e, tol=1e-6, max_iter=1000):
    F = math.log(((2*M)/(e)+1.8))  #starting point, generally good
    for _ in range(max_iter):
        f = e * math.sinh(F) -F -M
        f_prime = e * math.cosh(F) -1 
        delta = -f / f_prime
        F += delta
        if abs(delta) < tol:
            return F
    raise ValueError("Newton-Raphson method doesn't converge")

## INPUT
t = float(input("Time elapsed (s): "))
e = float(input("Eccentricity: "))
h = float(input("Specific angular momentum (km^2/s): "))
mu = 398600

## ELABORATION

## STEP 1: obtain Mean Hyperbolic Anomaly
Mh = ((mu**2)*math.sqrt((e**2 - 1)**3)*t)/h**3
print("Mh: ", Mh)

## STEP 2: obtain Hyperbolic Anomaly
F = solve_kepler(Mh, e)
print("F: ", F)

## STEP 3: obtain True Anomaly
theta = 2 * math.atan(math.sqrt((e+1)/(e-1))*math.tanh(F/2))
print("True Anomaly (rad): ", theta)