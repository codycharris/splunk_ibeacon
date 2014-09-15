from socket import *
import errno
from subprocess import call
import os
try:
	s = socket(AF_INET, SOCK_STREAM)
	s.connect(('splunk-server', 8111))
	tm = s.recv(1024)
	s.close()
	myDateTime=tm.decode('ascii')
	dateArg='-s '+myDateTime.rstrip()
	FNULL=open(os.devnull, 'w')
	retcode=call(["date", dateArg], stdout=FNULL)
	logMsg = '{ errLevel=INFO timestamp="'+dateArg[3:]+'" msg="RaspberryPi Date/Time updated from indexer via socket call. Who says we need our own RTC on the Pi!?" }'
except:
	logMsg = '{ errLevel=FATAL msg="Time could not be set via socket. Server process running on splunk-server?" } '
finally:
	print(logMsg)
