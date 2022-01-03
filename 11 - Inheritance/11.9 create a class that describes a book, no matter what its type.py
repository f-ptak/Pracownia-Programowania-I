class Book():
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class TradBook(Book):
    def __init__(self, title, author, year, pages):
        self.pages = pages
        super().__init__(title, author, year)
    
    def __str__(self):
        return "Title: " + self.title + " | Author: " + self.author + " | Year: " + str(self.year) + " | Pages: " + str(self.pages)


class eBook(Book):
    def __init__(self, title, author, year, fileformat):
        self.fileformat = fileformat
        super().__init__(title, author, year)
    
    def __str__(self):
        return "Title: " + self.title + " | Author: " + self.author + " | Year: " + str(self.year) + " | Format: " + self.fileformat


paper = TradBook("Goodhill's Press", "Some Medival Dude", 1455, 22)
electr = eBook("Working and Displaying", "John, Son of John", 1922, "PDF")

print(paper)
print(electr)