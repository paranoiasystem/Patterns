#Person dovreebbe essere un interfaccia, ma useremo una classe perchè in python non esistono le interfacce.
#Python è un linguaggio dinamico.
#Il concetto di interfaccia in python è basato sui metodi e non sull'ereditarietà.
#Per distinguere le classi dalle interfacce scriveremo Interface prima del proprio nome

class InterfacePerson(object):
    def __init__(self):
        super().__init__()
    
    def getSaluto(self):
        pass

    
class Italian(InterfacePerson):
    def __init__(self):
        super().__init__()
        
    def getSaluto(self):
        return ItalianGetSaluto()
        pass


class English(InterfacePerson):
    def __init__(self):
        super().__init__()

    def getSaluto(self):
        return EnglishGetSaluto()
        pass
    
    
class InterfaceGetSaluto(object):
	def __init__(self):
		super().__init__()
		
	def Saluta(self):
		pass

class ItalianGetSaluto(InterfaceGetSaluto):
	def __init__(self):
		super().__init__()
		
	def Saluta(self):
		print("Ciao, Come va?")
		pass

class EnglishGetSaluto(InterfaceGetSaluto):
	def __init__(self):
		super().__init__()
		
	def Saluta(self):
		print("Hello, How are you?")
		pass

def main():
    #nation = "Italia"
    nation = "USA"
    person = None
    
    #Instanziamo l'oggetto di cui abbiamo bisogno in base ad un if
    if(nation == "Italia"):
        person = Italian()
    else:
        person = English()
        
    #utliziamo gli stessi metodi per accedere ad oggetti di tipo differente
    #in base al tipo d'oggetto instanziato avremo una risposta diversa
    #che dipende dall'implementazione
    saluto = person.getSaluto()
    saluto.Saluta()

if __name__ == '__main__':
    main()