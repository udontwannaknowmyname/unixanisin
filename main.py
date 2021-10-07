
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # (IPV4, TCP)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # исключение ожидания
server_socket.bind(('localhost', 9905))  # domain:port
server_socket.listen(1)

while True:
    #  print('Before .accept()')
    client_socket, address = server_socket.accept()  # прием подключения, блокирующая операция
    print("Подключено! Адрес:", address)

    while True:
        #  print('Ожидание ответа!')
        request = client_socket.recv(1024)  # блокирующая операция
        print(request.decode())
        if not request:
            break
        else:
            message = input()
            client_socket.send(message.encode())

    print('Вышли из внутреннего цикла!')
    client_socket.close()
