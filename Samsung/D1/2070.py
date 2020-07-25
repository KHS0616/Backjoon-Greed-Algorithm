# 큰 놈, 작은 놈, 같은 놈
T = int(input())
for test_case in range(1, T + 1):
    A, B = map(int, input().split())
    if A>B:
        print("#{} {}".format(test_case, ">"))
    elif A<B:
        print("#{} {}".format(test_case, "<"))
    else:
        print("#{} {}".format(test_case, "="))