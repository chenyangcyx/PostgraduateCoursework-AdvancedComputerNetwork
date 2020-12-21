from Telnet import *
import time

if __name__ == '__main__':
    # 测试Telnet连接Router主机
    host_ip = '192.168.1.2'
    password_login = 'CISCO'
    password_enable = 'CISCO'
    commands_router = [
        "show ip route"
    ]
    logger = OutputLogger(True, True, "../telnet_log/%s.txt" % time.strftime("%Y-%m-%d %H.%M.%S", time.localtime()))
    telnet_client_Router = TelnetClient(logger)
    logger.handleMsg("*****原始输出*****")
    result_out = list()
    if telnet_client_Router.loginHostRouter(host_ip, password_login, password_enable):
        result_out = telnet_client_Router.executeSomeCommand(commands_router, "Router")
    logger.handleMsg("\n\n*****清理后的输出*****")
    result_out2 = MessageHandle.handleAllMsg(result_out)
    for out in result_out2:
        logger.handleMsg(out)

    # # 测试其他功能
    # telnet_client = TelnetClient(logger)
    # # 使用telnetlib自带的interact()函数实现实时交互
    # # 不建议使用下面的函数！无法return值
    # # telnet_client.interactInCMD()
    # # 使用自己写的interact方法实现交互，Router
    # # 先执行一次，获取最初的前缀字符串
    # if telnet_client.loginHostRouter(host_ip, password_login, password_enable):
    #     logger.handleMsg(telnet_client.interactSendMsgRouter(""), end="")
    #     while 1:
    #         logger.handleMsg(telnet_client.interactSendMsgRouter(input()), end="")
