testCases = int(input())

for l in range(testCases):
    N = int(input()) 

    S = [int(x) for x in input().split()]
    
    max = N
    S.sort()
    if S[len(S) - 1] < N:
        max = S[len(S) - 1]
    
    for k in range(3, max):
        iter = 0
        for j in S:
            if j > k:
                iter += 1
        if max - k > iter:
            max = k + iter
        else:
            continue
    print("Case #{}:".format(l + 1), max)

