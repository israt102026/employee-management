# Employee Salary Management System
# Practice: Functions and File Handling

FILE_NAME = "employees.txt"


def add_employee(name, emp_id, salary):
    """Save one employee record to employees.txt.

    Parameters: name, emp_id, salary
    Returns: True when the record is saved.
    """
    # "a" mode appends to the end, so old records are not erased
    with open(FILE_NAME, "a") as file:
        file.write(f"{name} | {emp_id} | {salary}\n")
    return True


def view_employees():
    """Read all records from employees.txt.

    Returns: a list of lines (empty list if the file does not exist yet).
    """
    try:
        # "r" mode reads the file
        with open(FILE_NAME, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []


def display_employees(records):
    """Print the records in a neat table."""
    if len(records) == 0:
        print("No employee records found.")
        return

    print("\n--- Employee Records ---")
    print(f"{'Name':<15}{'ID':<10}{'Salary':<10}")
    print("-" * 35)
    for record in records:
        # Split each line into name, id and salary
        name, emp_id, salary = record.strip().split(" | ")
        print(f"{name:<15}{emp_id:<10}{salary:<10}")
    print("-" * 35)


def main():
    """Show the menu and run the chosen option."""
    while True:
        print("\n1. Add Employee")
        print("2. View Employees")
        print("3. Exit")
        choice = input("Choose Option: ")

        if choice == "1":
            name = input("Enter Name: ")
            emp_id = input("Enter ID: ")
            salary = input("Enter Salary: ")

            # Make sure salary is a number
            if not salary.isdigit():
                print("Invalid salary! Please enter numbers only.")
                continue

            if add_employee(name, emp_id, salary):
                print("Employee Added Successfully")

        elif choice == "2":
            display_employees(view_employees())

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option! Please choose 1, 2 or 3.")


# Program starts here
if __name__ == "__main__":
    main()