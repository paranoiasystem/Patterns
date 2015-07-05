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