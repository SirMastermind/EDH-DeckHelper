from time import time
import numpy as np
import pandas as pd
import sys
import os
print("Choose a deck to continue:")
i = 1
for file in os.listdir("./data/decks"):
    if file.endswith(".csv"):
        fname = "./data/decks/" + file

        if "._" in fname:
            continue

        print("%d - %s" % (i, file.split(".csv")[0]))
        i += 1

deck_1 = input("Choose the first deck by number: ")

i = 1
for file in os.listdir("./data/decks"):
    if file.endswith(".csv"):
        fname = "./data/decks/" + file

        if "._" in fname:
            continue

        print("%d - %s" % (i, file.split(".csv")[0]))
        i += 1

deck_2 = input("Choose the second deck by number: ")

if int(deck_1) < 1 or int(deck_2) < 1:
    print("At least one of those decks doesn't exist.")
    exit()

i = 1
for file in os.listdir("./data/decks"):
    if file.endswith(".csv"):
        fname = "./data/decks/" + file
        if "._" in fname:
            continue
        if (int(deck_1) == i):
            deck_1_df = pd.read_csv(fname, delimiter=',', header=None)
            deck_1_df.columns = ['Number', 'Name']
        i += 1

i = 1
for file in os.listdir("./data/decks"):
    if file.endswith(".csv"):
        fname = "./data/decks/" + file
        if "._" in fname:
            continue
        if (int(deck_2) == i):
            deck_2_df = pd.read_csv(fname, delimiter=',', header=None)
            deck_2_df.columns = ['Number', 'Name']
        i += 1


merged_inner = pd.merge(left=deck_1_df, right=deck_2_df, left_on='Name', right_on='Name')

with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', 1000):
    print(merged_inner[['Name']])

exit()
