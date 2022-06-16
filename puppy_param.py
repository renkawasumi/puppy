# coding: utf-8
# Your code here!

m = 0.06
M = 0.315
r = 0.02825
J = 0.00115
L = 0.105
I = 0.0036973
g = 9.80665
D_theta = 0.0000002
D_psi = 0.0001

a = (m + M) * r**2 + J
b = M * r * L
c = M * L**2 + I
u = M * g * L

a_21 = a * u / (a * c - b**2)
a_22 = -a * D_theta / (a * c - b**2)
a_23 = (a + b) * D_psi / (a * c - b**2)
print(a_21, a_22, a_23)

a_31 = -(a + b) * u / (a * c - b**2)
a_32 = (a + b) * D_theta / (a * c - b**2)
a_33 = -(a + 2 * b + c) * D_psi / (a * c - b**2)
print(a_31, a_32, a_33)

b_2 = -(a + b) / (a * c - b**2)
b_3 = (a + 2 * b + c) / (a * c - b**2)
print(b_2, b_3)
