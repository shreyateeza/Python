# PUBLIC
class Student:
  name = None
  psp = None

  def __init__(self, name, psp):
    self.name = name
    self.psp = psp

  def printName():
    print('Name: ', self.name)

# PRIVATE
class privateStudent:
  def __init__(self, name):
    self.__name = name

  def printName():
    print('Name: ', self.__name)

# PROTECTED
class protectedStudent:
  def __init__(self, name):
    self._name = name

  def printName():
    print('Name: ', self._name)
