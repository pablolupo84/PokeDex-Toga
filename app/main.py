import toga

class PokeDex(toga.App):
	def __init__(self,title,id):
		toga.App.__init__(self,title,id)
		self.title=title

	def startup(self):
		self.main_window = toga.MainWindow('main',title=self.title,size=(400,500))
	
		box=toga.Box()

		self.main_window.content = box
		self.main_window.show()
		pass

	def create_elements(self):
		pass

	#CALLBACKS

if __name__ == '__main__':
	pokedex=PokeDex('PokeDex','com.pablolupo.PokeDex')
	pokedex.main_loop()