# 숙제의 개수 N을 입력받는다.
N = int(input())

# 숙제의 데드라인과 컵라면 수를 담을 리스트 question 선언
# N개의 숙제 정보를 저장
question = []
for _ in range(N):
    question.append(list(map(int, input().split())))

# 데드라인이 적은 순으로 정렬 한다.
question.sort()

# 반복문을 통해 각 데드라인별 최대 값들을 구한다.
# 데드라인이 1인 경우 1개, 2인 경우 2개 등으로 점점늘어난다.
# 늘어나는 순서는 데드라인이 작은 것부터 큰 것 순으로
answer = []
for data in question:
    deadline = data[0]
    answer.append(data[1])

    # 데드라인과 요소의 개수를 비교하여 최소값부터 제거
    while deadline < len(answer):
        answer.remove(min(answer))

# 정답 출력
print(sum(answer))