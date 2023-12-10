import numpy as np

# f = open("aoc04TestText.txt")
f = open("aoc04Text.txt")

# print(f.read())
cards = []
result = 0

for l in f:
    data1,data2 = l.split(": ")[1].split(" | ")
    data1 = data1.replace("  "," ").replace("\n", "").split(" ")
    data2 = data2.replace("  "," ").replace("\n", "").split(" ")
    if data1[0] == "":
        data1 = data1[1:]
    if data2[0] == "":
        data2 = data2[1:]
    cards.append([data1,data2])

for card in cards:
    nix = np.isin(card[0], card[1])
    print(nix)
    counted = np.count_nonzero(nix)
    print(counted)
    if counted > 0:
        res = 1
        for i in range(counted-1):
            res *= 2
        result += res
    print(res)

print(result)
          


# dataDict = [[None][None]]


# print(f.readline())