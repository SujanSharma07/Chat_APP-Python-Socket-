import socket
import pickle
import time
import threading

class client_socket():
    def __init__(self,c,number):
        self.number = number
        self.number_t = (self.number+1)%2
        self.client_from = c[self.number]['socket']
        self.client_to = c[self.number_t]['socket']

    def receive(self):
        
        while True:
           
            self.message = pickle.loads(self.client_from.recv(1024))
            self.sendto(self.client_to,self.message)



    def sendto(self,c,data):
        self.data = pickle.dumps(data)
        c.send(self.data)



	

#SOCK_STREAM corresponds to TCP and AF_INET corresponds to IPV4
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# SO_ - socket option
# SOL_ - socket option level
# Sets REUSEADDR (as a socket option) to 1 on socket
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

print(" Server Socket Created")

#local host indicate ip adddress and 9919 indixate the port
s.bind((socket.gethostname(),9919))

#this is to listen cleint, 3 indicate maximum number of client we will handeling
s.listen(2)

print("Waiting for the client request")
#to accept the connectio n from client

clients = []
clients_info = {}
clients_number = 0

while True:
    c, addr = s.accept()
    clients_number+=1
    print(f"client with c {c} address1 {addr}")
    print(f"Total {clients_number} clients are connected now")
    clients_info = {"socket":c,"addr":addr}
    clients.append(clients_info)
    if clients_number==2:
        break

print(f"all clients information is {clients}")

client1 = client_socket(clients,0)
client2 = client_socket(clients,1)
t1 = threading.Thread(target = client1.receive)
t2 = threading.Thread(target = client2.receive)
t1.start()
t2.start()
