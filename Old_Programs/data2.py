for a in range(9):
    if a < 6:
        print("I don't care")
    else: 
        print("I stil dont care")

#refresher on loops
colours = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
for colour in colours:
    print(colour)

new_col = [] #trying append with while 
i = 0
while colours[i] != 'm':
    new_col.append(colours[i])
    i += 1
print(new_col)

new_col2 = [] #trying the same with for
for i in colours:
    if(i != 'm'):
        new_col2.append(i)
print(new_col2)

for i, color in enumerate(colours): #trying out enumerate()
    print(i, color)
for i in range(len(colours)):
    colours[i] = 'white'
    print(colours)
print(colours)

#functions
def evenorOdd(num):
    '''documentation: evaluates whether the input is even or odd'''
    if num % 2 == 0:
        return 'even'
    else: 
        return 'odd'

print(evenorOdd(6), evenorOdd(79))
print(help(evenorOdd))

def useless(): #a function that does no work, returns None
    pass

#scope: local and global
#global variables accesible inside function
#local variables not accesible outside function
def globinLoc():
    global x #calling global var inside function
    x = 2

#Exeption Handling

try:
    int(input())
except ValueError:
    print("Don't input String!")
except TypeError:
    print("Wrong datatype")
except SyntaxError:
    print("Syntax error")
else:
    print("code executed Successfuly")