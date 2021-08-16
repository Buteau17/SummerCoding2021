class A:
    def a_method(self):
        print("This is a method form A")
class B(A):
    def b_method(self):
        print("This is a method form B")
class C(B):
    def c_method(self):
        print("This is a method form C")

c_object=C()
c_object.a_method()
c_object.b_method()
c_object.c_method()