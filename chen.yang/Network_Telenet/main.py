# Telnet的使用示例
from Telnet import *
import time

if __name__ == '__main__':
    host_ip = '10.201.2.10'
    username = 'root'
    password = 'njuchenyang'
    commands = ["cd /home",
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
                ]
    # 测试Telenet连接Linux主机
    telnet_client = TelnetClient(True,True,"%s.txt"%time.time())
    print("原始输出：")
    if telnet_client.loginHost(host_ip, username, password, "Linux"):
        telnet_client.interactiveExecuteCMD()
    #     result_out = telnet_client.executeSomeCommand(commands)
    #     telnet_client.logoutHost()
    #
    # print("清理后的输出：")
    # result_out2 = MessageHandle.handleAllMsg(result_out)
    # for out in result_out2:
    #     print(out)
    #
    # while 1:
    #     time.sleep(1)
    #     pass

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
