import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from TaxCalculator import CalculationFunctions, InputOutputFunctions, Database 

def show_menu():
    """Displays the options menu."""
    print("\nMenu:")
    print("1. Register User")
    print("2. Calculate taxes for registered user")
    print("3. Search user and add calculation")
    print("4. Modify parameters")
    print("5. View calculation history")
    print("6. View users by ID")
    print("7. Modify or delete user")
    print("8. Exit")


def register_user():
    """Registers a new user in the database."""
    username = input("Enter your username: ")
    email = input("Enter your email: ")

    user_id = Database.insert_user(username, email)
    if user_id:
        print(f"User {username} registered with ID {user_id}.")
        calculate_taxes(user_id)
    else:
        print("Failed to register user.")
        return None

def request_input_data():
    """Requests all necessary data for tax calculation."""
    try:
        gross_income = float(input("Enter gross income: "))
        deductions = float(input("Enter total deductions: "))
        tax_credits = float(input("Enter tax credits: "))
        return gross_income, deductions, tax_credits
    except ValueError:
        print("Error: You entered an invalid value. Make sure to enter numbers.")
        return None, None, None  # Returns None values in case of an error

def calculate_taxes(user_id):
    """Function to handle tax calculation and store the result in the database."""
    gross_income, deductions, tax_credits = request_input_data()
    if gross_income is not None and deductions is not None and tax_credits is not None:
        try:
            result = CalculationFunctions.calculate_net_tax(
                gross_income, deductions, InputOutputFunctions.tax_rate, tax_credits
            )
            print(f"The tax to be paid is: ${result:.2f}")
            # Save in db
            Database.insert_calculation(user_id, gross_income, deductions, tax_credits, result)
        except Exception as e:
            print(f"An error occurred during the tax calculation: {e}")
    else:
        print("Could not calculate the tax due to input data errors.")

def view_calculation_history(user_id):
    """View the history of tax calculations for the given user."""
    calculations = Database.get_user_calculations(user_id)
    if calculations:
        print("\nCalculation History:")
        for calc in calculations:
            print(f"Calculation ID: {calc[0]}, Gross Income: {calc[1]}, Deductions: {calc[2]}, Tax Credits: {calc[3]}, Tax Paid: {calc[4]}, Date: {calc[5]}")
    else:
        print("No calculations found.")

def view_user_by_id(user_id):
    """Retrieve and display a user's information by their ID."""
    user = Database.get_user_by_id(user_id)
    if user:
        print(f"User ID: {user[0]}, Username: {user[1]}, Email: {user[2]}")
    else:
        print(f"No user found with ID {user_id}.")

def modify_or_delete_user():
    """Allows the user to modify or delete a user by their ID."""
    user_id = int(input("Enter the user ID to modify or delete: "))
    user = Database.get_user_by_id(user_id)
    
    if user:
        print(f"User ID: {user[0]}, Username: {user[1]}, Email: {user[2]}")
        print("1. Modify email")
        print("2. Delete user")
        option = input("Select an option: ")
        
        if option == "1":
            new_email = input("Enter the new email: ")
            Database.update_user_email(user_id, new_email)
            print("Email updated successfully.")
        elif option == "2":
            Database.delete_user(user_id)
            print("User deleted successfully.")
        else:
            print("Invalid option.")
    else:
        print(f"No user found with ID {user_id}.")

def modify_parameters():
    """Allows the user to modify calculation parameters."""
    try:
        new_rate = float(input("Enter the new tax rate (as a decimal): "))
        if new_rate < 0 or new_rate > 1:
            raise ValueError("The tax rate must be a value between 0 and 1.")
        InputOutputFunctions.tax_rate = new_rate
        print(f"New tax rate set to: {InputOutputFunctions.tax_rate}")
    except ValueError as e:
        print(f"Error: {e}")

def search_user_and_add_calculation():
    """Busca a un usuario por ID y le permite agregar un nuevo cálculo."""
    user_id = int(input("Enter user ID to search: "))
    user = Database.get_user_by_id(user_id)
    
    if user:
        print(f"User ID: {user[0]}, Username: {user[1]}, Email: {user[2]}")
        calculate_taxes(user_id)  # Llama a la función de cálculo de impuestos
    else:
        print(f"No user found with ID {user_id}.")

def main():
    """Main function of the program."""
    Database.create_tables()  # Create tables in the database if they do not exist
    print("Welcome to the tax calculator")

    while True:
        show_menu()
        option = input("Select an option: ")

        if option == "1":
            register_user()  # Register user

        elif option == "2":
            user_id = int(input("Enter user ID to calculate taxes for: "))
            calculate_taxes(user_id)  # Calculate taxes for the registered user

        elif option == "3":
            search_user_and_add_calculation()  # Search user and add calculation

        elif option == "4":
            modify_parameters()  # Modify parameters

        elif option == "5":
            user_id = int(input("Enter user ID to view history: "))
            view_calculation_history(user_id)  # View calculation history

        elif option == "6":
            user_id = int(input("Enter user ID to view: "))
            view_user_by_id(user_id)  # View user details by ID

        elif option == "7":
            modify_or_delete_user()  # Modify or delete user

        elif option == "8":
            print("Thank you for using the tax calculator")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()