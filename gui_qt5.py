import pandas as pd
from PIL import Image
from random import *
from os import system

path = "artists.csv"
data = pd.read_csv(path)

while True:
    sp = data.iloc[randint(0, len(data[list(data.columns)]))]

    print(sp['NameOfArt'])
    
    system("start " + sp['PicturePath'])

    variants = dict(zip(["A", "B", "C"], [sp['TrueArt'], sp['False1Art'], sp['False2Art']]))
    
    valuess = list(variants.values())
    shuffle(valuess)

    keyss = variants.keys()

    variants = dict(zip(keyss, valuess))
    print(f"A.{variants['A']}  B.{variants['B']}  C.{variants['C']}")

    print("True") if variants[input()] == sp['TrueArt'] else print("False")