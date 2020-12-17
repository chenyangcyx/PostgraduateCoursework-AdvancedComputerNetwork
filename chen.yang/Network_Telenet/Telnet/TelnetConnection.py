import telnetlib
import time
from Telnet import *


class TelnetClient:
    def __init__(self, if_print=True, if_print_to_file=True, print_file_path="out.txt"):
        self.tn = telnetlib.Telnet()
        # 获取到输出后是否打印
        self.if_print = if_print
        # 结果是否输出到文件
        self.if_print_to_file = if_print_to_file
        if if_print_to_file:
            self.outfile = open(print_file_path, "w", encoding="utf-8")

    # 此函数实现telnet登录主机
    def loginHost(self, host_ip, username, password, host_type):
        try:
            self.tn.open(host_ip, port=23)
        except:
            print('%s网络连接失败' % host_ip)
            return False
        username_info = ""
        if host_type == "Linux":
            username_info = b'login'
        elif host_type == "Router":
            username_info = b'Username:'
        # 等待login出现后输入用户名，最多等待10秒
        self.tn.read_until(username_info, timeout=10)
        self.tn.write((username + '\n').encode())
        # 等待Password出现后输入用户名，最多等待10秒
        self.tn.read_until(b'Password', timeout=10)
        self.tn.write((password + '\n').encode())
        # 延时两秒再收取返回结果，给服务端足够响应时间
        time.sleep(2)
        # 获取登录结果
        # read_very_eager()获取到的是的是上次获取之后本次获取之前的所有输出
        command_result = self.tn.read_very_eager().decode()
        if host_type == "Linux":
            if 'Login incorrect' not in command_result:
                print('%s登录成功' % host_ip)
                return True
            else:
                print('%s登录失败，用户名或密码错误' % host_ip)
                return False
        elif host_type == "Router":
            if 'Login invalid' not in command_result:
                print('%s登录成功' % host_ip)
                return True
            else:
                print('%s登录失败，用户名或密码错误' % host_ip)
                return False

    # 执行传输过来的一条指令，返回所有原始输出结果
    def executeOneCommand(self, command):
        self.tn.write((command + '\n').encode())
        time.sleep(0.2)
        result = self.tn.read_very_eager().decode()
        result=result.replace("\r\n", "\n")
        if self.if_print:
            print(result)
        if self.if_print_to_file:
            self.outfile.write(result+"\n")
        return result

    # 执行传输过来的命令集合，返回所有原始输出结果
    def executeSomeCommand(self, commands):
        result_list = list()
        for com in commands:
            result_list.append(self.executeOneCommand(com))
        print(result_list)
        return result_list

    # 退出telnet
    def logoutHost(self):
        self.tn.write("exit\n".encode())
