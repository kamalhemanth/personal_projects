import java.util.ArrayList;
import java.util.Scanner;

class Task {
    private String description;
    private boolean isComplete;

    public Task(String description) {
        this.description = description;
        this.isComplete = false;
    }

    public void markComplete() {
        isComplete = true;
    }

    public boolean isComplete() {
        return isComplete;
    }

    public String getDescription() {
        return description;
    }

    @Override
    public String toString() {
        return description + " (Completed: " + isComplete + ")";
    }
}

public class TodoListApp {
    public static void main(String[] args) {
        ArrayList<Task> taskList = new ArrayList<>();
        Scanner scanner = new Scanner(System.in);
        
        boolean quit = false;
        
        while (!quit) {
            System.out.println("\nTo-Do List Menu:");
            System.out.println("1. Add Task");
            System.out.println("2. Remove Task");
            System.out.println("3. Mark Task as Complete");
            System.out.println("4. View All Tasks");
            System.out.println("5. Exit");
            System.out.print("Choose an option: ");
            
            int choice = scanner.nextInt();
            scanner.nextLine();  // Consume newline
            
            switch (choice) {
                case 1:
                    System.out.print("Enter task description: ");
                    String description = scanner.nextLine();
                    taskList.add(new Task(description));
                    System.out.println("Task added.");
                    break;
                case 2:
                    System.out.print("Enter task number to remove: ");
                    int removeIndex = scanner.nextInt();
                    if (removeIndex > 0 && removeIndex <= taskList.size()) {
                        taskList.remove(removeIndex - 1);
                        System.out.println("Task removed.");
                    } else {
                        System.out.println("Invalid task number.");
                    }
                    break;
                case 3:
                    System.out.print("Enter task number to mark as complete: ");
                    int completeIndex = scanner.nextInt();
                    if (completeIndex > 0 && completeIndex <= taskList.size()) {
                        taskList.get(completeIndex - 1).markComplete();
                        System.out.println("Task marked as complete.");
                    } else {
                        System.out.println("Invalid task number.");
                    }
                    break;
                case 4:
                    System.out.println("All Tasks:");
                    for (int i = 0; i < taskList.size(); i++) {
                        System.out.println((i + 1) + ". " + taskList.get(i));
                    }
                    break;
                case 5:
                    quit = true;
                    System.out.println("Exiting To-Do List App.");
                    break;
                default:
                    System.out.println("Invalid option. Please try again.");
            }
        }
        
        scanner.close();
    }
}
