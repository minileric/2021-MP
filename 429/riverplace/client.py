from Socket import Socket
from datetime import datetime
import threading
import queue
import sys
import random
import os
class Client(Socket):
       
    def __init__(self):
        super(Client,self).__init__()
        self.host = '127.0.0.1'
        self.port = 8080
        self.addr=(self.host,self.port)
        self.ports=random.randint(6000,10000)
        self.addres=(self.host,self.ports)
        self.bind(self.addres)
        threading.Thread(target=self.recv_data).start()
    def recv_data(self,sock=None):
        while True:
            try:
                data,addr = self.recvfrom(2048)
                print(data.decode('utf-8'))
                if data.decode('utf-8').split(' ')[0]=='changeport120923':
                    print('Поенял порт ')
                    self.port=int(data.decode('utf-8').split(' ')[1])
                    print(self.port)
                    print(self.addr)
            except:
                pass
    def send_data(self,data,addr,name=None):
        name=str(name)
        time=str(datetime.now().replace(microsecond=0))
        data ='['+name+']' + '->'+time+'/// '+ data
        self.sendto(data.encode('utf-8'),addr)
        
        
    def RunClient(self):
        ##host = '127.0.0.1'
        ##port = 8080
        ##addr=(host,port)
        name = input('Please write your name here: ')
        if name == '':
            name = 'Guest'+str(random.randint(1000,9999))
            print('Your name is:'+name)
        self.sendto(name.encode('utf-8'),self.addr)
        print(f'Приветствую в чате На Откосе  {name}')
        while True:
            data = input('Cообщение:')
            if data == 'qqq':
                self.sendto(data.encode('utf-8'),self.addr)
                break
            elif data=='changename':
                name=input('Please write your name here: ')
                data=data+' '+f'{name}'
                self.sendto(data.encode('utf-8'),self.addr)
                continue
            elif data=='changeport':  
                self.ports=input('Please write your port: ')
                print('Порт изменен ')
            elif data=='changeip': 
                ##self.sendto(data.encode('utf-8'),addr)
                pass
                
                
            elif data=='':
                continue
            self.send_data(data,self.addr,name)
        Client().close()
        os._exit(1)
if __name__=='__main__':
    client=Client()
    client.RunClient()
            