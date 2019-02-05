"""Pythagoras theorem

This module contains some functions from the pythagorean theorem.
"""

from math import sqrt as _sqrt

def hypotenuse(a: float, b: float) -> float:
  "Returns the hypotenuse of the triangle described by the a and b cathetus."
  return _sqrt(a**2 + b**2)

def cathetus(h: float, c: float) -> float:
  "Returns the cathetus of the triangle described by the hypothenuse (h) and the other cathetus (c)."
  return _sqrt(h**2 - c**2)

if __name__ == "__main__":
  print("(f) hypotenuse(3, 4): %f" % hypotenuse(3, 4))
  print("(f) cathetus(5, 3):   %f" % cathetus(5, 3))
