import Tkinter as tk
#from ttk import Frame, Button, Style
import matplotlib

LARGE_FONT = ("Veranda", 12)

class ArabicaApp(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		container = tk.Frame(self)

		container.pack(side='top', fill='both', expand=True)

		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}

		frame = GraphPage(container, self)

		self.frames[GraphPage] = frame

		frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(GraphPage)

	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

class GraphPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Graph Page", font=LARGE_FONT)
		label.pack(pady=10, padx=10)

app = ArabicaApp()
app.mainloop()	

#class Example(Frame):
#	def __init__(self, parent):
#		Frame.__init__(self, parent)
#
#		self.parent = parent
#		self.initUI()
#
#	def initUI(self):

#		sw = self.parent.title = ("Quit Button")
#		self.style = Style()
#		self.style.theme_use("default")
		
#		self.pack(fill=BOTH, expand=1)

#		quitButton = Button(self, text="Quit",
#			command=self.quit)
#		quitButton.place(x=50, y=50)

#def main():
# 	root = Tk()
 	#w = tk.Label(root, text="Hello, World!")
# 	root.geometry("250x150+300+300")
# 	app = Example(root)
# 	root.mainloop()

#if __name__ == '__main__':
# 	main()