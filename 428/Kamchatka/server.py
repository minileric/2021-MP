import socket
import threading
import queue
import sys
import random
import os
import re

def RecvData(sock,recvPackets):
    while True:
        data,addr = sock.recvfrom(1024) 
        recvPackets.put((data,addr))       
def blackList(self,userId):
        self.blackListUser.add(userId)   
def RunServer():
    host = socket.gethostbyname(socket.gethostname())
    port = 5000
    print('Server hosting on IP-> '+str(host))
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
    s.bind((host,port)) 
    clients = set() 
    recvPackets = queue.Queue() 

    print('Server Running...')    
    threading.Thread(target=RecvData,args=(s,recvPackets)).start() 
    with open('./log.txt', 'w') as f:
        while True:
            while not recvPackets.empty():
                data,addr = recvPackets.get()
                if addr not in clients:
                    clients.add(addr)
                    continue
                clients.add(addr) 
                data = data.decode('utf-8')  
                if ('вулкан' in data) or('полуостров'in data):
                       	message=str(addr)+data+'\n'
                        f.write(message)
                       	print(message)
                       	print('Запрещённое слово')
                        data=data.replace('вулкан', '******')
                        data=data.replace('полуостров', '**********')
                       	for c in clients: 
                           if c!=addr:                                 
                               	s.sendto(data.encode('utf-8'), c)
                       	continue              
                if data.endswith('qqq'): 
                    clients.remove(addr)
                    continue
                f.write(str(addr)+data + '\n')
                print(str(addr)+data)
                for c in clients:                                
                    if c!=addr: 
                        s.sendto(data.encode('utf-8'),c)
                            
        s.close()

if __name__ == '__main__':
    if len(sys.argv)==1:
        RunServer()
    elif len(sys.argv)==2:
        RunClient(sys.argv[1])
    else:
        print('Run Server:-> python Chat.py')
        print('Run Client:-> python Chat.py <ServerIP>')
