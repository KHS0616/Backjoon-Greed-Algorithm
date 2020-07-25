# 더블더블
T = int(input())
answer = ""
for i in range(T+1):
    answer += "{} ".format(str(2**i))
answer.strip()
print(answer)