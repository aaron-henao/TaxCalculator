import unittest
import sys
sys.path.append("scr")
from TaxCalculator.InputOutputFunctions import calculate_tax_value  # Import the function from the correct module

class TestTaxCalculator(unittest.TestCase):

    # Extraordinary test cases
    def test_extraordinary_tax_calculation_1(self):
        income = 10_000_000_000  # Extremely high income
        deductions = 500_000_000  # Significant deductions
        expected_result = 9_500_000_000  # Expected tax
        result = calculate_tax_value(income, deductions)
        self.assertEqual(result, expected_result)

    def test_extraordinary_tax_calculation_2(self):
        income = 1_000_000_000  # High income
        deductions = 0  # No deductions
        expected_result = 1_000_000_000  # Expected tax
        result = calculate_tax_value(income, deductions)
        self.assertEqual(result, expected_result)

    def test_extraordinary_tax_calculation_3(self):
        income = 0  # No income
        deductions = 1_000_000  # Applied deductions
        expected_result = 0  # Expected tax
        result = calculate_tax_value(income, deductions)
        self.assertEqual(result, expected_result)

    def test_extraordinary_tax_calculation_4(self):
        income = 10_000_000  # Moderately high income
        deductions = 10_000_000  # Deductions equal to income
        expected_result = 0  # Expected tax
        result = calculate_tax_value(income, deductions)
        self.assertEqual(result, expected_result)

    def test_extraordinary_tax_calculation_5(self):
        income = 100_000_000  # Significant income
        deductions = 1_000_000_000  # Deductions greater than income
        expected_result = 0  # Expected tax
        result = calculate_tax_value(income, deductions)
        self.assertEqual(result, expected_result)

    def test_extraordinary_tax_calculation_6(self):
        income = 500_000_000  # High income
        deductions = 250_000_000  # Significant deductions
        expected_result = 250_000_000  # Expected tax
        result = calculate_tax_value(income, deductions)
        self.assertEqual(result, expected_result)

    # Normal test cases
    def test_normal_tax_calculation_1(self):
        income = 100_000_000  # Normal income
        deductions = 10_000_000  # Normal deductions
        expected_result = 90_000_000  # Expected tax
        result = calculate_tax_value(income, deductions)
        self.assertEqual(result, expected_result)

    def test_normal_tax_calculation_2(self):
        income = 75_000_000  # Normal income
        deductions = 5_000_000  # Smaller deductions
        expected_result = 70_000_000  # Expected tax
        result = calculate_tax_value(income, deductions)
        self.assertEqual(result, expected_result)

    def test_normal_tax_calculation_3(self):
        income = 50_000_000  # Moderate income
        deductions = 10_000_000  # Moderate deductions
        expected_result = 40_000_000  # Expected tax
        result = calculate_tax_value(income, deductions)
        self.assertEqual(result, expected_result)

    def test_normal_tax_calculation_4(self):
        income = 25_000_000  # Moderate income
        deductions = 5_000_000  # Low deductions
        expected_result = 20_000_000  # Expected tax
        result = calculate_tax_value(income, deductions)
        self.assertEqual(result, expected_result)

    def test_normal_tax_calculation_5(self):
        income = 15_000_000  # Normal income
        deductions = 2_000_000  # Low deductions
        expected_result = 13_000_000  # Expected tax
        result = calculate_tax_value(income, deductions)
        self.assertEqual(result, expected_result)

    def test_normal_tax_calculation_6(self):
        income = 5_000_000  # Normal income
        deductions = 500_000  # Smaller deductions
        expected_result = 4_500_000  # Expected tax
        result = calculate_tax_value(income, deductions)
        self.assertEqual(result, expected_result)

    # Error test cases
    def test_error_negative_income(self):
        income = -100_000  # Negative income
        deductions = 50_000
        with self.assertRaises(ValueError):
            calculate_tax_value(income, deductions)

    def test_error_negative_deduction(self):
        income = 100_000
        deductions = -50_000  # Negative deduction
        with self.assertRaises(ValueError):
            calculate_tax_value(income, deductions)

    def test_error_negative_income_and_deductions(self):
        income = -100_000  # Negative income
        deductions = -50_000  # Negative deduction
        with self.assertRaises(ValueError):
            calculate_tax_value(income, deductions)

    def test_error_both_zero(self):
        income = 0  # Both values are zero
        deductions = 0
        expected_result = 0
        result = calculate_tax_value(income, deductions)
        self.assertEqual(result, expected_result)

    def test_error_deduction_greater_than_income(self):
        income = 100_000
        deductions = 200_000  # Deduction greater than income
        expected_result = 0
        result = calculate_tax_value(income, deductions)
        self.assertEqual(result, expected_result)

    def test_error_string_as_income(self):
        income = "one hundred thousand"  # String instead of number
        deductions = 50_000
        with self.assertRaises(ValueError):
            calculate_tax_value(income, deductions)

    def test_error_string_as_deduction(self):
        income = 100_000
        deductions = "fifty thousand"  # String instead of number
        with self.assertRaises(ValueError):
            calculate_tax_value(income, deductions)

    def test_error_incorrect_data_type(self):
        income = [100_000]  # List instead of number
        deductions = 50_000
        with self.assertRaises(TypeError):
            calculate_tax_value(income, deductions)

if __name__ == '__main__':
    unittest.main()
