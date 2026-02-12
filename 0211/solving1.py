T = int(input())
for tc in range(1, T+1):
    N = input()
    lst = list(map(int, input().split()))       # 입력값 받기

    num_lst = {}                                # 번호의 개수를 매길 딕셔너리 생성

    for i in lst:                               # 번호를 한 번 볼 때마다 밸류 값에 +1 하기
        if i not in num_lst:
            num_lst[i] = 1
        else:
            num_lst[i] += 1

    max_fq = num_lst[0]                         # 최빈값(밸류가 가장 큰 값 구하기)
    answer = 0                                  # 밸류가 가장 큰 값의 키를 입력할 변수
    for j in num_lst:
        if num_lst[j] >= max_fq:
            max_fq = num_lst[j]
            answer = j
        
        elif num_lst[j] == max_fq:              # 빈도수가 같은 게 있을 때
            if j > answer:                      # 최빈값의 키보다 j의 수가 더 크면
                answer = j                      # 최빈값에 j를 할당한다

    print(f'#{tc} {answer}')

