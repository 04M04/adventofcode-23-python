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


startPoses = [elem[0] for elem in positions if elem[0][2] == "A"]
for elem in startPoses:
    print(f"startPoses: {elem[2]}")

lastPaths = startPoses
print(all([False for elem in lastPaths if elem[2] == "Z"]))
while(all([False for elem in lastPaths if elem[2] == "Z"])):
    for dir in directions:
        # foundPaths = [pos for pos in positions if pos[0] == lastPaths]
        # print(foundPaths)
        for lastPath in lastPaths:
            # print(lastPaths)
            print(f"lastPath: {lastPath}")
            # print([elem for elem in positions if elem[2] == lastPath])
            foundCorner = [pos for pos in positions if pos[0] == lastPath][0]
            
            # print(f"newpath: {foundCorner}")
            if dir == "L":
                lastPath = foundCorner[0][1]
            else:
                lastPath = foundCorner[0][2]
        result += 1
        if all([False for el in lastPaths if el[2] == "Z"]):
            break
    
print(f"result: {result}")



