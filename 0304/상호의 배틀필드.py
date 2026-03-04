T = int(input())
for tc in range(1,1+T):
    H, W = map(int, input().split())
    matrix = [list(map(str, input())) for _ in range(H)]
    N = int(input())
    arr = list(input())

    d_dic = {'U':[1,0], 'D':[-1,0], 'L':[0,-1], 'R':[0,1]}
    for i in range(H):
        for j in range(W):
            if matrix[i][j] in '<>^v':
               pass 
               