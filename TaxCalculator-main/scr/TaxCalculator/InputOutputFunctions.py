def request_parameter_input(message, data_type=float):
    """Requests data from the user and handles exceptions."""
    while True:
        try:
            data = data_type(input(message))
            if data < 0:
                print("The value cannot be negative. Try again.")
                continue
            return data
        except ValueError:
            print(f"Invalid input. Please enter a {'whole number' if data_type is int else 'number'}.")

def request_input_data():
    """Requests input data from the user to calculate income tax."""
    total_employment_income = request_parameter_input("Enter the total employment income for the year: ")
    other_income_value = request_parameter_input("Enter the value of other income for the year: ")
    withholding_tax_value = request_parameter_input("Enter the value of withholding tax for the year: ")
    social_security_payments = request_parameter_input("Enter the value of social security payments for the year: ")
    pension_contributions = request_parameter_input("Enter the value of pension contributions for the year: ")
    mortgage_payments = request_parameter_input("Enter the value of mortgage payments for the year: ")
    donations_value = request_parameter_input("Enter the value of donations made during the year: ")
    education_expenses = request_parameter_input("Enter the value of education expenses for the year: ")

    return (total_employment_income, other_income_value, withholding_tax_value, social_security_payments,
            pension_contributions, mortgage_payments, donations_value, education_expenses)

def display_information(total_taxable_income, total_non_taxable_income, total_deductible_costs, tax_to_pay_value):
    """Displays the calculated information on the screen."""
    
    print("\nIncome tax declaration information:")
    print(f"Total taxable income: {total_taxable_income}")
    print(f"Total non-taxable income: {total_non_taxable_income}")
    print(f"Total deductible costs: {total_deductible_costs}")
    print(f"Amount to pay for income tax: {tax_to_pay_value}")

def show_how_to_use():
    """Displays usage instructions."""
    try:
        with open('resources/how_to_use.txt', 'r', encoding='utf-8') as file:
            message = file.read()
            print(message)
    except FileNotFoundError:
        print("The file 'how_to_use.txt' was not found in the 'resources' folder.")

def tax_rate():
    """Returns the current tax rate."""
    return _current_tax_rate

def modify_tax_rate(new_rate):
    """Modifies the current tax rate."""
    global _current_tax_rate
    _current_tax_rate = new_rate

def calculate_net_tax(gross_income, deductions, tax_rate, tax_credits):
    """Calculates net tax based on gross income, deductions, tax rate, and tax credits."""
    taxable_base = gross_income - deductions
    tax = taxable_base * tax_rate
    net_tax = tax - tax_credits
    return max(net_tax, 0)  # Tax cannot be negative

tax_rate = 0.25  # Default tax rate

def calculate_tax_value(income, deductions):
    """Calculate the tax value based on income and deductions.

    Args:
        income (float): Total income.
        deductions (float): Applicable deductions.

    Returns:
        float: The tax amount to pay.

    Raises:
        ValueError: If income or deductions are negative.
        TypeError: If income or deductions are not numbers.
    """
    # Validate that income and deductions are numbers
    if not isinstance(income, (int, float)) or not isinstance(deductions, (int, float)):
        raise TypeError("Income and deductions must be numbers.")
    
    # Validate that income and deductions are not negative
    if income < 0 or deductions < 0:
        raise ValueError("Income and deductions cannot be negative.")

    taxable_income = income - deductions
    if taxable_income < 0:
        taxable_income = 0
    
    
    # Calculate tax
    taxable_base = max(income - deductions, 0)  # Taxable base cannot be negative
    tax = taxable_base * tax_rate  # Calculate tax based on the rate
    return tax


    

