### Bridge Pattern

Il bridge pattern permette di separare l'astrazione di una classe dalla sua implementazione, per permettere loro di variare indipendentemente.

Per capire meglio pensiamo ad uno scenario reale, si vuole cambiare l’interfaccia grafica della nostra applicazione da Windows a Linux preservando la funzionalità di tutti i componenti grafici: in poche parole si vuole cambiare il LookAndFeel ma nello stesso momento fare in modo che il funzionamento rimanga inalterato.

Questo pattern è composto dai seguenti partecipanti:

-   Client(Main): colui che effettua l’invocazione all’operazione di interesse.
-   Abstraction(SistemaOperativo): definisce l’interfaccia del dominio applicativo utilizzata dal Client.
-   RefinedAbstraction(Testo): definisce l’implementazione dell’interfaccia utilizzata.
-   Implementor(SistemaOperativoAPI): definisce l’interfaccia da usare come Bridge e riferibile agli oggetti concreti da utilizzare.
-   ConcreteImplementor(Windows/Linux): implementa l’interfaccia Implementor usata come Bridge per il transito degli oggetti.


![Bridge UML](https://upload.wikimedia.org/wikipedia/commons/c/cf/Bridge_UML_class_diagram.svg)

Ora vediamone il codice, potete trovarlo qui [Python bridge]:

```python
class SistemaOperativoAPI(object):
	def __init__(self):
		super().__init__()

	def stampaTesto(self, testo):
		pass

class Windows(SistemaOperativoAPI):
	def __init__(self):
		super().__init__()

	def stampaTesto(self, testo):
		print("-" + testo + "-")
		
class Linux(SistemaOperativoAPI):
	def __init__(self):
		super().__init__()

	def stampaTesto(self, testo):
		print("->" + testo + "<-")

class SistemaOperativo(object):
	api = None

	def __init__(self, api):
		super().__init__()
		self.api = api

	def stampa(self):
		pass

class Testo(SistemaOperativo):
	testo = None

	def __init__(self, api, testo):
		super().__init__(api)
		self.testo = testo
		
	def stampa(self):
		self.api.stampaTesto(self.testo)

def main():
	linux = Testo(Linux(), "Ciao")
	linux.stampa()

	windows = Testo(Windows(), "Ciao")
	windows.stampa()

if __name__ == '__main__':
		main()	
```
Il codice risulta essere molto semplioce e credo non richieda spiegazioni. Quindi ora passerò ad illustrare i suoi vantaggi:

-	disaccoppia l’interfaccia dall’implementazione: disaccoppiando Abstraction e Implementor è possibile gestire i cambiamenti delle classi concrete senza cablare nel codice dei riferiementi diretti.
-	migliora l’estendibilità: è possibile estendere la gerarchia di Abstraction e Implementor senza problemi
-	nasconde l’implementazione al client: il Client non si deve porre il problema di conoscere l’implementazione delle classi concrete.

[Python bridge]:https://github.com/paranoiasystem/Patterns/blob/master/codice/bridge/bridge.py