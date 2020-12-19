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
    telnet_client_Linux = TelnetClient(True, True, "./log/%s.txt" % time.time())
    print("原始输出：")
    result_out = list()
    if telnet_client_Linux.loginHostLinux(host_ip, username, password):
        result_out = telnet_client_Linux.executeSomeCommand(commands_linux, "Linux")
    print("清理后的输出：")
    result_out2 = MessageHandle.handleAllMsg(result_out)
    for out in result_out2:
        print(out)


    # # 测试Telnet连接Router主机
    # host_ip = '192.168.1.1'
    # password = 'CISCO'
    # commands_router = [
    # ]
    # telnet_client_Router = TelnetClient(True, True, "./log/%s.txt" % time.time())
    # print("原始输出：")
    # result_out = list()
    # if telnet_client_Router.loginHostRouter(host_ip, password):
    #     result_out = telnet_client_Router.executeSomeCommand(commands_router, "Router")
    # print("清理后的输出：")
    # result_out2 = MessageHandle.handleAllMsg(result_out)
    # for out in result_out2:
    #     print(out)


    # # 测试其他功能
    # telnet_client = TelnetClient(True, True, "./log/%s.txt" % time.time())
    # # 使用telnetlib自带的interact()函数实现实时交互
    # # 不建议使用！无法return值
    # telnet_client.interactInCMD()
    # # 使用自己写的interact方法实现交互，Linux
    # # 先执行一次，获取最初的前缀字符串
    # print(telnet_client.interactSendMsgLinux(""), end="")
    # while 1:
    #     print(telnet_client.interactSendMsgLinux(input()), end="")
    # # 使用自己写的interact方法实现交互，Router
    # # 先执行一次，获取最初的前缀字符串
    # print(telnet_client.interactSendMsgRouter(""), end="")
    # while 1:
    #     print(telnet_client.interactSendMsgRouter(input()), end="")


    # # JsonParse的使用示例
    # from JsonParse import *
    # if __name__ == '__main__':
    #     json_parse = JsonParser("setting.json")
    #     json_parse.getData_groupId()
    #     json_parse.getData_groupMembers()
    #     json_parse.getData_subjectName()
    #     json_parse.getData_creationDate()
    #     json_parse.getData_routerNum()
    #     json_parse.getData_routerSettings()
