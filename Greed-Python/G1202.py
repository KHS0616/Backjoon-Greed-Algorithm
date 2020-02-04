# 보석의 개수 N, 가방의 개수 K를 입력 받은 후 정수형으로 변환한다.
N, K = map(int,input().split())

# 각 보석의 무게와 각 가방의 최대 무게 제한을 MV, C에 입력받는다.
MV = [input().split() for i in range(N)]
for i in range(N):
    MV[i] = list(map(int,MV[i]))
MV.sort(key=lambda x:x[1])
MV.reverse()

C = [int(input()) for i in range(K)]
print("{}--{}".format(MV,C))