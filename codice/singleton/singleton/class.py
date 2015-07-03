class Singleton(object):
  _instance = None
  def __new__(self):
    if not isinstance(self._instance, self):
        self._instance = object.__new__(self)
        return self._instance

class MyClass(Singleton):
    def saluta(self):
        print("ciao")

a = MyClass()
print(id(a))
b = MyClass()
print(id(b))
a.saluta()
b.saluta() #errore perchè non è stato instanziato nessun oggetto in b
