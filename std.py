class student:
    def __init__(self):
        self.name = "rama"
        self.age = 23
        self.quali = "BE"
        self.addr = "Bang"
    def eat(self):
        print("stud in eating")
    def study(self):
        print("i am sudeep")

s1=student()

print(s1.name)
print(s1.age)
print(s1.quali)
print(s1.addr)

s1.eat()

s1.study()