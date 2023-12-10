import numpy as np

# f = open("test-text-1.txt")
f = open("text-1.txt")

# print(f.read())
cards = []
result = 0

times = f.readline().split(": ")[1].replace("\n", "").split(" ")
dists = f.readline().split(": ")[1].replace("\n", "").split(" ")

times = [elem for elem in times if elem != ""]
dists = [elem for elem in dists if elem != ""]

print(f"times: {times}")
print(f"dists: {dists}")

data = []
for i in range(len(times)):
    data.append([times[i], dists[i]])

print(f"data: {data}")

results = []

for elem in data:
    print(f"elem: {elem}")
    for waitTime in range(int(elem[0])):
        res = (float(elem[0]) - waitTime) * waitTime
        
        if res > float(elem[1]):
            result += 1
    results.append(result)
    result = 0
    print(results)
    

# for elemIndex in times:
#     for i in range(times[elemIndex] - 1):
        

#         if i < times[i]:
#             result += 1



# res = speed * time - waitTime



result = 1
for val in results:
    result *= val

print(f"result: {result}")



