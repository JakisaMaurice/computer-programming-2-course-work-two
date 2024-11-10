# Part A: 
# 1.
"""this program is designed to greet the user and fetch their age
to best assess their year of birth """
name = input(f"Enter name: ") # allows the user enter their name into the program
greeting = print(f"Hello {name.upper()}, I hope you feel amazing.")#basic greeting to the user and .upper() makes the name capital
# greeting = print("Hello", name.upper(),",isn't it a beautiful morning?") 

while True: #allows to run a loop continuously till no error is found
  try: #allows the program try entries to catch errors if any are available
    age = int(input("How old are you?: ")) #allows age entry
    break #breaks the loop for age entry if value is correct
  except ValueError: #exception to grab any errors in entry of age
    print("Value error: invalid entry, enter valid number")

from datetime import datetime #allows the program get the datetime from the datetime module to be used
current_year = datetime.now().year # gets the current year which is 2024 from the system
year_of_birth = current_year - age #computes the year of birth 

print(f"You were born in, {year_of_birth}\n") #displays result of the year_of_birth

# Part B: Conditional Execution
# 1. Extended program: 
while True:
  try: 
    fav_number = int(input(f"What is your favorite number, {name.upper()}: "))
    print(f"{fav_number} is an amazing favorite number")
    if (fav_number % 2 == 0):
      print("and guess what, its an even number")
      if (fav_number > 10):
        print("its also greater than 10\n")
      elif (fav_number == 10):
        print("Did you know the number 10, is the base of the decimal system")
      elif (fav_number % 2 > 10):
        print("greater heights i see, result is greater than 10 when divided by 2 as well\n")
      else:
        print("but quite a low number\n")
    else:
      print("and guess what, its an odd number\n")
      break
    break
  except:
    print("Value error: invalid entry, enter valid number")


"""1. syntax error: used wrong syntax of using multiple else statements instead of using 
elif. 
Applied elif and defined parameters because using else multiple times displayed outputs of other else statements.
2. used a wrong variable name for fav_number which gave a TypeError: not all arguments converted during string formatting.
had to change the variable name used to fav_number to erase error"""

import time #allows us bring in the time module which provides functions for working with time 
while True: #an infinite loop that continues to execute as long as the condition remains true.
  question1 = input("Do you like reading?(yes/no): ") #inquiry to provide a user access to a library section of the program
  if question1.lower() == "yes": #if condition is "yes" the user is taken through the library 
    print("\nThere are some books available, hope you like them\n")
    time.sleep(2) #creates a delay in the program for 2 seconds
    
    class Book: 
      def __init__(self, title, author, year_published): #allows us initialize the class Book's attributes
        self.title = title
        self.author = author
        self.year_published = year_published
      def description(self): # method created to display book descriptions
            return f"{self.title} by {self.author}, published in {self.year_published}"

    """book1 = Book(input("enter title: "),input("enter author: "),input("enter year: "))
    book2 = Book(input("enter title: "),input("enter author: "),input("enter year: "))
    book3 = Book(input("enter title: "),input("enter author: "),input("enter year: "))"""

    book1 = Book("Oceans", "NatGeo", 1998)
    book2 = Book("Jungle Book","Rudyard Kipling",1894)
    book3 = Book("Harry Potter","J.K Rowling",1997)
    book4 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
    book5 = Book("Pride and Prejudice", "Jane Austen", 1813)
    book6 = Book("1984", "George Orwell", 1949)
    book7 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
    book8 = Book("Moby Dick", "Herman Melville", 1851)
    book9 = Book("The Catcher in the Rye", "J.D. Salinger", 1951)
    book10 = Book("The Hobbit", "J.R.R. Tolkien", 1937)

    """print(f"{book1.title} by {book1.author}, published in {book1.year_published}")
    print(f"{book2.title} by {book2.author}, published in {book2.year_published}")
    print(f"{book3.title} by {book3.author}, published in {book3.year_published}")"""
    for i, book in enumerate([book1,book2,book3,book4,book5,book6,book7,book8,book9,book10], start=1):
      #allows us number the books described in a list
      print(f"{i}. {book.description()}")

    print("\nPlease wait")
    print("Generating a list of available books sorted by year...")
    time.sleep(3) #creates a delay for 3 sends in the program at this point

    def sort_books_by_year(books): #function created to sort books by year published
        if not books: #checks if books list is empty
          print("the list is empty.")
        return sorted(books, key=lambda book:book.year_published) #used to display list in chronological order

    books = [book1, book2, book3, book4, book5, book6, book7, book8, book9, book10] #list of books
    # empty_list = []
    sorted_books = sort_books_by_year(books)

    # if (books == empty_list):
    #     print("no values in book list")

    while True:
        if books != []: #checks if books is not an empty list and runs the code below
            print("\nlist of sorted books".upper())
            for book in sorted_books:
              print(book.title, "by", book.author, "in", book.year_published)
        break
        
    # for books in sorted_books:
    #   print(books.title, "by", books.author, "in", books.year_published)

    def search_book_by_title(books, title): #function to search books by title 
      for book in books:
        if book.title.lower() == title.lower(): #allows te program fetch an entry whether in capital or lowercase
          print("\nBook found:")
          print(book.description()) #prints description of found book
          return
      print("\nBook not found.")

    while True:
      title_to_search = input("\nSearch book by title to check library or exit to end search: ") #allows user input book title
      if title_to_search.lower()== "exit": #if a user inputs exit then the search is exited
        print("Exiting the search.")
        time.sleep(2)
        print("Exiting the program")
        break
      search_book_by_title(books, title_to_search) #relates the title searched to available book title

    break    
  elif question1 == "no": #if reply is no when asked about reading it exits the rest of the program
   print("Exiting the program")
   break
   
 

# class Book:
#   def __init__(self, title, author, year_published):
#     self.title = title
#     self.author = author
#     self.year_published = year_published
#   def description(self):
#         print(f"{self.title} by {self.author}, published in {self.year_published}")

# """book1 = Book(input("enter title: "),input("enter author: "),input("enter year: "))
# book2 = Book(input("enter title: "),input("enter author: "),input("enter year: "))
# book3 = Book(input("enter title: "),input("enter author: "),input("enter year: "))"""

# book1 = Book("Oceans", "NatGeo", 1998)
# book2 = Book("Jungle Book","Rudyard Kipling",1894)
# book3 = Book("Harry Potter","J.K Rowling",1997)

# """print(f"{book1.title} by {book1.author}, published in {book1.year_published}")
# print(f"{book2.title} by {book2.author}, published in {book2.year_published}")
# print(f"{book3.title} by {book3.author}, published in {book3.year_published}")"""
# book1.description()
# book2.description()
# book3.description()

# def sort_books_by_year(books):
#     if not books:
#        print("the list is empty.")
#     return sorted(books, key=lambda book:book.year_published)

# books = [book1, book2, book3]
# # empty_list = []
# sorted_books = sort_books_by_year(books)

# # if (books == empty_list):
# #     print("no values in book list")

# while True:
#     if books != []:
#         print("\nlist of sorted books".upper())
#         for book in sorted_books:
#          print(book.title, "by", book.author, "in", book.year_published)
#     break
    
# # for books in sorted_books:
# #   print(books.title, "by", books.author, "in", books.year_published)

# def search_book_by_title(books, title):
#   for book in books:
#     if book.title.lower() == title.lower():
#       print("\nBook found:")
#       book.description()
#       return
#   print("\nBook not found.")

# while True:
#   title_to_search = input("\nSearch book by title to check library: ")
#   if title_to_search.lower()== "exit":
#     print("Exiting the search.")
#     break
#   search_book_by_title(books, title_to_search)