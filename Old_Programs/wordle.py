import string

let = list(string.ascii_lowercase)
words = []

let1 = ord(input('input one letter: ')) - 97
let2 = ord(input('input another letter: ')) - 97

exc_let = []
exclude = int(input('How many excluded letters?: '))
for i in range(exclude):
    exc_let.append(ord(input('excluded letter: ')) - 97)

for a in range(26):
    for b in range(25):
        for c in range(24):
            for d in range(23):
                for e in range(22):
                    if(a == let1 or b == let1 or c == let1 or d == let1 or e == let1):
                        if(a == let2 or b == let2 or c == let2 or d == let2 or e == let2):
                            for j in range(len(exc_let)):
                                if(a == exc_let[j] or b == exc_let[j] or c == exc_let[j] or d == exc_let[j] or e == exc_let[j]):
                                    break
                                else:
                                    words.append(let[a] + let[b] + let[c] + let[d] + let[e]) 
                            

print(len(words))


