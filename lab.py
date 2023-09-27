
import math

eps = 0.01
x = 0.1
s = 0
fakt = 1
z1 = 1
i = 1
z = 1

while math.fabs(z) > eps:
    s = s + z
    fakt = fakt * i
    z1 = z1 * x
    z = z1 / fakt
    i = i + 1

print('S =', s)