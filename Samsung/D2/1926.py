T = int(input())
answer = ""
for test_case in range(1, T + 1):
    temp = ""
    for num in str(test_case):
        if int(num)%3 == 0 and int(num) != 0:
            temp += "-"
    if temp == "":
        answer += "{} ".format(test_case)
    else:
        answer += "{} ".format(temp)
print(answer[:-1])