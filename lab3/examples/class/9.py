class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"    

p1 = Person("John", 36)

print(p1)

# параметр self является ссылкой на текущий экземпляр класса и используется для доступа к переменным, принадлежащим классу.