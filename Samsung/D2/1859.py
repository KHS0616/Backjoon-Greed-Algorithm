T = int(input())
price = []
answer = []
for test_case in range(1, T + 1):
    input()
    price.append(list(map(int, input().split())))
for i in range(T):
    temp = 0
    max_num = price[i][-1]
    for k in range(len(price[i])-2, -1, -1):
        if max_num > price[i][k]:
            temp += (max_num - price[i][k])
        else:
            max_num = price[i][k]
    answer.append(temp)
    temp = 0
for i in range(T):
    print("#{} {}".format(i+1, answer[i]))