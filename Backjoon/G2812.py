import sys
N, K = map(int, sys.stdin.readline().split())
num = input()
answer = ""
while K:
    if len(num) == K:
        break
    m = int(num[0:1])
    temp = 0
    for i in range(K):
        if i+1 == K:
            break
        elif m < int(num[i + 1]):
            temp = i + 1
            m = int(num[i + 1])
    K -= temp
    answer += num[temp:temp + 1]
    num = num[temp + 1:]
print(answer)
