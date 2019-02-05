from math import sqrt as _sqrt

def hypotenuse(a, b):
  return _sqrt(a**2 + b**2)

def cathetus(h, c):
  return _sqrt(h**2 - c**2)

if __name__ == "__main__":
  print("(f) hypotenuse(3, 4): %f" % hypotenuse(3, 4))
  print("(f) cathetus(5, 3):   %f" % cathetus(5, 3))
