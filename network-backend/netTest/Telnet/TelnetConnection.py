import _thread
import time
from netTest.Telnet import ciscolib


class TelnetClient:
    def __init__(self, logger):
        # 日志记录对象
        self.logger = logger
        # 用来进行Telnet连接的对象
        self.tn = None

    # telnet登录主机
    def loginRouter(self, host_ip, password_login, password_enable, if_send_heartbeat=False):
        self.tn = ciscolib.Device(host_ip, password_login, enable_password=password_enable)
        try:
            self.logger.handleMsg('开始连接主机: %s' % host_ip)
            self.tn.connect()
        except Exception as e:
            self.logger.handleMsg('无法连接到主机%s: %s' % (host_ip, str(e)))
            return False
        self.logger.handleMsg('连接成功！')
        # 发送心跳包，防止telnet连接断开
        if if_send_heartbeat:
            self.logger.handleMsg('创建线程发送心跳包……')
            _thread.start_new_thread(self.sendHeartbeat, (30,))
        return True

    # 发送心跳包，以保持telnet的连接
    def sendHeartbeat(self, delay_time):
        while 1:
            time.sleep(delay_time)
            self.tn.cmd('\n')

    # 进入enable模式
    def goEnable(self):
        try:
            self.logger.handleMsg('进入特权模式……')
            self.tn.enable()
        except Exception as e:
            self.logger.handleMsg('进入enalbe模式失败: %s' % str(e))
            return False
        self.logger.handleMsg('进入enable模式成功！')
        return True

    # 执行命令
    def executeCMD(self, cmd):
        self.logger.handleMsg('executeCMD:\n%s' % cmd)
        result = self.tn.cmd(cmd).replace("\r\n", "\n")
        self.logger.handleMsg('executeCMD-Result:\n%s' % result)
        return result

    # 执行多条命令
    def executeSomeCMD(self, commands):
        result_list = list()
        self.logger.handleMsg('executeSomeCMD:\n%s' % commands)
        for com in commands:
            result = self.executeCMD(com)
            result_list.append(result)
        self.logger.handleMsg('executeSomeCMD-Result:\n%s' % result_list)
        return result_list

    # 与Telnet实时交互，无返回值
    def interactInCMD(self):
        self.tn._connection.interact()

    # 获取路由器/交换机的neighbors
    # 返回值是一个dict的list，形式如下：
    # {hostname, ip, local_port, remote_port}
    def getNeighbors(self):
        self.logger.handleMsg('getNeighbors……')
        result = self.tn.get_neighbors()
        self.logger.handleMsg('getNeighbors-Result: %s' % result)

    # 获取路由器/交换机的版本号
    def getVersion(self, type=1):
        if type == 1:
            self.logger.handleMsg('getVersion, function:get_model()……')
            try:
                version = self.tn.get_model()
                self.logger.handleMsg('getVersion-Result: %s' % version)
            except Exception as e:
                self.logger.handleMsg('getVersion-Result: Error, %s' % str(e))
        elif type == 2:
            self.logger.handleMsg('getVersion, function:get_ios_version()……')
            try:
                version = self.tn.get_model()
                self.logger.handleMsg('getVersion-Result: %s' % version)
            except Exception as e:
                self.logger.handleMsg('getVersion-Result: Error, %s' % str(e))
        else:
            pass

    # 获取路由器/交换机的所有接口信息
    # 返回值是一个dict的list，形式如下：
    # {name, status, description, vlan, duplex, speed, media}
    def getAllInterfaces(self):
        self.logger.handleMsg('getAllInterfaces……')
        try:
            result = self.tn.get_interfaces()
            self.logger.handleMsg('getAllInterfaces-Result: %s' % result)
        except Exception as e:
            self.logger.handleMsg('getAllInterfaces: Error, %s' % str(e))

    # 获取路由器/交换机的所有ARP表
    def getARPTable(self):
        self.logger.handleMsg('getARPTable……')
        result = self.tn.get_arp_table()
        self.logger.handleMsg('getARPTable-Result: %s' % result)

    # 获取路由器/交换机的MAC表
    def getMACTable(self):
        self.logger.handleMsg('getMACTable……')
        result = self.tn.get_mac_table()
        self.logger.handleMsg('getMACTable-Result: %s' % result)

    # 退出telnet
    def logoutRouter(self):
        self.tn.disconnect()
