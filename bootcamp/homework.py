
class Library:
    def __init__(self,filename):
        self.filename = filename
        self.file = open(self.filename,"a+")
        print(f"File'{self.filename}' opened.")

    def __del__(self,filename):
        self.file.close()   
        print(f"File '{self.filename}' closed.")

    def add(self):
        title = input("Enter the book title: ")
        author = input("Enter the author: ")  
        release = input("Enter the release year: ")
        page = input("Enter the number of pages: ")

        book = f"{title},{author},{release},{page}\n"
        self.file.write(book)
        print(f"The book '{title}' added successfully.'")

    def remove(self):
        title = input("Enter the title of the book to remove: ")
        self.file.seek(0)
        books = self.file.readlines()

        updated_books = []
        
        found = False

        for book in books:
            if title in book:
                found = True
                print(f"Book '{title}' removed successfully.")
            else:
                updated_books.append(book)    
            
        if not found:
            print(f"Book '{title}' not found.") 

        self.file.seek(0)
        self.file.truncate()
        for book in updated_books:
            self.file.write(book)

    def list(self):
        self.file.seek(0)
        books = self.file.readlines()

        if books:
            print("List of Books:")
            for book in books:
                title, author, *_ = book.strip().split(",")
                print(f"Title: '{title}', Author: '{author}'")
        else:
            print("No books available.")     

if __name__ == "__main__":
    lib = Library("books.txt")      

    while True:
        print("***MENU***")
        print("1)List Books")
        print("2-)Add Book")
        print("3-)Remove Book")
        print("Press the button 'q' for quit.")

        x = input("Enter your choice (1-3) or q: ")
        
        if x == "1":
            lib.list()
        elif x == "2":
            lib.add()
        elif x == "3":
            lib.remove()
        elif x == "q":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please enter 1,2,3 or q.")

                 
            



          
        

 
