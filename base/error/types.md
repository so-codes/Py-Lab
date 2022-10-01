# ArithmeticError
It is raised when an arithmetic operation fails. For example, dividing by zero.

# AssertionError
It is raised when an assertion fails. For example, `assert 1 == 2`.

# AttributeError
It is raised when an attribute reference or assignment fails. For example, `x.y` where `y` is not an attribute of `x`.

# ImportError
It is raised when an import statement fails. For example, `import foo` where `foo` is not a module.

# IndexError
It is raised when an index is out of range. For example, `x[2]` where `x` has only one element.

# KeyError
It is raised when a key is not found in a dictionary. For example, `x['y']` where `x` has no key `'y'`.

# NameError
It is raised when a name is not found. For example, `x` where `x` is not defined.

# SystemExit
It is raised when the `sys.exit()` function is called.

# ValueError
It is raised when a built-in operation or function receives an argument that has the right type but an inappropriate value. For example, `int('foo')` where `foo` is not a number.

# ZeroDivisionError
It is raised when the second argument of a division or modulo operation is zero. For example, `1 / 0`.