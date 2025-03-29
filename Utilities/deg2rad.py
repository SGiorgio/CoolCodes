import math

def gradi_a_radianti(gradi):
    return gradi * (math.pi / 180)

# Esempio di utilizzo
gradi = float(input("Inserisci l'angolo in gradi: "))
radianti = gradi_a_radianti(gradi)
##print(f"{gradi} gradi equivalgono a {radianti:.6f} radianti")
print(radianti)