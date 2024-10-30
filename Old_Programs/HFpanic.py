phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

for i in range(4): plist.pop()

plist.pop(0)

plist.remove("'")

plist.extend([plist.pop(), plist.pop()])

plist.insert(2, plist.pop(3))

print(plist)

new_phrase = "".join(plist)
print(new_phrase)

##creating a function for it
def jon(list):
    new_phrase = ''
    for a in list: 
        new_phrase = str(new_phrase) + a
        if a not in list[len(list) - 1]: 
            new_phrase += '.'
    return new_phrase

print(jon(plist))