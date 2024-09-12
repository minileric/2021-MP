import threading
from Socket import Socket


class Client(Socket):
    def __init__(self):
        super(Client, self).__init__()

    def set_up(self):
        self.connect(("127.0.0.1", 9090))
        listened_thread = threading.Thread(target=self.listen_socket)
        listened_thread.start()

        send_thread = threading.Thread(target=self.send_data, args=(None,))
        send_thread.start()

    def listen_socket(self, listened_socket=None):
        while True:
            data = self.recv(2048)
            print(data.decode('utf-8'))

    def send_data(self, data):
        while True:
            self.send(input(':::').encode('utf-8'))


if __name__ == '__main__':
    client = Client()
    client.set_up()
