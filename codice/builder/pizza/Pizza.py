from abc import ABCMeta, abstractmethod

class Pizza(object):
    __impasto = None
    __salsa = None
    __condimento = None

    def __init__(self):
        super().__init__()

    def setImpasto(self, impasto):
        self.__impasto = impasto

    def setSalsa(self, salsa):
        self.__salsa = salsa

    def setCondimento(self, condimento):
        self.__condimento = condimento

    def getImpasto(self):
        return self.__impasto

    def getSalsa(self):
        return self.__salsa

    def getCondimento(self):
        return self.__condimento

class PizzaBuilder(metaclass=ABCMeta):
    _pizza = None

    def __init__(self):
        super().__init__()

    def getPizza(self):
        return self._pizza

    def createNewPizzaProduct(self):
        self._pizza = Pizza()

    @abstractmethod
    def buildImpasto():
        pass

    @abstractmethod
    def buildSalsa():
        pass

    @abstractmethod
    def buildCondimento():
        pass

class Margherita(PizzaBuilder):
    def __init__(self):
        super().__init__()

    def buildImpasto(self):
        self._pizza.setImpasto("Normale");

    def buildSalsa(self):
        self._pizza.setSalsa("Pomodoro");

    def buildCondimento(self):
        self._pizza.setCondimento("Mozzarella")

class Napoli(PizzaBuilder):
    def __init__(self):
        super().__init__()
        
    def buildImpasto(self):
        self._pizza.setImpasto("Normale");

    def buildSalsa(self):
        self._pizza.setSalsa("Pomodoro");

    def buildCondimento(self):
        self._pizza.setCondimento("Origano")

class Cuoco(object):
    __pizzaBuilder = None

    def __init__(self):
        super().__init__()

    def setPizzaBuilder(self, obj):
        self.__pizzaBuilder = obj

    def getPizza(self):
        return self.__pizzaBuilder.getPizza()

    def constructPizza(self):
        self.__pizzaBuilder.createNewPizzaProduct()
        self.__pizzaBuilder.buildImpasto()
        self.__pizzaBuilder.buildSalsa()
        self.__pizzaBuilder.buildCondimento()


def main():
    cuoco = Cuoco()

    cuoco.setPizzaBuilder(Margherita())
    cuoco.constructPizza()

    pizza = cuoco.getPizza()

    print("Pizza\n" + "Impasto: " + pizza.getImpasto() + "\n" + "Salsa: " + pizza.getSalsa() + "\n" + "Condimento: " + pizza.getCondimento() + "\n")

if __name__ == '__main__':
    main()
