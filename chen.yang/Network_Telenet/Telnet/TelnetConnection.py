import telnetlib
import time
import _thread
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
        command_result = self.tn.read_very_eager().decode()
        if host_type == "Linux":
            if 'Login incorrect' not in command_result:
                print('%s登录成功' % host_ip)
                # 开始发送心跳包，防止telnet连接断开
                # print("开始发送心跳包……\n")
                _thread.start_new_thread(self.sendHeartbeat, (10,))
                return True
            else:
                print('%s登录失败，用户名或密码错误' % host_ip)
                return False
        elif host_type == "Router":
            if 'Login invalid' not in command_result:
                print('%s登录成功' % host_ip)
                # 开始发送心跳包，防止telnet连接断开
                # print("开始发送心跳包……\n")
                _thread.start_new_thread(self.sendHeartbeat, (10,))
                return True
            else:
                print('%s登录失败，用户名或密码错误' % host_ip)
                return False

    # 发送心跳包，以保持telnet的连接
    def sendHeartbeat(self, delay_time):
        while 1:
            self.tn.write('\n'.encode())
            # show_content="%s: 发送了一个心跳包\n" % time.time()
            # print(show_content)
            # if self.if_print_to_file:
            #     self.outfile.write(show_content)
            #     self.outfile.flush()
            time.sleep(delay_time)

    # 执行传输过来的一条指令，返回所有原始输出结果
    def executeOneCommand(self, command, if_print, if_print_to_file):
        self.tn.write((command + '\n').encode())
        time.sleep(0.2)
        result = self.tn.read_very_eager().decode()
        result = result.replace("\r\n", "\n")
        if if_print:
            print(result)
        if if_print_to_file:
            self.outfile.write(result + "\n")
            self.outfile.flush()
        return result

    # 执行传输过来的命令集合，返回所有原始输出结果
    def executeSomeCommand(self, commands):
        result_list = list()
        for com in commands:
            result_list.append(self.executeOneCommand(com, self.if_print, self.if_print_to_file))
        print(result_list)
        return result_list

    # 实时交互的Telnet命令
    def interactiveExecuteCMD(self):
        while 1:
            input_cmd = input("Command# ")
            if input_cmd == "endend":
                break
            if self.if_print_to_file:
                self.outfile.write("Command# %s\n" % input_cmd)
                self.outfile.flush()
            execute_result = self.executeOneCommand(input_cmd, False, False)
            #execute_result = handleMsgFromLinux(execute_result)
            print("Result# %s" % execute_result)
            if self.if_print_to_file:
                self.outfile.write("Result# %s\n" % execute_result)
                self.outfile.flush()

    # 退出telnet
    def logoutHost(self):
        self.tn.write("exit\n".encode())
