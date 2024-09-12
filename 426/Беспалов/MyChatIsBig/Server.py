import threading
from Socket import Socket
from Log import LoggList


"""
Проект выполнен Беспаловым Сергеем, Маленьким Семёном, Головановым Кириллом.

"""


class Server(Socket):
    def __init__(self):
        super(Server, self).__init__()
        print('Waiting to messages')
        self.clients = []
        self.a = LoggList()

    def set_up(self):
        self.bind(("127.0.0.1", 9090))
        self.listen(2)
        self.accepted_sockets()

    def send_data(self, data):
        for client in self.clients:
            client.send(data)
            self.a.log('User sad: ' + bytes.decode(data, 'utf-8'))

    def listen_socket(self, listened_socket=None):
        print('Waiting to messages')

        while True:
            data = listened_socket.recv(2048)
            print(f'User send {data}')
            self.send_data(data)

    def accepted_sockets(self):
        while True:
            client, address = self.accept()
            print('Client', {address[0]}, 'has connected')

            self.clients.append(client)
            client.send("Successful".encode('utf-8'))

            listen_on = threading.Thread(target=self.listen_socket, args=(client,))
            listen_on.start()


if __name__ == "__main__":
    server = Server()
    server.set_up()
