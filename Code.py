from math import *
import os
x = float(input('x = '))
a = 0; n = 0; raz = 1;
while abs(raz) > 0.0001:
	b = a; a += (x**n)/factorial(n);