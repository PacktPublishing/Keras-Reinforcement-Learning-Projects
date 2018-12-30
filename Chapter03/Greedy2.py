P = 10
objects = [(5, 18),(2, 9), (4, 12), (6,25)]
print("Items available: ",objects)
print("***********************************")
objects = filter(lambda x: x[0]<=P, objects)
objects = sorted(objects, key=lambda x: x[1]/x[0], reverse=True)
weight, value, subset = 0, 0, []
print("Items filtered and sorted: ",objects)
print("***********************************")
for item in objects:
    if weight + item[0] <= P:
        weight = weight + item[0]
        value = value + item[1]
        subset.append(item)
print("Subset selected: ",subset)
print("Total value: " ,value)
print("Total weight: ",weight)
