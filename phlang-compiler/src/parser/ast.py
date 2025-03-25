class ASTNode:
    def __init__(self, node_type, children=None):
        self.node_type = node_type
        self.children = children if children is not None else []

    def __repr__(self):
        return f"{self.node_type}({', '.join(str(child) for child in self.children)})"


class Program(ASTNode):
    def __init__(self, statements):
        super().__init__('Program', statements)
        self.statements = statements

    def __repr__(self):
        return f"Program({len(self.statements)} statements)"


class Statement(ASTNode):
    def __init__(self, statement_type, children=None):
        super().__init__(statement_type, children)


class Expression(ASTNode):
    def __init__(self, expression_type, children=None):
        super().__init__(expression_type, children)


class BinaryOp(Expression):
    def __init__(self, left, operator, right):
        super().__init__('BinaryOp', [left, right])
        self.left = left
        self.operator = operator
        self.right = right

    def __repr__(self):
        return f"({self.left} {self.operator} {self.right})"


class UnaryOp(Expression):
    def __init__(self, operator, operand):
        super().__init__('UnaryOp', [operand])
        self.operator = operator
        self.operand = operand

    def __repr__(self):
        return f"{self.operator}({self.operand})"


class Number(Expression):
    def __init__(self, value):
        super().__init__('Number', [])
        self.value = value

    def __repr__(self):
        return str(self.value)


class String(Expression):
    def __init__(self, value):
        super().__init__('String', [])
        self.value = value

    def __repr__(self):
        return f'"{self.value}"'


class Identifier(Expression):
    def __init__(self, name):
        super().__init__('Identifier', [])
        self.name = name

    def __repr__(self):
        return self.name


class ArrayLiteral(Expression):
    def __init__(self, elements):
        super().__init__('ArrayLiteral', elements)
        self.elements = elements

    def __repr__(self):
        return f"[{', '.join(str(e) for e in self.elements)}]"


class ArrayIndexing(Expression):
    def __init__(self, array, index):
        super().__init__('ArrayIndexing', [array, index])
        self.array = array
        self.index = index

    def __repr__(self):
        return f"{self.array}[{self.index}]"


class VariableDeclaration(Statement):
    def __init__(self, var_name, var_type, initial_value=None):
        children = [var_name, var_type]
        if initial_value:
            children.append(initial_value)
        super().__init__('VariableDeclaration', children)
        self.var_name = var_name
        self.var_type = var_type
        self.initial_value = initial_value

    def __repr__(self):
        if self.initial_value:
            return f"var {self.var_name}: {self.var_type} = {self.initial_value}"
        return f"var {self.var_name}: {self.var_type}"


class Assignment(Statement):
    def __init__(self, var_name, value):
        super().__init__('Assignment', [value])
        self.var_name = var_name
        self.value = value

    def __repr__(self):
        return f"{self.var_name} = {self.value}"


class Block(Statement):
    def __init__(self, statements):
        super().__init__('Block', statements)
        self.statements = statements

    def __repr__(self):
        return f"Block({len(self.statements)} statements)"


class FunctionDefinition(Statement):
    def __init__(self, name, parameters, body):
        super().__init__('FunctionDefinition', [body])
        self.name = name
        self.parameters = parameters
        self.body = body

    def __repr__(self):
        params = ", ".join(self.parameters)
        return f"paraan {self.name}({params}) {{ ... }}"


class FunctionCall(Expression):
    def __init__(self, name, arguments):
        super().__init__('FunctionCall', arguments)
        self.name = name
        self.arguments = arguments

    def __repr__(self):
        args = ", ".join(str(arg) for arg in self.arguments)
        return f"{self.name}({args})"


class ReturnStatement(Statement):
    def __init__(self, value):
        super().__init__('ReturnStatement', [value])
        self.value = value

    def __repr__(self):
        return f"bumalik {self.value}"


class IfStatement(Statement):
    def __init__(self, condition, then_block, else_block=None):
        children = [condition, then_block]
        if else_block:
            children.append(else_block)
        super().__init__('IfStatement', children)
        self.condition = condition
        self.then_block = then_block
        self.else_block = else_block

    def __repr__(self):
        if self.else_block:
            return f"kung {self.condition} {{ ... }} kundi {{ ... }}"
        return f"kung {self.condition} {{ ... }}"


class WhileLoop(Statement):
    def __init__(self, condition, body):
        super().__init__('WhileLoop', [condition, body])
        self.condition = condition
        self.body = body

    def __repr__(self):
        return f"habang {self.condition} {{ ... }}"


class ForLoop(Statement):
    def __init__(self, variable, iterable, body):
        super().__init__('ForLoop', [iterable, body])
        self.variable = variable
        self.iterable = iterable
        self.body = body

    def __repr__(self):
        return f"para {self.variable} in {self.iterable} {{ ... }}"


class PrintStatement(Statement):
    def __init__(self, expression):
        super().__init__('PrintStatement', [expression])
        self.expression = expression

    def __repr__(self):
        return f"idikta {self.expression}"


class BreakStatement(Statement):
    def __init__(self):
        super().__init__('BreakStatement', [])

    def __repr__(self):
        return "itigil"


class ContinueStatement(Statement):
    def __init__(self):
        super().__init__('ContinueStatement', [])

    def __repr__(self):
        return "ituloy"


class TryExcept(Statement):
    def __init__(self, try_block, exception_var, except_block):
        super().__init__('TryExcept', [try_block, except_block])
        self.try_block = try_block
        self.exception_var = exception_var
        self.except_block = except_block

    def __repr__(self):
        return f"subukan {{ ... }} saluhin {self.exception_var} {{ ... }}"