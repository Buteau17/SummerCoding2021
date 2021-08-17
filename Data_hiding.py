class Myclass:
    __hiddenvariable = 0

    def add(self,increment):
        self.__hiddenvariable += increment
        print(self.__hiddenvariable)

objectone = Myclass()
objectone.add(5)
print(objectone.hiddenvariable)

