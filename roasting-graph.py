import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
from threading import Thread
import serial
import re



# serdev = '/dev/tty.usbmodem1412'
# s = serial.Serial(serdev)
# f=open('/Users/rebeccapledger/Documents/roasting/data', 'w',0)

# out = ''
# count = 1
# while count < 10:
# 	if s.inWaiting() > 0:
# 	  out= s.readline()
# 	  out = str.split('.', 1)
# 	  out= out.rstrip()
# 	  out = out.replace('\r','')
# 	  data= f.write(out+'\n')
# 	  time.sleep(1)
# 	  count = count + 1



#plt.plot([1, 2, 3, 4])
#plt.ylabel('some numbers')
#plt.show()

#data = np.array([1,2,3,4])
#plt.plot(data)
#plt.ylabel('time')
#plt.xlabel('temp')
#plt.show()

#x = [1,2,3,4,5]
#y = [1,4,9,16,25]
#plt.plot(x,y)
#plt.show()
count = 0
xar = []
yar = []
serdev = '/dev/tty.usbmodem1412'
s = serial.Serial(serdev)
#f=open('/Users/rebeccapledger/Documents/roasting/data', 'w',0)
s.reset_output_buffer()
s.reset_input_buffer()

def SerialWriter():
	#serdev = '/dev/tty.usbmodem1412'
	#s = serial.Serial(serdev)
	#f=open('/Users/rebeccapledger/Documents/roasting/data', 'w',0)
	#s.reset_output_buffer()
	#s.reset_input_buffer()

	global count
	regex = r"(\d+)\.(\d+)"
	out = ''
	#count = 0
	startTime = time.time()
	#while count < 20:
	s.reset_input_buffer()
	while 1:
		if s.inWaiting() > 0:
		  print s.inWaiting()
		  out= s.readline()
		  print "Out: " + out
		  match = re.search(regex, out)
		  if match:
		  	out = match.group(1)
		  else:
		  	continue
		  out= out.rstrip()
		  out = out.replace('\r','')
		  count = count + 1
		  print "Writing Data: " + str(count) + " "+ out
		  return out
		  #data= f.write(str(count) + "," + out+'\n')
		  #time.sleep(1)
		  #count = count + 1
		  #s.reset_input_buffer()
	elapsedTime = time.time() - startTime
	print "Finished in %d", elapsedTime

#t1=Thread(target=FileWriter)
#t1.start()

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_xlim(0,100)
ax1.set_ylim(0,100)
ax1.set_autoscale_on(False)
line, = ax1.plot([], lw=2)

#def init():
#	line.set_data([], [])
#	return line,

def animate(i):
	#pullData = open("data", "r").read()
	#dataArray = pullData.split('\n')
	#xar = []
	#yar = []

	#for eachLine in dataArray:
	#	if len(eachLine)>1:
	global count
	global xar
	global yar
	yar.append(SerialWriter())
	xar.append(count)
	return plt.plot(xar, yar, color='g')
	#line.set_data([x, y])
	#return line,
			#x,y = eachLine.split(',')
			#xar.append(int(x))
			#yar.append(int(y))
			#time.sleep(0.01)
	
	#ax1.clear()
	#ax1.axhline(80,color='r', linestyle='--')
	#ax1.plot(xar,yar)

	#	ax1.axvline(5,color='k', linestyle='--')
#	ax1.axvline(10,color='k', linestyle='--')
#	ax1.axvline(15,color='k', linestyle='--')
#	ax1.axvline(20,color='k', linestyle='--')
	# ax1.axhline(0,color='k', linestyle='--')
	# ax1.axhline(5,color='k', linestyle='--')
	# ax1.axhline(10,color='k', linestyle='--')
	# ax1.axhline(15,color='k', linestyle='--')


#t1=Thread(target=SerialWriter)
#t1.start()
#SerialWriter()
#init_func=init
ani = animation.FuncAnimation(fig, animate, frames=10, interval=20, blit=False)
plt.show()