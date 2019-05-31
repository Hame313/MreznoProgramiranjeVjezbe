import threading
import time
import datetime
from local_machine_info import print_machine_info

class myThread(threading.Thread):
	def __init__(self,threadID,name,counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter
	def run(self):
		print "Pokrecem nit " + self.name
		#Ostvari lock zbog sinkronizacije niti
		threadLock.acquire()
		print_time(self.name,self.counter,3)
		#Oslobodi lock da bi se izvrsila slijedeca nit
		threadLock.release()
		
def print_time(threadName,delay,counter):
	while counter:
		time.sleep(delay)
		print "%s: %s" %(threadName,time.ctime(time.time()))
		counter -=1
			
threadLock = threading.Lock()
threads = []
	
	#Kreiraj nove niti
thread1 = myThread(1,"Thread-1",1)
thread2 = myThread(2,"Thread-2",2)
	
	#Pokreni nove niti
thread1.start()
thread2.start()
	
	#Dodaj niti u thread listu sa svim nitima
	
threads.append(thread1)
threads.append(thread2)

danas = datetime.date.today()
print danas
print_machine_info()	
	#Cekaj dok se sve niti ne izvrse
for t in threads:
	t.join()
print "\nIzlazim iz glavne niti \n"