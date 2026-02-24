T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    di = [1,-1,0,0]
    dj = [0,0,-1,1]

    cnt_safty = 0

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                for d in range(4):
                    for step in range(N):
                        ni = i + di[d]*step
                        nj = j + dj[d]*step
                        if 0 <= ni < N and 0 <= nj < N:
                            if matrix[ni][nj] == 1:
                                break
                            if matrix[ni][nj] == 0: 
                                matrix[ni][nj] += 1

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 0:
                cnt_safty += 1

    print(f'#{tc} {cnt_safty}')
