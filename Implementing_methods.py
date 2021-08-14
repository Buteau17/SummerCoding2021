class Teddy():
    quantity=200
    def __init__(self, name, color):
        self.name=name
        self.color=color
    def change_color(self, color):
        print("This is a method")
        self.color=color
        
    def change_name(self, name):
        print("This is a name")
        self.name=name
        
teddy1=Teddy("Bob", "Brown")
print(teddy1.name)
print(teddy1.color)

teddy1.change_color("Black")
print(teddy1.name)
print(teddy1.color)

teddy1.change_name("Ralph")
print(teddy1.name)
print(teddy1.color)