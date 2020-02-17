# import sys
# import copy
# # 마을 수 N, 트럭의 용량 C, 박스 정보의 개수 M을 입력받는다.
# N, C = map(int, sys.stdin.readline().split())
# M = int(input())
#
# # 박스의 정보 box 선언 후 입력받는다.
# box = []
# for i in range(M):
#     box.append(list(map(int, sys.stdin.readline().split())))
#
# # 받는 마을 기준 오름차순으로 정렬하고 보내는 마을 기준 오름차순으로 box 리스트를 정렬한다.
# box = sorted(box, key=lambda x: (x[1], x[0]))
# tBox, answer = [], 0
#
# # 트럭을 1번 마을부터 이동시키면서 박스를 받고 내린다.
# for i in range(N):
#     temp, k = len(tBox), 0
#     while temp:
#         if tBox[k][1] == i+1:
#             C += tBox[k][2]
#             del tBox[k]
#             k = 0
#         else:
#             k += 1
#         temp -= 1
#     temp, k = len(box), 0
#     while temp:
#         if C <= 0:
#             break
#         elif C-box[0][2] >= 0:
#             C -= box[0][2]
#             answer += box[0][2]
#             tBox.append(copy.deepcopy(box[k]))
#             del box[0]
#         elif C-box[0][2] < 0:
#             tBox.append(copy.deepcopy(box[k]))
#             tBox[-1][2] = C
#             answer += C
#             C = 0
#             del box[0]
#         temp -= 1
#
#     print("--{}--{}--".format(box, tBox))
# print(answer)
