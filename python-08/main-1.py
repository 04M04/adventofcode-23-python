import numpy as np

# f = open("test-text-1.txt")
f = open("text-1.txt")

# print(f.read())
result = 0

directions = f.readline().replace("\n", "")
positions = []

f.readline()
for l in f:
    # print(l)
    pos,data = l.split(" = ")
    left,right = data.replace("\n", "").replace("(", "").replace(")", "").split(", ")
    positions.append([pos,left,right])


lastPath = "AAA"
while(lastPath != "ZZZ"):
    for c in directions:
        foundElem = [elem for elem in positions if elem[0] == lastPath]
        # print(foundElem)
        if c == "L":
            lastPath = foundElem[0][1]
        else:
            lastPath = foundElem [0][2]
        result += 1
        if lastPath == "ZZZ":
            break


# for pos in positions:
#     print(pos)

    
print(f"result: {result}")



