import json
import time
from netTest.Telnet import OutputLogger, TelnetClient

if __name__ == '__main__':
    logger_demo = OutputLogger(True, True,
                               "../program_log/%s.txt" % time.strftime("%Y-%m-%d %H.%M.%S", time.localtime()))
    json_file = json.load(open("../setting.json", 'r', encoding='utf-8'))

    configName = 'RIP_normal'
    settingNum = 0

    # 按照configName找到要验证的路由协议
    configItem = None
    for settingItem in json_file['routerSettings']:
        if settingItem['configName'] == configName:
            configItem = settingItem

    # 读取参数，对各个参数进行解析
    host_ip = configItem['configDetail'][settingNum]['hostIp']
    password_login = configItem['configDetail'][settingNum]['loginPassword']
    password_enable = configItem['configDetail'][settingNum]['enablePassword']
    configCommands = configItem['configDetail'][settingNum]['configCommands']
    testCommands = configItem['configDetail'][settingNum]['testCommands']
    logger_demo.handleMsg('具体配置：')
    logger_demo.handleMsg(host_ip)
    logger_demo.handleMsg(password_login)
    logger_demo.handleMsg(password_enable)
    logger_demo.handleMsg(configCommands)
    logger_demo.handleMsg(testCommands)
    logger_demo.handleMsg("")

    # 测试连接功能
    # 实例化一个TelnetClient类，传入logger对象
    # logger对象是一个用来屏幕输出和写文件记录的对象
    # 整个程序中所有和屏幕输出、写文件相关的操作全部调用logger.handleMsg(str)，不用print
    telnet_client_Router = TelnetClient(logger_demo)
    logger_demo.handleMsg("*****程序输出*****")
    result_out = list()
    # 首先，登录telnet客户端，这一步是必须的步骤，返回值是True或者False
    if telnet_client_Router.loginRouter(host_ip, password_login, password_enable):
        # 进入特权模式下执行指令
        telnet_client_Router.goEnable()
        # 其次，调用executeSomeCommand()函数，传入命令的列表
        result_out = telnet_client_Router.executeSomeCMD(configCommands)
        logger_demo.handleMsg(result_out)
