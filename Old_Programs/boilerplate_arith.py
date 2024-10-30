def arithmetic_arranger(problems):

    for i in range(len(problems)):
        count = 0
        for char in problems[i]:
            if char.isnumeric():
                print(char, end="")

            else:
                if char == '+' or char == '-':
                    print(char, end="  ")
                else:
                    count = count + 1
                    if count == 1:
                        print("\n")
                    else:
                        continue
        print("\n")
        print(f"{'-------'}")

set_1 = ['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380']
arithmetic_arranger(set_1)
