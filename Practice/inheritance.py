# Single inherentitence: one child class---> one parent class
class parent:
    def __init__(self):
        self.overall_property=1000000
class child(parent):
    print("hello")
p=parent()
print(p.overall_property)
c=child()
print(f"child:{c.overall_property}")

# Multiple: more parent--->1 child
class father:
    def hello(self):
        print("I am Father")
class Mother:
    def hi(self):
        print("I am Mother")
class Child(father,Mother):
    print("Child")
f=father()
m=Mother()
c=Child()
print(c.hello(), c.hi())


# Multilevel:1 grandparent--->1 parent (child to grand parent)-->child
class GrandParent:
    def __init__(self):
        self.overall_property=1000000
class Father(GrandParent):
    def __init__(self):
        super().__init__()
        self.father_property=500000
class Child(Father):
    def __init__(self):
        super().__init__()
        self.child_property=100000

c=Child()
print(f"GrandParent:{c.overall_property}")
print(f"Father:{c.father_property}")
print(f"Child:{c.child_property}")

# Hierarchical: 1 parent---> multiple child
class Parent:
    def __init__(self):
        self.overall_property=1000000
class Child1(Parent):
    print("Child1")
class Child2(Parent):
    print("Child2")
p=Parent()
c1=Child1()
c2=Child2()
print(c1.overall_property)
print(c2.overall_property)

# Hybrid :combines multiple and multilevel inheritance
class A:
    def method_A(self):
        print("Method from class A")
class B:
    def method_B(self):
        print("Method from class B")
