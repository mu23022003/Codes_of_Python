# #
# #
# # class Library:
# #     def __init__(self , list , name):
# #         self.bookList = list
# #         self.name = name
# #         self.lenDict = {}
# #
# #     def displayBooks(self):
# #         print(f"{self.name} , We have following books in our libraby")
# #         sno = 1
# #         for book in self.bookList:
# #             print(f"{sno} {book}")
# #
# #     def lendbook(self, book):
# #         if book in self.bookList:
# #             if book not in self.lenDict:
# #                 self.lendDict.update({book:self.name})
# #                 print("Lender-Book databse has been update. You can take the book now")
# #             else:
# #                 print(f"Book is already being used by {self.lendDict[book]}")
# #
# #     def addBook(self, book):
# #         self.bookList.append(book)
# #         print("Book has been added to the book list")
# #
# #     def returbBook(self, book):
# #         if book in self.bookList:
# #             if book in self.lendDict.keys():
# #                 self.lenDict.pop(book)
# #             else:
# #                 print(f"This book {book} is not use.")
# #         else:
# #             print(f"This book is not relate to our databse")
# #
# #
# # BinLibrary = Library(['Python ' , 'Java' , 'Data Science' , 'Data Mining' , 'C#'] , 'Ben')
# #
# # BinLibrary.__dict__()
# # print(BinLibrary.__dict__())
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# class Library:
#     def __init__(self, bookList, name):
#         self.bookList = bookList
#         self.name = name
#         self.lendDict = {}
#
#     def displayBooks(self):
#         print(f"{self.name}, We have the following books in our library:")
#         sno += 1
#         for book in self.bookList:
#             print(f"{sno} {book}")
#
#     def lendBook(self, book):
#         if book in self.bookList:
#             if book not in self.lendDict:
#                 self.lendDict.update({book: self.name})
#                 print("Lender-Book database has been updated. You can take the book now.")
#             else:
#                 print(f"The book is already being used by {self.lendDict[book]}.")
#
#     def addBook(self, book):
#         self.bookList.append(book)
#         print("The book has been added to the book list.")
#
#     def returnBook(self, book):
#         if book in self.bookList:
#             if book in self.lendDict.keys():
#                 self.lendDict.pop(book)
#             else:
#                 print(f"This book '{book}' is not borrowed.")
#         else:
#             print("This book is not in our database.")
#
#
# BinLibrary = Library(['Python', 'Java', 'Data Science', 'Data Mining', 'C#'], 'Ben')
#
# BinLibrary.displayBooks()  # Display the books in the library
# BinLibrary.lendBook('Python')  # Lend a book
# BinLibrary.addBook('JavaScript')  # Add a book to the library
# BinLibrary.returnBook('Python')# Return a book
#
#
# #BinLibrary.__dict__()
# #print(BinLibrary.__dict__())  # Print the dictionary representation of the BinLibrary instance
#
#
# print(BinLibrary.addBook('React Native')) #Adding book
# BinLibrary.displayBooks()



















class Library:
    def __init__(self, bookList, name):
        self.bookList = bookList
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"{self.name}, We have the following books in our library:")
        sno = 1  # Initialize sno to 1
        for book in self.bookList:
            print(f"{sno} {book}")
            sno += 1  # Increment sno for each book

    def lendBook(self, book):
        if book in self.bookList:
            if book not in self.lendDict:
                self.lendDict[book] = self.name  # Use square brackets to update lendDict
                print("Lender-Book database has been updated. You can take the book now.")
            else:
                print(f"The book '{book}' is already being used by {self.lendDict[book]}.")

    def addBook(self, book):
        self.bookList.append(book)
        print("The book has been added to the book list.")

    def returnBook(self, book):
        if book in self.bookList:
            if book in self.lendDict.keys():
                self.lendDict.pop(book)
            else:
                print(f"The book '{book}' is not borrowed.")
        else:
            print("This book is not in our database.")


BinLibrary = Library(['Python', 'Java', 'Data Science', 'Data Mining', 'C#'], 'Ben')

BinLibrary.displayBooks()  # Display the books in the library
BinLibrary.lendBook('Python')  # Lend a book
BinLibrary.addBook('JavaScript')  # Add a book to the library
BinLibrary.returnBook('Python')  # Return a book

BinLibrary.addBook('React Native')  # Adding a book
BinLibrary.displayBooks()
