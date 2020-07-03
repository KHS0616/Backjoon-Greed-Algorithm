# 테스트 케이스 T를 입력받는다.
T = int(input())
for k in range(T):
    # 책의 개수 N, 학생의 수 M 을 입력받는다.
    # book 변수에 줄 수 있는 책을 True 표기한다.
    # 학생들이 원하는 정수를 입력받고 num 리스트에 저장한다.
    N, M = map(int, input().split())
    book = [True for _ in range(N)]
    num = []
    count = 0
    for i in range(M):
        num.append(list(map(int, input().split())))

    # num 리스트를 마지막 수 기준 오름차순, 첫번째 수 기준 오름차순으로 정렬한다.
    # 정렬된 num 리스트의 범주 내에서 책이 True 일 때 첫번 째 책을 False 로 변경한다.
    # 변경 후 책을 준 학생 수 +1 을 해준 후 전부 반복하고 결과를 출력한다.
    num = sorted(num, key=lambda x: (x[1], x[0]))
    for i in range(M):
        temp = book[num[i][0]-1:num[i][1]]
        if temp.count(True) >= 1:
            for j in range(num[i][0]-1, num[i][1]):
                if book[j]:
                    book[j] = False
                    count += 1
                    break
    print(count)
