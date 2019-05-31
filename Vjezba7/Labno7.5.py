from multiprocessing import process,pool
import socket
import subprocess
import sys
import datetime
import os
from local_machine_info import print_machine_info
import time 
import multiprocessing


def	port_scanner(arg):
	targetIp,PortNumber = arg
	tcp_spcl = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	result = tcp_sock.connect_ex((targetIp,PortNumber))
	if result==0:
		return PortNumber,True
	else: 
		return PortNumber,False
	tcp_sock.close()
	

	

def pool_handler(ports):
	broj_cpu=multiprocessing.cpu_count()
	print "Broj coreova u ovo racunalu je " %(broj_cpu,broj_cpu*4)
	pool=multiprocessing.Pool(processes=broj_cpu*2)
		
	for port, status in pool.map(port_scanner,[(targetIp,port)for port in ports]):
		print "Skeniram port"% port
		if status ==True:
			print "port je otvoren "  %port
	
if __name__ == "__main__":
	
	host = raw_input("Unesi ime hosta")
	
	try:
		targetIp=socket.gethostbyname(host)
		print "Skeniranje " 
		print  host
		up=os.system('ping'+targetIp+'-n 1')
		if up == 0:
			print "Host % je dostupan "
			print "-"*50
			print "unesite od kojeg do kojeg porta zelite"
			start = int(raw_input("Pocetni port"))
			end = int(raw_input("Krajnji port"))
			
			ports =range(start,end + 1)
			start_time = time.time()
			pool_handler(ports)
			end_time=time.time()
			elapsed_time=end_time -start_time
			
			print "skeniranje portova zavrseno"
			print "trajanje %s" % elapsed_time
		else:
			print "."*50
			print "\nHost %s nije dostupan.Program zavrsava" %host
		
	except socket.gaierror:
		print "Zapis nije u dnsu"
		print "Zavrsavam program"
