# @author: Saikat

import sys
import shape.Rectangle as rect
import ctypes

b = sys.maxsize
print(type(b))
c = 3 + 4j
print(type(c))
print(c.real)
print(c.imag)

r = rect.Rectangle(20, 50)
c = r

print("Perimeter of the rect is ", r.perimeter())
print("Area of the rectangle is ", r.area())

print("Ref count of r ", sys.getrefcount(r))
print(id(r))
print(ctypes.c_long.from_address(id(r)).value)
print(type(r))
