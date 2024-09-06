import sys
sys.path.append("scr")
from TaxCalculator.InputOutputFunctions import tax_rate

def request_parameter_input(message, default=None, data_type=float):
    """Requests a parameter from the user and handles exceptions."""
    while True:
        data = input(message)
        if data.upper() == "DEF":
            return default
        try:
            data = data_type(data)
            if data < 0:
                print("The value cannot be negative. Please try again.")
                continue
            return data
        except ValueError:
            print(f"Invalid input. Please enter a{'n integer' if data_type is int else ''} number.")

def modify_parameters():
    """Allows the user to modify the global parameters of the tax calculator."""
    global pension_contribution_rate, health_deduction_rate, education_deduction_rate, donation_deduction_rate
    
    print("\nModify parameters:")
    
    pension_contribution_rate = request_parameter_input("New pension contribution % (DEF to keep current): ", pension_contribution_rate)
    health_deduction_rate = request_parameter_input("New health deduction % (DEF to keep current): ", health_deduction_rate)
    education_deduction_rate = request_parameter_input("New education deduction % (DEF to keep current): ", education_deduction_rate)
    donation_deduction_rate = request_parameter_input("New donation deduction % (DEF to keep current): ", donation_deduction_rate)
    
    print("Parameters modified successfully.")

def calculate_income_tax():
    """Calculates the income tax based on the entered data."""
    (total_employment_income, other_income_value, withholding_tax_value, 
    social_security_payments, pension_contributions, mortgage_payments, 
    donations_value, education_expenses) = request_input_data()
    
    total_income = total_employment_income + other_income_value
    total_taxable_income = total_income - (social_security_payments + pension_contributions)
    total_non_taxable_income = calculate_non_taxable_income(total_income)
    total_deductible_expenses = (donations_value * donation_deduction_rate +
                                 education_expenses * education_deduction_rate +
                                 mortgage_payments)
    
    taxable_base = total_taxable_income - total_deductible_expenses
    tax_to_pay = calculate_tax_amount(taxable_base, withholding_tax_value)
    
    display_information(total_taxable_income, total_non_taxable_income, total_deductible_expenses, tax_to_pay)

def calculate_taxes(income, deduction, tax_percentage):
    try:
        if not isinstance(income, (int, float)):
            raise NonNumericIncomeError()
        if not isinstance(deduction, (int, float)):
            raise NonNumericDeductionError()
        if income == 0:
            raise ZeroIncomeError()
        if deduction < 0 or deduction > income:
            raise InvalidDeductionError()
        if tax_percentage < 0 or tax_percentage > 100:
            raise InvalidPercentageError()

        # Tax calculation
        tax = (income - deduction) * (tax_percentage / 100)
        return tax

    except (NonNumericIncomeError, NonNumericDeductionError, ZeroIncomeError, InvalidDeductionError, InvalidPercentageError) as e:
        print(f"Error: {e}")

