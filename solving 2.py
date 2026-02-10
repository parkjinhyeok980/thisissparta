T = int(input())                                    # 테스트 케이스 값을 입력 받는다
for tc in range(1, T+1):                            # 테스트 케이스 번호를 tc에 할당한다
    num_lst = list(map(int, input().split()))       # 숫자 리스트를 입력받는다
    num_sum = 0                                     # 숫자 리스트의 합 변수를 0으로 초기화한다
    cnt = 0                                         # 숫자 리스트의 개수를 0으로 초기화한다
    for i in num_lst:                               # 숫자 리스트의 숫자를 하나하나 살펴서
        num_sum += i                                # 값을 num_sum에 더하고
        cnt += 1                                    # 순회할 때마다 1씩 더해서 총 개수를 구한다

    print(f'#{tc} {int(round(num_sum/cnt,0))}')     # 평균 값을 소숫점 첫째자리에서 반올림 한 후 정수형태로 변환해서 출력한다