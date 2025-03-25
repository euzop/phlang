from .tokens import Token, TokenType, KEYWORDS, OPERATORS, DELIMITERS

class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.position = 0
        self.line = 1
        self.column = 1
        self.current_char = self.source_code[self.position] if self.source_code else None
    
    def error(self):
        raise Exception(f'Hindi wastong karakter: "{self.current_char}" sa linya {self.line}, hanay {self.column}')
    
    def advance(self):
        if self.current_char == '\n':
            self.line += 1
            self.column = 1
        else:
            self.column += 1
            
        self.position += 1
        if self.position >= len(self.source_code):
            self.current_char = None
        else:
            self.current_char = self.source_code[self.position]
    
    def peek(self, n=1):
        peek_pos = self.position + n
        if peek_pos >= len(self.source_code):
            return None
        return self.source_code[peek_pos]
    
    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()
    
    def skip_comment(self):
        while self.current_char is not None and self.current_char != '\n':
            self.advance()
        
        if self.current_char == '\n':
            self.advance()
    
    def skip_c_style_comment(self):
        self.advance()  
        self.advance()  
        
        while self.current_char is not None and self.current_char != '\n':
            self.advance()
        
        if self.current_char == '\n':
            self.advance()
    
    def skip_c_style_multiline_comment(self):
        self.advance()  
        self.advance()  
        
        while self.current_char is not None:
            if self.current_char == '*' and self.peek() == '/':
                self.advance() 
                self.advance()  
                break
            self.advance()
    
    def identifier(self):
        start_column = self.column
        result = ''
        
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()
        
        if result in KEYWORDS:
            return Token(TokenType.KEYWORD, result, self.line, start_column)
        elif result in OPERATORS:
            return Token(TokenType.OPERATOR, result, self.line, start_column)
        else:
            return Token(TokenType.IDENTIFIER, result, self.line, start_column)
    
    def number(self):
        start_column = self.column
        result = ''
        is_float = False
        
        while self.current_char is not None and (self.current_char.isdigit() or self.current_char == '.'):
            if self.current_char == '.':
                if is_float: 
                    self.error()
                is_float = True
            result += self.current_char
            self.advance()
        
        if is_float:
            return Token(TokenType.NUMBER, float(result), self.line, start_column)
        else:
            return Token(TokenType.NUMBER, int(result), self.line, start_column)
    
    def string(self):
        start_column = self.column
        quote_char = self.current_char  
        self.advance()  
        result = ''
        
        while self.current_char is not None and self.current_char != quote_char:
            if self.current_char == '\\':
                self.advance()
                if self.current_char == 'n':
                    result += '\n'
                elif self.current_char == 't':
                    result += '\t'
                elif self.current_char == '\\':
                    result += '\\'
                elif self.current_char == quote_char:
                    result += quote_char
                else:
                    self.error()
            else:
                result += self.current_char
            self.advance()
        
        if self.current_char is None:
            raise Exception(f'Hindi nakumpleto ang string sa linya {self.line}, hanay {start_column}')
        
        self.advance() 
        return Token(TokenType.STRING, result, self.line, start_column)
    
    def operator(self):
        start_column = self.column
        op = self.current_char
        
        if (op in ['=', '!', '>', '<']) and self.peek() == '=':
            op += self.peek()
            self.advance() 
            self.advance() 
        else:
            self.advance()
        
        return Token(TokenType.OPERATOR, op, self.line, start_column)
    
    def delimiter(self):
        start_column = self.column
        delim = self.current_char
        self.advance()
        return Token(TokenType.DELIMITER, delim, self.line, start_column)
    
    def tokenize(self):
        tokens = []
        
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            
            if self.current_char == '#':
                self.skip_comment()
                continue
            
            if self.current_char == '/' and self.peek() == '/':
                self.skip_c_style_comment()
                continue
            
            if self.current_char == '/' and self.peek() == '*':
                self.skip_c_style_multiline_comment()
                continue
            
            if self.current_char.isalpha() or self.current_char == '_':
                tokens.append(self.identifier())
                continue
            
            if self.current_char.isdigit():
                tokens.append(self.number())
                continue
            
            if self.current_char in ['\'', '\"']:
                tokens.append(self.string())
                continue
            
            if self.current_char in '+-*/%=!><':
                tokens.append(self.operator())
                continue
            
            if self.current_char in '(){}[],.:;':
                tokens.append(self.delimiter())
                continue
            
            self.error()
        
        tokens.append(Token(TokenType.EOF, None, self.line, self.column))
        return tokens