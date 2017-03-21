import Tkinter as tk
import tkFileDialog
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
import pickle

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
event = 'pause'

xList = []
yList = []

def animate(i):
	#pullData = open("data", "r").read()
	global counter
	if event == 'start':
		s.flushInput()
		temp = s.readline()
		temp = temp.rstrip()
		temp = temp.replace('\n', '')

		xList.append(int(counter))
		yList.append(int(float(temp)))

		a.clear()
		a.plot(xList, yList)
		counter += 1
	#elif event == 'stop':
		#pickle.dump(a, file('myplot.pickle', 'w'))
		#quit()

	#print "X: {}, Y:{}".format(xList, yList)

#def popupsave():
	#return tkFileDialog.asksaveasfile(mode='w', **file_opt)
	#popup = tk.Tk()
	#popup.wm_title("Save")
	#label1 = tk.Label(popup, text="Filename", font=LARGE_FONT)
	#label1.pack(side="top", fill="x", pady=10)
	#entry1 = tk.Entry(popup)
	#entry1.pack()
	#save = tk.Button(popup, text="Save", command=lambda: self.save_file(entry1.get(), popup))
	#save.pack()

def save_file(file, popup):
	outfile = file + '.pickle'
	pickle.dump(a, open(outfile, 'w'))
	#saved_label = tk.Label(self, text="Saved!", font=LARGE_FONT)
	#saved_label.pack(side=tk.BOTTOM)
	popup.destroy()

class ArabicaApp(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		container = tk.Frame(self)

		container.pack(side='top', fill='both', expand=True)

		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		menubar = tk.Menu(container)
		filemenu = tk.Menu(menubar, tearoff=0)
		filemenu.add_command(label="Save", command=self.popupsave)
		filemenu.add_separator()
		filemenu.add_command(label="Exit", command=quit)
		menubar.add_cascade(label="File", menu=filemenu)

		tk.Tk.config(self, menu=menubar)

		self.frames = {}

		frame = GraphPage(container, self)

		self.frames[GraphPage] = frame

		frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(GraphPage)

		self.file_opt = options = {}
		options['defaultextension'] = '.pickle'
		options['filetypes'] = [('all files', ".*"), ('pickle files', '.pickle')]
		options['initialdir'] = 'C:\\'
		options['initialfile'] = 'myPlot.pickle'
		options['parent'] = container
		options['title'] = 'This is a title'

	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

	def popupsave(self):
		outfile = tkFileDialog.asksaveasfile(mode='w', **self.file_opt)
		pickle.dump(a, outfile)
		outfile.close()


class GraphPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Arabica Roasting Logger", font=LARGE_FONT)
		label.pack(pady=10, padx=10)

		button1 = tk.Button(self, text="Start", command=lambda: self.set_event('start'))
		button1.pack()
		button2 = tk.Button(self, text="Pause", command=lambda: self.set_event('pause'))
		button2.pack()
		button3 = tk.Button(self, text="Stop", command=lambda: self.set_event('stop'))
		button3.pack()

		canvas = FigureCanvasTkAgg(f, self)
		canvas.show()
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

		toolbar = NavigationToolbar2TkAgg(canvas, self)
		toolbar.update()
		canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

	def set_event(self, cmd):
		global event
		event = cmd


		#self.display_time = tk.Label(self, text=time_elapsed)
		#self.display_time.pack()

		#def display_elapsed():
		#	global time_elapsed
		#	global start_time
		#	new_time_elapsed = time.time() - start_time
		#	if new_time_elapsed != time_elapsed:
		#		time_elapsed = "{0:.2f}".format(new_time_elapsed)
		#		self.display_time.config(text=time_elapsed)
		#		self.display_time.after(200, display_elapsed)

		#display_elapsed()

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