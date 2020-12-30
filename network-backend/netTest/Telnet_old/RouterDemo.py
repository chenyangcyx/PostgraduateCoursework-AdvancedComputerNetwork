import json
import time

from netTest.Telnet_old import OutputLogger

if __name__ == '__main__':
    logger = OutputLogger(True, True, "telnet_log/%s.txt" % time.strftime("%Y-%m-%d %H.%M.%S", time.localtime()))
    # # 测试Telnet连接Router主机
    # host_ip = '192.168.1.2'
    # password_login = 'CISCO'
    # password_enable = 'CISCO'
    # commands_router = [
    #     "show ip route"
    # ]
    # 读取json文件
    # 所有的设置都是从json中读取，所以此处先调用JsonParse模块读取json获取设置
    json_file = json.load(open("setting.json", 'r', encoding='utf-8'))
    settingNUm = 0  # 选择不同的路由器的配置，具体见json文件内容
    host_ip = json_file['routerSettings'][0]['configDetail'][settingNUm]['hostIp']
    password_login = json_file['routerSettings'][0]['configDetail'][settingNUm]['loginPassword']
    password_enable = json_file['routerSettings'][0]['configDetail'][settingNUm]['enablePassword']
    configCommands = json_file['routerSettings'][0]['configDetail'][settingNUm]['configCommands']
    testCommands = json_file['routerSettings'][0]['configDetail'][settingNUm]['testCommands']
    logger.handleMsg('具体配置：')
    logger.handleMsg(host_ip)
    logger.handleMsg(password_login)
    logger.handleMsg(password_enable)
    logger.handleMsg(configCommands)
    logger.handleMsg(testCommands)
    logger.handleMsg("")

    # 测试连接功能
    # 实例化一个TelnetClient类，传入logger对象
    # logger对象是一个用来屏幕输出和写文件记录的对象
    # 整个程序中所有和屏幕输出、写文件相关的操作全部调用logger.handleMsg(str)，不用print
    telnet_client_Router = TelnetClient(logger)
    logger.handleMsg("*****原始输出*****")
    # 定义2个list列表，original_result_out和handle_result_out
    # original_result_out是用来存储所有的命令所产生的所有输出的集合，这里面是原始的Router的输出，有脏数据，并没有经过处理
    # handle_result_out是用来存储所有的命令所产生的所有经过处理的输出的集合，这里面的数据都经过处理，只有输出
    original_result_out = list()
    handle_result_out = list()
    # 首先，登录telnet客户端，这一步是必须的步骤，返回值是True或者False
    if telnet_client_Router.loginHostRouter(host_ip, password_login, password_enable):
        # 其次，调用executeSomeCommand()函数，传入命令的列表
        original_result_out, handle_result_out = telnet_client_Router.executeSomeCommand(configCommands, "Router")
    logger.handleMsg("\n\n*****清理后的输出*****")
    result_out2 = MessageHandle.handleAllMsg(handle_result_out)
    for out in result_out2:
        logger.handleMsg(out)
