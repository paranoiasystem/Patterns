Patterns
===================


Scritto da: [Marco Ferraioli].

Questo libro è decicato alla comunità OpenSource

Indice
-------------

[Introduzione](#introduzione)

1 [Cosa Sono I Patterns](#cosa-sono-i-patterns):

-	1.1 [Tipi di design patterns](#tipi-di-design-patterns)

2 [Design Patterns Creazionali](#design-patterns-creazionali) :

-	[Abstract Factory](#abstract-factory)
-	a
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

Questo non voglio definirlo propriamente un libro, anche se ha tutta la struttura di un libro. È il mio primo lavoro di questo genere, più che lavoro lo definirei un mio primo esperimento nella stesura di un libro/guida.

Ho deciso di rilasciare il libro ed il codice sotto licenza GNU, quindi sentitevi liberi di copiralo, modificarlo e creare nuove opere basato su esso, inoltre ricordate di citare la fonte.

Inoltre vi ricordo che all'interno degli articoli non verrà riportato tutto il codice ma solo i pezzi più importanti, comunque linkero prima di ogni esempio il file a cui fare riferimento.

## Cosa Sono I Patterns

Un design pattern è un concetto che può essere definito "una soluzione progettuale generale ad un problema ricorrente". Si tratta di una descrizione o modello logico da applicare per la risoluzione di un problema che può presentarsi in diverse situazioni durante le fasi di progettazione e sviluppo del software, ancor prima della definizione dell'algoritmo risolutivo della parte computazionale.

## Tipi di design patterns

I design pattern possono essere classificati con diversi criteri, i più comuni dei quali sono quelli che evidenziano il tipo di problema che si cerca di risolvere. 

Il tipo di problema può essere legato ad uno specifico dominio progettuale oppure, più comunemente, al problema progettuale in senso più ampio (nell'ingegneria del software, ad esempio, si può parlare di creazione, comportamento, navigazione di oggetti o strutture dati).

Nel loro libro la "banda dei quattro" identificò 23 tipi di design pattern, suddivisi in tre categorie: strutturali, creazionali e comportamentali.


## Design Patterns Creazionali

I design patterns creazionali astraggono il processo di istanziazione, essi consentono di rendere il sistema indipendente da come gli oggetti sono creati, rappresentati e dalle relazioni di composizione tra essi.

In parole povere: I pattern creazionali nascondono i costruttori delle classi e mettono dei metodi al loro posto creando un'interfaccia. In questo modo si possono utilizzare oggetti senza sapere come sono implementati.

## Abstract Factory

L'Abstract factory fornisce un'interfaccia per creare famiglie di oggetti connessi o dipendenti tra loro, in modo che non ci sia necessità da parte degli utilizzatori di specificare i nomi delle classi concrete all'interno del proprio codice.

L'Abstract factory è uno dei fondamentali design pattern creazionali della programmazione orientata agli oggetti.

Questo pattern è utile quando vogliamo creare oggetti complessi che sono composti da altri oggetti e dove gli oggetti composti sono tutti di una particolare famiglia.

Per esempio, in un sistema di GUI dove potremmo avere un Abstract Factory che ha tre sottoclassi che hanno gli stessi metodi per creare un bottone o una label ma lo fanno in modi diversi.

Ora vedremo subito un esempio di questo pattern, andremo a realizzare.

Questo pattern ha la seguente struttura:

+	AbstractFactory(Person): interfaccia che espone le operazioni realizzate dai oggetti concreti
+	ConcreteFactory(Italian/English): implementazione delle operazioni indicate nell'AbstractFactory per la creazione degli oggetti
+	AbstractPerson: interfaccia di esposizione delle operazioni delle persone
+	ConcretePerson: implementazione delle operazioni delle persone
+	Main: invocazione 

Per visualizzare il codice completo andate qui: [abstract person]

```python

```

## Design Patterns Strutturali

## Design Patterns Comportamentali

## Bibliografia

[2] Cosa Sono I Patterns

[2] Tipi di design patterns

[2] - [3] Design Patterns Creazionali

[1] - [2] - [4] - [5] Abstract Factory

[Marco Ferraioli]:https://marcoferraioli.com/
[1]:http://www.amazon.com/Python-Practice-Concurrency-Libraries-Developers/dp/0321905636
[2]:https://it.wikipedia.org/wiki/Design_pattern
[3]:http://www.federica.unina.it/ingegneria/programmazione-2/design-pattern-creazionali-esempi/
[4]:https://it.wikipedia.org/wiki/Abstract_factory
[5]:https://dellabate.wordpress.com/2011/01/04/gof-pattern-abstract-factory/
[abstract person]:#