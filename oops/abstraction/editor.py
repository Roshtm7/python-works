from abc import ABC,abstractmethod
class Editor(ABC):

    @abstractmethod
    def open(self):
        pass

    def execute(self):
        pass

    def debug(self):
        pass

class Vscode(Editor):
    def open(self):
        print("vscode open method")

    def execute(self):
        print("vscode execute method")

    def debug(self):
        print("vscode debug method")

vsc=Vscode()
vsc.open()
vsc.execute()
vsc.debug()





