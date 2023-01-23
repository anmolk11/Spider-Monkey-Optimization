import os
import pandas as pd

os.chdir("C:\\Users\\ADMIN\\Desktop\\smo")

df = pd.read_csv("diabetes.csv")

df.tail()

col = df.columns.tolist()
print(col)

def makeMonkey(args):
    monkey = {}
    
    i = 0
    
    for j in range(0,len(args),3):
        monkey[i] = args[j:j+3]
        i += 1
    
    return monkey

# spiderMonkey : args vector of 24 dimensions, sign : outcome (0 for positive and 1 for negative)
def fitness(spiderMonkey,sign):
    
    spiderMonkey = makeMonkey(spiderMonkey)
    
    hits = 0
    
    for i in range(0,df.shape[0]):
        ok = True
        for k,v in spiderMonkey.items():
            if v[0] == 1:
                if df.iloc[i][col[k]] < v[1] or df.iloc[i][col[k]] > v[2]:
                    ok = False
                    break
        if ok and df.iloc[i]["Outcome"] == sign:
            hits += 1

    return hits

#spiderMonkey = {
    #0 : [0,0,0],
    #1 : [1,81,106],
    #2 : [0,0,0],
    #3 : [1,12,85],
    #4 : [0,0,0],
    #5 : [0,0,0],
    #6 : [0,0,0],
    #7 : [0,0,0]
#}

argsVector = [0,0,0,1,81,106,0,0,0,1,12,85,0,0,0,0,0,0,0,0,0,0,0,0]

print(fitness(argsVector,0))
