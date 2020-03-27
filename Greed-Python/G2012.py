import heapq

# 예상 등수를 적은 학생의 수 N을 입력받는다.
N = int(input())

# 예상 등수 리스트 rank를 선언한다.
# 학생의 수 만큼 예상 등수를 입력받는다.
# 최소 힙 형태로 입력받아 오름차순 형태로 정렬한다.
rank = []
for _ in range(N):
    heapq.heappush(rank,int(input()))
# 예상 등수 - (인덱스 번호 + 1)의 절대 값을 합해 불만도의 최소값을 구한다.
answer = 0
for i in range(1,N+1):
    answer += abs((heapq.heappop(rank) - i))
print(answer)