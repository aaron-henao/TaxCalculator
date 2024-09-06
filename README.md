# Tax Calculator
The "Tax Calculator" project aims to develop an application to calculate the income tax return of an employee. The application will take into account various inputs, such as employment income, other income, withholdings, social security payments, pension contributions, mortgage loans, donations, and education expenses for the year. With this information, you will calculate the taxed and untaxed income, the deductible costs, and finally determine the amount to be paid for income tax. This tool will make it easier for employees to calculate and submit their annual income tax return.

## Characteristics

- Automates the calculation of income tax, minimizing errors and saving time.
- Allows entry of multiple sources of income and deductions.
- Calculate deductions and exemptions to obtain the final tax to pay.
- Generate detailed reports with a clear tax summary.
- It has a simple interface to facilitate use by anyone.
- It is updated according to current tax laws.
- It is accessible from any device and protects the confidentiality of data.

 ## How Do I Run It?
 # Prerequisites
Make sure you have Python installed on your system. No additional external dependencies are required to run the project.

 # Running the Program
To run the program outside of the development environment:

Navigate to the folder: Once you have cloned or downloaded the project, open the command prompt (cmd) or Anaconda Prompt, and navigate to the folder where you saved the project files. For example:

```bash

 "cd C:\Users\TuUsuario\Desktop\CalculadoraDeImpuestos"

````


Run the main script:

```bash

python scr/console.py

```

# How Is It Made?
 ## Project Architecture
The project is organized into two main folders:

scr: Contains the application's source code.
test: Contains unit tests to validate the functionality of the code.

## Module Organization
scr/console.py: Main file for user interaction. Collects user inputs and displays the results.
scr/FuncionesDeCalculo.py: Contains the logic functions for tax calculation, including input validation and tax computation.
scr/FuncionesDeEntradaySalida.py: Manages tax rates, deductions, and handles input/output operations.
# Dependencies
The project does not require external dependencies. It relies on Python's standard libraries.

# Usage
To run the unit tests from the test folder, use the following command:

```bash


python test/unit_tests.py

```

To run the main file, which launches the tax calculator console:

```bash

python scr/console.py

```

## System Requirements

- Python 3.x instalado.

## Members

- Juan Manuel García Gómez (jmgg1326)
- Santiago Perez Jimenez (santti19perez)
- Juan Felipe Ruiz Yepes (pipe0001)

