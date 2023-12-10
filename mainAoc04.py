f = open("aoc04TestText.txt")

# print(f.read())
cards = []

for l in f:
    data1,data2 = l.split(": ")[1].split(" | ")
    data1 = data1.replace("  "," ").replace("\n", "").split(" ")
    data2 = data2.replace("  "," ").replace("\n", "").split(" ")
    if data1[0] == "":
        data1 = data1[1:]
    if data2[0] == "":
        data2 = data2[1:]
    cards.append([data1,data2])

for elem in cards:
    print(elem)


# dataDict = [[None][None]]


# print(f.readline())