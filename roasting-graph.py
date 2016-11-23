import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
from threading import Thread
import serial

serdev = '/dev/tty.usbmodem1412'
s = serial.Serial(serdev)
f=open('/Users/rebeccapledger/Documents/roasting/data', 'w',0)

out = ''
count = 1
while count < 10:
	if s.inWaiting() > 0:
	  out= s.readline()
	  out= out.rstrip()
	  out = out.replace('\r','')
	  data= f.write(out+'\n')
	  #time.sleep(0.1)
	  count = count + 1



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

def FileWriter():
	f=open('/Users/rebeccapledger/Documents/roasting/data', 'w',0)
	k=0
	i=0
	while(k<20):
		i+=1
		j=np.random.randint(1,20,1)[0]
		data= f.write(str(i)+','+str(j)+'\n')
		print("wrote data")
		time.sleep(2)
		k+=1

#t1=Thread(target=FileWriter)
#t1.start()

#fig = plt.figure()
#ax1 = fig.add_subplot(1,1,1)
#ax1.set_xlim(0,20)
#ax1.set_ylim(0,20)
#ax1.set_autoscale_on(False)

def animate(i):
	pullData = open("data", "r").read()
	dataArray = pullData.split('\n')
	xar = []
	yar = []
	for eachLine in dataArray:
		if len(eachLine)>1:
			x,y = eachLine.split(',')
			xar.append(int(x))
			yar.append(int(y))
			time.sleep(0.01)
	ax1.clear()
	ax1.axvline(5,color='k', linestyle='--')
	ax1.axvline(10,color='k', linestyle='--')
	ax1.axvline(15,color='k', linestyle='--')
	ax1.axvline(20,color='k', linestyle='--')
	ax1.axhline(0,color='k', linestyle='--')
	ax1.axhline(5,color='k', linestyle='--')
	ax1.axhline(10,color='k', linestyle='--')
	ax1.axhline(15,color='k', linestyle='--')
	ax1.axhline(20,color='k', linestyle='--')
	ax1.plot(xar,yar)

#ani = animation.FuncAnimation(fig, animate, interval=1000)
#plt.show()