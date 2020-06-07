import socket
import pickle
import time
import threading


def receive():
	while True:
		time1 = time.asctime( time.localtime(time.time()) )
		received = pickle.loads(c.recv(1024))
		print("message from my friend ("+str(time1)+")"+ str(received))

def send():
	while True:
		name = input("Message from myside: ")
		name = pickle.dumps(name)
		c.send(name)

#SOCK_STREAM corresponds to TCP and AF_INET corresponds to IPV4
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# SO_ - socket option
# SOL_ - socket option level
# Sets REUSEADDR (as a socket option) to 1 on socket
c.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#local host ko thau ma ip address rakhni if different devices
c.connect((socket.gethostname(),9919))

t1 = threading.Thread(target = receive)
t2 = threading.Thread(target = send )

t1.start()
t2.start()

	
	
	

