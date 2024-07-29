from inheritance import Inheritance
class Book(Inheritance):
    def __init__(self, title, author, year, genre):
        super().__init__(title, author, year)
        self.genre = genre

    def display_info(self):
        super().display_info()
        print(f"Genre: {self.genre}")


class Magazine(Inheritance):
    def __init__(self, title, author, year, issue_number):
        super().__init__(title, author, year)
        self.issue_number = issue_number

    def display_info(self):
        super().display_info()
        print(f"Issue Number: {self.issue_number}")


class DVD(Inheritance):
    def __init__(self, title, author, year, duration):
        super().__init__(title, author, year)
        self.duration = duration

    def display_info(self):
        super().display_info()
        print(f"Duration: {self.duration} minutes")

# Creating Instances
book = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Novel")
magazine = Magazine("National Geographic", "Various", 2020, 5)
dvd = DVD("Inception", "Christopher Nolan", 2010, 148)

# Displaying Information
print("Book Information:")
book.display_info()
print("\nMagazine Information:")
magazine.display_info()
print("\nDVD Information:")
dvd.display_info()
