import json
import time
from netTest.Telnet_old import OutputLogger, TelnetClient, MessageHandle


if __name__ == '__main__':
    logger_demo = OutputLogger(True, True, "../program_log/%s.txt" % time.strftime("%Y-%m-%d %H.%M.%S", time.localtime()))
    # 读取json文件
    # 所有的设置都是从json中读取，所以此处先调用JsonParse模块读取json获取设置
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
    logger_demo.handleMsg('host_ip: %s' % host_ip)
    logger_demo.handleMsg('password_login: %s' % password_login)
    logger_demo.handleMsg('password_enable: %s' % password_enable)
    logger_demo.handleMsg('configCommands: %s' % configCommands)
    logger_demo.handleMsg('testCommands: %s' % testCommands)
    logger_demo.handleMsg("")

    # 实例化Telnet连接对象
    # 实例化一个TelnetClient类，传入logger对象
    # logger对象是一个用来屏幕输出和写文件记录的对象
    # 整个程序中所有和屏幕输出、写文件相关的操作全部调用logger.handleMsg(str)，不用print
    telnet_client = TelnetClient(logger_demo)
    # 登录telnet客户端，这一步是必须的步骤，返回值是True或者False
    while not telnet_client.loginHostRouter(host_ip, password_login, password_enable):
        logger_demo.handleMsg("Telnet连接失败，重试……")
    logger_demo.handleMsg("**程序输出**")
    # 定义2个list列表，original_result_out和handle_result_out
    # original_result_out是用来存储所有的命令所产生的所有输出的集合，这里面是原始的Router的输出，有脏数据，并没有经过处理
    # handle_result_out是用来存储所有的命令所产生的所有经过处理的输出的集合，这里面的数据都经过处理，只有输出
    # 调用executeSomeCommand()函数，传入命令的列表
    original_result_out, handle_result_out = telnet_client.executeSomeCommand(configCommands, "Router")
    logger_demo.handleMsg("\n\n*****清理后的输出*****")
    result_out2 = MessageHandle.handleAllMsg(handle_result_out)
    for out in result_out2:
        logger_demo.handleMsg(out)
