### Builder Pattern

Il Builder Pattern separa la costruzione di un oggetto complesso dalla sua rappresentazione, in modo che il processo di costruzione stesso possa creare diverse rappresentazioni.

L'algoritmo per la creazione di un oggetto complesso è indipendente dalle varie parti che costituiscono l'oggetto e da come vengono assemblate.

Ciò ha l'effetto immediato di rendere più semplice la classe, permettendo a una classe builder separata di focalizzarsi sulla corretta costruzione di un'istanza e lasciando che la classe originale si concentri sul funzionamento degli oggetti. 

Questo è particolarmente utile quando volete assicurarvi che un oggetto sia valido prima di istanziarlo, e non volete che la logica di controllo appaia nei costruttori degli oggetti. Un builder permette anche di costruire un oggetto passo-passo.

Analizziamo la stuttura di questo pattern:

+   Builder(PizzaBuilder): specifica l'interfaccia astratta che crea le parti dell'oggetto Prodotto.
+   ConcreteBuilder(Margherita): costruisce e assembla le parti del prodotto implementando l'interfaccia Builder; definisce e tiene traccia della rappresentazione che crea.
+   Director(Cuoco): costruisce un oggetto utilizzando l'interfaccia Builder.
+   Product(Pizza): rappresenta l'oggetto complesso e include le classi che definiscono le parti che lo compongono, includendo le interfacce per assemblare le parti nel risultato finale.

![Builder UML](https://upload.wikimedia.org/wikipedia/it/1/14/Builder.png)

Passiamo ora ad un esempio con relativa spiegazione step-by-step. Per il codice completo andate qui [builder pizza].

Iniziamo a definire il nostro prodotto, ovvero la pizza:

```python
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
```

🐍 🐍 🐍 Python 🐍 🐍 🐍

Prima di continuare voglio analizzare con voi la seguente riga:

```python
from abc import ABCMeta, abstractmethod
```

Importiamo ABCMeta ed abstractmethod che ci consentiranno di creare dei metodi astratti tramite l'uso della metaclasse ABCMeta.

In programmazione a oggetti, una metaclasse è una classe le cui istanze sono a loro volta classi. Questo concetto è strettamente legato al concetto di riflessione (reflection), che si applica a quegli strumenti concettuali che permettono di rappresentare, all'interno di un programma, informazioni sulle parti costituenti del programma stesso (tipicamente classi e oggetti).

Questo ci permette di creare una specie di interfaccia in Python, ovvero ci da la possibilità di definire la firma dei metodi proprio come un interfaccia, l'importante è ricordarsi che questi sono dei metodi astratti.

Se proviamo ad instanziare una metaclasse che contiene dei metodi astratti a run-time riceveremo un errore del genere:

>   TypeError: Can't instantiate abstract class XXX with abstract methods 

Nell'[Abstract Factory](#abstract-factory) ho già spiegato il perchè non esistono le interfacce in Python.

(all'interno della cartella dove risiede il codice del [builder pizza] potete trovare un file Test.py che illustra questo comportamento)

🐍 🐍 🐍 Python 🐍 🐍 🐍

Continuiamo a vedere il codice, ora vedremo il Builder:

```python
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
```

In questa classe non c'è nulla di particolare da spiegare, quindi passiamo al codice del ConcreteBuilder:

```python
class Margherita(PizzaBuilder):
    def __init__(self):
        super().__init__()

    def buildImpasto(self):
        self._pizza.setImpasto("Normale");

    def buildSalsa(self):
        self._pizza.setSalsa("Pomodoro");

    def buildCondimento(self):
        self._pizza.setCondimento("Mozzarella")
```

🐍 🐍 🐍 Python 🐍 🐍 🐍

Qui possiamo notare come la classe Margherita che ha esteso la metaclasse ABCMeta ha implementato tutti i metodi che sono stati definiti @abstractmethod.

Nel caso in cui la classe che implementa la nostra meta classe non implementa tutti i metodi in essa definiti ricerveremo un errore del genere:

>   TypeError: Can't instantiate abstract class XXX with abstract methods

(all'interno della cartella dove risiede il codice del [builder pizza] potete trovare un file Test.py che illustra questo comportamento)

🐍 🐍 🐍 Python 🐍 🐍 🐍

Ora passiamo al codice del Director ovvero il Cuoco, cioè la classe che si occupa di costruire il nostro oggetto

```python
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
```

Ed ora passiamo al main:

```python
cuoco = Cuoco()

cuoco.setPizzaBuilder(Margherita())
cuoco.constructPizza()

pizza = cuoco.getPizza()
```

Analizziamo i vantaggi di questo pattern:

+   consente di cambiare la rappresentazione interna del prodotto: il Builder non conosce la rappresentazione interna del prodotto che può essere cambiata semplicemente costruendo un nuovo Builder.
+   isolamento tra Builder: ogni Builder è indipendente dall’altro pertanto è possibile aumentare la modularità.
+   controllo accurato del processo di creazione: la creazione avviene step-by-step e questo consente di stabilire passo dopo passo cosa effettuare.

Possiamo concludere dicendo che questo pattern consente di utilizzare un Client che non debba essere a conoscenza dei passi necessari al fine della creazione di un oggetto ma tali passaggi vengono delegati ad un Director che sa come fare.

[builder pizza]:https://github.com/paranoiasystem/Patterns/blob/master/codice/builder/pizza/Pizza.py