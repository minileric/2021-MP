# Модуль socket для сетевого программирования
from socket import *
import datetime
import time

# данные сервера
host = 'localhost'
port = 5051
addres = (host, port)
# socket - функция создания сокета
# первый параметр socket_family может быть AF_INET или AF_UNIX
# второй параметр socket_type может быть SOCK_STREAM(для TCP) или SOCK_DGRAM(для UDP)
udp_socket = socket(AF_INET, SOCK_DGRAM)
# bind - связывает адрес и порт с сокетом
udp_socket.bind(addres)
host1 = 'localhost'
port1 = 5052
addres1 = (host1, port1)
udp_socket1 = socket(AF_INET, SOCK_DGRAM)
udp_socket1.bind(addres1)
client = []  # Массив где храним адреса клиентов
print('Start Server')
# Бесконечный цикл работы программы
while 1:
    now = datetime.datetime.now()
    flag = 0
    # print('rt')
    data, addres = udp_socket.recvfrom(1024)

    newdata = data.decode('utf-8')
    print(newdata)
    slovar = ['cock', 'finger', 'boy next door', 'slaves', 'cum', 'duengeon', 'dangeon master', 'latherman']
    zamena = ['twisted sword', 'hand', 'Yhorm, the Giant', 'hollows', 'estus', 'darkroot garden', 'nameless king', 'unbreakable patches']
    #slovar2 = {'fucking':'non-burning', 'subaru':'stuchat'}
    #slovar2['subaru']
    for i in range(0, len(slovar)):
        if newdata.find(slovar[i]) != -1:
            flag = 1
            newdata = newdata.replace(slovar[i], zamena[i])
        print(newdata)

    stringss = str(now.strftime("%d-%m-%Y %H:%M ")) + str(newdata)
# print('rt')
    number = 1 + newdata.find(']')
    print(number)
    newdata = newdata[:0] + newdata[number:]

    if flag == 1:
        udp_socket1.sendto(('your message has been changed to "' + newdata + '"').encode('utf-8'), addres)


    print(addres[0], addres[1])
    if addres not in client:
        client.append(addres)  # Если такого клиента нету , то добавить
    for clients in client:
        if clients == addres:
            continue  # Не отправлять данные клиенту, который их прислал

        udp_socket.sendto(stringss.encode('utf-8'), clients)
    zapis = open('data.txt', 'a')
    zapis.write(stringss + '\n' + '\n')
    zapis.close()