from time import time
import numpy as np
import pandas as pd
import sys
import os
# import warnings
# warnings.filterwarnings("ignore")

if len(sys.argv) < 2:
    print("No argument")
else:
    if (sys.argv[1] == "decks"):
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
                    deck_df = pd.read_csv(fname, delimiter=',', header=None)
                    deck_df.columns = ['Number', 'Name']

                    for file in os.listdir("./data/binder"):
                    	if file.endswith(".csv") and "._" not in file:
                    		fname = "./data/binder/" + file
                    binder_df = pd.read_csv(fname, delimiter=';')
                    binder_df.dropna(inplace=True, subset=['Name'])

                    merged_inner = pd.merge(left=binder_df, right=deck_df, left_on='Name', right_on='Name')

                    with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', 1000):
                        print(merged_inner[['Slot', 'Name']])

                    exit()
                i += 1
        print("There is no deck with that number.")
    elif (sys.argv[1] == "single" or sys.argv[1] == "missing"):
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
                    deck_df = pd.read_csv(fname, delimiter=',', header=None)
                    deck_df.columns = ['Number', 'Name']
                    deck_df.drop('Number', inplace=True, axis=1)

                    if (sys.argv[1] == "single"):
                    	for file in os.listdir("./data/binder"):
                    		if file.endswith(".csv") and "._" not in file:
                    			fname = "./data/binder/" + file
                    	binder_df = pd.read_csv(fname, delimiter=';')
                    	binder_df.dropna(inplace=True, subset=['Name'])
                    	binder_df.drop(['Slot', 'Have'], inplace=True, axis=1)
                    	merged_inner = pd.merge(left=binder_df, right=deck_df, left_on='Name', right_on='Name')
                    elif (sys.argv[1] == "missing"):
                        for file in os.listdir("./data/collection"):
                            if file.endswith(".csv") and "._" not in file:
                                fname = "./data/collection/" + file
                        collection_df = pd.read_csv(fname, delimiter=',')
                        collection_df.drop(['Quantity', 'Edition Name', 'Edition Code'], inplace=True, axis=1)
                        merged_inner = pd.merge(left=collection_df, right=deck_df, left_on='Name', right_on='Name')

                    diff_df = deck_df[(~deck_df['Name'].isin(merged_inner['Name']))]
                    
                    diff_df = diff_df.sort_values(by=['Name'])

                    with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', 1000):
                        print(diff_df)

                    exit()
                i += 1
        print("There is no deck with that number.")
    elif (sys.argv[1] == "all"):
        output = open("./output/want_list.txt", 'w')
        output_df = pd.DataFrame(columns=['Name'])
        for file in os.listdir("./data/decks"):
            if file.endswith(".csv"):
                fname = "./data/decks/" + file
                if "._" in fname:
                    continue

                deck_df = pd.read_csv(fname, delimiter=',', header=None)
                deck_df.columns = ['Number', 'Name']
                deck_df.drop('Number', inplace=True, axis=1)

                for file in os.listdir("./data/collection"):
                    if file.endswith(".csv") and "._" not in file:
                        fname = "./data/collection/" + file
                collection_df = pd.read_csv(fname, delimiter=',')
                collection_df.drop(['Quantity', 'Edition Name', 'Edition Code'], inplace=True, axis=1)
                merged_inner = pd.merge(left=collection_df, right=deck_df, left_on='Name', right_on='Name')

                diff_df = deck_df[(~deck_df['Name'].isin(merged_inner['Name']))]

                output_df = pd.concat([output_df, diff_df])

        for file in os.listdir("./data/binder"):
        	if file.endswith(".csv") and "._" not in file:
        		fname = "./data/binder/" + file
        binder_df = pd.read_csv(fname, delimiter=';')
        binder_df = binder_df.dropna(subset=['Name'])
        binder_df['Have'] = binder_df['Have'].fillna("No")
        binder_df['Have'] = binder_df['Have'].astype(str)
        binder_df['Have'] = binder_df['Have'].replace(to_replace='1.0', value='Yes')
        dontHave_df = binder_df.loc[binder_df['Have'] == "No"]
        dontHave_df = dontHave_df.drop(['Slot', 'Have'], axis=1)
        output_df = pd.concat([output_df, dontHave_df])
        print("Taking out duplicates...")
        output_df = output_df.drop_duplicates(keep='first')
        print("Sorting cards by name...")
        output_df = output_df.sort_values(by=['Name'])
        for value in output_df['Name']:
            output.write(value + '\n')
        print("File is ready!")
        output.close()

