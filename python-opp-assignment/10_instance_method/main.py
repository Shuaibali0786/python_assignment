class Dog:
    def __init__(self, name, breed):
        self.name = name # instance variable
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} is barking")

if __name__ == "__main__": 
    my_dog = Dog ("Tommy", "labrador")   
    my_dog.bark()
             