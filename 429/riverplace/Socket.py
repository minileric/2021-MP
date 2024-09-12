import socket 


class Socket(socket.socket):
        def __init__(self):
            super(Socket,self).__init__(
                socket.AF_INET,
                socket.SOCK_DGRAM
            
            )
        def recv_data(self,sock=None):
            raise NotImplementedError()
        def send_data(self,data,addr,name=None):
            raise NotImplementedError()
        