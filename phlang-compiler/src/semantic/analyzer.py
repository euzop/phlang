from ..parser.ast import *

class SymbolTable:
    def __init__(self, parent=None):
        self.symbols = {}
        self.parent = parent
    
    def define(self, name, symbol_type):
        self.symbols[name] = symbol_type
    
    def lookup(self, name):
        if name in self.symbols:
            return self.symbols[name]
        
        if self.parent:
            return self.parent.lookup(name)
        
        return None
    
    def is_local(self, name):
        return name in self.symbols

class Symbol:
    def __init__(self, name, symbol_type):
        self.name = name
        self.type = symbol_type

class VariableSymbol(Symbol):
    def __init__(self, name, var_type):
        super().__init__(name, "variable")
        self.var_type = var_type

class FunctionSymbol(Symbol):
    def __init__(self, name, return_type, parameters=None):
        super().__init__(name, "function")
        self.return_type = return_type
        self.parameters = parameters or []

class SemanticAnalyzer:
    def __init__(self):
        self.current_scope = SymbolTable()
        self.errors = []
        self.current_function = None
    
    def analyze(self, program):
        self.visit(program)
        return self.errors
    
    def enter_scope(self):
        self.current_scope = SymbolTable(self.current_scope)
    
    def exit_scope(self):
        if self.current_scope.parent:
            self.current_scope = self.current_scope.parent
    
    def add_error(self, message):
        self.errors.append(message)
    
    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)
    
    def generic_visit(self, node):
        if hasattr(node, 'children'):
            for child in node.children:
                if child is not None:
                    self.visit(child)
    
    def visit_Program(self, node):
        for statement in node.statements:
            self.visit(statement)
    
    def visit_VariableDeclaration(self, node):
        var_name = node.var_name
        
        if self.current_scope.is_local(var_name):
            self.add_error(f"Ang variable na '{var_name}' ay naideklara na sa kasalukuyang scope")
            return
        
        var_symbol = VariableSymbol(var_name, node.var_type)
        self.current_scope.define(var_name, var_symbol)
        
        if node.initial_value:
            self.visit(node.initial_value)
    
    def visit_Assignment(self, node):
        var_name = node.var_name
        
        symbol = self.current_scope.lookup(var_name)
        if not symbol:
            self.add_error(f"Ang variable na '{var_name}' ay hindi pa naideklara bago itinala")
            return
        
        self.visit(node.value)
    
    def visit_FunctionDefinition(self, node):
        func_name = node.name
        
        if self.current_scope.is_local(func_name):
            self.add_error(f"Ang function na '{func_name}' ay nakatuklang muli")
            return
        
        func_symbol = FunctionSymbol(func_name, None, node.parameters)
        self.current_scope.define(func_name, func_symbol)
        
        prev_function = self.current_function
        self.current_function = func_symbol
        
        self.enter_scope()
        
        for param in node.parameters:
            param_symbol = VariableSymbol(param, None)
            self.current_scope.define(param, param_symbol)
        
        self.visit(node.body)
        
        self.current_function = prev_function
        self.exit_scope()
    
    def visit_FunctionCall(self, node):
        func_name = node.name
        
        symbol = self.current_scope.lookup(func_name)
        if not symbol:
            self.add_error(f"Hindi naideklara ang function na '{func_name}'")
            return
        
        if symbol.type != "function":
            self.add_error(f"Ang '{func_name}' ay hindi isang function")
            return
        
        if len(node.arguments) != len(symbol.parameters):
            self.add_error(f"Ang function na '{func_name}' ay tinawag na may maling bilang ng mga argumento. Inaasahan: {len(symbol.parameters)}, nakuha: {len(node.arguments)}")
        
        for arg in node.arguments:
            self.visit(arg)
    
    def visit_ReturnStatement(self, node):
        if not self.current_function:
            self.add_error("Hindi pinapayagan ang return statement sa labas ng function")
            return
        
        if node.value:
            self.visit(node.value)
    
    def visit_IfStatement(self, node):
        self.visit(node.condition)
        
        self.enter_scope()
        self.visit(node.then_block)
        self.exit_scope()
        
        if node.else_block:
            self.enter_scope()
            self.visit(node.else_block)
            self.exit_scope()
    
    def visit_WhileLoop(self, node):
        self.visit(node.condition)
        
        self.enter_scope()
        self.visit(node.body)
        self.exit_scope()
    
    def visit_ForLoop(self, node):
        self.visit(node.iterable)
        
        self.enter_scope()
        
        var_symbol = VariableSymbol(node.variable, None)
        self.current_scope.define(node.variable, var_symbol)
        
        self.visit(node.body)
        self.exit_scope()
    
    def visit_BreakStatement(self, node):
        pass
    
    def visit_ContinueStatement(self, node):
        pass
    
    def visit_PrintStatement(self, node):
        self.visit(node.expression)
    
    def visit_TryExcept(self, node):
        self.enter_scope()
        self.visit(node.try_block)
        self.exit_scope()
        
        self.enter_scope()
        exception_symbol = VariableSymbol(node.exception_var, None)
        self.current_scope.define(node.exception_var, exception_symbol)
        self.visit(node.except_block)
        self.exit_scope()
    
    def visit_Block(self, node):
        for stmt in node.statements:
            self.visit(stmt)
    
    def visit_BinaryOp(self, node):
        self.visit(node.left)
        self.visit(node.right)
    
    def visit_UnaryOp(self, node):
        self.visit(node.operand)
    
    def visit_Number(self, node):
        pass
    
    def visit_String(self, node):
        pass
    
    def visit_Identifier(self, node):
        if not self.current_scope.lookup(node.name):
            self.add_error(f"Ang variable na '{node.name}' ay ginamit bago pa naideklara")