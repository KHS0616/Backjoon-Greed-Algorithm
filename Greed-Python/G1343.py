"""
민식이는 다음과 같은 폴리오미노 2개를 무한개만큼 가지고 있다. AAAA와 BB
이제 '.'와 'X'로 이루어진 보드판이 주어졌을 때,
민식이는 겹침없이 'X'를 모두 폴리오미노로 덮으려고 한다. 이때, '.'는 폴리오미노로 덮으면 안 된다.
폴리오미노로 모두 덮은 보드판을 출력하는 프로그램을 작성하시오.
"""

# 보드판을 입력받는다
# 입력받은 보드판을 리스트화 시킨다.
# 정답을 저장할 변수 answer 선언
B = list(input())
answer = ""
# 보드판 리스트를 순차적으로 탐색
# .일 경우 그대로 둔다.
# X일 경우 연속되는 X의 개수 측정
# 개수가 0개일 경우 기존에 . 있던 자리이므로 . 추가
# 개수가 홀수개일 경우 -1 출력
# 개수가 짝수개일 경우 4의 배수로 최대한 AAAA를 채운 후 남는경우 BB하나만 채우기
index = 0
while index <= len(B) -1:
    if B[index] == ".":
        answer += "."
        index += 1
    elif B[index] == "X":
        if index+3 <= len(B)-1 and B[index+1] == "X" and B[index+2] == "X" and B[index+3] == "X":
            answer += "AAAA"
            index += 4
        elif index+1 <= len(B)-1 and B[index+1] == "X":
            answer += "BB"
            index += 2
        else:
            answer = "-1"
            break
print(answer)