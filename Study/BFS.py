"""
너비 우선 탐색 BFS
너비를 우선으로 하여 탐색
시작점에서 가까운 것부터 접근하는 방식
맹목적인 탐색을 할 때 사용하는 방법
최단 경로, 최단 길이를 구할 때 자주 사용
큐를 이용한다.
"""
import queue

# 지점의 개수 N 선언
N = 7

# 결과를 저장할 큐 변수 선언
# 방문 확인용 리스트 선언
result = queue.Queue()
check = [False for i in range(N)]

# 각 지점별 인접한 지점의 정보가 담긴 리스트 선언
# 리스트 내용 채우기
loc = [[] for i in range(N)]
loc[0].append(1)
loc[0].append(2)

loc[1].append(0)
loc[1].append(2)
loc[1].append(3)
loc[1].append(4)

loc[2].append(0)
loc[2].append(1)
loc[2].append(5)
loc[2].append(6)

loc[3].append(2)

loc[4].append(2)

loc[5].append(3)

loc[6].append(3)

# BFS 함수 선언 및 정의
def BFS(start):
    # 전역 변수 사용 설정
    global result, loc, check

    # 임시 저장 큐 변수 선언
    q = queue.Queue()

    # 시작 지점을 저장 후 해당 방문 리스트의 방문 값 설정
    q.put(start)
    check[start] = True

    # 현 지점을 기준으로 인접한 지점 모두 방문할 때 까지 반복
    while(not q.empty()):
        # 현 지점을 꺼내고 방문한 결과 큐에 저장
        x = q.get()
        result.put(x)
        # 현 지점과 인접한 지점의 개수 만큼 반복
        # 인접한 지점을 방문 했으면 넘어간다.
        # 방문을 안 했으면 임시 저장 큐에 해당 지점을 저장한다.
        # 현 지점이 끝나면 다음 인접지점으로 자연스럽게 넘어간다.
        # 그 후, 방문 리스트의 값을 설정한다.
        for i in range(len(loc[x])):
            y = loc[x][i]
            if not check[y]:
                q.put(y)
                check[y] = True

BFS(0)
for i in range(result.qsize()):
    print(result.get())
