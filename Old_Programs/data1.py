a1 = 2
a2 = 3
a1, a2 = a2, a1


#tuples
tup1 = (3, 1, 4, 1, 5, 9)
tup2 = (2, 7, 1, 8, 2, 8)
print(tup1[0] == tup1[-6])
print(type(tup1))
print(tup1 + tup2)
print(tup1[0:3]) #tuple slicing, last numeral needs to be 1 larger

#immutability of tuples
sortpi = sorted(tup1) #stdlib function sorted(), creates a new 'list' from the tuple
print(sortpi)

#nesting,you can even access characters!
tup3 = ((7, 13), ('something', 'nothing'), (True, False))
print(tup3[2], tup3[1][1][3], tup3[0][0])

#lists, similar to tuples, but mutable
list1 = [2, 3, 5, 7, [10, 20], 'hey', (49, 69)]
del(list1[2])
print(list1)

#aliasing changes the original list
list2 = list1
list2[2] = 4
print(list1)
#the solution? CLONING!!
list3 = list1[:]
list3[2] = 5
print(list1, '\n', list3)

#split method, to turn a str into a list
list4 = 'who cares'.split()
print(list4)
list5 = 'Who cares?, well, I do, I can\'t stand this'.split(',') #delimiter(inside parentheses) is space by default
print(list5)


#one clear distnction
print("tuples --> parentheses()")
print("Dictionaries --> Curly braces{}")
print("Lists --> square brackets[]")


#dictionaries start now

dict1 = {2:'me', 3:'you', 4:'him'}
print(dict1)
print(dict1[2]) #index value
dict1[5] = 'her' #add value to dict
print(dict1[5])
del(dict1[2])#delete an entry
print(dict1)
print(3 in dict1) #checks whether entry is in the dict
print(dict1.keys()) #get all the keys using the keys method


#sets - like list and tuples, but curly braces, takes away repetitions
set1 = {'I', 'you', 'him', 'her'}
print(set1)
set1.add("them")
set1.remove("I")
print(set1)

set_list = [3, 5, "here", "there", 3]
set2 = set(set_list) #turns the list into a set, removes repetition
print(set2)

#union and intersection
set3 = {1, 2, 5, 6, 8}
set4 = {1, 4, 5, 7, 9}
int_set = set3 & set4
#or
int_set = set3.intersection(set4)
print(int_set)
uni_set = set3.union(set4)
print(uni_set)
diff_set = set3.difference(set4)
print(diff_set)
#subset method
set5 = {1, 9}
print(set5.issubset(set3))
print(set5.issubset(set4))

#sorting something
listx = [0, 29, 32, 45]
sort_list = sorted(listx) #sorted function
listx.sort() #sort method
print(sort_list, "\t", listx)
