# 문서 N, 검색하고 싶은 단어 S를 입력받는다.
# print(input().count(input()))
N = " ".join(input().split())
S = " ".join(input().split())
count = 0
while len(N) >= len(S):
    try:
        startPoint = N.index(S)
        count += 1
        N = N[startPoint+len(S):]
    except:
        break
print(count)