import socket

client_socket = socket.socket()
client_socket.connect(('localhost', 9905))

while True:
    try:
        message = input().encode()
        client_socket.send(message)
        #  print('Ожидание сообщения')
        request = client_socket.recv(1024)  # блокирующая операция
        print(request.decode())
    except KeyboardInterrupt:
        break

client_socket.close()
