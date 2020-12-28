import json
import time
from django.http import HttpResponse
from netTest.Telnet import OutputLogger, TelnetClient, MessageHandle

# 声明logger对象，用来屏幕输出和写文件记录
logger = OutputLogger(True, True,
                      "./netTest/Telnet/telnet_log/%s.txt" % time.strftime("%Y-%m-%d %H.%M.%S", time.localtime()))
logger_linux = OutputLogger(True, True,
                            "./netTest/Telnet/linux_log/%s.txt" % time.strftime("%Y-%m-%d %H.%M.%S", time.localtime()))

# json文件的读取，全局唯一
json_file = json.load(open("./netTest/commands/setting.json", 'r', encoding='utf-8'))

# telnet连接的映射，全局只创建一个对应路由器的连接
telnet_inst = dict()
