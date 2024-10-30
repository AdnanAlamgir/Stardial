#data types are objects? 
#that's it?
#how can that be so easy??
#and why use such a fancy name anyway
#this is absolutely ridiculous
#this file is for a few methods only

listA = [23, 32, 15, 65, 37, 24, 94, 57, 69, 22, 38]
listA.sort()
print(listA)
listA.reverse()
print(listA)

#creating a class
class circle(object):
    def __init__(self, radius, color):
        self.radius = radius;
        self.color = color;
    

#creating an object of the class
red_circle = circle(10, "red") #class(attributes)
#getting values out
print(red_circle.radius)

class ellipse(object):
    def __init__(self, a, b, colour):
        self.a = a;
        self.b = b;
        self.colour = colour;
    #Now, creating a method
    def squishy(self, a2):
        self.a = self.a + a2



