class TokenType:
    # Define token types
    IDENTIFIER = 'IDENTIFIER'
    KEYWORD = 'KEYWORD'
    NUMBER = 'NUMBER'
    STRING = 'STRING'
    OPERATOR = 'OPERATOR'
    DELIMITER = 'DELIMITER'
    COMMENT = 'COMMENT'
    WHITESPACE = 'WHITESPACE'
    EOF = 'EOF'

# Define keywords for PHLang
KEYWORDS = {
    'kung': TokenType.KEYWORD,      # if
    'kundi': TokenType.KEYWORD,     # else if
    'edi': TokenType.KEYWORD,       # else
    'idikta': TokenType.KEYWORD,    # print
    'habang': TokenType.KEYWORD,    # while
    'para': TokenType.KEYWORD,      # for
    'sa': TokenType.KEYWORD,        # in
    'saklaw': TokenType.KEYWORD,    # range
    'bumalik': TokenType.KEYWORD,   # return
    'itigil': TokenType.KEYWORD,    # break
    'ituloy': TokenType.KEYWORD,    # continue
    'paraan': TokenType.KEYWORD,    # def
    'klase': TokenType.KEYWORD,     # class
    'tama': TokenType.KEYWORD,      # true
    'mali': TokenType.KEYWORD,      # false
    'wala': TokenType.KEYWORD,      # none
    'subukan': TokenType.KEYWORD,   # try
    'saluhin': TokenType.KEYWORD,   # except
}

# Define operators for PHLang
OPERATORS = {
    '+': TokenType.OPERATOR,
    '-': TokenType.OPERATOR,
    '*': TokenType.OPERATOR,
    '/': TokenType.OPERATOR,
    '%': TokenType.OPERATOR,
    '=': TokenType.OPERATOR,
    '==': TokenType.OPERATOR,
    '!=': TokenType.OPERATOR,
    '<': TokenType.OPERATOR,
    '>': TokenType.OPERATOR,
    '<=': TokenType.OPERATOR,
    '>=': TokenType.OPERATOR,
    'at': TokenType.OPERATOR,
    'o': TokenType.OPERATOR,
    'hindi': TokenType.OPERATOR,
}

# Define delimiters for PHLang
DELIMITERS = {
    '(': TokenType.DELIMITER,
    ')': TokenType.DELIMITER,
    '{': TokenType.DELIMITER,
    '}': TokenType.DELIMITER,
    '[': TokenType.DELIMITER,
    ']': TokenType.DELIMITER,
    ',': TokenType.DELIMITER,
    '.': TokenType.DELIMITER,
    ';': TokenType.DELIMITER,
    ':': TokenType.DELIMITER,
}

class Token:
    def __init__(self, type, value, line, column):
        self.type = type
        self.value = value
        self.line = line
        self.column = column
    
    def __repr__(self):
        return f"Token({self.type}, '{self.value}', line={self.line}, col={self.column})"

__all__ = ['TokenType', 'Token', 'KEYWORDS', 'OPERATORS', 'DELIMITERS']