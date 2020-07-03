# A, B, C, D, E, F에 쓰여 있는 수가 주어진다.
# 지민이는 현재 동일한 주사위를 N^3개 가지고 있다.
# 이 주사위를 적절히 회전시키고 쌓아서, N*N*N 크기의 정육면체를 만들려고 한다.
# 이 정육면체는 탁자위에 있으므로, 5개의 면만 보인다.
# N과 주사위에 쓰여 있는 수가 주어질 때, 보이는 5개의 면에 쓰여 있는 수의 합의 최솟값을 출력하는 프로그램을 작성하시오.

# N, 주사위의 눈 6개를 입력받는다.
N = int(input())
dice = list(map(int, input().split()))
if N == 1:
    print(sum(dice)-max(dice))
else:
    answer = 0
    # 주사위의 눈이 1개만 보이는 경우 4(n-1)(n-2) + (n-2)**2
    # 주사위의 눈 중 최소값을 구한다.
    # 최소값은 찾기
    result = min(dice)
    answer = result * ((4*(N-1)*(N-2)) + ((N-2)*(N-2)))

    # 주사위의 눈이 2개만 보이는 경우 4(n-1) + 4(n-2)
    # 근접해있는 주사위의 눈 2개합의 최소값을 구한다.
    # 마주보는 면을 제외한 아무거나 2개 조합
    result = dice[0]+dice[1]
    for i in range(len(dice)):
        for j in range(i+1, len(dice)):
            if (i == 0 and j == 5) or (i == 1 and j == 4) or (i == 2 and j == 3):
                continue
            else:
                result = min(result, dice[i] + dice[j])
    answer = answer + (result*((4*(N-1)) + (4*(N-2))))

    # 주사위의 눈이 3개만 보이는 경우 4
    # 근접해있는 주사위의 눈 3개합의 최소값을 구한다.
    # 마주보는 면을 기준으로 2가지 경우로 분기하여 인접한 면의 2합의 최소값 계산
    result = dice[0] + dice[1] + dice[2]
    for i in range(2):
        if i == 0:
            temp = dice[0]
        else:
            temp = dice[5]
        result = min(result, dice[1] + dice[2] + temp, dice[1] + dice[3] + temp, dice[2] + dice[4] + temp, dice[3] + dice[4] + temp)
    answer += result*4
    print(answer)