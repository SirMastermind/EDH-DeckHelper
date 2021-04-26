import sys
import os
import pandas as pd

found = 0

wants_df = pd.read_csv("output/want_list.csv", delimiter = ';')

haves_df = pd.read_csv("data/haves/haves.csv", delimiter = ';')

haves_df = haves_df.drop_duplicates(keep='first')

output_df = pd.merge(wants_df, haves_df, on='card')

output_df.to_csv("output/wants_available.csv", index = False)