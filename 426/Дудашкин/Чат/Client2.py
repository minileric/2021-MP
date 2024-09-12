import socket
import threading


def read_sok():
    while 1:
        data = sor.recv(1024)
        print(data.decode('utf-8'))


server = 'localhost', 5051  # Данные сервера
print('Write psev')
alias = input()  # Вводим наш псевдоним
# print('Write')
sor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# print('Write')
sor.bind(('', 0))  # Задаем сокет как клиент
# print('Write')
sor.sendto((alias + ' Connect to server').encode('utf-8'), server)  # Уведомляем сервер о подключении
# print('Write')
potok = threading.Thread(target=read_sok)
potok.start()
while 1:
    # print('write mess')
    mensahe = input()
    if mensahe == '!out':
        sor.sendto((alias + ' !user has exit!').encode('utf-8'), server)
        break
    if mensahe == '!renick':
        kek = input('Enter your new nick: ')
        print('Your nick was changed!')
        sor.sendto(('[' + alias + ']' + 'has changed his nick to ' + kek).encode('utf-8'), server)
        alias = kek
    else:
        sor.sendto(('[' + alias + ']' + mensahe).encode('utf-8'), server)
