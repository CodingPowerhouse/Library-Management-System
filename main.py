class Library:
    def __init__(self, listOfBooks):
        self.listOfBooks = listOfBooks
    
    def displayAvailableBooks(self):
        print()
        print("The books available in the library are:")
        print()
        for book in self.listOfBooks:
            print(f"**** {book}")

    def borrowBook(self, bookName):
        if bookName in self.listOfBooks:
            print(f"You have been issued {bookName}. Please keep it safe and return it within 30 days")
            self.listOfBooks.remove(bookName)
        else:
            print(f"Sorry, We don't have {bookName} in our library or someone borrowed that book")
    
    def returnBook(self, bookName):
        print(f"Thanks for returning {bookName}. Hope you have an amazing day!")
        self.listOfBooks.append(bookName)


class Student:
    def requestBook(self):
        bookName = input("Enter the name of the book you want to borrow:    ")
        return bookName

    def returnBook(self):
        bookName = input("Enter the name of the book you want to return:    ")
        return bookName

library1 = Library(["Python For Begginers", "HTML For Nerds", "C++ In One Week"])
while True:
    welcomeMsg = '''
    
    
    Welcome To Dhaka Central Library
    Select an option from this
    1. List all the books
    2. Borrow a book
    3. Add/Return a book
    4. Exit the library


    '''
    student = Student()
    print(welcomeMsg)
    option = input("Please select an option:    ")
    option = int(option)
    if option == 1:
        library1.displayAvailableBooks()
    elif option == 2:
        library1.borrowBook(student.requestBook())
    elif option == 3:
        library1.returnBook(student.returnBook())
    elif option == 4:
        break
