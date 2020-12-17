# Telnet的使用示例
from Telnet import *

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
                "cat 2.txt",
                "cat 3.txt",
                "cat 4.txt",
                "cat 5.txt"
                ]
    # 测试Telenet连接Linux主机
    telnet_client = TelnetClient(True)
    print("原始输出：")
    if telnet_client.loginHost(host_ip, username, password, "Linux"):
        result_out = telnet_client.executeSomeCommand(commands)
        telnet_client.logoutHost()

    print("清理后的输出：")
    result_out2 = MessageHandle.handleAllMsg(result_out)
    for out in result_out2:
        print(out)

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
