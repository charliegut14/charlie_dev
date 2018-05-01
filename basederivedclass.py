class Parent():
    def __init__(self):
        self.parent = 'Parent Variable'
    def hello(self):
        print("I am a Parent Class")

class Child(Parent):
    def __init__(self):
        #super().__init__()
        self.child = 'Child Variable'
    def hellochild(self):
        print("I am a Child Class")
