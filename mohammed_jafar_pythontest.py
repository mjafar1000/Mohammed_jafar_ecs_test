medalResults = [
    {
        "sport": "cycling",
        "podium": ["1.China", "2.Germany", "3.ROC"]
    },
    {
        "sport": "fencing",
        "podium": ["1.ROC", "2.France", "3.Italy"]
    },
    {
        "sport": "high jump",
        "podium": ["1.Italy", "1.Qatar", "3.Belarus"]
    },
    {
        "sport": "swimming",
        "podium": ["1.USA", "2.France", "3.Brazil"]
    }
]



firstlist = []
secondlist = []
thirdlist = []

for x in medalResults[0:]:
    
    for p in x["podium"]:
        if "1" in p:
            firstlist.append(p)

        elif "2" in p:
            secondlist.append(p)
        else:
            thirdlist.append(p)          

table = (firstlist,secondlist,thirdlist)

nt = {}

for country in table[0]:
    if country[2:] in nt:
        nt[(country[2:])] += 3
    else:
        nt[(country[2:])] = 3
        
for country in table[1]:
    if country[2:] in nt:
        nt[(country[2:])] += 2
    else:
        nt[(country[2:])] = 2

for country in table[2]:
    if country[2:] in nt:
        nt[(country[2:])] += 1
    else:
        nt[(country[2:])] = 1


data_sorted = {k: v for k, v in sorted(nt.items(), key=lambda x: x[1], reverse = True)}
print("{" + "\n".join("{!r}: {!r},".format(k, v) for k, v in data_sorted.items()) + "}")


