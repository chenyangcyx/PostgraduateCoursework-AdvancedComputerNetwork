import json
import time

from netTest.Telnet import TelnetClient, OutputLogger, MessageHandle


# 声明logger对象，用来屏幕输出和写文件记录
logger = OutputLogger(True, True, "netTest/program_log/%s.txt" % time.strftime("%Y-%m-%d %H.%M.%S", time.localtime()))
# json文件的读取，全局唯一
json_file = json.load(open("netTest/setting.json", 'r', encoding='utf-8'))
# telnet连接的映射，全局只创建一个对应路由器的连接
telnet_dict = dict()
# 记录每个路由器接口的ip地址
router_interface_ip = dict()
# 记录每个路由器接口的子网掩码
router_interface_netmask = dict()


# 获取指定的Telnet连接对象
# 使用字典的单例模式，全局只有唯一的一个对象实例
def getTelnetObject(object_name, logger=None):
    if object_name in telnet_dict:
        return telnet_dict.get(object_name), True
    else:
        telnet_dict[object_name] = TelnetClient(logger)
        return telnet_dict[object_name], False


# 使用单例模式创建对象
def createObjectSingleton(object_name, logger, host_ip, password_login, password_enable):
    logger.handleMsg("获取Telnet:%s的唯一对象……" % object_name)
    local_telnet, if_exist = getTelnetObject(object_name, logger)
    if if_exist:
        logger.handleMsg("Telnet:%s对象已经创建，获取成功" % object_name)
        pass
    else:
        logger.handleMsg("Telnet:%s对象未被创建，开始创建……" % object_name)
        while not local_telnet.loginRouter(host_ip, password_login, password_enable, if_send_heartbeat=False):
            logger.handleMsg("Telnet连接失败，重试……")
        local_telnet.goEnable()
    return local_telnet


# 执行路由器上的一段脚本
def executeCommands(configName, routerNum, commands):
    if configName is not None:
        logger.handleMsg("configName:%s" % str(configName))
    else:
        configName = 'RIP'
    if routerNum is not None:
        logger.handleMsg("routerNum:%s" % str(routerNum))
    else:
        routerNum = 0
    logger.handleMsg("commands:%s" % str(commands))

    # 按照configName找到要验证的路由协议
    configItem = None
    for settingItem in json_file['routerSettings']:
        if settingItem['configName'] == configName:
            configItem = settingItem

    # 读取参数，对各个参数进行解析
    host_ip = configItem['configDetail'][routerNum]['hostIp']
    password_login = configItem['configDetail'][routerNum]['loginPassword']
    password_enable = configItem['configDetail'][routerNum]['enablePassword']

    # 使用单例模式创建对象
    dict_no = f'Router{routerNum}'
    local_telnet = createObjectSingleton(dict_no, logger, host_ip, password_login, password_enable)

    # 获取输出
    result_out_original = local_telnet.executeSomeCMD(commands)
    result_out = MessageHandle.reformatOriginalResult(result_out_original)
    logger.handleMsg("**程序输出**")
    for msg in result_out:
        logger.handleMsg(msg)
    logger.handleMsg('\n')

    return result_out


# 获取IP地址的ip域，不做ip格式检查，传入前保证正确
def getIPArea(ip_address: str, netmask: str):
    ip_address_split = ip_address.split('.')
    netmask_split = netmask.split('.')
    ip_result = ""
    for i in range(4):
        if i != 0:
            ip_result += '.'
        ip_result += str(int(ip_address_split[i]) & int(netmask_split[i]))
    return ip_result


# 获取子网掩码的反码
def getContrastNetmask(netmask: str):
    netmask_split = netmask.split('.')
    netmask_result = ""
    for i in range(4):
        if i != 0:
            netmask_result += '.'
        netmask_result += str(255 - int(netmask_split[i]))
    return netmask_result
