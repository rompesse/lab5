from dataclasses import dataclass
from math import sqrt
from typing import TypeAlias

# Створити ADT-тип (через добуток примітивних типів) для комплексних чисел 
# і реалізувати базову арифметику (додавання, віднімання, добуток, обчислення 
# спряженого числа, обчислення модуля комплексного числа).
@dataclass(frozen=True)
class Complex:
    a: float
    b: float

def add(c1: Complex, c2: Complex) -> Complex:
    match c1, c2:
        case Complex(a, b), Complex(c, d):
            return Complex(a + c, b + d)
        
def reduce(c1: Complex, c2: Complex) -> Complex:
    match c1, c2:
        case Complex(a, b), Complex(c, d):
            return Complex(a - c, b - d)
        
def multiply(с1: Complex, c2: Complex) -> Complex:
    match c1, c2:
        case Complex(a, b), Complex(c, d):
            return Complex(a*c - b*d, a*d + b*c)
        
def conjugate(c: Complex) -> Complex:
    match c:
        case Complex(a, b):
            return Complex(a, -b)
        
def abs_complex(c: Complex) -> float:
    match c:
        case Complex(a, b):
            return sqrt(a*a + b*b)
        
def to_string(c: MathTypes) -> str:
    match c:
        case Complex(a, b):
            sign = "+" if b >= 0 else "-"
            return f"{a} {sign} {abs(b)}i"
        case Vector3D(x, y, z):
            return f"({x}, {y}, {z})"
        case Matrix2(a, b, c, d):
            return f"{a:6.2f} {b:6.2f}\n{c:6.2f} {d:6.2f}"

c1 = Complex(3, 2)
c2 = Complex(-1, -5)
print(f"({to_string(c1)}) + ({to_string(c2)}) =", to_string(add(c1, c2))) 

c3 = Complex(3, 4)
c4 = Complex(1, 2)
print(f"({to_string(c3)}) - ({to_string(c4)}) =", to_string(reduce(c3, c4)))

c5 = Complex(3, 2)
c6 = Complex(1, -4)
print(f"({to_string(c5)}) * ({to_string(c6)}) =", to_string(multiply(c5, c6)))

c7 = Complex(3, 4)
print(f"|({to_string(c7)})| =", abs_complex(c7))

c8 = Complex(3, 4)
print(f"Спряжене ({to_string(c8)}) =", to_string(conjugate(c8)), "\n")

# Створити ADT для векторів у 3D (через добуток примітивних типів). 
# Реалізувати операції норми, скалярний, векторний добуток, змішаний добуток.
@dataclass(frozen=True)
class Vector3D:
    x: float
    y: float
    z: float

def norm(v: Vector3D) -> float:
    match v:
        case Vector3D(x, y, z):
            return sqrt(x*x + y*y + z*z)
        
def scalar_m(v1: Vector3D, v2: Vector3D) -> float:
    match v1, v2:
        case Vector3D(x1, y1, z1), Vector3D(x2, y2, z2):
            return x1*x2 + y1*y2 + z1*z2
        
def vector_m(v1: Vector3D, v2: Vector3D) -> Vector3D:
    match v1, v2:
        case Vector3D(x1, y1, z1), Vector3D(x2, y2, z2):
            return Vector3D(y1*z2 - z1*y2, z1*x2 - x1*z2, x1*y2 - y1*x2)
        
def mix_m(v1: Vector3D, v2: Vector3D, v3: Vector3D) -> float:
    return scalar_m(v1, vector_m(v2, v3))
        
v1 = Vector3D(3, 4, 0)
print(f"Норма вектору {to_string(v1)} =", norm(v1))

v2 = Vector3D(2, 1, 3)
v3 = Vector3D(4, -2, 5)
print(f"{to_string(v2)} * {to_string(v3)} =", scalar_m(v2, v3))

v4 = Vector3D(1, 2, 3)
v5 = Vector3D(4, 5, 6)
print(f"{to_string(v4)} x {to_string(v5)} =", to_string(vector_m(v4, v5)))

v6 = Vector3D(7, 8, -9)
print(f"{to_string(v4)} * ({to_string(v5)} x {to_string(v6)}) =", mix_m(v4, v5, v6), "\n")

#Добуток типів Matrix2. Операції: детермінант, обернена, добуток.
@dataclass(frozen=True)
class Matrix2:
    a11: float; a12: float
    a21: float; a22: float

def det(m: Matrix2) -> float:
    match m:
        case Matrix2(a, b, c, d):
            return a * d - b * c
        
def inverse(m: Matrix2) -> Matrix2:
    match m:
        case Matrix2(a, b, c, d):
            de = det(m)
            if (de == 0):
                print("Визначник дорівнює нулю. Неможливо створити обернену матрицю.")
                return m
            return Matrix2(d / de, -b / de, -c / de, a / de)
        
def matrix_multiply(m1: Matrix2, m2: Matrix2) -> Matrix2:
    match m1, m2:
        case Matrix2(a, b, c, d), Matrix2(e, f, g, h):
            return Matrix2(a*e + b*g, a*f + b*h, c*e + d*g, c*f + d*h)
        
MathTypes: TypeAlias = Complex | Vector3D | Matrix2
        
m1 = Matrix2(1, 5, 2, 10)
print(to_string(m1))
print(f"det(A) =", det(m1))

print("\nA^(-1)=")
print(to_string(inverse(m1)))

m2 = Matrix2(1, 2, 3, 4)
m3 = Matrix2(5, 6, 7, 8)

print("\nM=")
print(to_string(m2))

print("\nN=")
print(to_string(m3))

print("\nM*N=")
print(to_string(matrix_multiply(m2, m3)))