T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    for _ in range(M):
        i, j = map(int, input().split())
        mid = i - 1

        for step in range(1, j+1):
            left = mid - step
            right = mid + step

            if left < 0 or right >= N:
                break
            
            if arr[left] == arr[right]:
                arr[left] = 1 - arr[left]
                arr[right] = 1 - arr[right]

    print(f'#{tc}', *arr)