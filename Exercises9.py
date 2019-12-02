import sympy as sym
from sympy import *
from sympy import symbols
from sympy.plotting import plot
from sympy.plotting import plot3d
import xlsxwriter
from xlwt import Workbook, Formula
from xlrd import open_workbook
# =============================================================================
#                                   Exercise 1
# =============================================================================

#------------------------------------ A --------------------------------#
x = sym.symbols('x')
expr = x**2+x**3+21*x**4+10*x+1
print ( expr.subs(x, 7) )
#------------------------------------ B --------------------------------#
print(sym.expand((x+y)**2))
#------------------------------------ C --------------------------------#
print( sym.simplify((4*x**3 + 21*x**2 + 10*x + 12)))
#------------------------------------ D --------------------------------#
print(sym.limit(1/(x**2), x,sym.oo))
#------------------------------------ E --------------------------------#
i,n = sym.symbols('i, n')
print(sym.summation(2*i + i-1, (i, 5, n)))
#------------------------------------ F --------------------------------#
print(sym.integrate(sin(x) + exp(x)*cos(x)+tan(x), x))
#------------------------------------ G --------------------------------#
print( sym.factor(x**3 + 12*x*y*z + 3*y**2*z) )
#------------------------------------ H --------------------------------#
print (sym.solveset(x-4, x) )
#------------------------------------ I --------------------------------#
m1 = sym.Matrix([[5, 12, 40], [30, 70, 2]])
m2 = sym.Matrix([2, 1, 0])
print( m1*m2 )

#------------------------------------ J --------------------------------#
plot(x**3+3, (x, -10, 10))
#------------------------------------ K --------------------------------#

x, y = symbols('x y')
f=x**2*y**3
plot3d(f, (x, -6, 6), (y, -6, 6))

#-----------------------------------------------------------------------#

# =============================================================================
#                                   Exercise 2
# =============================================================================

workbook = xlsxwriter.Workbook('example.xlsx')
worksheet = workbook.add_worksheet()

str1 = 'This is Example'
str2 = 'My first export examlpe'

format1 = workbook.add_format({
		'bold': True,
		'font_color': 'red',
		'font_size': 14
		})

format2 = workbook.add_format({'font_size': 14})

worksheet.write('A1', str1, format1)
worksheet.write('A2', str2, format2)
worksheet.write('A3', 1, format2)
worksheet.write('A4', 2, format2)
worksheet.write('A5', 3, format1)

workbook.close()


# =============================================================================
#                                   Exercise 3
# =============================================================================

wb = open_workbook('sample.xlsx')

for s in wb.sheets():
    print('Sheet:',s.name)
    for row in range(s.nrows):
        values = []
        for col in range(s.ncols):
            values.append(s.cell(row, col).value)
        print(values)






























