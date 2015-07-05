### Prototype Pattern

Il prototype pattern permette di creare nuovi oggetti clonando un oggetto iniziale, detto appunto prototipo. A differenza di altri pattern come Abstract factory o Factory method permette di specificare nuovi oggetti a tempo d'esecuzione (run-time), utilizzando un gestore di prototipi (prototype manager) per salvare e reperire dinamicamente le istanze degli oggetti desiderati.

Esso è uno dei design pattern fondamentali definiti dalla cosiddetta gang of four.

Durante la creazione del clone dell’oggetto occorre prestare molta attenzione alla creazione degli oggetti annidati. Una classe può contenere al suo interno dei riferimenti ad altre classi pertanto la clonazione dell’oggetto principale deve effettuare la clonazione anche di tutti gli altri oggetti al suo interno. La clonazione dell’intero albero degli oggetti genera un clone detto deep-clone ossia clone-approfondito in quanto copia di tutti gli oggetti presenti. Se la clonazione si limita solo all’oggetto principale “contenitore” allora nel clone verranno mantenuti gli stessi  riferimenti agli oggetti secondari in questo caso si parla di shallow-clone ossia di clone-superficiale.

Vediamone la struttura:

+   Prototype: definisce un'interfaccia per clonare sé stesso.
+   ConcretePrototype: Le sottoclassi ConcretePrototype implementano l'interfaccia di Prototype, fornendo un'operazione per clonare sé stessi.
+   Client: crea un nuovo oggetto del tipo desiderato chiedendo a un prototipo di clonarsi, ovvero invocando il metodo clone definito da ConcretePrototype.

![Prototype Pattern](https://upload.wikimedia.org/wikipedia/commons/1/14/Prototype_UML.svg)

Per il codice completo: [prototype cookie]
Vediamone subito il codice, iniziamo dalla nostra prototype class:

```python
class Cookie:
    def __init__(self, name):
        self.name = name
    
    def clone(self):
        return copy.deepcopy(self)
```

Ora passiamo ai ConcretePrototype:

```python
class CoconutCookie(Cookie):
    def __init__(self):
        Cookie.__init__(self, 'Coconut')
        
class ChocolateCookie(Cookie):
    def __init__(self):
        Cookie.__init__(self, 'Chocolate')
```

Ed ora il nostro client e main:

```python
class CookieMachine:
    def __init__(self, cookie):
        self.cookie = cookie
 
    def make_cookie(self):
        return self.cookie.clone()


prot = CoconutCookie()
cm = CookieMachine(prot)

for i in range(10):
    temp_cookie = cm.make_cookie()
```

Tale pattern presenta i seguenti vantaggi/svantaggi:
-   aggiungere/rimuovere prodotti a RunTime: è possibile decidere a Runtime se aggiungere nuovi oggetti
-   specificare nuovi oggetti cambiando il loro valore: invece di creare nuove classi per definire nuovi comportamenti, possiamo cambiare il valore di un oggetto per definire un nuovo comportamento. In questo modo vengono ridotti i numeri delle classi.

[prototype cookie]:https://github.com/paranoiasystem/Patterns/blob/master/codice/prototype/cookie/cookie.py