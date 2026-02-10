T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())                                            # 학생 수와 알고 싶은 학생 K를 입력받는다
    student_score = [list(map(int, input().split())) for _ in range(N)]         # 학생 성적 리스트를 2차원 배열로 받는다
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']        # 나중에 사용할 성적 리스트를 미리 만든다
    lst = []                                                                    # 비율을 반영한 최종 성적을 입력할 리스트를 만든다
    K_score = 0                                                                 # K 학생의 성적을 입력 받을 변수를 만든다
    for i in range(len(student_score)):                                         # i에 인덱스 번호(학생 번호)를 할당한다(인덱스 번호가 필요해서)
        s = student_score[i]                                                    # 각 학생의 성적 리스트를 s에 할당한다
        total_score = s[0]*0.35 + s[1]*0.45 + s[2]*0.2                          # 반영 비율 만큼 곱한 최종 성적을 구한다
        lst.append(total_score)                                                 # 최종 성적을 리스트에 추가한다

        if i == K-1:                                                            
            K_score = total_score                                               # K 학생의 성적은 따로 K_score 리스트에 저장한다

    lst.sort(reverse=True)                                                      # 최종 성적을 내림차순으로 정렬한다
    K_idx = lst.index(K_score)                                                  # K학생의 성적을 찾아서 인덱스 번호(순위)를 추출한다

    K_grade = grade[K_idx//(N//10)]                                             # 총 학생 수의 /10 만큼 제일 앞 인덱스에 할당되기 때문에,                 
                                                                                # N/10이 될 때마다 다음 성적(grade의 다음 인덱스)으로 넘어가도록 한다
    print(f'#{tc} {K_grade}')                                                   # 결과 출력