import telnetlib
import time


def handle_msg_from_linux(msg):
    # 处理从linux终端返回的字符串，清理
    if msg.find("]#") != -1 and msg.find("[") != -1:
        if msg[msg.find("#") + 2:] == "":
            return ""
        else:
            return msg[msg.find("#") + 2:]
    else:
        return msg


class TelnetClient:
    def __init__(self, ):
        self.tn = telnetlib.Telnet()

    # 此函数实现telnet登录主机
    def login_host(self, host_ip, username, password):
        try:
            # self.tn = telnetlib.Telnet(host_ip,port=23)
            self.tn.open(host_ip, port=23)
        except:
            print('%s网络连接失败' % host_ip)
            return False
        # 等待login出现后输入用户名，最多等待10秒
        self.tn.read_until(b'login:', timeout=10)
        self.tn.write((username + '\n').encode())
        # 等待Password出现后输入用户名，最多等待10秒
        self.tn.read_until(b'Password:', timeout=10)
        self.tn.write((password + '\n').encode())
        # 延时两秒再收取返回结果，给服务端足够响应时间
        time.sleep(2)
        # 获取登录结果
        # read_very_eager()获取到的是的是上次获取之后本次获取之前的所有输出
        command_result = self.tn.read_very_eager().decode()
        if 'Login incorrect' not in command_result:
            print('%s登录成功' % host_ip)
            return True
        else:
            print('%s登录失败，用户名或密码错误' % host_ip)
            return False

    # 此函数实现执行传过来的命令，并输出其执行结果
    def execute_some_command(self, commands):
        # 执行命令
        for com in commands:
            self.tn.write((com + '\n').encode())
            time.sleep(0.2)
            command_result = self.tn.read_very_eager().decode()
            all_commands = command_result.split("\n")
            for com2 in all_commands:
                cmd_handle = handle_msg_from_linux(com2)
                if cmd_handle != "":
                    print(cmd_handle)
        # time.sleep(2)
        # 获取命令结果

    # 退出telnet
    def logout_host(self):
        self.tn.write("exit\n".encode())


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
    if telnet_client.login_host(host_ip, username, password):
        telnet_client.execute_some_command(commands)
        telnet_client.logout_host()
