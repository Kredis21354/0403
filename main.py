class Person:
  name = "Name"

  def __init__(self, name):
    self.name = name

class Dad(Person):
  name = "Ivan"
  age = 49
  
  def __init__(self):
    super().__init__("Dad")
  










  