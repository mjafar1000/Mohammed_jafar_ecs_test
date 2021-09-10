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

def createMedalTable(results):
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
    return nt


def test_function():
    #This it the test function, please don't change me
    medalTable = createMedalTable(medalResults)
    expectedTable = {
        "Italy": 4,
        "France": 4,
        "ROC": 4,
        "USA": 3,
        "Qatar": 3,
        "China": 3,
        "Germany": 2,
        "Brazil": 1,
        "Belarus": 1,
    }
    assert medalTable == expectedTable
    if medalTable == expectedTable:
        print("y")

test_function()
