T = int(input())
for tc in range(1, T+1):
    N = input()
    lst = list(map(int, input().split()))

    num_lst = {}

    for i in lst:
        if i not in num_lst:
            num_lst[i] = 1
        else:
            num_lst[i] += 1

    max_fq = num_lst[0]
    answer = 0
    for j in num_lst:
        if num_lst[j] >= max_fq:
            max_fq = num_lst[j]
            answer = j
        
        elif num_lst[j] == max_fq:
            if j > answer:
                answer = j

    print(f'#{tc} {answer}')

