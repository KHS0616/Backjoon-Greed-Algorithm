T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    temp = []
    ttemp = []
    for i in range(N):
        row = list(map(int, input().split()))
        temp.append(row)
    for x in range(N-M+1):
        for y in range(N-M+1):
            data = 0
            for count in range(M):
                data += sum(temp[x+count][y:M+y])
            ttemp.append(data)
    print("#{} {}".format(test_case, max(ttemp)))