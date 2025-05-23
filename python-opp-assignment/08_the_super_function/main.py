class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, sub):
        super().__init__(name)
        self.sub = sub   
    
    
    def display(self):
        print(f"Name:{self.name}\nSub:{self.sub}")

p = Teacher("Shuaib", "English")
p.display()            
             