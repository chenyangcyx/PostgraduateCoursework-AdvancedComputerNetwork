import base64
import json
from netTest import *


# 执行路由器的配置脚本
def executeConfigCommand(request):
    if request.method == 'GET':
        configName = request.GET.get('configName')
        settingNum = int(request.GET.get('settingNum'))
        json_file = json.load(open("./netTest/commands/setting.json", 'r', encoding='utf-8'))

        logger.handleMsg('[call api]\n调用时间：%s' % time.strftime("%Y-%m-%d %H.%M.%S", time.localtime()))
        logger.handleMsg("调用接口：executeConfigCommand")
        logger.handleMsg("configName:%s" % str(configName))
        logger.handleMsg("settingNum:%s" % str(settingNum))

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

        logger.handleMsg("**原始输出**")
        local_telnet = None
        dict_no = str(configName) + str(settingNum)
        if telnet_inst[dict_no] is None:
            telnet_inst[dict_no] = TelnetClient(logger)
            local_telnet = telnet_inst[dict_no]
            while not local_telnet.loginHostRouter(host_ip, password_login, password_enable):
                logger.handleMsg("连接失败，重试……")
                pass
        else:
            local_telnet = telnet_inst[dict_no]
        original_result_out, handle_result_out = local_telnet.executeSomeCommand(configCommands, "Router")
        result_out1 = list()
        for msg in original_result_out:
            for one_cmd in msg.split("\n"):
                result_out1.append(one_cmd)
        logger.handleMsg("\n**清理后的输出**")
        result_out2 = MessageHandle.handleAllMsg(handle_result_out)
        for out in result_out2:
            logger.handleMsg(out)
        logger.handleMsg('\n\n')

        return HttpResponse(json.dumps({'original_result': result_out1, 'handle_result': result_out2}),
                            content_type='application/json;charset=utf-8')


# 执行路由器的测试脚本
def executeTestCommand(request):
    if request.method == 'GET':
        configName = request.GET.get('configName')
        settingNum = int(request.GET.get('settingNum'))
        json_file = json.load(open("./netTest/commands/setting.json", 'r', encoding='utf-8'))

        logger.handleMsg('[call api]\n调用时间：%s' % time.strftime("%Y-%m-%d %H.%M.%S", time.localtime()))
        logger.handleMsg("调用接口：executeTestCommand")
        logger.handleMsg("configName:%s" % str(configName))
        logger.handleMsg("settingNum:%s" % str(settingNum))

        # 按照configName找到要验证的路由协议
        configItem = None
        for settingItem in json_file['routerSettings']:
            if settingItem['configName'] == configName:
                configItem = settingItem

        # 读取参数，对各个参数进行解析
        host_ip = configItem['configDetail'][settingNum]['hostIp']
        password_login = configItem['configDetail'][settingNum]['loginPassword']
        password_enable = configItem['configDetail'][settingNum]['enablePassword']
        configCommands = configItem['configDetail'][settingNum]['testCommands']

        logger.handleMsg("**原始输出**")
        local_telnet = None
        dict_no = str(configName) + str(settingNum)
        if telnet_inst[dict_no] is None:
            telnet_inst[dict_no] = TelnetClient(logger)
            local_telnet = telnet_inst[dict_no]
            while not local_telnet.loginHostRouter(host_ip, password_login, password_enable):
                logger.handleMsg("连接失败，重试……")
                pass
        else:
            local_telnet = telnet_inst[dict_no]
        original_result_out, handle_result_out = local_telnet.executeSomeCommand(configCommands, "Router")
        result_out1 = list()
        for msg in original_result_out:
            for one_cmd in msg.split("\n"):
                result_out1.append(one_cmd)
        logger.handleMsg("\n**清理后的输出**")
        result_out2 = MessageHandle.handleAllMsg(handle_result_out)
        for out in result_out2:
            logger.handleMsg(out)
        logger.handleMsg('\n\n')

        return HttpResponse(json.dumps({'original_result': result_out1, 'handle_result': result_out2}),
                            content_type='application/json;charset=utf-8')


# 执行路由器上的一条脚本
def executeOneCommand(request):
    if request.method == 'GET':
        configName = request.GET.get('configName')
        settingNum = int(request.GET.get('settingNum'))
        singleCommand = list()
        singleCommand.append(base64.b64decode(request.GET.get('command')).decode("utf-8"))
        json_file = json.load(open("./netTest/commands/setting.json", 'r', encoding='utf-8'))

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

        # 读取参数，对各个参数进行解析
        host_ip = configItem['configDetail'][settingNum]['hostIp']
        password_login = configItem['configDetail'][settingNum]['loginPassword']
        password_enable = configItem['configDetail'][settingNum]['enablePassword']

        logger.handleMsg("**原始输出**")
        local_telnet = None
        dict_no = str(configName) + str(settingNum)
        if telnet_inst[dict_no] is None:
            telnet_inst[dict_no] = TelnetClient(logger)
            local_telnet = telnet_inst[dict_no]
            while not local_telnet.loginHostRouter(host_ip, password_login, password_enable):
                logger.handleMsg("连接失败，重试……")
                pass
        else:
            local_telnet = telnet_inst[dict_no]
        original_result_out, handle_result_out = local_telnet.executeSomeCommand(singleCommand, "Router")
        result_out1 = list()
        for msg in original_result_out:
            for one_cmd in msg.split("\n"):
                result_out1.append(one_cmd)
        logger.handleMsg("\n**清理后的输出**")
        result_out2 = MessageHandle.handleAllMsg(handle_result_out)
        for out in result_out2:
            logger.handleMsg(out)
        logger.handleMsg('\n\n')

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
        terminalType = request.GET.get('terminalType')

        logger.handleMsg('[call api]\n调用时间：%s' % time.strftime("%Y-%m-%d %H.%M.%S", time.localtime()))
        logger.handleMsg("调用接口：executeCommand")
        logger.handleMsg("host:%s" % str(host))
        logger.handleMsg("loginpassword:%s" % str(loginpassword))
        logger.handleMsg("enablepassword:%s" % str(enablepassword))
        logger.handleMsg("isSingleCommand:%s" % str(isSingleCommand))
        logger.handleMsg("command:%s" % str(command))
        logger.handleMsg("terminalType:%s" % str(terminalType))

        logger.handleMsg("**原始输出**")
        local_telnet = None
        dict_no = str(host) + str(loginpassword) + str(enablepassword)
        if telnet_inst[dict_no] is None:
            telnet_inst[dict_no] = TelnetClient(logger)
            local_telnet = telnet_inst[dict_no]
            while not local_telnet.loginHostRouter(host, loginpassword, enablepassword):
                logger.handleMsg("连接失败，重试……")
                pass
        else:
            local_telnet = telnet_inst[dict_no]
        original_result_out, handle_result_out = local_telnet.executeSomeCommand(command, terminalType)
        result_out1 = list()
        for msg in original_result_out:
            for one_cmd in msg.split("\n"):
                result_out1.append(one_cmd)
        logger.handleMsg("\n**清理后的输出**")
        result_out2 = MessageHandle.handleAllMsg(handle_result_out)
        for out in result_out2:
            logger.handleMsg(out)
        logger.handleMsg('\n\n')

        return HttpResponse(json.dumps({'original_result': result_out1, 'handle_result': result_out2}),
                            content_type='application/json;charset=utf-8')


# 用来测试Linux的Telnet的函数
def executeSomeCommandInLinux(request):
    if request.method == 'GET':
        configName = request.GET.get('configName')
        settingNum = int(request.GET.get('settingNum'))

        logger.handleMsg('[call api]\n调用时间：%s' % time.strftime("%Y-%m-%d %H.%M.%S", time.localtime()))
        logger_linux.handleMsg("调用接口：executeSomeCommandInLinux")
        logger_linux.handleMsg("configName:%s" % str(configName))
        logger_linux.handleMsg("settingNum:%s" % str(settingNum))

        host_ip = '10.201.2.10'
        username = 'root'
        password = 'njuchenyang'
        commands_linux = [
            "cd /home",
            "rm -f *.txt",
            "touch 1.txt",
            "echo `ll` > 1.txt",
            "touch 2.txt",
            "echo `ll` > 2.txt",
            "touch 3.txt",
            "echo `ll` > 3.txt",
            "touch 4.txt",
            "echo `ll` > 4.txt",
            "touch 5.txt",
            "echo `ll` > 5.txt",
            "ll",
            "cat 1.txt",
            "rm -f 1.txt",
            "ll",
            "cat 2.txt",
            "rm -f 2.txt",
            "ll",
            "cat 3.txt",
            "rm -f 3.txt",
            "ll",
            "cat 4.txt",
            "rm -f 4.txt",
            "ll",
            "cat 5.txt",
            "rm -f 5.txt",
            "ll",
            "ping baidu.com -c 2"
        ]
        logger_linux.handleMsg("**原始输出**")
        local_telnet = None
        dict_no = str(configName) + str(settingNum)
        if dict_no not in telnet_inst:
            telnet_inst[dict_no] = TelnetClient(logger_linux)
            local_telnet = telnet_inst[dict_no]
            while not local_telnet.loginHostLinux(host_ip, username, password):
                logger_linux.handleMsg("连接失败，重试……")
                pass
        else:
            local_telnet = telnet_inst[dict_no]
        original_result_out, handle_result_out = local_telnet.executeSomeCommand(commands_linux, "Linux")
        result_out1 = list()
        for msg in original_result_out:
            for one_cmd in msg.split("\n"):
                result_out1.append(one_cmd)
        logger_linux.handleMsg("\n**清理后的输出**")
        result_out2 = MessageHandle.handleAllMsg(handle_result_out)
        for out in result_out2:
            logger_linux.handleMsg(out)
        logger_linux.handleMsg('\n\n')

        return HttpResponse(json.dumps({'original_result': result_out1, 'handle_result': result_out2}),
                            content_type='application/json;charset=utf-8')


# 用来测试Linux的Telnet的函数
def executeOneCommandInLinux(request):
    if request.method == 'GET':
        configName = request.GET.get('configName')
        settingNum = int(request.GET.get('settingNum'))
        singleCommand = list()
        singleCommand.append(base64.b64decode(request.GET.get('command')).decode("utf-8"))

        logger.handleMsg('[call api]\n调用时间：%s' % time.strftime("%Y-%m-%d %H.%M.%S", time.localtime()))
        logger_linux.handleMsg("调用接口：executeOneCommandInLinux")
        logger_linux.handleMsg("configName:%s" % str(configName))
        logger_linux.handleMsg("settingNum:%s" % str(settingNum))
        logger_linux.handleMsg("singleCommand:%s" % str(singleCommand))

        host_ip = '10.201.2.10'
        username = 'root'
        password = 'njuchenyang'

        logger_linux.handleMsg("**原始输出**")
        local_telnet = None
        dict_no = str(configName) + str(settingNum)
        if dict_no not in telnet_inst:
            telnet_inst[dict_no] = TelnetClient(logger_linux)
            local_telnet = telnet_inst[dict_no]
        else:
            local_telnet = telnet_inst[dict_no]
        while not local_telnet.loginHostLinux(host_ip, username, password):
            logger_linux.handleMsg("连接失败，重试……")
            pass
        original_result_out, handle_result_out = local_telnet.executeSomeCommand(singleCommand, "Linux")
        result_out1 = list()
        for msg in original_result_out:
            for one_cmd in msg.split("\n"):
                result_out1.append(one_cmd)
        logger_linux.handleMsg("\n**清理后的输出**")
        result_out2 = MessageHandle.handleAllMsg(handle_result_out)
        for out in result_out2:
            logger_linux.handleMsg(out)
        logger_linux.handleMsg('\n\n')

        return HttpResponse(json.dumps({'original_result': result_out1, 'handle_result': result_out2}),
                            content_type='application/json;charset=utf-8')
