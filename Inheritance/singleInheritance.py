class Parent:
    def __init__(self):
        print("Parent Constructor")
        self.eyes = 2
      
    def speak(self):
        print("I am a parent.")
      
class Child(Parent):
    def __init__(self):
        print("child constructor")
        self.age = 10
        super().__init__()
      
    def speak(self):
        print("I am a child")


c = Child()
print('C')
print(c.eyes)
c.speak()

p = Parent()
print('P')
print(p.eyes)
p.speak()
