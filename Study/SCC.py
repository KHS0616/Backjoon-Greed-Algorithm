line = []
line.append([4, 5])
line.append([1])
line.append([4])
line.append([3])
line.append([2])

# stack = [False for _ in range(len(line))]
id = [0 for _ in range(len(line))]
finished = [False for _ in range(len(line))]
scc = []
s = []
def dfs(x):
    global s, id, line, finished, scc
    # 각각의 노드에 아이디 할당
    id[x-1] = x
    
    # 스택에 자기 자신을 삽입
    s.append(x)
    #print(s)
    # 부모 설정
    parent = id[x-1]

    # 반복문을 돌면서 부모 값을 찾는다.
    # 방문 예정인 노드가 방문하지 않았을 경우, DFS실행 후 부모 설정
    # 방문 예정인 노드가 방문했을 경우, 최소가 되는 값을 부모로 설정
    # 최대로 하던 최소로 하던 SCC의 목적인 서로 왕래가 가능한 부모를 찾기위한 기준을 정하면된다
    for i in range(len(line[x-1])):
        y = line[x-1][i]
        if id[y-1] == 0:
            parent = min(parent, dfs(y))
        elif not finished[y-1]:
            parent = id[y-1]#min(parent, id[y-1])

    # 부모가 자신인 경우
    if parent == id[x-1]:
        temp_scc = []
        while(True):
            t = s.pop()
            #print("{}, {}".format(t, x))
            temp_scc.append(t)
            finished[t-1] = True
            if t == x:
                break
        scc.append(temp_scc)
    return parent

for i in range(1, 5+1, 1):
    if id[i-1] == 0:
        dfs(i)
print("SCC의 갯수 : {}".format(len(scc)))
for i in range(len(scc)):
    print("{}번째 SCC : {}".format(i, scc[i]))




# def dfs(x):    
#     if stack[x]:
#         return
#     stack[x] = True
#     print(x+1)
#     for i in range(len(line[x])):
#         y = line[x][i]-1
#         dfs(y)

# dfs(1)