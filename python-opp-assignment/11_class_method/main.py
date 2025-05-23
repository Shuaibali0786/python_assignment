class Book:
    totoal_book = 0 # class variable
    
    @classmethod
    def increment_book_count(cls):
        cls.totoal_book +=1
        
 
if __name__ == "__main__":
    Book.increment_book_count()
    Book.increment_book_count()
    Book.increment_book_count()
    Book.increment_book_count()

    
    print(f"Total books: {Book.totoal_book}")        