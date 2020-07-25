# 몫과 나머지 출력하기
T = int(input())
for i in range(T):
    P, K = map(int, input().split())
    print("#{} {} {}".format(i+1, P//K, P%K))