# 중간값 찾기
T = int(input())
temp = list(map(int, input().split()))
temp.sort()
print(temp[T//2])    