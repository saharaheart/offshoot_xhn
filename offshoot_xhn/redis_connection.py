import redis
import socket
sock = socket.socket(socket.AF_UNIX,socket.SOCK_STREAM)
sock.connect("/tmp/redis.sock")
message = 'This is the first letter'.encode('utf-8')
sock.sendall(message)
data = ''
while True:

    data_one = sock.recv(16)
    data = data+data_one
    print(f'receive data is {data}')
    if not data_one:
        print('no more data')
sock.close()