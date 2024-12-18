DATABASE_FILE = "./database/books.txt"
import os
full_path = os.path.abspath(DATABASE_FILE)

def initialize_database():
    """
    Initialize the database file if it doesn't exist.
    """
    file_exists = os.path.isfile(full_path)
    if not file_exists:
        with open(DATABASE_FILE, 'a') as db:
            pass
    else:
        pass

def add_book(title, author):
    """
    Add a new book to the library.
    :param title: The title of the book
    :param author: The author of the book
    """
    # TODO: Append the book's title and author to the database file
    
    with open(DATABASE_FILE, 'a') as file:
        file.write(f'')
        file.write(f'{title},{author}')


def search_book(title):
    """
    Search for a book by title.
    :param title: The title of the book to search for
    :return: A dictionary with the book's details if found, else None
    """
    # TODO: Implement logic to search for a book in the database file

    with open(full_path, mode = 'r') as file:
        for line in file:
            line_list = line.strip().split(',')
            if title in line_list:
                return dict([line_list])
    return None


def list_books():
    """
    List all books in the library.
    :return: A list of dictionaries with each book's details
    """
    # TODO: Read all books from the database file and return them as a list of dictionaries

    with open(full_path, mode = 'r') as file:
        data_base = [dict([line.strip().split(',')]) for line in file.readlines()][1: ]

    return data_base

print(list_books())