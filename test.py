from sympy import symbols, cos, sin, sec, csc, tan, cot

# Define a symbol
x ,y= symbols('x y')

# Create expressions with trigonometric functions
expr1 = cos(y*x+x)
expr2 = sin(x)
expr3 = sec(x)
expr4 = csc(x)
expr5 = tan(x)
expr6 = x+cot(x)

from sympy.functions.elementary.trigonometric import TrigonometricFunction

# Assuming fun1 and fun2 are your functions
print(expr6.has(TrigonometricFunction))  # This will return True if fun1 is a trigonometric function
print(expr2.has(TrigonometricFunction))  # This will return False if fun2 is not a trigonometric function


# Extract the argument inside the trigonometric functions
arg1 = expr1.args[0]
arg2 = expr2.args[0]
arg3 = expr3.args[0]
arg4 = expr4.args[0]
arg5 = expr5.args[0]
arg6 = expr6.args[0]

# Print the extracted arguments
print("Argument inside cos(x):", arg1)
print("Argument inside sin(x):", arg2)
print("Argument inside sec(x):", arg3)
print("Argument inside csc(x):", arg4)
print("Argument inside tan(x):", arg5)
print("Argument inside cot(x):", arg6)
