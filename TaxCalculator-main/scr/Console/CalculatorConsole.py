import sys
sys.path.append("scr")
from TaxCalculator import CalculationFunctions, InputOutputFunctions

def show_menu():
    """Displays the options menu."""
    print("\nMenu:")
    print("1. Calculate taxes")
    print("2. Modify parameters")
    print("3. Exit")

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

def calculate_taxes():
    """Function to handle tax calculation interaction."""
    gross_income, deductions, tax_credits = request_input_data()
    if gross_income is not None and deductions is not None and tax_credits is not None:
        try:
            result = CalculationFunctions.calculate_net_tax(
                gross_income, deductions, InputOutputFunctions.tax_rate, tax_credits
            )
            print(f"The tax to be paid is: ${result:.2f}")
        except Exception as e:
            print(f"An error occurred during the tax calculation: {e}")
    else:
        print("Could not calculate the tax due to input data errors.")

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

def main():
    """Main function of the program."""
    print("Welcome to the tax calculator")

    while True:
        show_menu()
        option = input("Select an option: ")

        if option == "1":
            calculate_taxes()

        elif option == "2":
            modify_parameters()

        elif option == "3":
            print("Thank you for using the tax calculator")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
