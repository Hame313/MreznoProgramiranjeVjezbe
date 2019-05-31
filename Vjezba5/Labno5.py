import socket
import subprocess
import sys
from datetime import datetime


subprocess.call('clear', shell=True)

remoteServer    = raw_input("Unesi host za scan ")
remoteServerIP  = socket.gethostbyname(remoteServer)
start = raw_input("Unesi pocetni port: ") 
end = raw_input("Unesi krajnji port: ")

print "-" * 60
print "Cekajte", remoteServerIP
print "-" * 60

t1 = datetime.now()



try:
	for port in range(int(start), int(end)):  
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print "Skeniram port %d" % port
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			print "Port { %d}: Open".format(port)
		
		sock.close()
	


except KeyboardInterrupt:
    print "You pressed Ctrl+C"
    sys.exit()

except socket.gaierror:
    print 'Hostname could not be resolved. Exiting'
    sys.exit()

except socket.error:
    print "Couldn't connect to server"
    sys.exit() 
	

t2 = datetime.now()


total =  t2 - t1


print 'Scanning Completed in: ', total
