from time import time
import numpy as np
import pandas as pd
import sys
import os
print("Choose a list of decks to continue:")
i = 1
for file in os.listdir("./data/decks"):
    if file.endswith(".csv"):
        fname = "./data/decks/" + file

        if "._" in fname:
            continue

        print("%d - %s" % (i, file.split(".csv")[0]))
        i += 1

decks = input("Enter the decks by their number separated by a '-': ")

list_decks = decks.split('-')

for deck in list_decks:
    if deck == '':
        print("Incorrect input form...")
        exit()

if len(list_decks) < 2:
    print("That is less than two decks...")
    exit()

i = 1
for file in os.listdir("./data/decks"):
    if file.endswith(".csv"):
        fname = "./data/decks/" + file
        if "._" in fname:
            continue
        if (int(list_decks[0]) == i):
            output_df = pd.read_csv(fname, delimiter=',', header=None)
            output_df.columns = ['Number', 'Name']
        i += 1

i = 1
for file in os.listdir("./data/decks"):
    if file.endswith(".csv"):
        fname = "./data/decks/" + file
        if "._" in fname:
            continue
        if (int(list_decks[1]) == i):
            deck_2_df = pd.read_csv(fname, delimiter=',', header=None)
            deck_2_df.columns = ['Number', 'Name']
        i += 1

merged_inner = pd.merge(left=output_df, right=deck_2_df, left_on='Name', right_on='Name')

if len(list_decks) > 2:
    deck = 2
    while deck < len(list_decks):
        if list_decks[deck] == '':
            break
        i = 1
        for file in os.listdir("./data/decks"):
            if file.endswith(".csv"):
                fname = "./data/decks/" + file
                if "._" in fname:
                    continue
                if (int(list_decks[deck]) == i):
                    deck_df = pd.read_csv(fname, delimiter=',', header=None)
                    deck_df.columns = ['Number', 'Name']
                    merged_inner = pd.merge(left=merged_inner, right=deck_df, left_on='Name', right_on='Name')
                i += 1
        deck+=1
        
with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', 1000):
    print(merged_inner[['Name']])

exit()
