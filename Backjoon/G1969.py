from collections import Counter

# DNA의 수 N 과 길이 M을 입력받은 후 정수형으로 변환 후 다시 저장한다.
N, M = map(int,input().split())
# DNA배열 초기화 후 DNA를 입력받는다.
dna = ["" for i in range(N)]
for i in range(N):
    dna[i] = input()

# DNA배열의 같은 위치의 문자를 임시 리스트에 저장 후 최빈수 문자를 구한다.
# 최빈수 문자를 구할 때 사전순으로 정렬을 한 후 문자를 구한다.
# 최빈수 문자로 이루어진 결과 DNA를 저장한다.
cDna = []
tDna = ["" for i in range(N)]
for i in range(M):
    for j in range(N):
        tDna[j] = dna[j][i]
    tDna.sort()
    c = Counter(tDna)
    mode = c.most_common()
    cDna.append(mode[0][0])

#결과 DNA 최종 저장
rDna = "".join(cDna)

#결과 DNA와 입력받은 각 DNA 사이의 Haming Distance 의 합 계산
hd = 0
for i in range(N):
    for j in range(M):
        if not dna[i][j] == rDna[j]:
            hd += 1
        else:
            pass
print("{}\n{}\n".format(rDna,hd))