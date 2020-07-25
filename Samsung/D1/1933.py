# 간단한 N의 약수
T = int(input())
answer = ""
for i in range(1, T+1, 1):
    if T%i == 0:
        answer += "{} ".format(str(i))
answer.strip()
print(answer)