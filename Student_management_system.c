#include <stdio.h>
#include <string.h>

struct Student {
    int rollNo;
    char name[100];
    float marks;
};

struct Student students[100];
int studentCount = 0;

void addStudent() {
    printf("Enter Roll Number: ");
    scanf("%d", &students[studentCount].rollNo);
    
    printf("Enter Name: ");
    scanf("%s", students[studentCount].name);
    
    printf("Enter Marks: ");
    scanf("%f", &students[studentCount].marks);
    
    studentCount++;
    printf("Student added successfully.\n");
}

void displayStudents() {
    printf("\nStudent List:\n");
    for (int i = 0; i < studentCount; i++) {
        printf("Roll No: %d, Name: %s, Marks: %.2f\n", students[i].rollNo, students[i].name, students[i].marks);
    }
}

void updateStudent() {
    int rollNo;
    printf("Enter Roll Number of the student to update: ");
    scanf("%d", &rollNo);
    
    for (int i = 0; i < studentCount; i++) {
        if (students[i].rollNo == rollNo) {
            printf("Enter new Name: ");
            scanf("%s", students[i].name);
            
            printf("Enter new Marks: ");
            scanf("%f", &students[i].marks);
            
            printf("Student updated successfully.\n");
            return;
        }
    }
    printf("Student with Roll No %d not found.\n", rollNo);
}

void deleteStudent() {
    int rollNo;
    printf("Enter Roll Number of the student to delete: ");
    scanf("%d", &rollNo);
    
    for (int i = 0; i < studentCount; i++) {
        if (students[i].rollNo == rollNo) {
            for (int j = i; j < studentCount - 1; j++) {
                students[j] = students[j + 1];
            }
            studentCount--;
            printf("Student deleted successfully.\n");
            return;
        }
    }
    printf("Student with Roll No %d not found.\n", rollNo);
}

int main() {
    int choice;
    while (1) {
        printf("\n1. Add Student\n2. Display Students\n3. Update Student\n4. Delete Student\n5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);
        
        switch (choice) {
            case 1:
                addStudent();
                break;
            case 2:
                displayStudents();
                break;
            case 3:
                updateStudent();
                break;
            case 4:
                deleteStudent();
                break;
            case 5:
                return 0;
            default:
                printf("Invalid choice. Try again.\n");
        }
    }
    return 0;
}
