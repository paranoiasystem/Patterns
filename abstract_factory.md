### Abstract Factory

L'Abstract factory fornisce un'interfaccia per creare famiglie di oggetti connessi o dipendenti tra loro, in modo che non ci sia necessità da parte degli utilizzatori di specificare i nomi delle classi concrete all'interno del proprio codice.

L'Abstract factory è uno dei fondamentali design pattern creazionali della programmazione orientata agli oggetti.

Questo pattern è utile quando vogliamo creare oggetti complessi che sono composti da altri oggetti e dove gli oggetti composti sono tutti di una particolare famiglia.

Per esempio, in un sistema di GUI dove potremmo avere un Abstract Factory che ha tre sottoclassi (Linux,Windows,OSX), le tre sotto classi hanno gli stessi metodi per creare un bottone o una label ma lo fanno in modi diversi.

Ora vedremo subito un esempio di questo pattern.

Questo pattern ha la seguente struttura:

+	AbstractFactory(Person): interfaccia che espone le operazioni realizzate dai oggetti concreti
+	ConcreteFactory(Italian/English): implementazione delle operazioni indicate nell'AbstractFactory
+	AbstractSaluta(InterfaceGetSaluto): interfaccia di esposizione dell'operazione di saluto
+	ConcreteSaluta(ItalianGetSaluto/EnglishGetSaluto): implementazione dell'operazione di saluto
+	Main: invocazione 

![Abstact UML](https://upload.wikimedia.org/wikipedia/commons/9/9d/Abstract_factory_UML.svg)

🐍 🐍 🐍 Python 🐍 🐍 🐍

In Python non esistono le interfacce, quindi per implementare il codice useremo delle normali classi, questo non è da ritenersi un errore.

Python è un linguaggio dinamico, che usa fortemente il [Duck Typing].

Il concetto di interfaccia in python è basato sui metodi e non sull'ereditarietà. Ad esempio qualsiasi classe che abbia dei metodi come open(), read(), write(), eccetera è assimilabile ad un file,  quindi può essere usata come sostituto di un file. Un po' come quando guidi, non ti interessa sapere come funziona il motore o il tipo di automobile. Ma sai che se schiacci un pedale acceleri, un altro freni, con il volante si sterza ed eccetera, quindi che tu stia guidando un tir, un motocarro o una ferrari l'interfaccia è la stessa!

🐍 🐍 🐍 Python 🐍 🐍 🐍

Nel codice per distinguere le classi dalle interfacce scriveremo Interface prima del nome della classe che dovrebbe essere un'interfaccia.

Per visualizzare il codice completo andate qui: [abstract person]

Per prima cosa creaiamo l'AbstractFactory(Person) 

```python
class InterfacePerson(object):
    def __init__(self):
        super().__init__()
    
    def getSaluto(self):
        pass
```

Una volta definita l'interfaccia Person passiamo a definire le classi che conterrano l'implementazione dei metodi definiti nell'interfaccia, ovvero il ConcreteFactory(Italian).

(Di seguito per comodità vedremo solo la classe Italian e tutto ciò che è correleato ad essa, per il resto del codice sopra trovate il link) 

```python
class Italian(InterfacePerson):
    def __init__(self):
        super().__init__()
        
    def getSaluto(self):
        return ItalianGetSaluto()
        pass
```

É bene notare che all'interno di getSaluto avremmo potuto scrivere direttamente l'implementazione finale della nostra funzione.

In questo caso ho deciso di far ritornare l'instanza di un oggetto che si fa carico dell'implementazione ovvero AbstractSaluta(InterfaceGetSaluto), vediamo la sua implementazione:

```python
class InterfaceGetSaluto(object):
	def __init__(self):
		super().__init__()
		
	def Saluta(self):
		pass
```

Ora andiamo a definire l'implementazione per la classe che ci permette di salutare, ConcreteSaluta(ItalianGetSaluto):

```python
class ItalianGetSaluto(InterfaceGetSaluto):
	def __init__(self):
		super().__init__()
		
	def Saluta(self):
		print("Ciao, Come va?")
		pass
```

Ora passiamo al Main:

```python
nation = "Italia"
person = None

if(nation == "Italia"):
    person = Italian()
else:
    person = English()

saluto = person.getSaluto()
saluto.Saluta()
```

In output riceveremo: Ciao, Come va?

É importante notare che in questo caso il pattern Abstract Factory è stato usato due volte. La prima volta per definire l'esistenza di persone di diversa nazionalità e la seconda per definire l'esistenza di vari linguaggi.

Ora analizziamo i suoi vantaggi:

+	Isola le classi concrete: tutte le manipolazioni client-side sono fatte tramite interfacce astratte.
+	Semplifica lo scambio di famiglie di prodotti: basta cambiare la ConcreteFactory.
+	Favorisce la consistenza tra i prodotti: semplifica la cooperazione tra oggetti della stessa famiglia.

Ecco gli svantaggi:

-	Supportare nuovi tipi di prodotto è difficile, occorre riscrivere la AbstractFactory e tutte le sottoclassi.


Possiamo concludere dicendo che l'uso dell'Abstract Factory è utile quando:

+	un sistema deve essere indipendente da come i suoi prodotti sono creati, composti e rappresentati;
+	un sistema deve essere configurato con uno di tante famiglie di prodotti;
+	si vuole fornire una libreria di classi di prodotti e si vuole rivelare solo la loro interfaccia, non la loro implementazione.

[abstract person]:https://github.com/paranoiasystem/Patterns/blob/master/codice/abstract/person/Person.py
[Duck Typing]:https://it.wikipedia.org/wiki/Duck_typing