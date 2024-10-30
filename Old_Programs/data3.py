#read and write files in python
#built in function 'open()'
#r for reading, w for writing, a for appeding
#cretes an object 'file1'
file1 = open("C:\\Users\\User\\Documents\\Rainmeter\\Skins\\Spectrum\\1.txt","r")
print(file1.name, file1.mode)
file1.close()

#using with (closes the file at the end of indent)
with open("C:\\Users\\User\\Documents\\Rainmeter\\Skins\\Spectrum\\1.txt","r") as file2:
    file_text = file2.read()
    file_first = file2.readline()
#print(file_text)
print(file_first)
print(file2.closed)

#edX lab
import urllib.request
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
filename = 'Example1.txt'
urllib.request.urlretrieve(url, filename)

exm1 = "example1.txt"
file3 = open(exm1, "r")
file_content = file3.read()
print(file_content, type(file_content))
file3.close

#better way (spoiler alert!)
#file.read() or any reading process operates in an order, no same characters are read twice
with open(exm1, "r") as file4:
    #fileCont = file4.read()
    #print(fileCont)
    print("1st line:" + file4.readline())
    print(file4.read(6))
    print(file4.read(9))
    print(file4.read(5))

#using loop to read all at once
with open(exm1, "r") as file5:
    for line in file5:
        print(line)
        print(type(line))
    
with open(exm1, "r") as file6:
    listFile = file6.readlines()
print(listFile[0])

#write and append
with open(exm1, "a") as file7:
    file7.write("\nThis is line 4")

file8 = open(exm1, "r")
print(file8.read())


    


