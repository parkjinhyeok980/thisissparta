T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    for _ in range(M):
        i, j = map(int, input().split())
        end = min(N, i-1+j)

        for k in range(i-1, end):
            arr[k] = arr[i-1]

    print(f'#{tc}', *arr)
