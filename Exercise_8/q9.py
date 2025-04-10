# Abstract base class for items
class Item:
    def __init__(self, title, year):
        self.__title = title
        self.__year = year

    @property
    def title(self):
        return self.__title

    @property
    def year(self):
        return self.__year

    def print_item_description(self):
        description = f"Title: {self.title}, Year: {self.year}"
        return description

    def update_info(self, title=None, year=None):
        if title:
            self.__title = title
        if year:
            self.__year = year


# Subclass for Book
class Book(Item):
    def __init__(self, title, author, year):
        super().__init__(title, year)
        self.__author = author

    @property
    def author(self):
        return self.__author

    def print_item_description(self):
        description = super().print_item_description()
        description += f", Author: {self.author}"
        return description

    def update_info(self, title=None, author=None, year=None):
        super().update_info(title, year)
        if author:
            self.__author = author


# Subclass for Music
class Music(Item):
    def __init__(self, title, artist, year):
        super().__init__(title, year)
        self.__artist = artist

    @property
    def artist(self):
        return self.__artist

    def print_item_description(self):
        description = super().print_item_description()
        description += f", Artist: {self.artist}"
        return description

    def update_info(self, title=None, artist=None, year=None):
        super().update_info(title, year)
        if artist:
            self.__artist = artist


# Subclass for Movie
class Movie(Item):
    def __init__(self, title, director, year):
        super().__init__(title, year)
        self.__director = director

    @property
    def director(self):
        return self.__director

    def print_item_description(self):
        description = super().print_item_description()
        description += f", Director: {self.director}"
        return description

    def update_info(self, title=None, director=None, year=None):
        super().update_info(title, year)
        if director:
            self.__director = director


# Subclass for Game
class Game(Item):
    def __init__(self, title, developer, year):
        super().__init__(title, year)
        self.__developer = developer

    @property
    def developer(self):
        return self.__developer

    def print_item_description(self):
        description = super().print_item_description()
        description += f", Developer: {self.developer}"
        return description

    def update_info(self, title=None, developer=None, year=None):
        super().update_info(title, year)
        if developer:
            self.__developer = developer


# Box to hold all items
class Box:
    def __init__(self):
        self.items = {}

    def add_item(self, key, item: Item):
        self.items[key] = item

    def remove_item(self, key):
        if key in self.items:
            del self.items[key]
        else:
            print("No item found")

    def replace_item(self, old_key, new_key, new_item):
        if old_key in self.items:
            del self.items[old_key]
            self.items[new_key] = new_item
        else:
            print("No item found")

    def get_descriptions(self):
        return [item.print_item_description() for item in self.items.values()]

    def update_item(self, key, title=None, author=None, artist=None, director=None, developer=None, year=None):
        if key in self.items:
            item = self.items[key]
            if isinstance(item, Book):
                item.update_info(title, author, year)
            elif isinstance(item, Music):
                item.update_info(title, artist, year)
            elif isinstance(item, Movie):
                item.update_info(title, director, year)
            elif isinstance(item, Game):
                item.update_info(title, developer, year)
        else:
            print("No item found")


# User Interface for adding, editing, removing items
class PackItems:
    def __init__(self):
        self.box = Box()
        self.log = []

    def user_interface(self):
        while True:
            print("\nOptions:")
            print("1. Add item")
            print("2. Remove item")
            print("3. Replace item")
            print("4. View items")
            print("5. Edit item")
            print("6. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                self.add_item()
            elif choice == "2":
                self.remove_item()
            elif choice == "3":
                self.replace_item()
            elif choice == "5":
                self.edit_item()
            elif choice == "6":
                self.save_log()
                break
            else:
                print("Invalid option. Please try again.")

    def add_item(self):
        title = input("Enter title: ")
        item_type = input("Enter item type (book/music/movie/game): ").lower()

        if item_type == "book":
            author = input("Enter author: ")
            year = input("Enter year: ")
            item = Book(title, author, year)
        elif item_type == "music":
            artist = input("Enter artist: ")
            year = input("Enter year: ")
            item = Music(title, artist, year)
        elif item_type == "movie":
            director = input("Enter director: ")
            year = input("Enter year: ")
            item = Movie(title, director, year)
        elif item_type == "game":
            developer = input("Enter developer: ")
            year = input("Enter year: ")
            item = Game(title, developer, year)
        else:
            print("Invalid item type.")
            return

        self.box.add_item(title, item)
        self.log.append(f"Added item: {title}")

    def remove_item(self):
        title = input("Enter title of item to remove: ")
        self.box.remove_item(title)
        self.log.append(f"Removed item: {title}")

    def replace_item(self):
        old_title = input("Enter title of item to replace: ")
        new_title = input("Enter new title: ")
        item_type = input("Enter item type (book/music/movie/game): ").lower()

        if item_type == "book":
            author = input("Enter author: ")
            year = input("Enter year: ")
            new_item = Book(new_title, author, year)
        elif item_type == "music":
            artist = input("Enter artist: ")
            year = input("Enter year: ")
            new_item = Music(new_title, artist, year)
        elif item_type == "movie":
            director = input("Enter director: ")
            year = input("Enter year: ")
            new_item = Movie(new_title, director, year)
        elif item_type == "game":
            developer = input("Enter developer: ")
            year = input("Enter year: ")
            new_item = Game(new_title, developer, year)
        else:
            print("Invalid item type.")
            return

        self.box.replace_item(old_title, new_title, new_item)
        self.log.append(f"Replaced item: {old_title} with {new_title}")

    def edit_item(self):
        title = input("Enter title of item to edit: ")
        new_title = input("Enter new title (or leave blank): ")
        item_type = input("Enter item type to edit (book/music/movie/game): ").lower()

        author = artist = director = developer = None
        if item_type == "book":
            author = input("Enter new author (or leave blank): ")
        elif item_type == "music":
            artist = input("Enter new artist (or leave blank): ")
        elif item_type == "movie":
            director = input("Enter new director (or leave blank): ")
        elif item_type == "game":
            developer = input("Enter new developer (or leave blank): ")

        year = input("Enter new year (or leave blank): ")

        self.box.update_item(title, new_title, author, artist, director, developer, year)
        self.log.append(f"Edited item: {title}")

    def save_log(self):
        with open("log.txt", "w") as file:
            for entry in self.log:
                file.write(entry + "\n")


if __name__ == "__main__":
    pack_items = PackItems()
    pack_items.user_interface()
