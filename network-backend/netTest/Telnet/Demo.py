import json
import time

from netTest.Telnet import OutputLogger, TelnetClient, MessageHandle

if __name__ == '__main__':
    json_file = json.load(open("../setting.json", 'r', encoding='utf-8'))

    configName = 'RIP'
    settingNum = 1

    # 按照configName找到要验证的路由协议
    configItem = None
    for settingItem in json_file['routerSettings']:
        if settingItem['configName'] == configName:
            configItem = settingItem

    # 实例化一个TelnetClient类，传入logger对象
    # logger对象是一个用来屏幕输出和写文件记录的对象
    # 整个程序中所有和屏幕输出、写文件相关的操作全部调用logger.handleMsg(str)，不用print
    logger_demo = OutputLogger(True, True,
                               "../program_log/%s.txt" % time.strftime("%Y-%m-%d %H.%M.%S", time.localtime()))

    # 读取参数，对各个参数进行解析
    host_ip = configItem['configDetail'][settingNum]['hostIp']
    password_login = configItem['configDetail'][settingNum]['loginPassword']
    password_enable = configItem['configDetail'][settingNum]['enablePassword']
    configCommands = configItem['configDetail'][settingNum]['configCommands']
    testCommands = configItem['configDetail'][settingNum]['testCommands']
    logger_demo.handleMsg('具体配置：')
    logger_demo.handleMsg('host_ip: %s' % host_ip)
    logger_demo.handleMsg('password_login: %s' % password_login)
    logger_demo.handleMsg('password_enable: %s' % password_enable)
    logger_demo.handleMsg('configCommands: %s' % configCommands)
    logger_demo.handleMsg('testCommands: %s' % testCommands)
    logger_demo.handleMsg("")

    # 实例化Telnet连接对象
    telnet_client = TelnetClient(logger_demo)
    # 登录telnet客户端
    while not telnet_client.loginRouter(host_ip, password_login, password_enable, True):
        logger_demo.handleMsg("Telnet连接失败，重试……")
    # 进入特权模式
    telnet_client.goEnable()

    # 测试发送命令
    test_command = ['show ip interface']
    logger_demo.handleMsg('\n测试发送命令……')
    result_out = telnet_client.executeSomeCMD(test_command)
    logger_demo.handleMsg("**程序输出**")
    # 处理原始输出
    result_out1 = MessageHandle.reformatOriginalResult(result_out)
    for msg in result_out1:
        logger_demo.handleMsg(msg)
    # 获取命令执行结果
    logger_demo.handleMsg("**清理后输出**")
    result_out2 = MessageHandle.deleteLineWithCmdPrefix(telnet_client.tn.hostname, result_out1)
    for msg in result_out2:
        logger_demo.handleMsg(msg)

    # # 测试获取neighbors
    # logger_demo.handleMsg('\n测试获取Neighbors……')
    # logger_demo.handleMsg("**程序输出**")
    # telnet_client.getNeighbors()
    #
    # # 测试获取版本号-1
    # logger_demo.handleMsg('\n测试获取Version-1……')
    # logger_demo.handleMsg("**程序输出**")
    # telnet_client.getVersion(1)
    #
    # # 测试获取版本号-2
    # logger_demo.handleMsg('\n测试获取Version-2……')
    # logger_demo.handleMsg("**程序输出**")
    # telnet_client.getVersion(2)
    #
    # # 测试获取所有接口信息
    # logger_demo.handleMsg('\n测试获取Interfaces……')
    # logger_demo.handleMsg("**程序输出**")
    # telnet_client.getAllInterfaces()
    #
    # # 测试获取所有ARP表
    # logger_demo.handleMsg('\n测试获取ARPTable……')
    # logger_demo.handleMsg("**程序输出**")
    # telnet_client.getARPTable()
    #
    # # 测试获取所有MAC表
    # logger_demo.handleMsg('\n测试获取MACTable……')
    # logger_demo.handleMsg("**程序输出**")
    # telnet_client.getMACTable()
