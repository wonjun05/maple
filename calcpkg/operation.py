def add(a,b):
  return a+b
def minus(a,b):
  return a-b
def multi(a,b):
  try:
    return a*b
  except ZeroDivisionError as e:
    return e
def divide(a,b):
  return a/b