class SymbolTable:
    def __init__(self):
        self.symbols = {}
        self.scopes = [{}]
    
    def enter_scope(self):
        self.scopes.append({})
    
    def exit_scope(self):
        if len(self.scopes) > 1:
            self.scopes.pop()
    
    def define(self, name, symbol):
        self.scopes[-1][name] = symbol
        return symbol
    
    def lookup(self, name):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        return None
    
    def lookup_current_scope(self, name):
        return self.scopes[-1].get(name)
    
    def is_global_scope(self):
        return len(self.scopes) == 1
    
    def current_scope_level(self):
        return len(self.scopes) - 1
    
    def __str__(self):
        result = "Symbol Table:\n"
        for i, scope in enumerate(self.scopes):
            result += f"Scope {i}: {scope}\n"
        return result

class Symbol:
    def __init__(self, name):
        self.name = name

class VariableSymbol(Symbol):
    def __init__(self, name, var_type=None):
        super().__init__(name)
        self.var_type = var_type
    
    def __str__(self):
        return f"Variable({self.name}, {self.var_type})"
    
    def __repr__(self):
        return self.__str__()

class FunctionSymbol(Symbol):
    def __init__(self, name, params=None, return_type=None):
        super().__init__(name)
        self.params = params or []
        self.return_type = return_type
    
    def __str__(self):
        params_str = ", ".join([str(p) for p in self.params])
        return f"Function({self.name}, params=[{params_str}], returns={self.return_type})"
    
    def __repr__(self):
        return self.__str__()