import numpy as np

# f = open("test-text-2.txt")
f = open("text-1.txt")

# print(f.read())
cards = []
result = 0

id = 0
for l in f:
    id += 1
    data1,data2 = l.split(": ")[1].split(" | ")
    data1 = data1.replace("  "," ").replace("\n", "").split(" ")
    data2 = data2.replace("  "," ").replace("\n", "").split(" ")
    if data1[0] == "":
        data1 = data1[1:]
    if data2[0] == "":
        data2 = data2[1:]
    cards.append([data1, data2, id, 1])

# for card in cards:
#     print(card)

for card in cards:
    for i in range(card[3]):
        found = np.isin(card[0], card[1])
        counted = np.count_nonzero(found)
        for counts in range(card[2], card[2]+counted):
            cards[counts][3] += 1

for card in cards:
    # print(card)
    result += card[3]

print(result)
          


# dataDict = [[None][None]]


# print(f.readline())