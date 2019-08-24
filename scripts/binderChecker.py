from time import time
import numpy as np
import pandas as pd
import sys
import os

cards = []

binder_df = pd.read_csv('./data/binder/Binder.csv', delimiter=';')
binder_df.dropna(inplace=True, subset=['Name'])
binder_df.drop(['Slot', 'Have'], axis=1, inplace=True)

output_df = pd.DataFrame(columns=['Name'])

for file in os.listdir("./data/decks"):
    if file.endswith(".csv"):
        fname = "./data/decks/" + file
        if "._" in fname:
            continue

        deck_df = pd.read_csv(fname, delimiter=',', header=None)
        deck_df.columns = ['Number', 'Name']
        deck_df.drop('Number', inplace=True, axis=1)

        output_df = pd.concat([output_df, deck_df])

print("Sorting cards by name...")
output_df.sort_values(by=['Name'], inplace=True)

for value in output_df['Name']:
    cards.append(value)

print("Counting cards...")
cardsDict = dict((card, cards.count(card)) for card in cards)

multiple = []
single = []

for card, count in cardsDict.items():
    if count > 1:
        multiple.append(card)
    else:
        single.append(card)

multiple.sort()
single.sort()

finalCopy = multiple.copy()

i=0
print("Checking target cards...")
for card in multiple:
    for value in binder_df['Name']:
        if card == value:
            finalCopy.remove(card)
            i+=1
            break

if ("Plains" in finalCopy):
    finalCopy.remove("Plains")
if ("Island" in finalCopy):
    finalCopy.remove("Island")
if ("Swamp" in finalCopy):
    finalCopy.remove("Swamp")
if ("Mountain" in finalCopy):
    finalCopy.remove("Mountain")
if ("Forest" in finalCopy):
    finalCopy.remove("Forest")

if ("Snow-Covered Plains" in finalCopy):
    finalCopy.remove("Snow-Covered Plains")
if ("Snow-Covered Island" in finalCopy):
    finalCopy.remove("Snow-Covered Island")
if ("Snow-Covered Swamp" in finalCopy):
    finalCopy.remove("Snow-Covered Swamp")
if ("Snow-Covered Mountain" in finalCopy):
    finalCopy.remove("Snow-Covered Mountain")
if ("Snow-Covered Forest" in finalCopy):
    finalCopy.remove("Snow-Covered Forest")

print("Cards to add:")
for card in finalCopy:
    print("-> " + card)