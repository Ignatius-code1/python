
class Shape:

    def __init__(self,name):
        self.name=name

    def describe(self):
        print (f"This shape is called {self.name}")


class Rectangle(Shape): 
    def __init__(self,length,width):
        super().__init__("Rectangle")
        self.length=length
        self.width=width


    def area(self):
        a=self.width * self.length
        print(f"The area of the rectangle is {a}")
        return a
    
    class Circle(Shape):
        def __init__(self, name):
            super().__init__(name)
            self.radius = 0