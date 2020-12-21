from Telnet import *
import time


if __name__ == '__main__':
    # 测试Telenet连接Linux主机
    host_ip = '10.201.2.10'
    username = 'root'
    password = 'njuchenyang'
    commands_linux = [
        "cd /home",
        "rm -f *.txt",
        "touch 1.txt",
        "echo `ll` > 1.txt",
        "touch 2.txt",
        "echo `ll` > 2.txt",
        "touch 3.txt",
        "echo `ll` > 3.txt",
        "touch 4.txt",
        "echo `ll` > 4.txt",
        "touch 5.txt",
        "echo `ll` > 5.txt",
        "ll",
        "cat 1.txt",
        "rm -f 1.txt",
        "ll",
        "cat 2.txt",
        "rm -f 2.txt",
        "ll",
        "cat 3.txt",
        "rm -f 3.txt",
        "ll",
        "cat 4.txt",
        "rm -f 4.txt",
        "ll",
        "cat 5.txt",
        "rm -f 5.txt",
        "ll",
        "ping baidu.com -c 2"
    ]
    logger = OutputLogger(True, True, "./linux_log/%s.txt" % time.time())
    telnet_client_Linux = TelnetClient(logger)
    logger.handleMsg("原始输出：")
    result_out = list()
    if telnet_client_Linux.loginHostLinux(host_ip, username, password):
        result_out = telnet_client_Linux.executeSomeCommand(commands_linux, "Linux")
    logger.handleMsg("清理后的输出：")
    result_out2 = MessageHandle.handleAllMsg(result_out)
    for out in result_out2:
        logger.handleMsg(out)

    # # 测试其他功能
    # telnet_client = TelnetClient(logger)
    # # 使用telnetlib自带的interact()函数实现实时交互
    # # 不建议使用下面的函数！无法return值
    # # telnet_client.interactInCMD()
    # # 使用自己写的interact方法实现交互，Linux
    # # 先执行一次，获取最初的前缀字符串
    # if telnet_client.loginHostLinux(host_ip, password):
    #     logger.handleMsg(telnet_client.interactSendMsgLinux(""), end="")
    #     while 1:
    #         logger.handleMsg(telnet_client.interactSendMsgLinux(input()), end="")
