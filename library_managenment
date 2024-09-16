import java.util.ArrayList;
import java.util.Scanner;

class Book {
    private String title;
    private String author;
    private boolean isAvailable;

    public Book(String title, String author) {
        this.title = title;
        this.author = author;
        this.isAvailable = true;
    }

    public void checkOut() {
        if (isAvailable) {
            isAvailable = false;
            System.out.println("Book checked out successfully.");
        } else {
            System.out.println("Book is already checked out.");
        }
    }

    public void returnBook() {
        if (!isAvailable) {
            isAvailable = true;
            System.out.println("Book returned successfully.");
        } else {
            System.out.println("Book was not checked out.");
        }
    }

    public boolean isAvailable() {
        return isAvailable;
    }

    @Override
    public String toString() {
        return title + " by " + author + " (Available: " + isAvailable + ")";
    }
}

public class LibraryApp {
    public static void main(String[] args) {
        ArrayList<Book> library = new ArrayList<>();
        Scanner scanner = new Scanner(System.in);

        boolean quit = false;

        while (!quit) {
            System.out.println("\nLibrary Management Menu:");
            System.out.println("1. Add Book");
            System.out.println("2. Check Out Book");
            System.out.println("3. Return Book");
            System.out.println("4. View Available Books");
            System.out.println("5. Exit");
            System.out.print("Choose an option: ");

            int choice = scanner.nextInt();
            scanner.nextLine();  // Consume newline

            switch (choice) {
                case 1:
                    System.out.print("Enter book title: ");
                    String title = scanner.nextLine();
                    System.out.print("Enter book author: ");
                    String author = scanner.nextLine();
                    library.add(new Book(title, author));
                    System.out.println("Book added to library.");
                    break;
                case 2:
                    System.out.print("Enter book number to check out: ");
                    int checkOutIndex = scanner.nextInt();
                    if (checkOutIndex > 0 && checkOutIndex <= library.size()) {
                        library.get(checkOutIndex - 1).checkOut();
                    } else {
                        System.out.println("Invalid book number.");
                    }
                    break;
                case 3:
                    System.out.print("Enter book number to return: ");
                    int returnIndex = scanner.nextInt();
                    if (returnIndex > 0 && returnIndex <= library.size()) {
                        library.get(returnIndex - 1).returnBook();
                    } else {
                        System.out.println("Invalid book number.");
                    }
                    break;
                case 4:
                    System.out.println("Available Books:");
                    for (int i = 0; i < library.size(); i++) {
                        if (library.get(i).isAvailable()) {
                            System.out.println((i + 1) + ". " + library.get(i));
                        }
                    }
                    break;
                case 5:
                    quit = true;
                    System.out.println("Exiting Library Management System.");
                    break;
                default:
                    System.out.println("Invalid option. Please try again.");
            }
        }

        scanner.close();
    }
}
