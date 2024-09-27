class ZeroIncomeError(Exception):
    """Raised when the income is equal to zero."""
    def __init__(self, message="Income cannot be zero"):
        self.message = message
        super().__init__(self.message)

class InvalidDeductionError(Exception):
    """Raised when an invalid deduction is entered (less than zero or greater than the income)."""
    def __init__(self, message="The deduction is not valid"):
        self.message = message
        super().__init__(self.message)

class InvalidPercentageError(Exception):
    """Raised when the tax percentage is less than 0 or greater than 100."""
    def __init__(self, message="The tax percentage must be between 0 and 100"):
        self.message = message
        super().__init__(self.message)

class NonNumericIncomeError(Exception):
    """Raised when a non-numeric value is entered for income."""
    def __init__(self, message="Income must be a number"):
        self.message = message
        super().__init__(self.message)

class NonNumericDeductionError(Exception):
    """Raised when a non-numeric value is entered for the deduction."""
    def __init__(self, message="Deduction must be a number"):
        self.message = message
        super().__init__(self.message)
