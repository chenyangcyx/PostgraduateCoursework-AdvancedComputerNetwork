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
    telnet_client = TelnetClient()
    # 如果登录结果返加True，则执行命令，然后退出
    if telnet_client.login_host(host_ip, username, password,"Linux"):
        telnet_client.execute_some_command(commands)
        telnet_client.logout_host()
