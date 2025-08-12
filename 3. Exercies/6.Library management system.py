class library:
    book = 0
    noofbooks = 0
    def add_book(self, book):
        self.book = book
        self.noofbooks += 1
        print(f"Book {self.book} added successfully")
    def check_book(self):
        if self.noofbooks == 0:
            print("No books available")
        else:
            print(f"Book name: {self.book}")
    def show_no_of_books(self):
        print(f"Number of books available: {self.noofbooks}")
    def showbook(self):
        print(f"Book name: {self.book}")

daksh = library()
daksh.add_book("Python")
daksh.check_book()
daksh.show_no_of_books()
daksh.showbook()
daksh.add_book("Java")
daksh.check_book()
daksh.show_no_of_books()
daksh.showbook()
