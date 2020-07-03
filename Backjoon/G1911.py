# 올림을 사용하기 위해 math 모듈을 가져온다.
import math

# 웅덩이의 개수 N, 널빤지의 길이 L을 입력받는다.
N, L = map(int, input().split())

# 웅덩이의 정보 리스트 water를 입력받는다.
water = []
for _ in range(N):
    start, end = map(int, input().split())
    end = end - 1
    water.append([start, end])

# 웅덩이를 시작지점을 기준으로 오름차순으로 정렬한다.
water.sort(key=lambda x: (x[0], x[1]))
# 첫 번째 웅덩이를 시작지점을 널빤지의 시작지점으로 한다.
# 웅덩이의 간격을 구한 후 3으로 나누고 올림을 통해 필요한 널빤지 개수를 구한다.
# 널빤지 개수만큼 현재 널빤지의 시작지점을 옮긴다.
# 널빤지의 시작지점이 다음 웅덩이의 내부에 있는지, 끝까지 있는지에 따라 분기한다.
# 널빤지의 시작지점이 마지막 웅덩이의 끝 지점과 같거나 클때까지 반복한다.
answer = 0
startPoint = water[0][0]
while water[-1][1] > startPoint:
    if water[0][1] >= startPoint >= water[0][0]:
        pass
    elif water[0][0] > startPoint:
        startPoint = water[0][0]
    else:
        del water[0]
        if not len(water):
            break
        continue
    length = water[0][1] - startPoint + 1
    answer += math.ceil(length/L)
    startPoint += math.ceil(length/L) * L
    del water[0]
    if not len(water):
        break
print(answer)