T = int(int(input()))
for tc in range(1,1+T):
    N = int(input())
    matrix = [list(map(str,input())) for _ in range(N)]

    di = [1,0,1,1]
    dj = [0,1,1,-1]

    answer = "NO"

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 'o':
                for d in range(4):
                    cnt = 1
                    ni, nj = i, j
                    for _ in range(4):
                        ni += di[d]
                        nj += dj[d]

                        if 0 <= ni < N and 0 <= nj < N and matrix[ni][nj] == 'o':
                            cnt += 1

                    if cnt == 5:
                        answer ="YES"
                        
    print(f'#{tc} {answer}')