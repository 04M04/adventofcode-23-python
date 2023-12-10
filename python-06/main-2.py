import numpy as np

# f = open("test-text-1.txt")
f = open("text-1.txt")

# print(f.read())
cards = []
result = 0

time = f.readline().split(": ")[1].replace("\n", "").replace(" ", "")
dist = f.readline().split(": ")[1].replace("\n", "").replace(" ", "")



# times = [elem for elem in times if elem != ""]
# dists = [elem for elem in dists if elem != ""]

print(f"time: {time}")
print(f"dist: {dist}")

# data = []
# for i in range(len(times)):
#     data.append([times[i], dists[i]])

# print(f"data: {data}")

# results = []


for waitTime in range(int(time)):
    res = (float(time) - waitTime) * waitTime

    if res > float(dist):
        result += 1




print(f"result: {result}")



