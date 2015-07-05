### Factory Method Pattern

Il Factory method pattern fornisce un'interfaccia per creare un oggetto, ma lascia che le sottoclassi decidano quale oggetto istanziare.

Come altri pattern creazionali, esso indirizza il problema della creazione di oggetti senza specificarne l'esatta classe. Questo pattern raggiunge il suo scopo fornendo un'interfaccia per creare un oggetto, ma lascia che le sottoclassi decidano quale oggetto istanziare.

Questo pattern ha la seguente struttura:

-	Creator: dichiara la Factory che avrà il compito di ritornare l’oggetto appropriato.
-	ConcreteCreator: effettua l’overwrite del metodo della Factory al fine di ritornare l’implementazione dell’oggetto.
-	Product: implementa l’oggetto.

![Factory method](https://upload.wikimedia.org/wikipedia/commons/a/a3/FactoryMethod.svg)

Vediamone ora il codice che per comodità ed anche perchè semplice verrà riportato tutto di seguito:

```python
class Scarpe(object):
	
	tipo = None

	def __init__(self, tipo):
		super().__init__()
		self.tipo = tipo

	def getTipo(self):
		return self.tipo
		
class Commesso(object):
	def __init__(self):
		super().__init__()

	def getScarpe(self, tipo):
		if (tipo == "Tennis"):
			scarpe = CommessoTennis.getScarpe(self, tipo);
		return scarpe

class CommessoTennis(Commesso):
	def __init__(self):
		super().__init__()

	def getScarpe(self, tipo):
		return Scarpe(tipo)

def main():
	commesso = Commesso()
	scarpe = commesso.getScarpe("Tennis")
	print(scarpe.getTipo())

if __name__ == '__main__':
	main()
```

Nel seguente codice possiamo dire che le Scarpe sono il Product, Commesso è il Creator e CommessoTennis è il ConcreteCreator.

Tale pattern presenta i seguenti vantaggi/svantaggi:

-	rappresenta un gancio alle sotto-classi: tramite il Creator è possibile scegliere quale classe concreta utilizzare e decidere di cambiarla senza avere nessun impatto verso il Client

Questo pattern può essere utilizzato quando:

-	La creazione di un oggetto preclude il suo riuso senza una significativa duplicazione di codice.
-	La creazione di un oggetto richiede l'accesso ad informazioni o risorse che non dovrebbero essere contenute nella classe di composizione.
-	La gestione del ciclo di vita degli oggetti gestiti deve essere centralizzata in modo da assicurare un comportamento coerente all'interno dell'applicazione.
