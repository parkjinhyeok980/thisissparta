T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    Ci = list(map(int, input().split()))
    Ci.sort()
 
    cut_point = [] #자를 수 있는 구간(인덱스) 후보들
    for i in range(1, N):       
        if Ci[i] != Ci[i-1]:    # 숫자가 바뀌는 부분의 위치
            cut_point.append(i)
    cut_len = len(cut_point)
 
    if cut_len < 2:
        print(f'#{tc} -1')
        continue
 
    min_diff = 1000 #임의 값
    for i in range(cut_len-1):  #후보들 중에서 하나의 인덱스를 i로 정하고       
        for j in range(i+1, cut_len):   # i 다음부터 끝까지의 인덱스 하나를 j로 정한다
            s = Ci[0:cut_point[i]]      
            m = Ci[cut_point[i]:cut_point[j]] # cut_point[i], cut_point[j]도 다 인덱스
            l = Ci[cut_point[j]:N]
 
            max_ci = max(len(s), len(m), len(l))
            min_ci = min(len(s), len(m), len(l))
            diff = max_ci - min_ci
            if min_diff > diff:
                min_diff = diff
     
    print(f'#{tc} {min_diff}')