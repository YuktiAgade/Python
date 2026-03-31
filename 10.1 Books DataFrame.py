import pandas as pd
import numpy as np

# Create sample books.csv data (if file doesn't exist)
def create_sample_books_csv():
    """Create a sample books.csv file for testing"""
    data = {
        'title': [
            'Python Programming', 
            'Data Science Handbook', 
            'Machine Learning Basics',
            'Web Development with Flask', 
            'Artificial Intelligence', 
            'Deep Learning',
            'JavaScript Essentials', 
            'Database Management'
        ],
        'author': [
            'John Smith', 
            'Sarah Johnson', 
            'Michael Brown',
            'Emily Davis', 
            'David Wilson', 
            'Sarah Johnson',
            'Robert Taylor', 
            'Emily Davis'
        ],
        'edition': [3, 2, 1, 2, 1, 1, 4, 3],
        'publication_year': [2020, 2019, 2021, 2020, 2018, 2021, 2019, 2020],
        'publishing_house': [
            'TechPress', 
            'DataPub', 
            'MLBooks',
            'WebPub', 
            'AIPress', 
            'DataPub',
            'TechPress', 
            'DataPub'
        ],
        'price': [45.99, 67.50, 55.00, 42.99, 89.99, 79.99, 35.50, 52.00]
    }
    
    df = pd.DataFrame(data)
    df.to_csv('books.csv', index=False)
    print("Sample books.csv file created successfully!\n")

# Read the CSV file
try:
    books_df = pd.read_csv('books.csv')
except FileNotFoundError:
    print("books.csv not found. Creating sample data...")
    create_sample_books_csv()
    books_df = pd.read_csv('books.csv')

print("=" * 80)
print("BOOK DATABASE MANAGEMENT SYSTEM")
print("=" * 80)

# a) Print the complete report of books in Tabular form
print("\na) Complete Report of Books:")
print("-" * 80)
print(books_df.to_string(index=False))
print("\n")

# b) Print the list of available books of a given author
def get_books_by_author(author_name):
    """Get books by a specific author"""
    author_books = books_df[books_df['author'].str.lower() == author_name.lower()]
    if not author_books.empty:
        print(f"\nb) Books by {author_name}:")
        print("-" * 80)
        print(author_books[['title', 'publication_year', 'price']].to_string(index=False))
    else:
        print(f"\nNo books found by author: {author_name}")
    return author_books

# Example usage
get_books_by_author('Sarah Johnson')
print("\n")

# c) Print the list of available books of a given publishing house
def get_books_by_publisher(publisher_name):
    """Get books by a specific publishing house"""
    publisher_books = books_df[books_df['publishing_house'].str.lower() == publisher_name.lower()]
    if not publisher_books.empty:
        print(f"\nc) Books published by {publisher_name}:")
        print("-" * 80)
        print(publisher_books[['title', 'author', 'publication_year', 'price']].to_string(index=False))
    else:
        print(f"\nNo books found from publisher: {publisher_name}")
    return publisher_books

# Example usage
get_books_by_publisher('TechPress')
print("\n")

# d) Print the Titles of cheapest & costliest book available
print("d) Cheapest and Costliest Books:")
print("-" * 80)
cheapest_book = books_df.loc[books_df['price'].idxmin()]
costliest_book = books_df.loc[books_df['price'].idxmax()]

print(f"Cheapest Book: {cheapest_book['title']} - ${cheapest_book['price']:.2f}")
print(f"Costliest Book: {costliest_book['title']} - ${costliest_book['price']:.2f}")
print("\n")

# e) Print the list by sorting based on the year of publication
print("e) Books Sorted by Publication Year:")
print("-" * 80)
sorted_books = books_df.sort_values('publication_year')
print(sorted_books[['title', 'author', 'publication_year', 'price']].to_string(index=False))
print("\n")

# Interactive menu for Lab Assignment 1
print("\n" + "=" * 80)
print("INTERACTIVE MENU - LAB ASSIGNMENT 1")
print("=" * 80)
while True:
    print("\nSelect an operation:")
    print("1. Print complete report")
    print("2. Search books by author")
    print("3. Search books by publishing house")
    print("4. Show cheapest and costliest books")
    print("5. Sort books by publication year")
    print("6. Exit")
    
    choice = input("\nEnter your choice (1-6): ")
    
    if choice == '1':
        print("\nComplete Report:")
        print(books_df.to_string(index=False))
    
    elif choice == '2':
        author = input("Enter author name: ")
        get_books_by_author(author)
    
    elif choice == '3':
        publisher = input("Enter publishing house name: ")
        get_books_by_publisher(publisher)
    
    elif choice == '4':
        print(f"\nCheapest Book: {cheapest_book['title']} - ${cheapest_book['price']:.2f}")
        print(f"Costliest Book: {costliest_book['title']} - ${costliest_book['price']:.2f}")
    
    elif choice == '5':
        print("\nBooks Sorted by Publication Year:")
        print(sorted_books[['title', 'author', 'publication_year', 'price']].to_string(index=False))
    
    elif choice == '6':
        print("Exiting...")
        break
    
    else:
        print("Invalid choice! Please try again.")
