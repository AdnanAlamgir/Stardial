testCases = int(input())

c = [0, 0, 0]
m = [0, 0, 0]
y = [0, 0, 0]
k = [0, 0, 0]

for l in range(testCases):
    for a in range(3):
        c[a], m[a], y[a], k[a] = input().split()
        c[a] = int(c[a])
        m[a] = int(m[a])
        y[a] = int(y[a])
        k[a] = int(k[a])
    
    c.sort()
    m.sort()
    y.sort()
    k.sort()
    sum = c[0] + m[0] + y[0] + k[0]
    if sum < 10 ** 6:
        print("Case #{}:".format(l + 1) + " IMPOSSIBLE")
    elif sum > 10 ** 6 and c[0] > 10 ** 6:
        print("Case #{}:".format(l + 1), 100000, 0, 0, 0)
    elif sum > 10 ** 6 and c[0] + m[0] > 10 ** 6:
        print("Case #{}:".format(l + 1), c[0], 1000000 - c[0], 0, 0)
    elif sum > 10 ** 6 and c[0] + m[0] + y[0] > 10 ** 6:
        print("Case #{}:".format(l + 1), c[0], m[0], 1000000 - (c[0] + m[0]), 0)
    else:
        print("Case #{}:".format(l + 1), c[0], m[0], y[0], 1000000 - (c[0] + m[0] + y[0]))
    

