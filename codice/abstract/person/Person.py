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
    nation = "Italia"
    #nation = "USA"
    person = None

    if(nation == "Italia"):
        person = Italian()
    else:
        person = English()
        
    saluto = person.getSaluto()
    saluto.Saluta()

if __name__ == '__main__':
    main()