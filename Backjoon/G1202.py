# import sys
# # 보석의 개수 N, 가방의 개수 K를 입력 받은 후 정수형으로 변환한다.
# N, K = map(int, sys.stdin.readline().split())
#
# # 각 보석의 무게와 각 가방의 최대 무게 제한을 MV, C에 입력받는다.
# MV = [sys.stdin.readline().split() for i in range(N)]
# for i in range(N):
#     MV[i] = list(map(int, MV[i]))
# MV.sort(key=lambda x:x[1])
# MV.reverse()
# C = [int(sys.stdin.readline()) for i in range(K)]
# C.sort()
#
# # 보석의 최대 가격 answer 변수 선언
# # 보석의 가격이 비싼 순서대로, 가방의 무게제한이 적은 순서대로 비교를 한다.
# # 조건에 일치하는 보석은 리스트에서 제외하고 가격을 더한다.
# # 계산 후 보석의 최대 가격 answer 을 출력한다.
# answer = 0
# while len(C) and len(MV):
#     for j in range(K):
#         if MV[0][0] < C[j]:
#             K -= 1
#             answer += MV[0][1]
#             del MV[0]
#             del C[j]
#             break
#         elif j == K-1:
#             del MV[0]
#             break
# print(answer)


