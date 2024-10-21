import sys
import os
import unittest
from unittest.mock import patch, MagicMock

# Asegúrate de que esta ruta sea correcta según tu estructura de carpetas
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../scr')))

# Importa la función que necesitas
from TaxCalculator.Database import (
    connect_db,
    create_tables,
    insert_user,
    get_user_by_email,
    get_user_by_id,
    update_user_email,
    delete_user,
    insert_calculation,
    get_user_calculations
)
from TaxCalculator.InputOutputFunctions import calculate_tax_value
from TaxCalculator.Exceptions import UserDontExist
from TaxCalculator.Calculator import search_user


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

class TestUserFunctions(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Método que se ejecuta una vez antes de todas las pruebas."""
        cls.test_username = "Test User"
        cls.test_email = "test_user@example.com"
        cls.updated_email = "updated_user@example.com"
        cls.invalid_email = "invalid_email"
        
        # Crea las tablas necesarias antes de ejecutar las pruebas
        create_tables()

    def test_insert_user(self):
        """Prueba que un usuario se inserta correctamente."""
        user_id = insert_user(self.test_username, self.test_email)
        self.assertIsNotNone(user_id, "El ID del usuario no debería ser None.")

    def test_get_user_by_email_found(self):
        """Prueba que se puede encontrar un usuario por su correo electrónico."""
        user = get_user_by_email(self.test_email)
        self.assertIsNotNone(user, "Se esperaba que se encontrara un usuario.")
        self.assertEqual(user[1], self.test_username, "El nombre del usuario no coincide.")

    def test_get_user_by_email_not_found(self):
        """Prueba que devuelve None si no se encuentra un usuario por su correo electrónico."""
        user = get_user_by_email("non_existent_user@example.com")
        self.assertIsNone(user, "Se esperaba que no se encontrara un usuario.")

    def test_update_user_email(self):
        """Prueba que se actualiza el correo electrónico de un usuario."""
        user_id = insert_user(self.test_username, self.test_email)
        update_user_email(user_id, self.updated_email)

        user = get_user_by_email(self.updated_email)
        self.assertIsNotNone(user, "Se esperaba que se encontrara el usuario.")
        self.assertEqual(user[2], self.updated_email, "El correo electrónico no se actualizó correctamente.")

    def test_delete_user(self):
        """Prueba que se puede eliminar un usuario de la base de datos."""
        user_id = insert_user(self.test_username, self.test_email)
        delete_user(user_id)

        user = get_user_by_email(self.test_email)
        self.assertIsNone(user, "Se esperaba que el usuario no se encontrara después de la eliminación.")

    def test_get_user_by_id(self):
        """Prueba que se puede obtener un usuario por su ID."""
        user_id = insert_user(self.test_username, self.test_email)
        user = get_user_by_id(user_id)
        self.assertIsNotNone(user, "Se esperaba que se encontrara un usuario.")
        self.assertEqual(user[1], self.test_username, "El nombre del usuario no coincide.")

    def test_get_user_calculations(self):
        """Prueba que se puede obtener cálculos de un usuario."""
        user_id = insert_user(self.test_username, self.test_email)
        insert_calculation(user_id, 50000, 5000, 5000, 45000)
        calculations = get_user_calculations(user_id)

        self.assertIsNotNone(calculations, "Se esperaba que se encontraran cálculos.")
        self.assertGreater(len(calculations), 0, "Se esperaba que hubiera al menos un cálculo.")

if __name__ == "__main__":
    unittest.main()
