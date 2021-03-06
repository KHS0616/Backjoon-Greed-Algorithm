"""
다솜이는 0과 1로만 이루어진 문자열 S를 가지고 있다.
다솜이는 이 문자열 S에 있는 모든 숫자를 전부 같게 만들려고 한다.
다솜이가 할 수 있는 행동은 S에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것이다. 뒤집는 것은 1을 0으로, 0을 1로 바꾸는 것을 의미한다.
예를 들어 S=0001100 일 때, 전체를 뒤집으면 1110011이 된다.
4번째 문자부터 5번째 문자까지 뒤집으면 1111111이 되어서 2번 만에 모두 같은 숫자로 만들 수 있다.
하지만, 처음부터 4번째 문자부터 5번째 문자까지 문자를 뒤집으면 한 번에 0000000이 되어서 1번 만에 모두 같은 숫자로 만들 수 있다.
문자열 S가 주어졌을 때, 다솜이가 해야하는 행동의 최소 횟수를 출력하시오.
"""

# 문자열 S를 입력받는다.
# S의 길이는 100만보다 작다.
S = input()

# S의 요소를 차례대로 비교한다.
# 이전과 다른 요소일 경우 0, 1인지 구분하여 뒤집는 회수를 추가한다.
# 마지막 요소 비교 후 뒤집는 회수가 적은 결과를 출력한다.

# S의 첫번째 요소 저장 후 뒤집는 횟수 초기화
# 첫번째 요소의 따른 뒤집는 횟수 추가
preNum = S[0:1]
zeroCount, oneCount = 0, 0
if preNum == "0":
    zeroCount += 1
else:
    oneCount += 1
    
# 문자열 요수 비교하는 반복문 실행
for n in S:
    if preNum == n:
        continue
    elif n == "0":
        zeroCount += 1
        preNum = n
    elif n == "1":
        oneCount += 1
        preNum = n
        
# 뒤집는 횟수가 적은 값 출력
print(min(zeroCount, oneCount))