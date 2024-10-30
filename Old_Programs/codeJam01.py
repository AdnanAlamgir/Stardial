testCases = int(input())
R = []
C = []
for l in range(testCases):
    r, c = input().split()

    R.append(int(r))
    C.append(int(c))


for k in range(testCases):
    print("Case #{}:".format(k + 1))

    for i in range(R[k] * 2 + 1):
        if i == 0:
            print("..", end="")
            for j in range(C[k] * 2 - 1):
                if j % 2 == 0:
                    print("+", end="")
                else:
                    print("-", end="")
            print("\n")
        
        elif i == 1:
            print("..", end="")
            for j in range(C[k] * 2 - 1):
                if j % 2 == 0:
                    print("|", end="")
                else:
                    print(".", end="")
            print("\n")
        
        elif i % 2 == 0:
            for j in range(C[k] * 2 + 1):
                if j % 2 == 0:
                    print("+", end="")
                else:
                    print("-", end="")
            print("\n")
        else:
            for j in range(C[k] * 2 + 1):
                if j % 2 == 0:
                    print("|", end="")
                else:
                    print(".", end="")
            print("\n")