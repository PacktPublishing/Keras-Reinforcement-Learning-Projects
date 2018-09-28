import itertools

objects = [(5, 18),(2, 9), (4, 12), (6,25)]

print("Items available: ",objects)
print("***********************************")

AllCombination = [comb for k in range(0, len(objects)+1) for comb in itertools.combinations(objects, k)]

print("All combination: ")
for x in range(len(AllCombination)):
    print(AllCombination[x]),

print("***********************************")        
def ConditionControl(Subset):    
    totweight = totvalue = 0
    for weight, value in Subset:
        totweight  += weight
        totvalue += value
    return (totvalue, totweight) if totweight <= 10 else (0, 0)
 


Subset = max(AllCombination, key=ConditionControl)
print("Subset selected: ",Subset)

value, weight = ConditionControl(Subset)
print("Total value: " ,value)
print("Total weight: ",weight)


