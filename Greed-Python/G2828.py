"""
상근이는 오락실에서 바구니를 옮기는 오래된 게임을 한다. 스크린은 N칸으로 나누어져 있다.
스크린의 아래쪽에는 M칸을 차지하는 바구니가 있다.
(M<N) 플레이어는 게임을 하는 중에 바구니를 왼쪽이나 오른쪽으로 이동할 수 있다.
하지만, 바구니는 스크린의 경계를 넘어가면 안 된다. 가장 처음에 바구니는 왼쪽 M칸을 차지하고 있다.
스크린의 위에서 사과 여러 개가 떨어진다.
각 사과는 N칸중 한 칸의 상단에서 떨어지기 시작하며, 스크린의 바닥에 닿을때까지 직선으로 떨어진다.
한 사과가 바닥에 닿는 즉시, 다른 사과가 떨어지기 시작한다.
바구니가 사과가 떨어지는 칸을 차지하고 있다면, 바구니는 그 사과가 바닥에 닿을 때, 사과를 담을 수 있다.
상근이는 사과를 모두 담으려고 한다. 이때, 바구니의 이동 거리의 최솟값을 구하는 프로그램을 작성하시오.
"""

# 스크린의 크기 N, 바구니의 크기 M을 입력받는다.
# 사과의 개수 A를 입력받고 각 사과의 떨어지는 위치를 apple 리스트에 입력받는다.
# 정답을 출력할 변수 answer 선언
# 사과가 떨어지는 위치를 인덱스로 변환하기 때문에 1을 빼주고 리스트에 저장한다.
N, M = map(int, input().split())
A = int(input())
apple = []
answer = 0
for i in range(A):
    apple.append(int(input())-1)

# 초기 바구니의 왼쪽 좌표 left, 오른쪽 좌표 right를 지정한다.
# 좌표(인덱스)를 지정하기 때문에 1을 빼준다.
left = 0
right = left + M - 1

# 사과의 개수만큼 사과를 받기위해 움직이는 반복문 실행
# 사과의 위치에 바구니의 범위가 들어가는 최소 움직임을 구한다.
# 움직인 후 바구니의 왼쪽, 오른쪽 좌표 수정 후 반복실행
for i in range(A):
    if apple[i] >= left and apple[i] <= right:
        continue
    elif apple[i] < left:
        answer += (left - apple[i])
        right -= (left - apple[i])
        left = apple[i]
    elif apple[i] > right:
        answer += (apple[i] - right)
        left += (apple[i] - right)
        right = apple[i]
print(answer)
