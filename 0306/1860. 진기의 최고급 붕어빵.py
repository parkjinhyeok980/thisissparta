T = int(input())
for tc in range(1,1+T):
    N, M, K = map(int,input().split())
    arr = list(map(int, input().split()))
    bread = 0
    state = 'Possible'

    for i in range(0, max(arr)+1):
        if i and i % M == 0:
            bread += K
        if i in arr:
            bread -= 1
        if bread < 0:
            state = 'Impossible'
            break

    print(f'#{tc} {state}')
