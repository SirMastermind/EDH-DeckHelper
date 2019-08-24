from time import time
import numpy as np
import pandas as pd
import sys
import os

if len(sys.argv) < 2:
    print("No argument")
else:
    if (sys.argv[1] == "collection"):
    	for file in os.listdir("./data/collection"):
    		if file.endswith(".csv") and "._" not in file:
    			fname = "./data/collection/" + file
    	collection_df = pd.read_csv(fname, delimiter=',')
    	collection_df = collection_df.sort_values(by=['Name'])
    	with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', 1000):
    		print(collection_df)
    	print("\n\nTotal number of different cards is %s" % (len(collection_df.index)))
    	print("\nTotal number of cards is %s" % (collection_df['Quantity'].sum()))

    elif (sys.argv[1] == "binder" or sys.argv[1] == "have" or sys.argv[1] == "miss"):
    	binder_df = pd.read_csv('./data/binder/Binder.csv', delimiter=';')
    	binder_df.dropna(inplace=True, subset=['Name'])
    	binder_df['Have'].fillna("No", inplace=True)
    	binder_df['Have'] = binder_df['Have'].astype(str)
    	binder_df['Have'].replace(to_replace='1.0', value='Yes', inplace=True)
    	binder_df = binder_df.sort_values(by=['Name'])
    	with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', 1000):
    		if(sys.argv[1] == "binder"):
    			print(binder_df)
    		elif (sys.argv[1] == "have"):
    			print(binder_df[binder_df['Have'] == "Yes"])
    		elif (sys.argv[1] == "miss"):
    			print(binder_df[binder_df['Have'] == "No"])

    elif (sys.argv[1] == "decks"):
    	print("Choose a deck to continue:")
    	i = 1
    	for file in os.listdir("./data/decks"):
    		if file.endswith(".csv"):
    			fname = "./data/decks/" + file

    			if "._" in fname:
        			continue

    			print("%d - %s" % (i, file.split(".csv")[0]))
    			i += 1

    	txt = input("Choose the deck by number: ")

    	i = 1
    	for file in os.listdir("./data/decks"):
    		if file.endswith(".csv"):
    			fname = "./data/decks/" + file
    			if "._" in fname:
    				continue
    			if (int(txt) == i):
    				deck_df = pd.read_csv(fname, delimiter=',')
    				with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', 1000):
    					print(deck_df)
    				exit()
    			i += 1
    	print("There is no deck with that number.")
