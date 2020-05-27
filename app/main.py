import toga
from consts import *

class PokeDex(toga.App):
	def __init__(self,title,id):
		toga.App.__init__(self,title,id)
		self.title=title
		self.size=(WIDTH,HEIGHT)
		self.heading=['Name']
		self.data=['python','laravel','c++']

		self.create_elements()

	def startup(self):
		self.main_window = toga.MainWindow('main',title=self.title,size=self.size)
	
		box=toga.Box()
		
		split=toga.SplitContainer()
		split.content=[self.table,box]

		self.main_window.content = split
		self.main_window.show()
		pass

	def create_elements(self):
		self.create_table()

	def create_table(self):
		self.table=toga.Table(self.heading,data=self.data,on_select=self.select_element)

	#CALLBACKS

	def select_element(self,widget,row):
		if row:
			print(row.name)

if __name__ == '__main__':
	pokedex=PokeDex('PokeDex','com.pablolupo.PokeDex')
	pokedex.main_loop()