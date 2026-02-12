T = int(input())
for tc in range(1, T +1):
    N = input()

    current_num = []

    for i in range(1000000):
        current_num = list(map(int, i*N))
    
        num_lst = {}

        for i in current_num:
            if i not in num_lst:
                num_lst[i] = 1
            else:
                num_lst[i] += 1

        for j in num_lst:


            answer = 0

    print(f'#{tc} {answer}')