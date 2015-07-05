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