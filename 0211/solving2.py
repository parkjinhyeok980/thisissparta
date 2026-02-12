T = int(input())
for tc in range(1, 1+T):
    N = int(input())                                                    # 입력값 받기
    arr = [[0]*10 for _ in range(10)]                                   # 10*10의 빈 2차원 배열 생성

    for _ in range(N):                                                  # 색칠하는 범위의 수 만큼 입력값을 받는다
        r1, c1, r2, c2, color = list(map(int, input().split()))

        for r in range(r1, r2+1):                                       # 범위 값에 컬러의 번호를 더한다
            for c in range(c1, c2+1):
                arr[r][c] += color

    answer = 0                                                          # 보라색(3)의 개수를 입력하기 위한 변수 선언

    for i in range(10):                                                 # 2차원 배열을 순회하면서 3을 찾을 때마다 개수에 1씩 더한다
        for j in range(10):
            if arr[i][j] == 3:
                answer += 1

    print(f'#{tc} {answer}')                                            # 결과를 출력한다

