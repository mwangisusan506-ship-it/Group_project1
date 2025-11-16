# main.py

# ===== Using math module =====
from math import sqrt, pi, ceil

print("Square root of 81:", sqrt(81))
print("Area of circle (radius 5):", pi * 5**2)
print("Ceiling of 7.2:", ceil(7.2))
print()


# ===== Using random module =====
import random

print("Random number (1–10):", random.randint(1, 10))
names = ["Susan", "Brian", "Kevin", "Ann"]
print("Random name:", random.choice(names))
print()


# ===== Using custom module =====
import s_modules

print(modules.greet("Susan"))
print("Sum of 5 and 10:", modules.add_numbers(5, 10))
