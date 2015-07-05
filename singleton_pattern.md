### Singleton Pattern

Il singleton è un design pattern creazionale che ha lo scopo di garantire che di una determinata classe venga creata una e una sola istanza, e di fornire un punto di accesso globale a tale istanza.

Questo pattern viene utilizzato quando si desidera avere un unico punto di accesso. Per esempio si desidera avere solo un Window Manager oppure una sola Coda di Stampa oppure un unico accesso al database.

In Python abbiamo due metodi per creare un oggetto singleton.

Il primo metodo consiste nel creare una classe da estendere, tramite l'override del metodo __new__ così che nel momento in cui questa classe viene instanziata ne venga salvata una referenza, rendendo impossibile instanziarne un altra classe perchè già ne è presente un riferimento.

Il secondo consiste nell'uso di una metaclasse ma il comportamento è lo stesso del primo metodo.

Iniziamo dando uno sguardo al primo metodo, per il codice completo [singleton class]:

```python
class Singleton(object):
  _instance = None
  def __new__(self):
    if not isinstance(self._instance, self):
        self._instance = object.__new__(self)
        return self._instance

class MyClass(Singleton):
    pass
```

Ora vediamo il secondo metodo, per il codice completo [singleton metaclass]:

```python
class Singleton(type):
    _instances = None
    def __call__(self):
        if not isinstance(self._instance, self):
            self._instance = object.__new__(self)
            return self._instance

class MyClass(metaclass=Singleton):
    pass
```

[singleton class]:https://github.com/paranoiasystem/Patterns/blob/master/codice/singleton/singleton/class.py
[singleton metaclass]:https://github.com/paranoiasystem/Patterns/blob/master/codice/singleton/singleton/metaclass.py