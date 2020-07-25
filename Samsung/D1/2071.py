# 평균 값 구하기
T = int(input())
for test_case in range(1, T + 1):
    temp = list(map(int, input().split()))
    print("#{} {}".format(test_case, round(sum(temp)/len(temp))))