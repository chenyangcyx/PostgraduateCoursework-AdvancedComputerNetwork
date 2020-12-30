import base64
import json
import time
from django.http import HttpResponse
from netTest.Telnet import TelnetClient, OutputLogger, MessageHandle

# 声明logger对象，用来屏幕输出和写文件记录
logger = OutputLogger(True, True, "program_log/%s.txt" % time.strftime("%Y-%m-%d %H.%M.%S", time.localtime()))
# json文件的读取，全局唯一
json_file = json.load(open("setting.json", 'r', encoding='utf-8'))
# telnet连接的映射，全局只创建一个对应路由器的连接
telnet_dict = {}


# 获取指定的Telnet连接对象
# 使用字典的单例模式，全局只有唯一的一个对象实例
def getTelnetObject(object_name, logger=None):
    if object_name in telnet_dict:
        return telnet_dict.get(object_name), True
    else:
        telnet_dict[object_name] = TelnetClient(logger)
        return telnet_dict[object_name], False


# 输出获取到的json数据
def printJsonObject(json_object):
    logger.handleMsg('获取到的JSON数据：')
    logger.handleMsg('configName: %s' % json_object['configName'])
    logger.handleMsg('configDescription: %s' % json_object['configDescription'])
    logger.handleMsg('routerNum: %s' % json_object['routerNum'])
    logger.handleMsg('configDetail: %s' % json_object['configDetail'])


# 执行路由器的配置脚本
def executeConfigCommand(request):
    if request.method == 'GET':
        configName = request.GET.get('configName')
        settingNum = int(request.GET.get('settingNum'))

        logger.handleMsg('[call api]\n调用时间：%s' % time.strftime("%Y-%m-%d %H.%M.%S", time.localtime()))
        logger.handleMsg("调用接口：executeConfigCommand")
        logger.handleMsg("configName:%s" % str(configName))
        logger.handleMsg("settingNum:%s" % str(settingNum))

        # 按照configName找到要验证的路由协议
        configItem = None
        for settingItem in json_file['routerSettings']:
            if settingItem['configName'] == configName:
                configItem = settingItem
        logger.handleMsg('获取configItem成功')
        printJsonObject(configItem)

        # 读取参数，对各个参数进行解析
        host_ip = configItem['configDetail'][settingNum]['hostIp']
        password_login = configItem['configDetail'][settingNum]['loginPassword']
        password_enable = configItem['configDetail'][settingNum]['enablePassword']
        configCommands = configItem['configDetail'][settingNum]['configCommands']
        logger.handleMsg('获取程序参数成功')
        logger.handleMsg('host_ip: %s' % host_ip)
        logger.handleMsg('password_login: %s' % password_login)
        logger.handleMsg('password_enable: %s' % password_enable)
        logger.handleMsg('configCommands: %s' % configCommands)

        # # 不使用单例模式创建对象
        # local_telnet = TelnetClient(logger)
        # local_telnet.loginHostRouter(host_ip, password_login, password_enable)
        # local_telnet.goEnable()

        # 使用单例模式创建对象
        dict_no = str(configName) + str(settingNum)
        logger.handleMsg("获取Telnet:%s的唯一对象……" % dict_no)
        local_telnet, if_exist = getTelnetObject(dict_no, logger)
        if if_exist:
            logger.handleMsg("Telnet:%s对象已经创建，获取成功" % dict_no)
            pass
        else:
            logger.handleMsg("Telnet:%s对象未被创建，开始创建……" % dict_no)
            while not local_telnet.loginRouter(host_ip, password_login, password_enable, False):
                logger.handleMsg("Telnet连接失败，重试……")
            local_telnet.goEnable()
        logger.handleMsg("Telnet:%s对象创建成功！" % dict_no)

        result_out = local_telnet.executeSomeCMD(configCommands)
        result_out1 = list()
        for msg in result_out:
            for one_cmd in msg.split("\n"):
                result_out1.append(one_cmd)
        logger.handleMsg("**程序输出**")
        for msg in result_out1:
            logger.handleMsg(msg)
        logger.handleMsg("\n**清理后的输出**")
        result_out2 = MessageHandle.deleteLineWithCmdPrefix(local_telnet.tn.hostname, result_out1)
        for msg in result_out2:
            logger.handleMsg(msg)
        logger.handleMsg('\n')

        return HttpResponse(json.dumps({'original_result': result_out1, 'handle_result': result_out2}),
                            content_type='application/json;charset=utf-8')


# 执行路由器的测试脚本
def executeTestCommand(request):
    if request.method == 'GET':
        configName = request.GET.get('configName')
        settingNum = int(request.GET.get('settingNum'))

        logger.handleMsg('[call api]\n调用时间：%s' % time.strftime("%Y-%m-%d %H.%M.%S", time.localtime()))
        logger.handleMsg("调用接口：executeTestCommand")
        logger.handleMsg("configName:%s" % str(configName))
        logger.handleMsg("settingNum:%s" % str(settingNum))

        # 按照configName找到要验证的路由协议
        configItem = None
        for settingItem in json_file['routerSettings']:
            if settingItem['configName'] == configName:
                configItem = settingItem
        logger.handleMsg('获取configItem成功')
        printJsonObject(configItem)

        # 读取参数，对各个参数进行解析
        host_ip = configItem['configDetail'][settingNum]['hostIp']
        password_login = configItem['configDetail'][settingNum]['loginPassword']
        password_enable = configItem['configDetail'][settingNum]['enablePassword']
        testCommands = configItem['configDetail'][settingNum]['testCommands']
        logger.handleMsg('获取程序参数成功')
        logger.handleMsg('host_ip: %s' % host_ip)
        logger.handleMsg('password_login: %s' % password_login)
        logger.handleMsg('password_enable: %s' % password_enable)
        logger.handleMsg('testCommands: %s' % testCommands)

        # # 不使用单例模式创建对象
        # local_telnet = TelnetClient(logger)
        # local_telnet.loginHostRouter(host_ip, password_login, password_enable)
        # local_telnet.goEnable()

        # 使用单例模式创建对象
        dict_no = str(configName) + str(settingNum)
        logger.handleMsg("获取Telnet:%s的唯一对象……" % dict_no)
        local_telnet, if_exist = getTelnetObject(dict_no, logger)
        if if_exist:
            logger.handleMsg("Telnet:%s对象已经创建，获取成功" % dict_no)
            pass
        else:
            logger.handleMsg("Telnet:%s对象未被创建，开始创建……" % dict_no)
            while not local_telnet.loginRouter(host_ip, password_login, password_enable, False):
                logger.handleMsg("Telnet连接失败，重试……")
            local_telnet.goEnable()
        logger.handleMsg("Telnet:%s对象创建成功！" % dict_no)

        result_out = local_telnet.executeSomeCMD(testCommands)
        result_out1 = list()
        for msg in result_out:
            for one_cmd in msg.split("\n"):
                result_out1.append(one_cmd)
        logger.handleMsg("**程序输出**")
        for msg in result_out1:
            logger.handleMsg(msg)
        logger.handleMsg("\n**清理后的输出**")
        result_out2 = MessageHandle.deleteLineWithCmdPrefix(local_telnet.tn.hostname, result_out1)
        for msg in result_out2:
            logger.handleMsg(msg)
        logger.handleMsg('\n')

        return HttpResponse(json.dumps({'original_result': result_out1, 'handle_result': result_out2}),
                            content_type='application/json;charset=utf-8')


# 执行路由器上的一条脚本
def executeOneCommand(request):
    if request.method == 'GET':
        configName = request.GET.get('configName')
        settingNum = int(request.GET.get('settingNum'))
        singleCommand = list()
        singleCommand.append(base64.b64decode(request.GET.get('command')).decode("utf-8"))

        logger.handleMsg('[call api]\n调用时间：%s' % time.strftime("%Y-%m-%d %H.%M.%S", time.localtime()))
        logger.handleMsg("调用接口：executeOneCommand")
        logger.handleMsg("configName:%s" % str(configName))
        logger.handleMsg("settingNum:%s" % str(settingNum))
        logger.handleMsg("singleCommand:%s" % str(singleCommand))

        # 按照configName找到要验证的路由协议
        configItem = None
        for settingItem in json_file['routerSettings']:
            if settingItem['configName'] == configName:
                configItem = settingItem
        logger.handleMsg('获取configItem成功')
        printJsonObject(configItem)

        # 读取参数，对各个参数进行解析
        host_ip = configItem['configDetail'][settingNum]['hostIp']
        password_login = configItem['configDetail'][settingNum]['loginPassword']
        password_enable = configItem['configDetail'][settingNum]['enablePassword']
        logger.handleMsg('获取程序参数成功')
        logger.handleMsg('host_ip: %s' % host_ip)
        logger.handleMsg('password_login: %s' % password_login)
        logger.handleMsg('password_enable: %s' % password_enable)

        # # 不使用单例模式创建对象
        # local_telnet = TelnetClient(logger)
        # local_telnet.loginHostRouter(host_ip, password_login, password_enable)
        # local_telnet.goEnable()

        # 使用单例模式创建对象
        dict_no = str(configName) + str(settingNum)
        logger.handleMsg("获取Telnet:%s的唯一对象……" % dict_no)
        local_telnet, if_exist = getTelnetObject(dict_no, logger)
        if if_exist:
            logger.handleMsg("Telnet:%s对象已经创建，获取成功" % dict_no)
            pass
        else:
            logger.handleMsg("Telnet:%s对象未被创建，开始创建……" % dict_no)
            while not local_telnet.loginRouter(host_ip, password_login, password_enable, False):
                logger.handleMsg("Telnet连接失败，重试……")
            local_telnet.goEnable()
        logger.handleMsg("Telnet:%s对象创建成功！" % dict_no)

        result_out = local_telnet.executeSomeCMD(singleCommand)
        result_out1 = list()
        for msg in result_out:
            for one_cmd in msg.split("\n"):
                result_out1.append(one_cmd)
        logger.handleMsg("**程序输出**")
        for msg in result_out1:
            logger.handleMsg(msg)
        logger.handleMsg("\n**清理后的输出**")
        result_out2 = MessageHandle.deleteLineWithCmdPrefix(local_telnet.tn.hostname, result_out1)
        for msg in result_out2:
            logger.handleMsg(msg)
        logger.handleMsg('\n')

        return HttpResponse(json.dumps({'original_result': result_out1, 'handle_result': result_out2}),
                            content_type='application/json;charset=utf-8')


# 执行一条命令
def executeCommand(request):
    if request.method == 'GET':
        host = base64.b64decode(request.GET.get('host')).decode("utf-8")
        loginpassword = base64.b64decode(request.GET.get('loginpassword')).decode("utf-8")
        enablepassword = base64.b64decode(request.GET.get('enablepassword')).decode("utf-8")
        isSingleCommand = request.GET.get('isSingleCommand')
        command_str = base64.b64decode(request.GET.get('command')).decode("utf-8")
        command = None
        if isSingleCommand == '0':
            command = list()
            for com in command_str.split('\n'):
                command.append(com)
        elif isSingleCommand == '1':
            command = command_str

        logger.handleMsg('[call api]\n调用时间：%s' % time.strftime("%Y-%m-%d %H.%M.%S", time.localtime()))
        logger.handleMsg("调用接口：executeCommand")
        logger.handleMsg("host:%s" % str(host))
        logger.handleMsg("loginpassword:%s" % str(loginpassword))
        logger.handleMsg("enablepassword:%s" % str(enablepassword))
        logger.handleMsg("isSingleCommand:%s" % str(isSingleCommand))
        logger.handleMsg("command:%s" % str(command))

        # # 不使用单例模式创建对象
        # local_telnet = TelnetClient(logger)
        # local_telnet.loginHostRouter(host_ip, password_login, password_enable)
        # local_telnet.goEnable()

        # 使用单例模式创建对象
        dict_no = str(host) + str(loginpassword) + str(enablepassword)
        logger.handleMsg("获取Telnet:%s的唯一对象……" % dict_no)
        local_telnet, if_exist = getTelnetObject(dict_no, logger)
        if if_exist:
            logger.handleMsg("Telnet:%s对象已经创建，获取成功" % dict_no)
            pass
        else:
            logger.handleMsg("Telnet:%s对象未被创建，开始创建……" % dict_no)
            while not local_telnet.loginRouter(host, loginpassword, enablepassword, False):
                logger.handleMsg("Telnet连接失败，重试……")
            local_telnet.goEnable()
        logger.handleMsg("Telnet:%s对象创建成功！" % dict_no)

        result_out = local_telnet.executeSomeCMD(command)
        result_out1 = list()
        for msg in result_out:
            for one_cmd in msg.split("\n"):
                result_out1.append(one_cmd)
        logger.handleMsg("**程序输出**")
        for msg in result_out1:
            logger.handleMsg(msg)
        logger.handleMsg('\n')

        return HttpResponse(json.dumps(result_out1), content_type='application/json;charset=utf-8')
