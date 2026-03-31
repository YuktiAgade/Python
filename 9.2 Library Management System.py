import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

// Book class
class Book {
    private String bookId;
    private String title;
    private String author;
    private boolean isAvailable;

    public Book(String bookId, String title, String author) {
        this.bookId = bookId;
        this.title = title;
        this.author = author;
        this.isAvailable = true;
    }

    public String getBookId() {
        return bookId;
    }

    public String getTitle() {
        return title;
    }

    public String getAuthor() {
        return author;
    }

    public boolean isAvailable() {
        return isAvailable;
    }

    public void setAvailable(boolean available) {
        isAvailable = available;
    }

    public void displayInfo() {
        System.out.println("Book ID: " + bookId);
        System.out.println("Title: " + title);
        System.out.println("Author: " + author);
        System.out.println("Status: " + (isAvailable ? "Available" : "Issued"));
    }
}

// Member class
class Member {
    private String memberId;
    private String name;
    private List<Book> borrowedBooks;

    public Member(String memberId, String name) {
        this.memberId = memberId;
        this.name = name;
        this.borrowedBooks = new ArrayList<>();
    }

    public String getMemberId() {
        return memberId;
    }

    public String getName() {
        return name;
    }

    public List<Book> getBorrowedBooks() {
        return borrowedBooks;
    }

    public boolean canBorrow() {
        return borrowedBooks.size() < 3; // Limit: max 3 books per member
    }

    public void borrowBook(Book book) {
        borrowedBooks.add(book);
    }

    public void returnBook(Book book) {
        borrowedBooks.remove(book);
    }

    public void displayInfo() {
        System.out.println("Member ID: " + memberId);
        System.out.println("Name: " + name);
        System.out.println("Books Borrowed: " + borrowedBooks.size());
        if (!borrowedBooks.isEmpty()) {
            System.out.println("Borrowed Books:");
            for (Book b : borrowedBooks) {
                System.out.println("  - " + b.getTitle());
            }
        }
    }
}

// Library class
class Library {
    private List<Book> books;
    private List<Member> members;

    public Library() {
        books = new ArrayList<>();
        members = new ArrayList<>();
    }

    // Add a book
    public void addBook(Book book) {
        books.add(book);
        System.out.println("Book added successfully: " + book.getTitle());
    }

    // Add a member
    public void addMember(Member member) {
        members.add(member);
        System.out.println("Member added successfully: " + member.getName());
    }

    // Find book by ID
    private Book findBookById(String bookId) {
        for (Book book : books) {
            if (book.getBookId().equals(bookId)) {
                return book;
            }
        }
        return null;
    }

    // Find member by ID
    private Member findMemberById(String memberId) {
        for (Member member : members) {
            if (member.getMemberId().equals(memberId)) {
                return member;
            }
        }
        return null;
    }

    // Lend a book to a member
    public void lendBook(String bookId, String memberId) {
        Book book = findBookById(bookId);
        Member member = findMemberById(memberId);

        if (book == null) {
            System.out.println("Book not found!");
            return;
        }
        if (member == null) {
            System.out.println("Member not found!");
            return;
        }
        if (!book.isAvailable()) {
            System.out.println("Book is already issued!");
            return;
        }
        if (!member.canBorrow()) {
            System.out.println("Member has already borrowed maximum books (3)!");
            return;
        }

        book.setAvailable(false);
        member.borrowBook(book);
        System.out.println("Book issued successfully to " + member.getName());
    }

    // Return a book
    public void returnBook(String bookId, String memberId) {
        Book book = findBookById(bookId);
        Member member = findMemberById(memberId);

        if (book == null) {
            System.out.println("Book not found!");
            return;
        }
        if (member == null) {
            System.out.println("Member not found!");
            return;
        }
        if (!member.getBorrowedBooks().contains(book)) {
            System.out.println("This book was not borrowed by the member!");
            return;
        }

        book.setAvailable(true);
        member.returnBook(book);
        System.out.println("Book returned successfully!");
    }

    // Display all books
    public void displayAllBooks() {
        if (books.isEmpty()) {
            System.out.println("No books in the library.");
            return;
        }
        System.out.println("\n--- All Books ---");
        for (Book book : books) {
            book.displayInfo();
            System.out.println();
        }
    }

    // Display all members
    public void displayAllMembers() {
        if (members.isEmpty()) {
            System.out.println("No members registered.");
            return;
        }
        System.out.println("\n--- All Members ---");
        for (Member member : members) {
            member.displayInfo();
            System.out.println();
        }
    }
}

// Main class with menu-driven interface
public class LibraryManagementSystem {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Library library = new Library();

        while (true) {
            System.out.println("\n===== Library Management System =====");
            System.out.println("1. Add Book");
            System.out.println("2. Add Member");
            System.out.println("3. Issue Book");
            System.out.println("4. Return Book");
            System.out.println("5. Display All Books");
            System.out.println("6. Display All Members");
            System.out.println("7. Exit");
            System.out.print("Enter your choice: ");

            int choice = sc.nextInt();
            sc.nextLine(); // consume newline

            switch (choice) {
                case 1:
                    System.out.print("Enter Book ID: ");
                    String bookId = sc.nextLine();
                    System.out.print("Enter Title: ");
                    String title = sc.nextLine();
                    System.out.print("Enter Author: ");
                    String author = sc.nextLine();
                    library.addBook(new Book(bookId, title, author));
                    break;

                case 2:
                    System.out.print("Enter Member ID: ");
                    String memberId = sc.nextLine();
                    System.out.print("Enter Member Name: ");
                    String name = sc.nextLine();
                    library.addMember(new Member(memberId, name));
                    break;

                case 3:
                    System.out.print("Enter Book ID: ");
                    String lendBookId = sc.nextLine();
                    System.out.print("Enter Member ID: ");
                    String lendMemberId = sc.nextLine();
                    library.lendBook(lendBookId, lendMemberId);
                    break;

                case 4:
                    System.out.print("Enter Book ID: ");
                    String returnBookId = sc.nextLine();
                    System.out.print("Enter Member ID: ");
                    String returnMemberId = sc.nextLine();
                    library.returnBook(returnBookId, returnMemberId);
                    break;

                case 5:
                    library.displayAllBooks();
                    break;

                case 6:
                    library.displayAllMembers();
                    break;

                case 7:
                    System.out.println("Exiting Library Management System. Goodbye!");
                    sc.close();
                    return;

                default:
                    System.out.println("Invalid choice! Please try again.");
            }
        }
    }
}
