T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))          # 값 받기
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))

    if N >= M:                                      # S가 길이가 짧은 값, L이 긴 값이 되도록 맞춤
        L, S = Ai, Bj
    else:
        L, S = Bj, Ai

    max_product = 0                                 # 처음 값을 임의의 최댓값으로 할당함
    for i in range(len(S)):
        max_product += S[i]*L[i]

    for start in range(len(L) - len(S) + 1):        # 긴 거에서 짧은 걸 뺀다음 +1 한게 짧은 숫자열이 이동할 수 있는 범위
        cur = 0                                     # 현재 곱 값을 구하기 위한 변수 선언
        for i in range(len(S)):                     # 짧은 길이에서 같은 인덱스의 값끼리 곱하고 더함
            cur += S[i] * L[start + i]              # start가 for 문에 의해 한 칸씩 이동하므로(더해지므로) 모든 경우의 수의 곱 값 구하기 가능
        if cur > max_product:                       # 최댓값 구하는 알고리즘
            max_product = cur
 
    print(f'#{tc} {max_product}')                   # 출력