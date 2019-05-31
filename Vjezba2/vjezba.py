import socket # for socket
import sys 

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "Socket uspjesno napravljen"
except socket.error as err:
    print "socket creation failed with error %s" %(err)


port = 80

try:
    host_ip = socket.gethostbyname('www.google.com')
except socket.gaierror:
   
    print "Error"
    sys.exit()

s.connect((host_ip,port))

print "Socket je uspjesno konektovan na Google \
on port == %s" %(port)
print "Te ip adresa je== %s " %(host_ip)
