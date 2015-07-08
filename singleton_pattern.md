### Singleton Pattern

Il singleton è un design pattern creazionale che ha lo scopo di garantire che di una determinata classe venga creata una e una sola istanza, e di fornire un punto di accesso globale a tale istanza.

Questo pattern viene utilizzato quando si desidera avere un unico punto di accesso. Per esempio si desidera avere solo un Window Manager oppure una sola Coda di Stampa oppure un unico accesso al database.

In Python abbiamo un semplice metodo per creare un Singleton.

Questo consiste nell'uso di una metaclasse:

```python
class Singleton(type):
    _instance = None
    def __call__(self):
        if not isinstance(self._instance, self):
            self._instance = object.__new__(self)
            self._instance.__init__()
        return self._instance


class MyClass(metaclass = Singleton):
    def __init__(self):
      # il costruttore
```

[singleton class]:https://github.com/paranoiasystem/Patterns/blob/master/codice/singleton/singleton/class.py
[singleton metaclass]:https://github.com/paranoiasystem/Patterns/blob/master/codice/singleton/singleton/metaclass.py
