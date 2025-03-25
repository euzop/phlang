class CompilerError(Exception):
    def __init__(self, message, line=None, column=None):
        self.message = message
        self.line = line
        self.column = column
        super().__init__(self.format_message())
    
    def format_message(self):
        if self.line is not None and self.column is not None:
            return f"Mali sa linya {self.line}, hanay {self.column}: {self.message}"
        elif self.line is not None:
            return f"Mali sa linya {self.line}: {self.message}"
        else:
            return f"Mali: {self.message}"

def report_error(error_message, line_number=None):
    if line_number is not None:
        print(f"Mali sa linya {line_number}: {error_message}")
    else:
        print(f"Mali: {error_message}")

def handle_syntax_error(line_number, token):
    report_error(f"Mali sa syntax: hindi inaasahang token '{token}'", line_number)

def handle_invalid_token(line_number, token):
    report_error(f"Hindi wastong token '{token}' ang natagpuan", line_number)

def handle_unexpected_eof(line_number):
    report_error("Hindi inaasahang pagtatapos ng file", line_number)

def handle_type_error(variable_name, expected_type, actual_type):
    report_error(f"Mali sa uri: ang variable na '{variable_name}' ay inaasahang uri '{expected_type}', ngunit '{actual_type}' ang nakuha")

def handle_undefined_variable(variable_name, line_number=None):
    report_error(f"Hindi nakatuklang variable: '{variable_name}'", line_number)

def handle_undefined_function(function_name, line_number=None):
    report_error(f"Hindi nakatuklang function: '{function_name}'", line_number)

def handle_argument_count_error(function_name, expected, actual, line_number=None):
    report_error(f"Ang function na '{function_name}' ay nangangailangan ng {expected} na mga argumento ngunit {actual} ang naibigay", line_number)

def handle_return_error(expected_type, actual_type, line_number=None):
    report_error(f"Hindi tugma ang uri ng return: inaasahan ay '{expected_type}', ngunit '{actual_type}' ang nakuha", line_number)

def handle_division_by_zero(line_number=None):
    report_error("Paghahati sa zero", line_number)

def handle_invalid_operation(operator, types, line_number=None):
    report_error(f"Hindi wastong operasyon: ang '{operator}' ay hindi maaaring gamitin sa {types}", line_number)

def handle_duplicate_declaration(name, line_number=None):
    report_error(f"Pagkakaulit ng deklarasyon: ang '{name}' ay naideklara na", line_number)

def handle_semantic_error(message, line_number=None):
    report_error(f"Mali sa semantiko: {message}", line_number)