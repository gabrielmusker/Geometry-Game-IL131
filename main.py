import SymPy as sp
x, y = sp.symbols('x y')
sp.plot3d(x*y, (x, -5, 5), (y, -5, 5))
