class Logger:
    def __init__(self):
        print("Object created")  
    
    def __del__(self):
        print("Object destroyed")

if __name__  == "__main__":
    log = Logger()
    del log            