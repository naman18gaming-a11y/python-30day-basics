#Python Program to Compute a Polynomial Equation

a, b, c, d = 5, 5, 2, 3   # coefficients
x = 2                     

# Monomial
mono = -a**x
print("Monomial:", mono)

# Quadratic: ax^2 + bx + c
quadratic = a*x**2 + b*x + c
print("Quadratic:", quadratic)

# Cubic: ax^3 + bx^2 + cx + d
cubic = a*x**3 + b*x**2 + c*x + d
print("Cubic:", cubic)
