#Defining Class and Methods
class book:

    def __init__(self, title, author, publication_year):
        self.__title = title
        self.__author = author
        self.__publication_year = publication_year
        self.__is_available = True

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_publication_year(self):
        return self.__publication_year

    def is_book_available(self):
        return self.__is_available

    def borrow_book(self):
        self.__is_available = False

    def return_book(self):
        self.__is_available = True

library = []

#Adding Books into the Library
i = 0
addAnother = "a"
while i == 0:
    Title = input("Enter Title ")
    Author = input("Enter Author ")
    Year = int(input("Enter Publication Year "))
    temp = book(Title,Author,Year)
    library.append(temp)
    print("")
        
    while addAnother != "n" or addAnother != "y" or addAnother != "Y" or addAnother != "N":
        addAnother = input("Do you want to add another book? (y/n) ")
        addAnother.lower()

        if addAnother == "y" or addAnother == "Y" or addAnother == "n" or addAnother == "N":
            break
        else:
            print("invalid input, y or n only")
            print("")

    if addAnother == "n" or addAnother == "N":
        break


print("")
#Borrowing Books
while i == 0:
    #Display Available Books
    print("Books in Library: ")
    for x in range(len(library)):
        if library[x].is_book_available() == True:
            print("Title:",library[x].get_title(),"Author:",library[x].get_author(),"Publication Year:",library[x].get_publication_year(),
                  "Index:",x,sep=" ")
        else:
            continue
    print("")
    
    Borrow=int(input("Enter the index of the book you want to borrow "))
    print("")

    
    if library[Borrow].is_book_available() == True:
        library[Borrow].borrow_book()
        print(library[Borrow].get_title(), "by author", library[Borrow].get_author(), "has been successfully borrowed", sep=" ")
        print("")
    else:
        print(library[Borrow].get_title(), "by author", library[Borrow].get_author(), "is not available at the moment", sep=" ")
        print("")
    
    while addAnother != "n" or addAnother != "y" or addAnother != "Y" or addAnother != "N":
        addAnother = input("Do you want to borrow another book? (y/n) ")
        addAnother.lower()
        print("")

        if addAnother == "y" or addAnother == "Y" or addAnother == "n" or addAnother == "N":
            break
        else:
            print("invalid input, y or n only")
            print("")

    if addAnother == "n" or addAnother == "N":
        break



print("")
#Returning Books
while i == 0:
    #Display Available Books
    print("Books in Library: ")
    for x in range(len(library)):
        if library[x].is_book_available() == True:
            print("Title:",library[x].get_title(),"Author:",library[x].get_author(),"Publication Year:",library[x].get_publication_year(),
                  "Index:",x,sep=" ")
        else:
            continue
    print("")
    Return = int(input("Enter the index of the book you want to return "))
    print("")
    
    if library[Return].is_book_available() == False:
        library[Return].return_book()
        print(library[Return].get_title(), "by author", library[Return].get_author(), "has been successfully returned", sep=" ")
        print("")
    else:
        print(library[Return].get_title(), "by author", library[Return].get_author(), "is already on the shelf", sep=" ")
        print("")
    
    while addAnother != "n" or addAnother != "y" or addAnother != "Y" or addAnother != "N":
        addAnother = input("Do you want to return another book? (y/n) ")
        addAnother.lower()
        print("")

        if addAnother == "y" or addAnother == "Y" or addAnother == "n" or addAnother == "N":
            break
        else:
            print("invalid input, y or n only")
            print("")

    if addAnother == "n" or addAnother == "N":
        break

#Last Display of Available Books
print("Books in Library: ")
for x in range(len(library)):
    if library[x].is_book_available() == True:
        print("Title:",library[x].get_title(),"Author:",library[x].get_author(),"Publication Year:",library[x].get_publication_year(),
                "Index:",x,sep=" ")
    else:
        continue

