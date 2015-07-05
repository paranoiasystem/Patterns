### Adapert pattern

Con il nome adapter si denota un design pattern utilizzato in informatica nella programmazione orientata agli oggetti.

Il fine dell'adapter è di fornire una soluzione astratta al problema dell'interoperabilità tra interfacce differenti. Il problema si presenta ogni qual volta nel progetto di un software si debbano utilizzare sistemi di supporto (come per esempio librerie) la cui interfaccia non è perfettamente compatibile con quanto richiesto da applicazioni già esistenti. Invece di dover riscrivere parte del sistema che risulta un compito oneroso e non sempre possibile si scrive un adapter che faccia da tramite.

L'Adapter è un pattern strutturale che può essere basato sia su classi che su oggetti.

L'Adapter è costituito da:

-	Adaptee: definisce l'interfaccia che ha bisogno di essere adattata.
-	Target: definisce l'interfaccia che usa il Client.
-	Client: collabora con gli oggetti in conformità con l'interfaccia Target.
-	Adapter: adatta l'interfaccia Adaptee all'interfaccia Target.

![Adapter UML](https://upload.wikimedia.org/wikipedia/commons/8/8c/Adapter_using_delegation_UML_class_diagram.svg)

Esistono due tipi di Adapter

-	Object Adapter
	-	basato su delega/composizione.

-	Class Adapter
	-	basato su ereditarietà;
	-	l’adattatore eredita sia dall’interfaccia attesa sia dalla classe adattata;
	-	non si ha eredità multipla: l’interfaccia attesa deve essere un’interfaccia, non una classe.

🐍 🐍 🐍 Python 🐍 🐍 🐍

In Python grazie all'uso delle metaclassi potenzialmente possiamo implementarli entrambi, all'interno del libro vedremo solo l'Object Adapter, ma sarà reso disponibile il codice di entrambi.

🐍 🐍 🐍 Python 🐍 🐍 🐍

Vediamo il codice dell'Object Adapter, qui potete trovare il codice [object adapter]:

```python
class Impiegato(object):
	
	__cognome = None

	def __init__(self):
		super().__init__()
	
	def	setCognome(self, cognome):
		self.__cognome = cognome

	def getCognome(self):
		return self.__cognome

class Employer(object):

	__lastName = None

	def __init__(self):
		super().__init__()

	def setLastName(self, lastName):
		self.__lastName = lastName

	def getLastName(self):
		return self.__lastName

class AdattatoreEmployer(Employer):
	employer = None
	def __init__(self):
		super().__init__()
		self.employer = Employer()

	def getCognome(self):
		return self.employer.getLastName()

	def setCognome(self, cognome):
		self.employer.setLastName(cognome)
		
def main():
	impiegato = Impiegato()
	impiegato.setCognome("Rossi")
	print(impiegato.getCognome())

	adattatoreemployer = AdattatoreEmployer()
	adattatoreemployer.setCognome("Simpson")
	print(adattatoreemployer.getCognome())

if __name__ == '__main__':
	main()
```

Usiamo Adapter quando:

-	vogliamo utilizzare una classe esistente la cui interfaccia non risponde alle nostre necessità;
-	si vuole realizzare una classe riusabile che coopera con classi che non necessariamente hanno un’interfaccia compatibile;
-	occorre utilizzare sottoclassi esistenti le cui interfacce non possono essere adattate sottoclassando ciascuna di esse. Un object adapter può adattare l’interfaccia della classe base.

Conseguenze

Class Adapter:

-	non va bene se vogliamo adattare anche le sottoclassi;
-	adapter potrebbe sovrascrivere dei comportamenti di Adaptee;

Object Adapter:

-	un singolo Adapter funziona con gli oggetti Adaptee e quelli delle sottoclassi;
-	é difficile sovrascrivere il comportamento di Adaptee.

[object adapter]:https://github.com/paranoiasystem/Patterns/blob/master/codice/adapter/object/adapter.py