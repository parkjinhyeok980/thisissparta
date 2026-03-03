T = int(input())
for tc in range(1,1+T):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]

    cnt_safty = 0

    di = [0,0,-1,1]
    dj = [1,-1,0,0]

    # 술래 위치 찾기
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
            # 술래 위치로부터 한 칸씩 퍼져나가며
                for d in range(4):
                    for step in range(1,N):
                        ni = i + di[d]*step
                        nj = j + dj[d]*step
                        # 범위 내에 있고 통로면 감시공간(3)으로 변경, 벽을 만나면 중단
                        if 0 <= ni < N and 0 <= nj < N:
                            if matrix[ni][nj] == 1:
                                break

                            elif matrix[ni][nj] == 0:
                                matrix[ni][nj] = 3
    # 안전한 공간 개수 출력
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 0:
                cnt_safty += 1

    print(f'#{tc} {cnt_safty}')