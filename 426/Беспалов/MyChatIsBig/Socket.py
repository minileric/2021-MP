import threading
import socket
import time
import ssl
import os


"""
Проект выполнен Беспаловым Сергеем, Маленьким Семёном, Головановым Кириллом.
Главный класс на котором держатся остальные

"""


class Socket(socket.socket):
    def __init__(self):
        super(Socket, self).__init__(socket.SOCK_DGRAM)

    def send_data(self, data):
        raise NotImplementedError()

    def listen_socket(self, listened_socket=None):
        raise NotImplementedError()

    def set_up(self):
        raise NotImplementedError()
