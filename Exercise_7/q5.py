# Define the base class and all derived classes before creating any instances.

class LibraryItem:
    def __init__(self, title, author, publication_year, item_id, status='available'):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.item_id = item_id
        self.status = status

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.publication_year}, ID: {self.item_id}, Status: {self.status}"

    def borrow_item(self):
        if self.status == 'available':
            self.status = 'borrowed'
        else:
            raise ValueError(f"Item '{self.title}' is currently {self.status}.")

    def return_item(self):
        if self.status == 'borrowed':
            self.status = 'available'
        else:
            raise ValueError(f"Item '{self.title}' is not borrowed.")

class Book(LibraryItem):
    def __init__(self, title, author, publication_year, item_id, isbn, publisher, pages, edition, status='available'):
        super().__init__(title, author, publication_year, item_id, status)
        self.isbn = isbn
        self.publisher = publisher
        self.pages = pages
        self.edition = edition

    def reserve_book(self):
        if self.status == 'available':
            self.status = 'reserved'
        else:
            raise ValueError(f"Book '{self.title}' is currently {self.status}.")

class Magazine(LibraryItem):
    def __init__(self, title, author, publication_year, item_id, issue_number, publication_month, status='available'):
        super().__init__(title, author, publication_year, item_id, status)
        self.issue_number = issue_number
        self.publication_month = publication_month

    def get_issue_details(self):
        return f"Issue Number: {self.issue_number}, Month: {self.publication_month}"

class DVD(LibraryItem):
    def __init__(self, title, author, publication_year, item_id, director, duration, rating, status='available'):
        super().__init__(title, author, publication_year, item_id, status)
        self.director = director
        self.duration = duration
        self.rating = rating

    def play_preview(self):
        return f"Playing preview of '{self.title}' directed by {self.director}."

class CD(LibraryItem):
    def __init__(self, title, author, publication_year, item_id, artist, duration, status='available'):
        super().__init__(title, author, publication_year, item_id, status)
        self.artist = artist
        self.duration = duration

    def play_sample(self):
        return f"Playing sample of '{self.title}' by {self.artist}."

class eBook(LibraryItem):
    def __init__(self, title, author, publication_year, item_id, file_format, download_link, status='available'):
        super().__init__(title, author, publication_year, item_id, status)
        self.file_format = file_format
        self.download_link = download_link

    def open_ebook(self):
        return f"Opening eBook '{self.title}' in {self.file_format} format."

class Audiobook(LibraryItem):
    def __init__(self, title, author, publication_year, item_id, narrator, audio_length, status='available'):
        super().__init__(title, author, publication_year, item_id, status)
        self.narrator = narrator
        self.audio_length = audio_length

    def play_sample_audio(self):
        return f"Playing audio sample of '{self.title}' narrated by {self.narrator}."


# Now create instances of the classes

book1 = Book(title="1984", author="George Orwell", publication_year=1949, item_id="B001", isbn="978-0451524935", publisher="Harcourt", pages=328, edition="1st Edition")
magazine1 = Magazine(title="National Geographic", author="National Geographic Society", publication_year=2023, item_id="M001", issue_number=150, publication_month="April")
dvd1 = DVD(title="Inception", author="Christopher Nolan", publication_year=2010, item_id="D001", director="Christopher Nolan", duration=148, rating="PG-13")
cd1 = CD(title="Thriller", author="Michael Jackson", publication_year=1982, item_id="C001", artist="Michael Jackson", duration=42)
ebook1 = eBook(title="Python Programming", author="John Doe", publication_year=2020, item_id="E001", file_format="PDF", download_link="http://example.com/python_programming")
audiobook1 = Audiobook(title="Becoming", author="Michelle Obama", publication_year=2018, item_id="A001", narrator="Michelle Obama", audio_length=192)

# Display information
print(book1.display_info())
print(magazine1.display_info())
print(dvd1.display_info())
print(cd1.display_info())
print(ebook1.display_info())
print(audiobook1.display_info())

# Borrowing and Returning Items
try:
    book1.borrow_item()
    print(f"Borrowed book: {book1.display_info()}")
    book1.return_item()
    print(f"Returned book: {book1.display_info()}")
except ValueError as e:
    print(e)

# Reserving a Book
try:
    book1.reserve_book()
    print(f"Reserved book: {book1.display_info()}")
except ValueError as e:
    print(e)

# Playing previews or samples
print(dvd1.play_preview())
print(cd1.play_sample())
print(ebook1.open_ebook())
print(audiobook1.play_sample_audio())

# Getting Magazine Issue Details
print(magazine1.get_issue_details())
