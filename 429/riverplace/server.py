from Socket import Socket 
import threading
import queue
import sys
import random
import os
import string 
import json
class Server(Socket):
    def __init__(self):
        super(Server,self).__init__()
        self.host='127.0.0.1'
        self.port=8080
        self.addr=(self.host,self.port)
        self.bind(self.addr)
        print("Server work")
        self.users =[]
        self.name=[]
        self.ban=[]
    def send_data(self,data,addr):
        if data.decode('utf-8').split(' ')[0]=='changename':
            pass
        else:
            for c in self.users:
                if c!=addr:
                    self.sendto(data,c)
    def send_all(self,data):
        for c in self.users:
                    self.sendto(data.encode('utf-8'),c)
    def recv_data(self,sock=None,recvPackets=None):
        while True:
            try:
                data,addr = self.recvfrom(2048)
                print(str(addr)+data.decode('utf-8'))
                self.save(data.decode('utf-8'))
                if {i.lower().translate(str.maketrans('','',string.punctuation))for i in data.decode('utf-8').split(' ')}\
                .intersection(set(json.load(open('cenz.json'))))!= set():
                    print('не прошел ')
                    data=str("Ууу кого отшлёпать ")
                    self.sendto(data.encode('utf-8'),addr) 
                elif 'откос' in data.decode('utf-8').lower().split(' '):
                    sentense=data.decode('utf-8')
                    new_sentense=sentense.replace("откос","СУПЕР ОТКОС ")
                    data=new_sentense.encode('utf-8')
                    mess=str("Красавчик что упомянул откос ")
                    self.sendto(mess.encode('utf-8'),addr) 
                    recvPackets.put((data,addr))
                else:
                    recvPackets.put((data,addr))
            except ConnectionResetError:
                print(f'Client remove {addr} ')
                if addr in self.users:
                    self.users.remove(addr)
                return 
    def save(self,data):
        chat=json.load(open('save.json'))
        chat.append(data)
        with open('save.json','w',encoding='utf-8') as file:
            json.dump(chat,file,indent=3)
    def commands(self):
        while True:
            x=input('Commanda')
            if x=='q':
                print('Rab')
                print(self.name)
            if x=='port':
                self.port=input('Номер порта')
                data="changeport120923 "+f"{self.port}"
                self.send_all(data)
                print(self.addr)
            if x=='ban':
                print(self.name)
                addr=int(input("Введите адресс чела которого хотите замутить "))
                print(addr,'Вы ввелли')
                for i in range(len(self.users)):
                    print(self.users[i][1],' итый юзер')
                    if int(self.users[i][1])==addr:
                        data='Вы добавлены в бан '
                        print(data)
                        addr=self.users[i]
                        self.ban.append(addr)
                        self.sendto(data.encode('utf-8'),addr)
                        self.users.remove(addr)
                        print(self.users,'New self users')
                        for  i in range(len(self.name)):
                            if self.name[i][1]==addr:
                                self.name.remove(self.name[i])
                                
            if x=='fldel':
                data=json.load(open('cenz.json'))
                print(data)
                for i in range(len(data)):
                    print(data[i],'  элемент номер',i)
                art=int(input('Введите номер элемента который хотите удалить'))
                if art>len(data):
                    print('Неправильное значение')
                else:
                    del data[art]
                    print(data)
                    with open('cenz.json','w',encoding='utf-8') as e:
                        json.dump(data,e)
            if x=='flopen':
                data=json.load(open('cenz.json'))
                print(data)
            
            if x=='flappend':   
                data=json.load(open('cenz.json'))
                print(data)
                word=str(input('Введите слово которое хотите добавить в фильтр'))
                data.append(word)
                with open('cenz.json','w',encoding='utf-8') as e:
                        json.dump(data,e)
            if x=='savech':
                data=json.load(open('save.json'))
                for i in range(len(data)):
                    print(data[i])
            if x=='asis':
                print('q  список пользователей')
                print('ban добавить в бан ')
                print('fldel удалить слова из фильтра запрещенки')
                print('flopen посмотреть запрещенные слова')
                print('flappend добавить слово в запрещёнку')
                print('savech посмотреть лог чата')
            
    def RunServer(self):
        recvPackets = queue.Queue()
        print('Server Running...')
        accepted_user=threading.Thread(target=self.recv_data,args=(Server,recvPackets))
        accepted_user.start()
        commands=threading.Thread(target=self.commands)
        commands.start()
        while True:
                while not recvPackets.empty():
                    data,addr = recvPackets.get()
                    if addr in self.users:
                        self.send_data(data,addr)
                    elif addr not in self.users:
                        if addr in self.ban:
                            pass
                        else:
                            dan=[data.decode('utf-8'),addr]
                            self.users.append(addr)
                            self.name.append(dan)
                            print(f"Добивл нового пользователя {addr}")
                            print(self.name)
                        continue
            
                        
                    data = data.decode('utf-8')
                    if data.endswith('qqq'):
                        self.users.remove(addr)
                        for  i in range(len(self.name)):
                            if self.name[i][1]==addr:
                                Name=self.name[i][0]
                                self.name.remove(self.name[i])
                        data=f"{Name}  Pass the Chat" 
                        print(data)
                        continue
                    if data.split(' ')[0]=='changename':
                        name=data.split(' ')[1]
                        for  i in range(len(self.name)):
                            print(self.name[i])
                            if self.name[i][1]==addr:
                                self.name[i][0]=name
                                data=f"Ваше имя успешно изменено на {name} "
                                self.sendto(data.encode('utf-8'),addr)
                                break     
                   
           
if __name__=='__main__':
    server=Server()
    server.RunServer()
 ##C:\Users\Артем\Desktop\messenger