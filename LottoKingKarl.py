# Lotto King Karl Zahlen Generator
#================================
from math import *
from random import *
#================================
# Banner
print("\n###", "Lotto King Karl", "###")

# Eine Liste
LottoZahlenListe = []

# 6 Lottozahlen aus 1 - 49
while len(LottoZahlenListe) < 7:
  LottoZahl = randint(1,49)
  
  # und die zufällig generierte Zahl nicht schon in der Liste steht
  if LottoZahl not in LottoZahlenListe:
    # die gnerierte Zahl an die Liste anhängen
    LottoZahlenListe.append(LottoZahl)

# Super Zahl generieren aus 0 - 9
SuperZahl = randint(0,9)
LottoZahlenListe.append(SuperZahl)

# Lotto Zahlen Liste ausgeben ###########
#
# Die ersten 6 Einträge in der Liste ausgeben
for i in range(0,6):
  print("LottoZahl ", i, ": ", LottoZahlenListe[i])
  i = i + 1

# SuperZahl Ausgeben
print("SuperZahl: ", LottoZahlenListe[7], "\n")
