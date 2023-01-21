import os
import pandas as pd

os.chdir("C:\\Users\\ADMIN\\Desktop\\smo")

df = pd.read_csv("diabetes.csv")

df.tail()

col = df.columns.tolist()
print(col)

def fitness(spiderMonkey):
    hits = 0
    
    for i in range(0,df.shape[0]):
        ok = True
        for k,v in spiderMonkey.items():
            if v[0] == 1:
                if df.iloc[i][col[k]] < v[1] or df.iloc[i][col[k]] > v[2]:
                    ok = False
                    break
        if ok and df.iloc[i]["Outcome"] == 0:
            hits += 1

    return hits

spiderMonkey = {
    0 : [0,0,0],
    1 : [1,81,106],
    2 : [0,0,0],
    3 : [1,12,85],
    4 : [0,0,0],
    5 : [0,0,0],
    6 : [0,0,0],
    7 : [0,0,0]
}

print(fitness(spiderMonkey))
