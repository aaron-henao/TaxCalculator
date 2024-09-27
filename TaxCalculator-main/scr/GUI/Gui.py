import sys
import os

# Add the parent directory to sys.path to allow imports from sibling directories
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup

from TaxCalculator.CalculationFunctions import (
    calculate_taxable_income,
    calculate_withholding_tax,
    calculate_social_security_contribution,
    calculate_pension_contribution,
    calculate_total_deductions,
    calculate_tax_payment_value
)

class ErrorPopup(Popup):
    def __init__(self, message, **kwargs):
        super().__init__(**kwargs)
        self.title = 'Error'
        self.size_hint = (None, None)
        self.size = (300, 200)
        
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        content.add_widget(Label(text=message))
        close_button = Button(text='Close', size_hint=(None, None), size=(100, 50))
        close_button.bind(on_press=self.dismiss)
        content.add_widget(close_button)
        
        self.content = content

class InputScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        layout.add_widget(Label(text='Tax Calculator', font_size=24))

        self.inputs = {}
        input_fields = [
            'Total Employment Income',
            'Other Income',
            'Withholding Tax',
            'Social Security Payments',
            'Pension Contributions',
            'Mortgage Payments',
            'Donations',
            'Education Expenses'
        ]

        for field in input_fields:
            box = BoxLayout()
            box.add_widget(Label(text=field, size_hint_x=0.4))
            text_input = TextInput(multiline=False, input_filter='float', size_hint_x=0.6)
            self.inputs[field] = text_input
            box.add_widget(text_input)
            layout.add_widget(box)

        self.calculate_button = Button(text='Calculate Taxes', on_press=self.calculate_taxes)
        layout.add_widget(self.calculate_button)

        self.add_widget(layout)

    def calculate_taxes(self, instance):
        try:
            # Check if all fields are filled
            for field, input_widget in self.inputs.items():
                if not input_widget.text.strip():
                    raise ValueError(f"Please fill in the {field} field.")

            # Get input values and perform calculations
            total_employment_income = float(self.inputs['Total Employment Income'].text)
            other_income = float(self.inputs['Other Income'].text)
            withholding_tax = float(self.inputs['Withholding Tax'].text)
            social_security_payments = float(self.inputs['Social Security Payments'].text)
            pension_contributions = float(self.inputs['Pension Contributions'].text)
            mortgage_payments = float(self.inputs['Mortgage Payments'].text)
            donations = float(self.inputs['Donations'].text)
            education_expenses = float(self.inputs['Education Expenses'].text)

            total_taxable_income = calculate_taxable_income(total_employment_income, other_income)
            withholding_tax = calculate_withholding_tax(total_taxable_income)
            social_security = calculate_social_security_contribution(total_taxable_income)
            pension = calculate_pension_contribution(total_taxable_income)
            total_deductions = calculate_total_deductions(
                social_security_payments, pension_contributions, mortgage_payments, donations, education_expenses
            )
            tax_payment = calculate_tax_payment_value(total_taxable_income, total_deductions)

            # Prepare result text
            result_text = (
                f"Total Taxable Income: {total_taxable_income:.2f}\n"
                f"Withholding Tax: {withholding_tax:.2f}\n"
                f"Social Security Contribution: {social_security:.2f}\n"
                f"Pension Contribution: {pension:.2f}\n"
                f"Total Deductions: {total_deductions:.2f}\n"
                f"Tax Payment: {tax_payment:.2f}"
            )

            # Switch to result screen and display results
            result_screen = self.manager.get_screen('result')
            result_screen.display_results(result_text)
            self.manager.current = 'result'

        except ValueError as e:
            # Show error popup
            error_popup = ErrorPopup(str(e))
            error_popup.open()

class ResultScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.result_label = Label(text='', size_hint_y=None, height=300)
        scroll_view = ScrollView(size_hint=(1, None), size=(self.width, 300))
        scroll_view.add_widget(self.result_label)
        layout.add_widget(scroll_view)

        self.back_button = Button(text='Back to Calculator', on_press=self.go_back)
        layout.add_widget(self.back_button)

        self.add_widget(layout)

    def display_results(self, result_text):
        self.result_label.text = result_text

    def go_back(self, instance):
        self.manager.current = 'input'

class TaxCalculatorApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InputScreen(name='input'))
        sm.add_widget(ResultScreen(name='result'))
        return sm

if __name__ == '__main__':
    TaxCalculatorApp().run()