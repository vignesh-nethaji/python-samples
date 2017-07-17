# Comparision Operator Overloading in Python
# Operator	Expression	Internally
# Less than	p1 < p2	p1.__lt__(p2)
# Less than or equal to	p1 <= p2	p1.__le__(p2)
# Equal to

# p1 == p2	p1.__eq__(p2)
# Not equal to	p1 != p2	p1.__ne__(p2)
# Greater than	p1 > p2	p1.__gt__(p2)
# Greater than or equal to	p1 >= p2	p1.__ge__(p2)

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    
    def __lt__(self,other):
        self_mag = (self.x ** 2) + (self.y ** 2)
        other_mag = (other.x ** 2) + (other.y ** 2)
        return self_mag < other_mag


p1 = Point(1,1)
p2 = Point(-2,-3)
print(p1 < p2)

p3 = Point(1,1)
p4 = Point(0.5,-0.2)
print(p3 < p4)

p5 = Point(1,1)
p6 = Point(1,1)
print(p5 < p6)