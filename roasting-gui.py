import Tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
style.use('ggplot')
from threading import Thread
import time
import serial
import re

LARGE_FONT = ("Veranda", 12)

f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)

serdev = '/dev/tty.usbmodem1412'
s = serial.Serial(serdev)
s.reset_output_buffer()
s.reset_input_buffer()

time_elapsed = 0
start_time = 0
counter = 0

xList = []
yList = []

def animate(i):
	#pullData = open("data", "r").read()
	global counter
	s.flushInput()
	temp = s.readline()
	temp = temp.rstrip()
	temp = temp.replace('\n', '')
	print temp
	#dataList = pullData.split('\n')
	#xList = []
	#yList = []
	#for eachLine in dataList:
	#	if len(eachLine)>1:
	#x, y = line.split('.')
	xList.append(int(counter))
	yList.append(int(float(temp)))

	a.clear()
	a.plot(xList, yList)
	counter += 1
	print "X: {}, Y:{}".format(xList, yList)


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

def qf():
	print ("you did it!")

class GraphPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Arabica Roasting Logger", font=LARGE_FONT)
		label.pack(pady=10, padx=10)

		button1 = tk.Button(self, text="Button Example", command=qf)
		button1.pack()

		canvas = FigureCanvasTkAgg(f, self)
		canvas.show()
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

		toolbar = NavigationToolbar2TkAgg(canvas, self)
		toolbar.update()
		canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

		self.display_time = tk.Label(self, text=time_elapsed)
		self.display_time.pack()

		def display_elapsed():
			global time_elapsed
			global start_time
			new_time_elapsed = time.time() - start_time
			if new_time_elapsed != time_elapsed:
				time_elapsed = "{0:.2f}".format(new_time_elapsed)
				self.display_time.config(text=time_elapsed)
				self.display_time.after(200, display_elapsed)

		display_elapsed()

#t1 = Thread(target=SerialWriter)
start_time = time.time()
#t1.start()
app = ArabicaApp()
ani = animation.FuncAnimation(f, animate, interval=1000)
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