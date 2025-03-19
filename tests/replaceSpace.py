import os
from pandas import DataFrame
from pandas import read_csv

PATH = "maps.csv"

fileName = os.path.join(os.getcwd(), f"resources/{PATH}")
df = read_csv(fileName)

#repalce space with %20 in column[link]
df['link'] = df['link'].str.replace(" ", "%20")

#rewrite the file
df.to_csv(fileName, index=False)
print("Done")
