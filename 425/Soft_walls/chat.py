import socket
import threading
import queue
import sys
import random
import os





#Client Code
class Client:
    def start(self):
        self.sct = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.host = socket.gethostbyname(socket.gethostname())
        self.port = random.randint(6000, 10000)
        self.sct.bind((self.host, self.port))
        self.SctIsnRun = False

        print('\nClient IP: ' + str(self.host) + ' Port: ' + str(self.port))

    def stop(self):
        self.SctIsnRun = True
        self.sct.close()

        print('Client Closed')

    def getSocket(self):
        return self.sct

    def getSctIsnRun(self):
        return self.SctIsnRun


class DataControl:
    def receiver(self, sock, sctrn):
        while True:
            if sctrn():
                break
            try:
                data, addr = sock.recvfrom(1024)
                print(data.decode('utf-8'))
            except:
                pass

    def sender(self, sock, data):
        data = '[' + self.name + '] -> ' + data
        sock.sendto(data.encode('utf-8'), self.server)

    def setName(self):
        self.name = input()

    def startDC(self, sock, sctrn, IP, PRT):
        self.server = (str(IP), int(PRT))
        self.name = input('Your nickname: ')
        if self.name == '':
            self.name = 'Guest' + str(random.randint(1000, 9999))
            print('Your name is: ' + self.name)
        sock.sendto(self.name.encode('utf-8'), self.server)
        print(self.server)

        self.thrdRcv = threading.Thread(target=self.receiver, args=(sock, sctrn,))
        self.thrdRcv.start()

    def stopDC(self):
        self.thrdRcv.join()


def RunClient(IP, Port):
    c = Client()
    dc = DataControl()
    c.start()
    dc.startDC(c.getSocket(), lambda: c.getSctIsnRun(), IP, Port)

    while True:
        inp = input('SW Client: ')

        if inp == '/quit':
            dc.sender(c.getSocket(), inp)
            c.stop()
            dc.stopDC()
            break


        else:
            dc.sender(c.getSocket(), inp)

    os._exit(1)
#Client Code Ends Here


#Server Code
class Server:
    def start(self):
        self.sct = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.host = socket.gethostbyname(socket.gethostname())
        self.port = 5000
        self.sct.bind((self.host, self.port))
        self.SctIsnRun = False

        print('\nServer hosting on IP: ' + str(self.host))
        print('Server running...\n')
        print('<< /help >> ')

    def stop(self):
        self.SctIsnRun = True
        self.sct.close()

        print('Server Closed')

    def getSocket(self):
        return self.sct

    def getSctIsnRun(self):
        return self.SctIsnRun


class ClientsBase:
    def receiver(self, sock, sctrn, dubl):
        while True:
            if sctrn():
                break
            try:
                data, addr = sock.recvfrom(1024)
                dubl.put((data, addr))
            except:
                pass

    def sender(self, sock, sctrn, dubl):
        log = open('SWlog.txt', 'a')
        while True:
            if sctrn():
                break
            try:
                if not dubl.empty():
                    data, addr = dubl.get()
                    data = data.decode('utf-8')
                    if addr not in self.clients:
                        self.clients.add(addr)

                        if self.mode == 1:
                            print( str(addr) + ' [' + data + '] присоединился')
                            log.write( str(addr) + ' [' + data + '] присоединился')
                        continue
                    if data.endswith('/quit'):
                        self.clients.remove(addr)
                        continue


                    if self.mode == 1:
                        print(  str(addr) + ' ' + data)
                        log.write( str(addr) + ' ' + data + '\n')
                    for c in self.clients:
                        if c != addr:
                            sock.sendto(data.encode('utf-8'), c)
            except:
                pass
        log.close()

    def tradeMS(self, sctrn, dubl,dublF):
        while True:
            if sctrn():
                break
            try:
                if not dubl.empty():
                    data, addr = dubl.get()
                    data = data.decode('utf-8')
                    dublF.put((data.encode('utf-8'), addr))
            except:
                pass



    def startCBase(self, sock, sctrn):
        self.clients = set()
        self.dublet = queue.Queue()
        self.dubletF = queue.Queue()

        self.mode = 1

        self.thrdRcv = threading.Thread(target=self.receiver, args=(sock, sctrn, self.dublet))
        self.thrdSnd = threading.Thread(target=self.sender, args=(sock, sctrn, self.dubletF))
        self.thrdTrd = threading.Thread(target=self.tradeMS, args=(sctrn, self.dublet, self.dubletF))
        self.thrdRcv.start()
        self.thrdSnd.start()
        self.thrdTrd.start()

    def stopCBase(self):
        self.thrdRcv.join()
        self.thrdSnd.join()
        self.thrdTrd.join()


def RunServer():
    s = Server()
    cb = ClientsBase()
    s.start()
    cb.startCBase(s.getSocket(), lambda: s.getSctIsnRun())

    while True:
        inp = input('SW Console: ')

        if inp == '/restart':
            s.stop()
            cb.stopCBase()
            s.start()
            cb.startCBase(s.getSocket(), lambda: s.getSctIsnRun())
        if inp == '/help':
            print(' /restart  - перезапуск сервера')
            print(' /stop  -остановка сервер ')
        if inp == '/stop':

            s.stop()
            cb.stopCBase()
            break

#Server Code Ends Here


#Связываем Клиент и сервер
if __name__ == '__main__':
    if len(sys.argv)==1:
        RunServer()
    elif len(sys.argv)==3:
        RunClient(sys.argv[1],sys.argv[2])
    else:
        print('Run Serevr:-> python Chat.py')
        print('Run Client:-> python Chat.py <ServerIP>')