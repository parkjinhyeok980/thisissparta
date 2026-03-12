T= int(input())
for tc in range(1,1+T):
    N = int(input())
    matrix =[list(map(int, input().split())) for _ in range(N)]

    # 교차점의 개수는 시작점이 순서대로 있을 때 도착점 보다 작은 것들의 개수
    matrix.sort()
    cnt = 0

    for i in range(N):
        for j in range(i+1, N):
            if matrix[i][1] > matrix[j][1]:
                cnt += 1

    print(f'{tc} {cnt}')
        