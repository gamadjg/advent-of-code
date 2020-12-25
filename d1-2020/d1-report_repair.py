'''
Open the input data and convert to sorted int list. 

Part 1: Subtract n from 2020 and see if the result exists within the rest of the list. 

Part 2: Iterate through list[n]+list[n+1]+list[n+2] until we find the combination that reaches 2020
'''

def get_sorted_list():
    dataList = []

    with open("d1-2020\puzzle_input.txt", "r") as f:
        dataList = [line.strip() for line in f]
        dataList = list(map(int, dataList))
        dataList.sort()
    return dataList

def part_1(dataList):
    for entry in range(len(dataList)):
        lookFor = 2020-dataList[entry]
        if lookFor in dataList:
            print("Original entry: "+ str(dataList[entry]))
            print("2nd entry found: "+ str(lookFor))
            return dataList[entry]*lookFor

def part_2(dataList):
    for a in range(len(dataList)):
        for b in range(a+1, len(dataList)):
            for c in range(b+1, len(dataList)):
                if dataList[a]+ dataList[b]+ dataList[c] > 2020:
                    break
                elif dataList[a]+ dataList[b]+ dataList[c] < 2020:
                    break
                else:
                    print(dataList[a], dataList[b], dataList[c])
                    return dataList[a]* dataList[b]*dataList[c]


dataList = get_sorted_list()

result_1 = part_1(dataList)
print("Part 1 result: "+ str(result_1))

result_2= part_2(dataList)
print("Part 2 result: "+ str(result_2))
