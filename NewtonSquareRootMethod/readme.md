In numerical analysis, Newton's method, also known as the Newton–Raphson method, named after Isaac Newton and Joseph Raphson, is a root-finding algorithm which produces successively better approximations to the roots (or zeroes) of a real-valued function. The most basic version starts with a single-variable function f defined for a real variable x, the function's derivative f ′, and an initial guess x0 for a root of f. If the function satisfies sufficient assumptions and the initial guess is close, then

{\displaystyle x_{1}=x_{0}-{\frac {f(x_{0})}{f'(x_{0})}}\,.}x_{1}=x_{0}-{\frac {f(x_{0})}{f'(x_{0})}}\,.
is a better approximation of the root than x0. Geometrically, (x1, 0) is the intersection of the x-axis and the tangent of the graph of f at (x0, f (x0)): that is, the improved guess is the unique root of the linear approximation at the initial point. The process is repeated as

{\displaystyle x_{n+1}=x_{n}-{\frac {f(x_{n})}{f'(x_{n})}}\,}x_{n+1}=x_{n}-{\frac {f(x_{n})}{f'(x_{n})}}\,
until a sufficiently precise value is reached. This algorithm is first in the class of Householder's methods, succeeded by Halley's method. The method can also be extended to complex functions and to systems of equations.
