import redis
import sys
import socket
import os
r = redis.Redis(host = 'localhost',port = 6379,db=0)
r.set('foo','bar')
print(r.get('foo'))
print(sys.stderr)
'''This is the server'''
server_add ="/tmp/redis.sock"
try:
    os.unlink(server_add)
except OSError:
    if os.path.exists(server_add):
        raise
sock = socket.socket(socket.AF_UNIX,socket.SOCK_STREAM)
sock.bind(server_add)
sock.listen(1)
data = ''
while True:
    conn,re_add = sock.accept()
    print('connection from ' + 're_add')

    while True:
        data_one = conn.recv(16)
        data = data + data_one.decode()
        print(f'receiving content is {data}')
        if not data_one:
            print('no more data')
            break
    conn.close()




