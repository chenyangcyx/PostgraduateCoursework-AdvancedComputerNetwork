from Telnet import *
import time
import json

if __name__ == '__main__':
    logger = OutputLogger(True, True, "../telnet_log/%s.txt" % time.strftime("%Y-%m-%d %H.%M.%S", time.localtime()))
    # # 测试Telnet连接Router主机
    # host_ip = '192.168.1.2'
    # password_login = 'CISCO'
    # password_enable = 'CISCO'
    # commands_router = [
    #     "show ip route"
    # ]
    # 读取json文件
    json_file = json.load(open("setting.json", 'r', encoding='utf-8'))
    settingNUm = 0
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
    telnet_client_Router = TelnetClient(logger)
    logger.handleMsg("*****原始输出*****")
    original_result_out = list()
    handle_result_out = list()
    if telnet_client_Router.loginHostRouter(host_ip, password_login, password_enable):
        original_result_out, handle_result_out = telnet_client_Router.executeSomeCommand(configCommands, "Router")
    logger.handleMsg("\n\n*****清理后的输出*****")
    result_out2 = MessageHandle.handleAllMsg(handle_result_out)
    for out in result_out2:
        logger.handleMsg(out)

    # # 测试其他功能
    # telnet_client = TelnetClient(logger)
    # # 使用telnetlib自带的interact()函数实现实时交互
    # # 不建议使用下面的函数！无法return值
    # # telnet_client.interactInCMD()
    # # 使用自己写的interact方法实现交互，Router
    # # 先执行一次，获取最初的前缀字符串
    # if telnet_client.loginHostRouter(host_ip, password_login, password_enable):
    #     logger.handleMsg(telnet_client.interactSendMsgRouter(""), end="")
    #     while 1:
    #         logger.handleMsg(telnet_client.interactSendMsgRouter(input()), end="")
