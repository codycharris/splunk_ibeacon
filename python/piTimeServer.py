from socket import *
import time

s = socket(AF_INET, SOCK_STREAM)
bindto = ('',8111)
s.bind(bindto)
s.listen(5)

while True:
	client, addr = s.accept()
	print("Received connection from %s" % str(addr))
	timestr = time.ctime(time.time()) + "\r\n"
	client.send(timestr.encode('ascii'))
	client.close()
