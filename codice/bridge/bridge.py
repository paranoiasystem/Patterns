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