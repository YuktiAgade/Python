import java.util.Scanner;

// Base class Employee
class Employee {
    protected String name;
    protected int age;
    protected String address;
    protected double salary;

    // Method to get employee information
    public void getInput(Scanner sc) {
        System.out.print("Enter Name: ");
        this.name = sc.nextLine();
        System.out.print("Enter Age: ");
        this.age = sc.nextInt();
        sc.nextLine(); // consume newline
        System.out.print("Enter Address: ");
        this.address = sc.nextLine();
        System.out.print("Enter Salary: ");
        this.salary = sc.nextDouble();
        sc.nextLine(); // consume newline
    }

    // Method to print employee information
    public void printInfo() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("Address: " + address);
        System.out.println("Salary: " + salary);
    }
}

// Derived class Manager
class Manager extends Employee {
    private String department;

    // Override getInput to include department
    @Override
    public void getInput(Scanner sc) {
        super.getInput(sc);
        System.out.print("Enter Department: ");
        this.department = sc.nextLine();
    }

    // Override printInfo to include department
    @Override
    public void printInfo() {
        super.printInfo();
        System.out.println("Department: " + department);
    }
}

// Main class to process 10 managers
public class EmployeeManagerDemo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Manager[] managers = new Manager[10];

        System.out.println("Enter information for 10 Managers:\n");
        for (int i = 0; i < managers.length; i++) {
            System.out.println("--- Manager " + (i + 1) + " ---");
            managers[i] = new Manager();
            managers[i].getInput(sc);
            System.out.println();
        }

        System.out.println("\n--- Manager Details ---");
        for (int i = 0; i < managers.length; i++) {
            System.out.println("--- Manager " + (i + 1) + " ---");
            managers[i].printInfo();
            System.out.println();
        }
        sc.close();
    }
}
