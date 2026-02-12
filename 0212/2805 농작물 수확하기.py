T = int(input())

for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]

    sum_value = 0

    for i in range(N):

        if i <= N//2:
            for j in range((N//2)-i, (N//2)+i+1):
                sum_value += farm[i][j]

        if i > N//2:
            for j in range(i-N//2, N - (i - N//2)):
                sum_value += farm[i][j]

    print(f'#{tc} {sum_value}')


