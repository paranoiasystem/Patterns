Patterns
===================


Scritto da: [Marco Ferraioli].

Questo libro è decicato alla comunità OpenSource

Indice
-------------

[Introduzione](#introduzione)

1 [Cosa Sono I Design Patterns](#cosa-sono-i-design-patterns):

-	1.1 [Tipi di design patterns](#tipi-di-design-patterns)

2 [Design Patterns Creazionali](#design-patterns-creazionali) :

-	2.1 [Abstract Factory](#abstract-factory)
-	2.2 [Builder Pattern](#builder-pattern)
-	a
-	a

3 [Design Patterns Strutturali](#design-patterns-strutturali) :

-	a
-	a
-	a
-	a

4 [Design Patterns Comportamentali](#design-patterns-comportamentali) :

-	a
-	a
-	a
-	a

[Bibliografia](#bibliografia)

## Introduzione

Salve, sono [Marco Ferraioli]. 

Sono uno studente dell'Univesità degli studi di Salerno, frequento il corso di studi in Scienze Informatiche. 

Mi occupo di sviluppo Software ed anche di elettronica, in particolare dello sviluppo di progetti su Arduino.

Il seguente libro nasce con l'intento di mettere assieme tutto lo studio da me fatto sui vari pattern durante il corso di TPA (Tecniche di Programmazione Avanzata).

Tutti i pattern all'interno di questo libro saranno implementati in Python.

Questo non voglio definirlo propriamente un libro, anche se ha tutta la struttura di un libro. È il mio primo lavoro di questo genere, più che lavoro lo definirei un mio primo esperimento nella stesura di un libro/guida.

Ho deciso di rilasciare il libro ed il codice sotto licenza GNU, quindi sentitevi liberi di copiralo, modificarlo e creare nuove opere derivate, ricordate di citare la fonte.

Vi ricordo che all'interno degli articoli non verrà riportato tutto il codice ma solo i pezzi più importanti, comunque linkero prima di ogni esempio il file a cui fare riferimento.

## Cosa Sono I Design Patterns

Un design pattern è un concetto che può essere definito "una soluzione progettuale generale ad un problema ricorrente". Si tratta di una descrizione o modello logico da applicare per la risoluzione di un problema che può presentarsi in diverse situazioni durante le fasi di progettazione e sviluppo del software, ancor prima della definizione dell'algoritmo risolutivo della parte computazionale.

## Tipi di design patterns

I design pattern possono essere classificati con diversi criteri, i più comuni sono quelli che evidenziano il tipo di problema che si cerca di risolvere. 

Il tipo di problema può essere legato ad uno specifico dominio progettuale oppure, più comunemente, al problema progettuale in senso più ampio (nell'ingegneria del software, ad esempio, si può parlare di creazione, comportamento, navigazione di oggetti o strutture dati).

Nel loro libro la "banda dei quattro" identificò 23 tipi di design pattern, suddivisi in tre categorie: strutturali, creazionali e comportamentali.


## Design Patterns Creazionali

I design patterns creazionali astraggono il processo di istanziazione, essi consentono di rendere il sistema indipendente da come gli oggetti sono creati, rappresentati e dalle relazioni di composizione tra essi.

In parole povere: I pattern creazionali nascondono i costruttori delle classi e mettono dei metodi al loro posto creando un'interfaccia. In questo modo si possono utilizzare oggetti senza sapere come sono implementati.

## Abstract Factory

L'Abstract factory fornisce un'interfaccia per creare famiglie di oggetti connessi o dipendenti tra loro, in modo che non ci sia necessità da parte degli utilizzatori di specificare i nomi delle classi concrete all'interno del proprio codice.

L'Abstract factory è uno dei fondamentali design pattern creazionali della programmazione orientata agli oggetti.

Questo pattern è utile quando vogliamo creare oggetti complessi che sono composti da altri oggetti e dove gli oggetti composti sono tutti di una particolare famiglia.

Per esempio, in un sistema di GUI dove potremmo avere un Abstract Factory che ha tre sottoclassi (Linux,Windows,OSX) che hanno gli stessi metodi per creare un bottone o una label ma lo fanno in modi diversi.

Ora vedremo subito un esempio di questo pattern.

Questo pattern ha la seguente struttura:


+	AbstractFactory(Person): interfaccia che espone le operazioni realizzate dai oggetti concreti
+	ConcreteFactory(Italian/English): implementazione delle operazioni indicate nell'AbstractFactory
+	AbstractSaluta(InterfaceGetSaluto): interfaccia di esposizione dell'operazione di saluto
+	ConcreteSaluta(ItalianGetSaluto/EnglishGetSaluto): implementazione dell'operazione di saluto
+	Main: invocazione 

![Abstact UML](https://upload.wikimedia.org/wikipedia/commons/9/9d/Abstract_factory_UML.svg)


Vorrei fare una piccola nota: In Python non esistono le interfacce, quindi per implementare il codice useremo delle normali classi, questo non è da ritenersi un errore.

Python è un linguaggio dinamico, che usa fortemente il [Duck Typing].

Il concetto di interfaccia in python è basato sui metodi e non sull'ereditarietà. Ad esempio qualsiasi classe che abbia dei metodi come open(), read(), write(), eccetera è assimilabile ad un file,  quindi può essere usata come sostituto di un file. Un po' come quando guidi, non ti interessa sapere come funziona il motore o il tipo di automobile. Ma sai che se schiacci un pedale acceleri, un altro freni, con il volante si sterza ed eccetera, quindi che tu stia guidando un tir, un motocarro o una ferrari l'interfaccia è la stessa!

Nel codice per distinguere le classi dalle interfacce scriveremo Interface prima del proprio nome

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

(Di seguito per comodità vedremo solo la classe Italian e tutto ciò che è correleato ad essa, per il resto del codice andare qui: [abstract person] ) 

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

É importante notare che in questo caso sono il pattern Abstract Factory è stato usato due volte. La prima volta per definire l'esistenza di vari tipi di persona e la seconda per definire l'esistenza di vari tipi di modi si salutare.

Possiamo concludere dicendo brevemente che l'Abstract Factory ci permette di  utilizzare gli stessi metodi per accedere ad oggetti di tipo differente, quindi avremo una risposta diversa che dipende dalla loro implementazione dei metodi della classe.

## Builder Pattern

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

Passiamo ora ad un esempio con relativa spiegazione step-by-step. Per il codice completo andate qui [builder pizza]

## Design Patterns Strutturali

## Design Patterns Comportamentali

## Bibliografia - Referenze

[2] Cosa Sono I Patterns

[2] Tipi di design patterns

[2] - [3] Design Patterns Creazionali

[1] - [2] - [4] - [5] - [6] Abstract Factory

[1] - [2] - [7] Builder Pattern

[Marco Ferraioli]:https://marcoferraioli.com/
[1]:http://www.amazon.com/Python-Practice-Concurrency-Libraries-Developers/dp/0321905636
[2]:https://it.wikipedia.org/wiki/Design_pattern
[3]:http://www.federica.unina.it/ingegneria/programmazione-2/design-pattern-creazionali-esempi/
[4]:https://it.wikipedia.org/wiki/Abstract_factory
[5]:https://dellabate.wordpress.com/2011/01/04/gof-pattern-abstract-factory/
[6]:http://www.python-it.org/forum/index.php?topic=1910.0
[abstract person]:https://github.com/paranoiasystem/Patterns/blob/master/codice/abstract/person/Person.py
[Duck Typing]:https://it.wikipedia.org/wiki/Duck_typing
[7]:https://it.wikipedia.org/wiki/Builder
[builder pizza]:https://github.com/paranoiasystem/Patterns/blob/master/codice/builder/pizza/Pizza.py