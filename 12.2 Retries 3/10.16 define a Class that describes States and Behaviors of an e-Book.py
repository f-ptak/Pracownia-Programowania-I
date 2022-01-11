class eBook():
    def __init__(self, title, author, pagenum):
        self.title = title
        self.author = author
        self.pagenum = pagenum
        self.curpage = 1
        self.opened = False
    
    def showinfo(self):
        print("==========================================================================================")
        if self.opened:
            message = f"You opened the book on the page number {self.curpage}."
            print(f"{message:^90}")
        else:
            message = f"""The book seems to be closed. Upon further inspection you deduce that the book was written
by a certain individual named \"{self.author}\" and is titled \"{self.title}\".
It has {self.pagenum} pages and is bookmarked at the page number {self.curpage}."""
            print(f"{message}")
        print("==========================================================================================\n")
    
    def openclose(self):
        if self.opened:
            self.opened = False
        else:
            self.opened = True
    
    def prevpage(self):
        if self.opened:
            if self.curpage > 0:
                self.curpage -= 1
    
    def nextpage(self):
        if self.opened:
            if self.curpage < self.pagenum:
                self.curpage += 1
    
    def changepage(self, num):
        if 0 <= num <= self.pagenum:
            self.curpage = num

b = eBook("The Grand History of eBooks","John Eebuck", 253)

b.showinfo()
b.openclose()
b.showinfo()
b.changepage(117)
b.showinfo()
b.nextpage()
b.nextpage()
b.nextpage()
b.nextpage()
b.showinfo()
b.prevpage()
b.prevpage()
b.prevpage()
b.showinfo()
b.openclose()
b.showinfo()
b.nextpage()
b.nextpage()
b.showinfo()