import random


"""
Проект выполнен Беспаловым Сергеем, Маленьким Семёном, Головановым Кириллом.
Данный скрипт шифрует логи сервера по алгоритму RSA. Зашифрованную версию можно посмотреть в server_log_RSA.txt

"""


def FermaTest(p):
    base = 10
    f = True
    for a in range(2, base + 1):
        answer = pow(a, p - 1, p)
        if answer != 1:
            f = False
            break

    return f


def FermaGenAndTest(N):

    f = True
    while f:
        p = int(random.random() * 10) % 9 + 1
        p = int((p + random.random()) * 10 ** (N - 2))

        last = [1, 3, 9, 7]
        q = random.random() * 10
        q = int(q) % 4
        p = p * 10 + last[q]

        if FermaTest(p):
            f = False

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

    file = open(name, "r")
    oll_text = file.read()
    file.close()
    oll_text_in_bytes = oll_text.encode('utf8')

    list_of_80_bytes = [oll_text_in_bytes[x: x + 80] for x in
                        range(0, len(oll_text_in_bytes), 80)]
    list_of_80_int = [int.from_bytes(list_of_80_bytes[i], byteorder='big') for i in
                      range(0, len(list_of_80_bytes))]
    return list_of_80_int


def getKeys():

    p = getnumber(100)
    q = getnumber(100)
    n = p * q
    phi = (p - 1) * (q - 1)

    for e in range(5, phi):
        nod, x, y = gcd_extended(phi, e)

        if nod == 1:
            break

    d = y
    return e, d, n


def coding(name):

    list_int = getText(name)
    e, d, n = getKeys()
    coding = [pow(list_int[i], e, n) for i in range(0, len(list_int))]
    with open('server_log_RSA.txt', 'w') as data:
        data.write(str(coding))

    return coding, d, n


def decoding(codingtext, d, n):

    uncoding = [pow(codingtext[i], d, n) for i in range(0, len(codingtext))]
    my_list_of_80_bytes = [uncoding[i].to_bytes(80, byteorder='big') for i in range(0, len(uncoding))]
    my_oll_text_in_bytes = bytes([])
    for i in range(len(my_list_of_80_bytes)):
        my_oll_text_in_bytes = my_oll_text_in_bytes + my_list_of_80_bytes[i]
    my_oll_text = bytes.decode(my_oll_text_in_bytes, 'utf-8')
    return (my_oll_text)


coding, d, n = coding('server_log.txt')
text = decoding(coding, d, n)
print(text)
