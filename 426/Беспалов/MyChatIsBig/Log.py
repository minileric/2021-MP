import time


class Logg:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))
        with open('server_log.txt', 'a') as data:
            data.write(str(time.ctime()) + ": " + str(msg) + '\n')


class LoggList(Logg, list):
    log_list = []

    def append(self, msg):
        super().log(msg)
        super().append(msg)


