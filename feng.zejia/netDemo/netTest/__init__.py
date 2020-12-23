import time

from django.http import HttpResponse
from netTest.Telnet import OutputLogger, TelnetClient, MessageHandle


# 声明logger对象，用来屏幕输出和写文件记录
logger=OutputLogger(True, True,"./netTest/Telnet/telnet_log/%s.txt" % time.strftime("%Y-%m-%d %H.%M.%S", time.localtime()))
logger_linux=OutputLogger(True, True,"./netTest/Telnet/linux_log/%s.txt" % time.strftime("%Y-%m-%d %H.%M.%S", time.localtime()))

telnet_inst=dict()