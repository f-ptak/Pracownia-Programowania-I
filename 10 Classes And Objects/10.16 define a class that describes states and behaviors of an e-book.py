class ebook():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.page_no = 1
        self.is_open = False
    
    def open_book(self):
        self.is_open = True
    def close_book(self):
        self.is_open = False
    
    def nextpage(self):
        if self.is_open == False:
            print("Book is not opened")
        else:
            if self.page_no < self.pages:
                self.page_no+=1
    def prevpage(self):
        if self.is_open == False:
            print("Book is not opened")
        else:
            if self.page_no > 1:
                self.page_no-=1
    
    def disp_status(self):
        print("===================")
        print("Book info:")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Number of pages: {self.pages}")
        print(f"Current page: {self.page_no}")
        print("===================")


ahh = ebook("Naj Kawon's Rather Quirky Escapades", "John Doe", 512)

ahh.open_book()
ahh.disp_status()
ahh.nextpage()
ahh.nextpage()
ahh.nextpage()
ahh.nextpage()
ahh.nextpage()
ahh.nextpage()
ahh.disp_status()
ahh.close_book()
ahh.nextpage()
ahh.nextpage()
ahh.prevpage()