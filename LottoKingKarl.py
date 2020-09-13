# Name: Lotto King Karl Generator
# Written by: Daniel Toschlaeger, d.toschlaeger@gmail.com
# Date: 10.09.2020
# Description: Generate 7 unique numbers from 1-49
#================================
from math import *
from random import *
#================================
# Banner
print("\n###", "Lotto King Karl", "###")

# Eine Liste
LottoZahlenListe = []

# 6 Lottozahlen + Superzahl
while len(LottoZahlenListe) < 8:
  LottoZahl=randint(1,49)

  # und die zufällig generierte Zahl nicht schon in der Liste steht
  if LottoZahl not in LottoZahlenListe:
    # die gnerierte Zahl an die Liste anhängen
    LottoZahlenListe.append(LottoZahl)

# Lotto Zahlen Liste ausgeben
# Zähler Variable für die Ausgabe
i = 1

# Die ersten 6 Einträge in der Liste ausgeben
while i < 7:
  print("LottoZahl ", i, ": ", LottoZahlenListe[i])
  i = i + 1
