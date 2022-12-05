with open('day1.txt') as f:
    my_list = f.readlines()

#for x in my_list:
#    print(x)

numLines = len(my_list)
totalCalList = []
totalCals = 0
for x in range(0, numLines):
    if my_list[x] == '\n':
        totalCalList.append(totalCals)
        totalCals = 0
    else:
        #print(my_list[x] + ", " + str(len(my_list[x])))
        totalCals = totalCals + float(my_list[x])

mostCals = max(totalCalList)
print("MOST CALORIES: " + str(mostCals))

totalCalList.sort()
#for x in totalCalList:
#    print(x)

print("Top 3: " + str(totalCalList[-1]) + " , " + str(totalCalList[-2]) + ", and " + str(totalCalList[-3]))
top3total = totalCalList[-1] + totalCalList[-2] + totalCalList[-3]
print("Top 3 Total: " + str(top3total))