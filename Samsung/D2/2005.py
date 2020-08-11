T = int(input())
answer = []
for test_case in range(1, T + 1):
    temp = []
    for count in range(int(input())):
        index = 0
        if count == 0:
            temp.append([1])
        else:
            while index < count + 1:
                if index == 0:
                    temp.append([1])
                elif index == count:
                    temp[count].append(1)
                else:
                    temp[count].append(temp[count-1][index-1] + temp[count-1][index])
                index += 1
    print("#{}".format(test_case))
    for data in temp:
        for num in data:
            print(num, end=" ")
        print()