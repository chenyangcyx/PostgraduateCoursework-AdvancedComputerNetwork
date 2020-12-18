# Telnet的使用示例
from Telnet import *
import time

if __name__ == '__main__':
    host_ip = '192.168.1.2'
    username = 'root'
    password = 'CISCO'
    commands = [
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
        "ll"
    #             "enable",
    #             "CISCO",
    #             "configure terminal",
    #             "router rip",
    #             "version 1",
    #             "network 192.168.12.0",
    #             "network 192.168.23.0",
    #             "exit",
    #             "exit",
    #             "show ip route",
    #
    #             "ping 192.168.12.0",
    #             "ping 192.168.23.0"
    ]
    # 测试Telenet连接Linux主机
    telnet_client_Linux = TelnetClient(True, True, "%s.txt" % time.time())
    print("原始输出：")
    if telnet_client_Linux.loginHostLinux(host_ip, username, password):
        # telnet_client.interactiveExecuteCMD()
        result_out = telnet_client_Linux.executeSomeCommand(commands)

    # # 测试Telnet连接Router主机
    # telnet_client_Router=TelnetClient(True,True,"%s.txt"%time.time())
    # print("原始输出：")
    # if telnet_client_Router.loginHostRouter(host_ip, password):
    #     # telnet_client.interactiveExecuteCMD()
    #     result_out = telnet_client_Router.executeSomeCommand(commands)

    print("清理后的输出：")
    result_out2 = MessageHandle.handleAllMsg(result_out)
    for out in result_out2:
        print(out)

    while 1:
        time.sleep(1)
        pass

# JsonParse的使用示例
# from JsonParse import *
#
# if __name__ == '__main__':
#     json_parse = JsonParser("setting.json")
#     json_parse.getData_groupId()
#     json_parse.getData_groupMembers()
#     json_parse.getData_subjectName()
#     json_parse.getData_creationDate()
#     json_parse.getData_routerNum()
#     json_parse.getData_routerSettings()
