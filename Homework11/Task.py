from sympy import *
from sympy.solvers import solve
from sympy.plotting import plot


x = Symbol('x')
f = -12 * x**4 *sin(cos(x)) - 18 * x**3 + 5 * x**2 + 10 * x - 30

plot(f, (x, -100, 100))
solution = solve(f, x)