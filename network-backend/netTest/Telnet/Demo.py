import json
import time
from netTest.Telnet import *

if __name__ == '__main__':
    logger = OutputLogger(True, True, "telnet_log/%s.txt" % time.strftime("%Y-%m-%d %H.%M.%S", time.localtime()))
    json_file = json.load(open("setting.json", 'r', encoding='utf-8'))
    settingNUm = 0
    host_ip = json_file['routerSettings'][0]['configDetail'][settingNUm]['hostIp']
    password_login = json_file['routerSettings'][0]['configDetail'][settingNUm]['loginPassword']
    password_enable = json_file['routerSettings'][0]['configDetail'][settingNUm]['enablePassword']
    configCommands = json_file['routerSettings'][0]['configDetail'][settingNUm]['configCommands']
    testCommands = json_file['routerSettings'][0]['configDetail'][settingNUm]['testCommands']
    logger.handleMsg('具体配置：')
    logger.handleMsg(host_ip)
    logger.handleMsg(password_login)
    logger.handleMsg(password_enable)
    logger.handleMsg(configCommands)
    logger.handleMsg(testCommands)
    logger.handleMsg("")

    # 测试连接功能
    # 实例化一个TelnetClient类，传入logger对象
    # logger对象是一个用来屏幕输出和写文件记录的对象
    # 整个程序中所有和屏幕输出、写文件相关的操作全部调用logger.handleMsg(str)，不用print
    telnet_client_Router = TelnetClient(logger)
    logger.handleMsg("*****程序输出*****")
    result_out = list()
    # 首先，登录telnet客户端，这一步是必须的步骤，返回值是True或者False
    if telnet_client_Router.loginRouter(host_ip, password_login, password_enable):
        # 进入特权模式下执行指令
        telnet_client_Router.goEnable()
        # 其次，调用executeSomeCommand()函数，传入命令的列表
        result_out= telnet_client_Router.executeSomeCMD(configCommands)
        logger.handleMsg(result_out)
