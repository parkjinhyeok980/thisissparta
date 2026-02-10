T = int(input())                                    # 테스트 케이스 값을 입력 받는다
for tc in range(1, T+1):                            # 테스트 케이스 범위의 숫자를 tc에 할당한다
    num_lst = list(map(int, input().split()))       # 숫자 리스트 값을 입력받는다
    answer = 0                                      # answer 변수를 0으로 초기화 한다
    for i in num_lst:                               # 숫자 리스트 안의 숫자를 하나하나 불러온다
        if i % 2 == 1:                              # 하나하나 불러온 값이 홀수라면(나눠서 나머지가 1이라면)
            answer += i                             # answer 변수에 그 값을 더한다
    
    print(f'#{tc} {answer}')                        # 테스트 케이스 번호와 정답을 출력한다