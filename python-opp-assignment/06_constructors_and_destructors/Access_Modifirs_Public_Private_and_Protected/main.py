class Emloyee:
    def __init__(self, name, salary, ssn):
        self.name = name # Public variable
        self._salary = salary # Protected variabale
        self.__ssn = ssn # Private variable
        
if __name__ == "__main__":
    exm = Emloyee("Shuaib", 30000, "234-44-5454")
    print(f"Public:{exm.name}")
    print(f"Protected:{exm._salary}")
    try:
        print(f"Private:{exm.__ssn}")
    except AttributeError:
        print("Cannot Variable name")    
    

    
      