Patterns
===================


Scritto da: [Marco Ferraioli].

Questo libro è decicato alla comunità OpenSource

Indice
-------------

[Introduzione](#introduzione)

1 [Cosa sono i design patterns](#cosa-sono-i-design-patterns):

-	1.1 [Tipi di design patterns](#tipi-di-design-patterns)
-	1.2 [Vantaggi dei patterns](#vantaggi-dei-patterns)
-	1.3 [Storia dei patterns](#storia-dei-patterns)

2 [Design Patterns Creazionali](#design-patterns-creazionali):

-	2.1 [Abstract Factory](#abstract-factory)
-	2.2 [Builder Pattern](#builder-pattern)
-   2.3 [Factory Method Pattern](#factory-method-pattern)
-   2.4 [Prototype Pattern](#prototype-pattern)
-   2.5 [Singleton Pattern](#singleton-pattern)

3 [Design Patterns Strutturali](#design-patterns-strutturali):

4 [Design Patterns Comportamentali](#design-patterns-comportamentali):

[Bibliografia - Referenze](#bibliografia---referenze)

## Introduzione

Salve, sono Marco Ferraioli. 

Sono uno studente dell'Università degli studi di Salerno, frequento il corso di studi in Scienze Informatiche. 

Mi occupo di sviluppo Software ed anche di elettronica, in particolare dello sviluppo di progetti su Arduino.

Il seguente libro nasce con l'intento di mettere insieme tutto lo studio da me fatto sui vari pattern durante il corso di TPA (Tecniche di Programmazione Avanzata).

Tutti i pattern all'interno di questo libro saranno implementati in Python.

In merito a Python vorrei aprire una piccola parentesi. La scelta dell'usare Python come linguaggio si deve al fatto che il libro di testo usato per il corso di TPA è stato: "Python in Practice, di Mark Summerfield". Inoltre il libro è da considerarsi rivolto maggiormente verso i neofiti di Python, per questo di tanto in tanto mi soffermerò ad analizzare delle funzionalità o la sintassi specifica di questo linguaggio.

Ogni volta che parlerò di questi aspetti di Python essi verranno delimitati da :snake: , quindi a chi non interessano questi miei interventi potrà individuare subito il blocco da saltare.

Vi ricordo che la sintassi e versione di Python usata in tutto il libro è la 3.0, questa versione di Python viene anche chiamata "Python 3000" o "Py3k".

Questo non voglio definirlo propriamente un libro, anche se ne ha tutta la struttura. È il mio primo lavoro di questo genere, più che lavoro lo definirei un mio primo esperimento nella stesura di un libro/guida.

Ho deciso di rilasciare il libro ed il codice sotto licenza GNU, quindi sentitevi liberi di copiarlo, modificarlo e creare opere da esso derivate, vi chiedo solo di ricordarvi di citare la fonte.

Vi ricordo che all'interno degli articoli non verrà riportato tutto il codice ma solo i pezzi più importanti che servono a rendere possibile la comprensione del pattern, comunque linkerò prima di ogni esempio il file contenente tutto il codice a cui la spiegazione fa riferimento.

## Cosa sono i design patterns

Un design pattern è un concetto che può essere definito "una soluzione progettuale generale ad un problema ricorrente". Si tratta di una descrizione o modello logico da applicare per la risoluzione di un problema che può presentarsi in diverse situazioni durante le fasi di progettazione e sviluppo del software, ancor prima della definizione dell'algoritmo risolutivo della parte computazionale.

Un design pattern è costituito da:

-	il nome, costituito da una o due parole che siano il più possibile rappresentative del pattern stesso;

-	il problema, ovvero la descrizione della situazione alla quale si può applicare il pattern;

-	la soluzione, che descrive gli elementi costitutivi del progetto con le relazioni e relative implicazioni, senza però addentrarsi in una specifica implementazione;

-	le conseguenze, i risultati e i vincoli che derivano dall'applicazione del pattern. Sono fondamentali in quanto possono essere l'ago della bilancia nella scelta dei pattern;

## Tipi di design patterns

I design pattern possono essere classificati con diversi criteri, i più comuni sono quelli che evidenziano il tipo di problema che si cerca di risolvere. 

Il tipo di problema può essere legato ad uno specifico dominio progettuale oppure, più comunemente, al problema progettuale in senso più ampio (nell'ingegneria del software, ad esempio, si può parlare di creazione, comportamento, navigazione di oggetti o strutture dati).

Nel loro libro la "banda dei quattro" identificò 23 tipi di design pattern, suddivisi in tre categorie: strutturali, creazionali e comportamentali.

## Vantaggi dei patterns

I patterns in programmazione offrono alcuni vantaggi, ora ne vedremo alcuni:

Ci consentono il riuso della conoscenza/esperienza di progettazione:
-	Raramente i problemi sono nuovi e unici.
-	I patterns forniscono indicazioni su “dove cercare soluzioni ai problemi”.

Stabiliscono una terminologia comune e condivisa:
-	Es.: è facile dire “Qui ci serve un Façade”.

Forniscono una prospettiva di alto livello, cioè ci liberano dal dover gestire troppo presto i dettagli della progettazione.

## Storia dei patterns

Design Patterns - Elementi per il riuso di software ad oggetti è un saggio del 1995 scritto da Gamma, E., Helm, R., Johnson, R. e Vlissides, J. Gli autori di questo libro divennero noti come la Banda dei Quattro (“Gang of four“, Go4, GoF).

Nel libro gli autori riprendono il concetto di design pattern dell'architetto Christopher Alexander, adattandolo all'informatica.

Anche se il concetto di patterns come soluzione ricorrente a un problema è anteriore all'uscita del libro, infatti nel 1987 W. Cunningham e K. Beck lavoravano al linguaggio Smalltalk e individuano alcuni patterns.

Ma fù il libro che con il suo enorme successo a da dare inizio ad un'intera corrente filosofica della programmazione: il movimento pattern.

![Gang of four](http://podcast.federica.unina.it/mini/img.php?src=/files/_docenti/russo-stefano/img/stefano-russo-35111-012-9.jpg)

-> Gang of Four <-

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

Ora analizziamo i suoi vantaggi:

+   isolamento delle classi concrete: il client non ha modo di instanziare direttamente le classi concrete, ma può creare le instanze delle classi semplicemente tramite le interfacce.
+   semplificazione della modifica delle relazioni: le relazioni tra le classi concrete possono essere facilmente modificate senza pregiudicare il client che, poichè non ha visibilità della struttura implementativa, non avrà nessuna ricaduta sulle modifiche effettuate.

Ecco gli svantaggi:

+   difficoltà nell’aggiungere nuovi prodotti(metodi): la creazione di nuovi prodotti comporta delle modifiche in AbstractFactory e tutte le classi figlie e questa modifica non è indolore.

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

Prima di continuare voglio analizzare con voi la seguente riga:

```python
from abc import ABCMeta, abstractmethod
```

Importiamo ABCMeta ed abstractmethod che ci consentiranno di creare dei metodi astratti tramite l'uso della metaclasse ABCMeta.

In programmazione a oggetti, una metaclasse è una classe le cui istanze sono a loro volta classi. Questo concetto è strettamente legato al concetto di riflessione (reflection), che si applica a quegli strumenti concettuali che permettono di rappresentare, all'interno di un programma, informazioni sulle parti costituenti del programma stesso (tipicamente classi e oggetti).

Questo ci permette di creare una specie di interfaccia, ovvero ci fa creare dei metodi rendendoli astratti così da richiedre la loro implementazione nelle classi che la estendono.

Nell'[Abstract Factory](#abstract-factory) ho già spiegato il perchè non esistono le interfacce.

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

Qui possiamo notare come la classe Margherita che ha esteso la metaclasse ABCMeta ha implementato tutti i metodi che sono stati definiti @abstractmethod.

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

## Factory Method Pattern

coming soon

## Prototype Pattern

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

## Singleton Pattern

Il singleton è un design pattern creazionale che ha lo scopo di garantire che di una determinata classe venga creata una e una sola istanza, e di fornire un punto di accesso globale a tale istanza.

Questo pattern viene utilizzato quando si desidera avere un unico punto di accesso. Per esempio si desidera avere solo un Window Manager oppure una sola Coda di Stampa oppure un unico accesso al database.

In Python abbiamo due metodi per creare un oggetto singleton, il primo consiste nel creare una classe da estendere, il secondo consiste nell'uso di una metaclasse.

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

## Design Patterns Strutturali

## Design Patterns Comportamentali

## Bibliografia - Referenze

[2] Cosa Sono I Patterns

[2] Tipi di design patterns

[2] - [3] Design Patterns Creazionali

[1] - [2] - [4] - [5] - [6] Abstract Factory

[1] - [2] - [7] - [8] - [9] - [10] - [11]  Builder Pattern

[1] - [2] - [12] - [13] Prototype Pattern

[1] - [2] - [14] - [15] - [16] Singleton Pattern

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
[8]:https://dellabate.wordpress.com/2011/01/10/gof-patterns-builder/
[9]:http://www.cosenonjaviste.it/dai-costruttori-al-builder-pattern-in-java/
[10]:http://www.helldragon.eu/marcello/galli_python/14-Classi.html
[11]:https://it.wikipedia.org/wiki/Metaclasse
[builder pizza]:https://github.com/paranoiasystem/Patterns/blob/master/codice/builder/pizza/Pizza.py
[12]:https://it.wikipedia.org/wiki/Prototype_pattern
[13]:https://dellabate.wordpress.com/2011/01/18/gof-patterns-prototype/
[prototype cookie]:https://github.com/paranoiasystem/Patterns/blob/master/codice/prototype/cookie/cookie.py
[14]:https://it.wikipedia.org/wiki/Singleton
[15]:https://dellabate.wordpress.com/2010/09/20/il-pattern-singleton/
[16]:http://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
[singleton class]:https://github.com/paranoiasystem/Patterns/blob/master/codice/singleton/singleton/class.py
[singleton metaclass]:https://github.com/paranoiasystem/Patterns/blob/master/codice/singleton/singleton/metaclass.py
