from time import time
import numpy as np
import pandas as pd
import sys
import os

cards = []

for file in os.listdir("./data/binder"):
	if file.endswith(".csv") and "._" not in file:
		fname = "./data/binder/" + file
binder_df = pd.read_csv(fname, delimiter=';')
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

with open('./data/binder/core.txt', 'r') as f:
    core = f.read().split('\n')

finalCopy = []

for card in binder_df['Name']:
    finalCopy.append(card)

print("Checking target cards...")
for card in binder_df['Name']:
    for value in multiple:
        if card == value:
            finalCopy.remove(card)
            break

for card in binder_df['Name']:
    for value in core:
        if card == value:
            try:
                finalCopy.remove(card)
                break
            except:
                break

print("Cards to remove:")
for card in finalCopy:
    print("-> " + card)