T = int(input())
for tc in range(1, 1+T):
    N, M = map(int,input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    di = [1, -1, 0, 0, 1, 1, -1, -1]
    dj = [0, 0, 1, -1, 1, -1, 1, -1]

    cnt_safty = 0

    for i in range(N):
        for j in range(M):

            cnt = 0
            for d in range(8):
                ni = i + di[d]
                nj = j + dj[d]

                if 0 <= ni < N and 0 <= nj < M:
                    if matrix[ni][nj] < matrix[i][j]:
                        cnt += 1

            if cnt >= 4:
                cnt_safty += 1


    print(f'#{tc} {cnt_safty}')

