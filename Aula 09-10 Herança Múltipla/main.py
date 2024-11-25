from luta import *

daniel = Boxeador("Daniel Perfect")
caique = Boxeador("Caique")

print(daniel)
print()
print(caique)
print()

print("--------- Boxe ---------")
print()
daniel.cruzado(caique)
print(caique)
print()
daniel.gancho(caique)
print(caique)
print()
caique.soco(daniel)
print(daniel)

print()

print("--------- Cadeirada ---------")
print()

caique.cadeira(daniel)
print(daniel)
print()
daniel.cadeira(caique)
print(caique)
