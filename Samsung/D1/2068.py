# 최대수 구하기
T = int(input())
for test_case in range(1, T + 1):
    print("#{} {}".format(test_case, max(map(int, input().split()))))