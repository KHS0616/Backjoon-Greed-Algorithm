# 알파벳을 숫자로 변환
T, answer = input(), ""
for data in T:
    answer += "{} ".format(str(ord(data)-64))
print(answer.strip())