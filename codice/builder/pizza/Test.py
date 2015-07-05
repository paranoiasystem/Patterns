from abc import ABCMeta, abstractmethod

class Test(metaclass=ABCMeta):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def saluta():
        pass

    @abstractmethod
    def saluta2():
        print("ciao")


class T(Test):

    def __init__(self):
        super().__init__()

    def saluta(self):
        print("asd")


def main():
    a = T()
    a.saluta()
    a.saluta2()

if __name__ == '__main__':
    main()
