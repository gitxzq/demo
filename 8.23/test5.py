#-*-coding:utf-8-*-
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('www.sina.com.cn',80))
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
buffer=[]
while True:
    d=s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data=b''.join(buffer)

s.close()

header,html=data.split(b'\r\n\r\n')
print(header.decode('utf-8'))

with open('sain.html','wb') as f:
    f.write(html)