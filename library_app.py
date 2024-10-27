import random
import datetime
import click
 
class Book:
   """Represents a book object.
 
   Attributes:
       book_id (int): A unique random ID for the book.
       title (str): The title of the book.
       author (str): The author of the book.
       year (int): The publication year of the book.
       publisher (str): The publisher of the book.
       num_available_copies (int): The number of available copies of the book.
       publication_date (datetime.date): The publication date of the book.
   """
 
   def __init__(self, title, author, year, publisher, num_available_copies):
       """Constructs a new Book object.
 
       Args:
           title (str): The title of the book.
           author (str): The author of the book.
           year (int): The publication year of the book.
           publisher (str): The publisher of the book.
           num_available_copies (int): The number of available copies of the book.
       """
       self.book_id = random.randint(100000, 999999)
       self.title = title
       self.author = author
       self.year = year
       self.publisher = publisher
       self.num_available_copies = num_available_copies
       self.publication_date = datetime.date(year, 1, 1)
 
   # Setter methods with error checking
   def set_title(self, title):
       """Sets the title of the book.
 
       Args:
           title (str): The new title of the book.
       """
       if not isinstance(title, str):
           raise ValueError("Title must be a string")
       self.title = title
 
   def set_author(self, author):
       """Sets the author of the book.
 
       Args:
           author (str): The new author of the book.
       """
       if not isinstance(author, str):
           raise ValueError("Author must be a string")
       self.author = author
 
   def set_year(self, year):
       """Sets the publication year of the book.
 
       Args:
           year (int): The new publication year of the book.
       """
       if not isinstance(year, int):
           raise ValueError("Year must be an integer")
       self.year = year
       self.publication_date = datetime.date(year, 1, 1)
 
   def set_publisher(self, publisher):
       """Sets the publisher of the book.
 
       Args:
           publisher (str): The new publisher of the book.
       """
       if not isinstance(publisher, str):
           raise ValueError("Publisher must be a string")
       self.publisher = publisher
 
   def set_num_available_copies(self, num_available_copies):
       """Sets the number of available copies of the book.
 
       Args:
           num_available_copies (int): The new number of available copies.
       """
       if not isinstance(num_available_copies, int) or num_available_copies < 0:
           raise ValueError("Number of available copies must be a non-negative integer")
       self.num_available_copies = num_available_copies
 
   def set_publication_date(self, publication_date):
       """Sets the publication date of the book.
 
       Args:
           publication_date (datetime.date): The new publication date.
       """
       if not isinstance(publication_date, datetime.date):
           raise ValueError("Publication date must be a datetime.date object")
       self.publication_date = publication_date
 
   # Getter methods
   def get_title(self):
       return self.title
 
   def get_author(self):
       return self.author
 
   def get_year(self):
       return self.year
 
   def get_publisher(self):
       return self.publisher
 
   def get_num_available_copies(self):
       return self.num_available_copies
 
   def get_publication_date(self):
       return self.publication_date
   
 
 
 
class BookList:
   """Represents a list of books.
 
   Attributes:
       books (dict): A dictionary storing book instances by their titles.
   """
 
   def __init__(self):
       """Constructs a new BookList object."""
       self.books = {}
 
   def add_book(self, book):
       """Adds a book to the collection.
 
       Args:
           book (Book): The book object to add.
       """
       if not isinstance(book, Book):
           raise TypeError("Book object expected")
       self.books[book.get_title()] = book
 
   def find_book(self, search_term):
       """Finds a book in the collection by title, author, publisher, or publication date.
 
       Args:
           search_term (str or datetime.date): The search term.
 
       Returns:
           Book or None: The found book, or None if not found.
       """
       if isinstance(search_term, str):
           # Search by title, author, or publisher
           for book in self.books.values():
               if search_term.lower() in book.get_title().lower() or \
                  search_term.lower() in book.get_author().lower() or \
                  search_term.lower() in book.get_publisher().lower():
                   return book
       elif isinstance(search_term, datetime.date):
           # Search by publication date
           for book in self.books.values():
               if book.get_publication_date() == search_term:
                   return book
       return None
 
   def remove_book(self, title):
       """Removes a book from the collection by title.
 
       Args:
           title (str): The title of the book to remove.
       """
       if title in self.books:
           del self.books[title]
 
   def get_num_books(self):
       """Returns the total number of books in the collection.
 
       Returns:
           int: The number of books.
       """
       return len(self.books)
   
 
 
 

class User:
    """Represents a user object.
    
    Attributes:
        username (str): The username of the user.
        firstname (str): The first name of the user.
        surname (str): The surname of the user.
        house_number (int): The house number of the user's address.
        street_name (str): The street name of the user's address.
        postcode (str): The postcode of the user's address.
        email_address (str): The email address of the user.
        date_of_birth (datetime.date): The date of birth of the user.
    """
    
    def __init__(self, username, firstname, surname, house_number, street_name, postcode, email_address, date_of_birth):
        """Constructs a new User object.
    
        Args:
            username (str): The username of the user.
            firstname (str): The first name of the user.
            surname (str): The surname of the user.
            house_number (int): The house number of the user's address.
            street_name (str): The street name of the user's address.
            postcode (str): The postcode of the user's address.
            email_address (str): The email address of the user.
            date_of_birth (datetime.date): The date of birth of the user.
        """
        self.username = username
        self.firstname = firstname
        self.surname = surname
        self.house_number = house_number
        self.street_name = street_name
        self.postcode = postcode
        self.email_address = email_address
        self.date_of_birth = date_of_birth
    
    # Getter methods
    def get_username(self):
        return self.username
    
    def get_firstname(self):
        return self.firstname
    
    def get_surname(self):
        return self.surname
    
    def get_house_number(self):
        return self.house_number
    
    def get_street_name(self):
        return self.street_name
    
    def get_postcode(self):
        return self.postcode
    
    def get_email_address(self):
        return self.email_address
    
    def get_date_of_birth(self):
        return self.date_of_birth
    
    # Setter methods with error checking
    def set_firstname(self, firstname):
        if not isinstance(firstname, str):
            raise ValueError("First name must be a string")
        self.firstname = firstname
    
    def set_surname(self, surname):
        if not isinstance(surname, str):
            raise ValueError("Surname must be a string")
        self.surname = surname
    
    def set_email_address(self, email_address):
        # Implement email validation here (e.g., using a regular expression)
        if not isinstance(email_address, str) or not email_address.endswith("@example.com"):
            raise ValueError("Invalid email address")
        self.email_address = email_address
    
    def set_date_of_birth(self, date_of_birth):
        if not isinstance(date_of_birth, datetime.date):
            raise ValueError("Date of birth must be a datetime.date object")
        self.date_of_birth = date_of_birth
        
    def set_street_name(self, street_name):
        self.street_name = street_name
        
    def set_house_number(self, street_number):
        self.street_number = street_number
        
    def set_postcode(self, postcode):
        self.postcode = postcode
 
 
 
class UserList:
    """Represents a list of users.

    Attributes:
        users (dict): A dictionary storing user instances by their usernames.
        """

    def __init__(self):
        """Constructs a new UserList object."""
        self.users = {}
    
    def add_user(self, user):
        """Adds a user to the collection.
    
        Args:
            user (User): The user object to add.
        """
        if not isinstance(user, User):
            raise TypeError("User object expected")
        if user.get_username() in self.users:
            raise ValueError("Username already exists")
        self.users[user.get_username()] = user
    
    def remove_user_by_firstname(self, firstname):
        """Removes a user from the collection by first name.
    
        Args:
            firstname (str): The first name of the user to remove.
        """
        found_users = [user for user in self.users.values() if user.get_firstname() == firstname]
        if len(found_users) == 0:
            print("User not found.")
        elif len(found_users) > 1:
            print("Multiple users found with the same first name. Please specify the username.")
        else:
            del self.users[found_users[0].get_username()]
    
    def get_num_users(self):
        """Returns the total number of users in the collection.
    
        Returns:
            int: The number of users.
        """
        return len(self.users)
    
    def get_user_by_username(self, username):
        """Returns a user by username.
    
        Args:
            username (str): The username of the user to find.
    
        Returns:
            User or None: The found user, or None if not found.
        """
        return self.users.get(username)

 
 

class Loans:
    """Represents a list of loans.

    Attributes:
        loans (dict): A dictionary storing loans by book IDs, where each entry has the structure {book_id: (user, borrow_date)}.
    """

    def __init__(self):
        """Constructs a new Loans object."""
        self.loans = {}

    def borrow_book(self, user, book):
        """Assigns a book to a user.

        Args:
            user (User): The user object borrowing the book.
            book (Book): The book object being borrowed.
        """
        if book.get_num_available_copies() == 0:
            raise ValueError("Book is not available")
        if book.get_book_id() in self.loans:
            raise ValueError("Book is already borrowed")
        
        borrow_date = datetime.datetime.now().date()
        self.loans[book.get_book_id()] = (user, borrow_date)
        book.set_num_available_copies(book.get_num_available_copies() - 1)

    def return_book(self, book):
        """Un-assigns a book from a user.

        Args:
            book (Book): The book object being returned.
        """
        if book.get_book_id() not in self.loans:
            raise ValueError("Book is not currently borrowed")
        
        del self.loans[book.get_book_id()]
        book.set_num_available_copies(book.get_num_available_copies() + 1)

    def count_user_loans(self, user):
        """Counts the number of books a user is currently borrowing.

        Args:
            user (User): The user object.

        Returns:
            int: The number of books borrowed by the user.
        """
        return len([loan_user for loan_user, _ in self.loans.values() if loan_user == user])


    def is_overdue(self, borrow_date, current_date, loan_duration=14):
        """Determines if a book is overdue based on the borrow date and loan duration.

        Args:
            borrow_date (datetime.date): The date the book was borrowed.
            current_date (datetime.date): The current date.
            loan_duration (int): The number of days for which the loan is valid (default is 14 days).

        Returns:
            bool: True if the book is overdue, False otherwise.
        """
        due_date = borrow_date + datetime.timedelta(days=loan_duration)
        return current_date > due_date

    def print_overdue_books(self, current_date):
        """Prints overdue books along with user information.

        Args:
            current_date (datetime.date): The current date.
        """
        overdue_books = [
            (book_id, user) for book_id, (user, borrow_date) in self.loans.items()
            if self.is_overdue(borrow_date, current_date)
        ]

        if not overdue_books:
            print("No overdue books.")
        else:
            for book_id, user in overdue_books:
                print(f"Book ID: {book_id}")
                print(f"User: {user.get_username()} ({user.get_firstname()})")

        
        
        

 
def modify_book(book):
   """Modifies a book's attributes from the command line."""
   new_title = click.prompt("Enter new title:", default=book.get_title())
   new_author = click.prompt("Enter new author:", default=book.get_author())
   new_year = click.prompt("Enter new year:", default=book.get_year())
   new_publisher = click.prompt("Enter new publisher:", default=book.get_publisher())
   new_num_copies = click.prompt("Enter new number of copies:", default=book.get_num_available_copies())
 
   book.set_title(new_title)
   book.set_author(new_author)
   book.set_year(new_year)
   book.set_publisher(new_publisher)
   book.set_num_available_copies(new_num_copies)
 
def modify_user(user):
   """Modifies a user's attributes from the command line."""
   new_firstname = click.prompt("Enter new first name:", default=user.get_firstname())
   new_surname = click.prompt("Enter new surname:", default=user.get_surname())
   new_house_number = click.prompt("Enter new house number:", default=user.get_house_number())
   new_street_name = click.prompt("Enter new street name:", default=user.get_street_name())
   new_postcode = click.prompt("Enter new postcode:", default=user.get_postcode())
 
   user.set_firstname(new_firstname)
   user.set_surname(new_surname)
   user.set_house_number(new_house_number)
   user.set_street_name(new_street_name)
   user.set_postcode(new_postcode)
 
 
 
if __name__ == "__main__":
   # Create book and user instances
   book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Charles Scribner's Sons", 10)
   user1 = User("john_doe", "John", "Doe", 123, "Main Street", "AB12 3CD", "johndoe@example.com", datetime.date(1990, 1, 1))
 
   # Modify book attributes
   modify_book(book1)
 
   # Modify user attributes
   modify_user(user1)
