T = int(input())

for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]          # 입력값 받기

    sum_value = 0                                               # 값의 합 구하기(마름모로 순회만 할 줄 알면 여태까지 하던 것과 같음)

    for i in range(N):                                          

        if i <= N//2:                                           # 행이 중앙보다 작거나 같을 때는 중앙을 기준으로 행 수 만큼 양쪽으로 범위 증가(중)
            for j in range((N//2)-i, (N//2)+i+1):
                sum_value += farm[i][j]

        if i > N//2:                                            # 행이 중앙보다 클 때에의 범위에 따라 감소
            for j in range(i-N//2, N - (i - N//2)):
                sum_value += farm[i][j]

    print(f'#{tc} {sum_value}')


