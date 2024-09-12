import random


class RSA:

    def __init__(self):
        self.p = 0
        self.N = 0

    def FermaTest(self.p):
        base = 10  # число целых оснований
        f = True  # флаг
        for a in range(2, base + 1):  # перебор оснований
            answer = pow(a, self.p - 1, self.p)  # быстрое сравнение по модулю
            if answer != 1:
                f = False  # сброс флага
                break  # прерывание цикла

        return f

    def FermaGenAndTest(N):

        f = True  # Флаг, сообщающий, нужно ли генерировать число
        while f:
            # Генерируем число от 0 до 8 и прибавляем 1 чтобы получить рандомное число в интервале от 1 до 9
            p = int(random.random() * 10) % 9 + 1
            p = int((p + random.random()) * 10 ** (N - 2))

            # Генерируем последнее число
            last = [1, 3, 9, 7]
            q = random.random() * 10
            q = int(q) % 4  # число 0, 1, 2 или 3 - случайный индекс списка
            p = p * 10 + last[q]  # добавляем в конец

            if FermaTest(p):
                f = False  # сброс флага - число найденно

        return p

    def getnumber(N):
        p = FermaGenAndTest(N)

        return p

    def gcd_extended(num1, num2):
        if num1 == 0:
            return (num2, 0, 1)
        else:
            div, x, y = gcd_extended(num2 % num1, num1)
        return div, y - (num2 // num1) * x, x

    def getText(name):

        file = open(name, "r")  # открытие файла в режиме чтения
        oll_text = file.read()  # чтение файла
        file.close()  # закрытие файла
        oll_text_in_bytes = oll_text.encode('utf8')  # перевод текста в поток байтов

        list_of_80_bytes = [oll_text_in_bytes[x: x + 80] for x in
                            range(0, len(oll_text_in_bytes), 80)]  # разделение общей кучи байт на куски по 80 штук
        list_of_80_int = [int.from_bytes(list_of_80_bytes[i], byteorder='big') for i in
                          range(0, len(list_of_80_bytes))]  # перевод байтов в целые числа
        return list_of_80_int

    def getKeys():  # RSA - АЛГОРИТМ ГЕНЕРАЦИИ КЛЮЧЕЙ

        # 1 генерируем 2 простых
        p = getnumber(100)
        q = getnumber(100)
        # 2 модуль
        n = p * q
        # 3 функция эйлера от модуля
        phi = (p - 1) * (q - 1)

        # 4 открытая экспонента e

        for e in range(5, phi):
            nod, x, y = gcd_extended(phi, e)

            if nod == 1:
                break

        # 5 закрытая экспонента d
        print(y)
        d = y
        return e, d, n

    def coding(name):

        list_int = getText(name)
        e, d, n = getKeys()
        coding = [pow(list_int[i], e, n) for i in range(0, len(list_int))]
        return coding, d, n

    def decoding(codingtext, d, n):

        uncoding = [pow(codingtext[i], d, n) for i in range(0, len(codingtext))]
        my_list_of_80_bytes = [uncoding[i].to_bytes(80, byteorder='big') for i in range(0, len(uncoding))]
        my_oll_text_in_bytes = bytes([])
        for i in range(len(my_list_of_80_bytes)):
            my_oll_text_in_bytes = my_oll_text_in_bytes + my_list_of_80_bytes[i]
        my_oll_text = bytes.decode(my_oll_text_in_bytes, 'utf-8')
        return (my_oll_text)

    coding, d, n = coding('input.txt')
    text = decoding(coding, d, n)
    print(text)
