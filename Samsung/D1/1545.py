# 거꾸로 출력해 보아요
T = int(input())
answer = ""
for i in range(T, -1, -1):
    answer += "{} ".format(str(i))
answer.strip()
print(answer)