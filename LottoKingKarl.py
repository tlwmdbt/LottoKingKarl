# Platform: Nspire Calculators
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

# Empty list
LottoZahlenListe = []

# 6 regular + 1 special number, all from within a range from 1 to 49
while len(LottoZahlenListe) < 8:
  LottoZahl=randint(1,49)

  # check if number already in list
  if LottoZahl not in LottoZahlenListe:
    # if not already in list append to it
    LottoZahlenListe.append(LottoZahl)

# Output generated numbers #########################################
#
# counter for display loop
i = 1

# Print the first 6 entries of the list
while i < 7:
  print("LottoZahl ", i, ": ", LottoZahlenListe[i])
  i = i + 1
  
  # print the SuperZahl
  print("SuperZahl: ", LottoZahlenListe[7], "\n")
