from ..lexer.tokens import TokenType, Token

from .ast import (
    Program, Statement, Expression, BinaryOp, UnaryOp,
    Number, String, Identifier, Assignment, VariableDeclaration,
    FunctionDefinition, FunctionCall, ReturnStatement,
    IfStatement, WhileLoop, ForLoop, 
    PrintStatement, BreakStatement, ContinueStatement,
    Block, TryExcept
)

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.position = -1
        self.next_token()

    def next_token(self):
        self.position += 1
        if self.position < len(self.tokens):
            self.current_token = self.tokens[self.position]
        else:
            self.current_token = None

    def peek_token(self, n=1):
        peek_pos = self.position + n
        if peek_pos < len(self.tokens):
            return self.tokens[peek_pos]
        return None

    def expect(self, token_type, value=None):
        if self.current_token is None:
            self.error(f"Inaasahan ang {token_type} ngunit naabot na ang katapusan ng input")
        
        if self.current_token.type != token_type:
            self.error(f"Inaasahan ang {token_type} ngunit nakakuha ng {self.current_token.type}")
        
        if value is not None and self.current_token.value != value:
            self.error(f"Inaasahan ang '{value}' ngunit nakakuha ng '{self.current_token.value}'")
        
        token = self.current_token
        self.next_token()
        return token

    def parse(self):
        return self.program()

    def program(self):
        statements = []
        while self.current_token is not None and self.current_token.type != TokenType.EOF:
            statements.append(self.statement())
        
        return Program(statements)

    def statement(self):
        if self.current_token.type == TokenType.KEYWORD:
            if self.current_token.value == 'paraan':
                return self.function_definition()
            elif self.current_token.value == 'kung':
                return self.if_statement()
            elif self.current_token.value == 'habang':
                return self.while_loop()
            elif self.current_token.value == 'para':
                return self.for_loop()
            elif self.current_token.value == 'bumalik':
                return self.return_statement()
            elif self.current_token.value == 'idikta':
                return self.print_statement()
            elif self.current_token.value == 'itigil':
                return self.break_statement()
            elif self.current_token.value == 'ituloy':
                return self.continue_statement()
            elif self.current_token.value == 'subukan':
                return self.try_except_statement()
        
        if self.current_token.type == TokenType.IDENTIFIER:
            if self.peek_token() and self.peek_token().type == TokenType.OPERATOR and self.peek_token().value == '=':
                return self.assignment_statement()
        
        expr = self.expression()
        
        if (self.current_token and self.current_token.type == TokenType.DELIMITER 
            and self.current_token.value == ';'):
            self.next_token()
        
        return expr

    def block(self):
        self.expect(TokenType.DELIMITER, '{')
        statements = []
        
        while self.current_token is not None and self.current_token.type != TokenType.DELIMITER and self.current_token.value != '}':
            statements.append(self.statement())
        
        self.expect(TokenType.DELIMITER, '}')
        return Block(statements)

    def function_definition(self):
        self.expect(TokenType.KEYWORD, 'paraan')
        name = self.expect(TokenType.IDENTIFIER).value
        
        self.expect(TokenType.DELIMITER, '(')
        parameters = self.parameter_list()
        self.expect(TokenType.DELIMITER, ')')
        
        body = self.block()
        return FunctionDefinition(name, parameters, body)

    def parameter_list(self):
        parameters = []
        
        if self.current_token.type == TokenType.DELIMITER and self.current_token.value == ')':
            return parameters
        
        parameters.append(self.expect(TokenType.IDENTIFIER).value)
        
        while self.current_token.type == TokenType.DELIMITER and self.current_token.value == ',':
            self.next_token()
            parameters.append(self.expect(TokenType.IDENTIFIER).value)
        
        return parameters

    def if_statement(self):
        self.expect(TokenType.KEYWORD, 'kung')
        condition = self.expression()
        then_block = self.block()
        
        else_block = None
        
        if self.current_token and self.current_token.type == TokenType.KEYWORD and self.current_token.value == 'kundi':
            self.next_token()
            
            elif_condition = self.expression()
            elif_block = self.block()
            
            if self.current_token and self.current_token.type == TokenType.KEYWORD and self.current_token.value == 'edi':
                self.next_token()
                else_block = self.block()
                
                elif_statement = IfStatement(elif_condition, elif_block, else_block)
                return IfStatement(condition, then_block, elif_statement)
            else:
                return IfStatement(condition, then_block, IfStatement(elif_condition, elif_block, None))
        
        elif self.current_token and self.current_token.type == TokenType.KEYWORD and self.current_token.value == 'edi':
            self.next_token()
            else_block = self.block()
        
        return IfStatement(condition, then_block, else_block)

    def while_loop(self):
        self.expect(TokenType.KEYWORD, 'habang')
        condition = self.expression()
        body = self.block()
        return WhileLoop(condition, body)

    def for_loop(self):
        self.expect(TokenType.KEYWORD, 'para')
        variable = self.expect(TokenType.IDENTIFIER).value
        
        self.expect(TokenType.KEYWORD, 'in')
        iterable = self.expression()
        
        body = self.block()
        return ForLoop(variable, iterable, body)

    def return_statement(self):
        self.expect(TokenType.KEYWORD, 'bumalik')
        value = self.expression()
        
        if (self.current_token and self.current_token.type == TokenType.DELIMITER 
            and self.current_token.value == ';'):
            self.next_token()
            
        return ReturnStatement(value)

    def print_statement(self):
        self.expect(TokenType.KEYWORD, 'idikta')
        value = self.expression()
        
        if (self.current_token and self.current_token.type == TokenType.DELIMITER 
            and self.current_token.value == ';'):
            self.next_token()
            
        return PrintStatement(value)

    def break_statement(self):
        self.expect(TokenType.KEYWORD, 'itigil')
        
        if (self.current_token and self.current_token.type == TokenType.DELIMITER 
            and self.current_token.value == ';'):
            self.next_token()
            
        return BreakStatement()

    def continue_statement(self):
        self.expect(TokenType.KEYWORD, 'ituloy')
        
        if (self.current_token and self.current_token.type == TokenType.DELIMITER 
            and self.current_token.value == ';'):
            self.next_token()
            
        return ContinueStatement()

    def try_except_statement(self):
        self.expect(TokenType.KEYWORD, 'subukan')
        try_block = self.block()
        
        self.expect(TokenType.KEYWORD, 'saluhin')
        exception_var = self.expect(TokenType.IDENTIFIER).value
        except_block = self.block()
        
        return TryExcept(try_block, exception_var, except_block)

    def assignment_statement(self):
        identifier = self.expect(TokenType.IDENTIFIER).value
        self.expect(TokenType.OPERATOR, '=')
        value = self.expression()
        
        if (self.current_token and self.current_token.type == TokenType.DELIMITER 
            and self.current_token.value == ';'):
            self.next_token()
            
        return Assignment(identifier, value)

    def expression(self):
        return self.logical_or()

    def logical_or(self):
        node = self.logical_and()
        
        while self.current_token is not None and self.current_token.type == TokenType.OPERATOR and self.current_token.value == 'or':
            op = self.current_token.value
            self.next_token()
            right = self.logical_and()
            node = BinaryOp(node, op, right)
        
        return node

    def logical_and(self):
        node = self.equality()
        
        while self.current_token is not None and self.current_token.type == TokenType.OPERATOR and self.current_token.value == 'and':
            op = self.current_token.value
            self.next_token()
            right = self.equality()
            node = BinaryOp(node, op, right)
        
        return node

    def equality(self):
        node = self.comparison()
        
        while (self.current_token is not None and self.current_token.type == TokenType.OPERATOR 
              and self.current_token.value in ('==', '!=')):
            op = self.current_token.value
            self.next_token()
            right = self.comparison()
            node = BinaryOp(node, op, right)
        
        return node

    def comparison(self):
        node = self.term()
        
        while (self.current_token is not None and self.current_token.type == TokenType.OPERATOR 
              and self.current_token.value in ('<', '>', '<=', '>=')):
            op = self.current_token.value
            self.next_token()
            right = self.term()
            node = BinaryOp(node, op, right)
        
        return node

    def term(self):
        node = self.factor()
        
        while (self.current_token is not None and self.current_token.type == TokenType.OPERATOR 
              and self.current_token.value in ('+', '-')):
            op = self.current_token.value
            self.next_token()
            right = self.factor()
            node = BinaryOp(node, op, right)
        
        return node

    def factor(self):
        node = self.unary()
        
        while (self.current_token is not None and self.current_token.type == TokenType.OPERATOR 
              and self.current_token.value in ('*', '/', '%')):
            op = self.current_token.value
            self.next_token()
            right = self.unary()
            node = BinaryOp(node, op, right)
        
        return node

    def unary(self):
        if self.current_token is not None and self.current_token.type == TokenType.OPERATOR:
            if self.current_token.value in ('-', 'not'):
                op = self.current_token.value
                self.next_token()
                operand = self.unary()
                return UnaryOp(op, operand)
        
        return self.primary()

    def primary(self):
        token = self.current_token
        
        if token.type == TokenType.NUMBER:
            self.next_token()
            return Number(token.value)
        
        elif token.type == TokenType.STRING:
            self.next_token()
            return String(token.value)
        
        elif token.type == TokenType.IDENTIFIER:
            if self.peek_token() and self.peek_token().type == TokenType.DELIMITER and self.peek_token().value == '(':
                return self.function_call()
            else:
                self.next_token()
                return Identifier(token.value)
        
        elif token.type == TokenType.DELIMITER and token.value == '(':
            self.next_token()
            expr = self.expression()
            self.expect(TokenType.DELIMITER, ')')
            return expr
        
        self.error(f"Hindi inaasahang token: {token}")

    def function_call(self):
        name = self.expect(TokenType.IDENTIFIER).value
        self.expect(TokenType.DELIMITER, '(')
        arguments = self.argument_list()
        self.expect(TokenType.DELIMITER, ')')
        return FunctionCall(name, arguments)

    def argument_list(self):
        arguments = []
        
        if self.current_token.type == TokenType.DELIMITER and self.current_token.value == ')':
            return arguments
        
        arguments.append(self.expression())
        
        while self.current_token.type == TokenType.DELIMITER and self.current_token.value == ',':
            self.next_token()
            arguments.append(self.expression())
        
        return arguments

    def error(self, message):
        token = self.current_token
        if token:
            line = token.line
            column = token.column
            raise Exception(f"Mali sa pag-parse sa linya {line}, hanay {column}: {message}")
        else:
            raise Exception(f"Mali sa pag-parse: {message}")