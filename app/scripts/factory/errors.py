"""
Error classes for bot constructor
"""


class FactoryArgumentError(Exception):
    """Exception raised for errors in the input factory arguments
    Attributes:
        code -- code error
        error_arg -- arg which raise error
        message -- explanation of the error
    """
    def __init__(self, code: int, error_arg: str = "", message: str = ""):
        self.message = message
        if not message:
            match code:
                case 1:
                    self.message = "Wrong argument format"
                case 2:
                    self.message = "Function argument set earlier than function"
                case 3:
                    self.message = "No arguments set in main.py"
                case 4:
                    self.message = "Executable function not found"
            if error_arg:
                self.message += f" >>> {error_arg}"

        super().__init__(self.message)
