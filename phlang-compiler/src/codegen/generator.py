from ..parser.ast import (
    Program, Statement, Expression, BinaryOp, UnaryOp,
    Number, String, Identifier, Assignment, VariableDeclaration,
    FunctionDefinition, FunctionCall, ReturnStatement,
    IfStatement, WhileLoop, ForLoop, 
    PrintStatement, BreakStatement, ContinueStatement,
    Block, TryExcept, ArrayLiteral, ArrayIndexing
)
from ..error.error_handler import translate_error

class CodeGenerator:
    def __init__(self, ast):
        self.ast = ast
        self.indent_level = 0
        self.output = []
        self.imports_added = False
    
    def indent(self):
        self.indent_level += 1
    
    def dedent(self):
        if self.indent_level > 0:
            self.indent_level -= 1
    
    def write(self, line):
        self.output.append('    ' * self.indent_level + line)
    
    def generate(self):
        self.write("from src.error.error_handler import translate_error")
        self.write("")
        self.visit(self.ast)
        return '\n'.join(self.output)
    
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
    
    def visit_Block(self, node):
        for stmt in node.statements:
            self.visit(stmt)
    
    def visit_VariableDeclaration(self, node):
        initial_value = "None"
        if node.initial_value:
            initial_value = self.generate_expression(node.initial_value)
        
        self.write(f"{node.var_name} = {initial_value}")
    
    def visit_Assignment(self, node):
        value = self.generate_expression(node.value)
        self.write(f"{node.var_name} = {value}")
    
    def visit_FunctionDefinition(self, node):
        params = ", ".join(node.parameters)
        self.write(f"def {node.name}({params}):")
        self.indent()
        
        if not node.body.statements:
            self.write("pass")
        else:
            self.visit(node.body)
        
        self.dedent()
        self.write("")
    
    def visit_ReturnStatement(self, node):
        if node.value:
            value = self.generate_expression(node.value)
            self.write(f"return {value}")
        else:
            self.write("return")
    
    def visit_IfStatement(self, node):
        condition = self.generate_expression(node.condition)
        self.write(f"if {condition}:")
        self.indent()
        
        self.visit(node.then_block)
        
        self.dedent()
        
        if node.else_block:
            if isinstance(node.else_block, IfStatement):
                cond = self.generate_expression(node.else_block.condition)
                self.write(f"elif {cond}:")
                self.indent()
                self.visit(node.else_block.then_block)
                self.dedent()
                
                if node.else_block.else_block:
                    if isinstance(node.else_block.else_block, IfStatement):
                        self.visit_IfStatement(node.else_block.else_block)
                    else:
                        self.write("else:")
                        self.indent()
                        self.visit(node.else_block.else_block)
                        self.dedent()
            else:
                self.write("else:")
                self.indent()
                self.visit(node.else_block)
                self.dedent()
    
    def visit_WhileLoop(self, node):
        condition = self.generate_expression(node.condition)
        self.write(f"while {condition}:")
        self.indent()
        
        if not node.body.statements:
            self.write("pass")
        else:
            self.visit(node.body)
        
        self.dedent()
    
    def visit_ForLoop(self, node):
        iterable = self.generate_expression(node.iterable)
        self.write(f"for {node.variable} in {iterable}:")
        self.indent()
        
        if not node.body.statements:
            self.write("pass")
        else:
            self.visit(node.body)
        
        self.dedent()
    
    def visit_PrintStatement(self, node):
        value = self.generate_expression(node.expression)
        self.write(f"print({value})")
    
    def visit_BreakStatement(self, node):
        self.write("break")
    
    def visit_ContinueStatement(self, node):
        self.write("continue")
    
    def visit_TryExcept(self, node):
        self.write("try:")
        self.indent()
        self.visit(node.try_block)
        self.dedent()
        
        self.write(f"except Exception as {node.exception_var}:")
        self.indent()
        self.write(f"{node.exception_var} = translate_error({node.exception_var})")
        self.visit(node.except_block)
        self.dedent()
    
    def generate_expression(self, node):
        if isinstance(node, Number):
            return str(node.value)
        
        elif isinstance(node, String):
            return f'"{node.value}"'
        
        elif isinstance(node, Identifier):
            return node.name
        
        elif isinstance(node, BinaryOp):
            left = self.generate_expression(node.left)
            right = self.generate_expression(node.right)
            
            op_map = {
                'at': 'and',
                'o': 'or',
                '==': '==',
                '!=': '!=',
                '<': '<',
                '>': '>',
                '<=': '<=',
                '>=': '>=',
                '+': '+',
                '-': '-',
                '*': '*',
                '/': '/',
                '%': '%'
            }
            
            op = op_map.get(node.operator, node.operator)
            
            # Special case for string concatenation with +
            if op == '+' and (
                isinstance(node.left, String) or 
                isinstance(node.right, String)
            ):
                return f"str({left}) + str({right})"
            
            return f"({left} {op} {right})"
        
        elif isinstance(node, UnaryOp):
            operand = self.generate_expression(node.operand)
            
            op_map = {
                '-': '-',
                'hindi': 'not '
            }
            
            op = op_map.get(node.operator, node.operator)
            return f"{op}({operand})"
        
        elif isinstance(node, FunctionCall):
            args = ", ".join(self.generate_expression(arg) for arg in node.arguments)
            
            if node.name == 'saklaw':
                return f"range({args})"
            
            return f"{node.name}({args})"
        
        elif isinstance(node, ArrayLiteral):
            elements = ", ".join(self.generate_expression(element) for element in node.elements)
            return f"[{elements}]"
        
        elif isinstance(node, ArrayIndexing):
            array = self.generate_expression(node.array)
            index = self.generate_expression(node.index)
            return f"{array}[{index}]"
        
        else:
            return str(node)