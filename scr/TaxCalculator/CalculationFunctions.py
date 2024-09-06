# Global Variables
withholding_tax_rate = 0.035  # Withholding tax percentage (example)
social_security_rate = 0.04  # Social security percentage
pension_contribution_rate = 0.04  # Pension contribution percentage
income_tax_rate = 0.19  # Income tax rate (example)

# Calculation Functions

def calculate_taxable_income(total_employment_income, other_income_value):
    """Calculates the total taxable income."""
    return total_employment_income + other_income_value

def calculate_non_taxable_income(total_non_taxable_income):
    """Returns the value of non-taxable income."""
    return total_non_taxable_income

def calculate_withholding_tax(total_taxable_income):
    """Calculates withholding tax."""
    return total_taxable_income * withholding_tax_rate

def calculate_social_security_contribution(total_taxable_income):
    """Calculates the social security contribution."""
    return total_taxable_income * social_security_rate

def calculate_pension_contribution(total_taxable_income):
    """Calculates the pension contribution."""
    return total_taxable_income * pension_contribution_rate

def calculate_total_deductions(social_security_payments, pension_contributions, mortgage_payments, donations_value, education_expenses):
    """Calculates the total deductions."""
    return social_security_payments + pension_contributions + mortgage_payments + donations_value + education_expenses

def calculate_tax_payment_value(total_taxable_income, total_deductible_expenses):
    """Calculates the amount to be paid in income tax."""
    taxable_base = total_taxable_income - total_deductible_expenses
    return taxable_base * income_tax_rate

def calculate_net_tax(gross_income, deductions, tax_rate, tax_credits):
    """Calculates the net tax payable."""
    net_income = gross_income - deductions
    if net_income < 0:
        net_income = 0  # Net income cannot be negative
    gross_tax = net_income * tax_rate
    net_tax = gross_tax - tax_credits
    if net_tax < 0:
        net_tax = 0  # Net tax cannot be negative
    return net_tax
