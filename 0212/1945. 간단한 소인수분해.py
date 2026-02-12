T = int(input())
for tc in range(1, T+1):
    N = int(input())

    prime_num = [2, 3, 5, 7, 11]                                            # 사용되는 소수 리스트 생성
    prime_dict = {}                                                         # 소수의 개수(지수)를 담을 딕셔너리 생성

    for i in prime_num:                                                     # 소수로 나눈 나머지가 0이 안나올 때까지 계속 나누기 
        while N % i == 0:                                                   
            N = N//i
            if i not in prime_dict:                                         # 나눈 나머지가 0이되면 그 소수를 딕셔너리에 추가
                prime_dict[i] = 1
            else:
                prime_dict[i] += 1

    answer = " ".join(str(prime_dict.get(p, 0)) for p in prime_num)         # 딕셔너리의 밸류 값을 문자열로 나열


    print(f'#{tc} {answer}')