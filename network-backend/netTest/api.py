import base64

from django.http import HttpResponse

from netTest.api_function import *


# 设置路由器接口IP地址，GET
# telnetHost:base64(string)
# interface:base64(string)
# ipAddress:base64(string)
# netMask:base64(string)
def setRouterIP(request):
    if request.method == 'GET':
        telnetHost = base64.b64decode(request.GET.get('telnetHost')).decode()
        interface = base64.b64decode(request.GET.get('interface')).decode()
        ipAddress = base64.b64decode(request.GET.get('ipAddress')).decode()
        netMask = base64.b64decode(request.GET.get('netMask')).decode()
        logger.handleMsg('[call api]\n调用时间：%s' % time.strftime("%Y-%m-%d %H.%M.%S", time.localtime()))
        logger.handleMsg("调用接口：setRouterIP")
        logger.handleMsg(f'telnetHost: {telnetHost}')
        logger.handleMsg(f'interface: {interface}')
        logger.handleMsg(f'ipAddress: {ipAddress}')
        logger.handleMsg(f'netMask: {netMask}')
        # 判断输入变量是否合法
        telnetHost_re = r'(192.168.1.1)|(192.168.1.2)|(192.168.1.3)'
        ip_address_re = r'((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}'
        interface_re = r'(s0/0/(0|1))|(f0/(0|1))'
        netMask_re = r'^(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])(\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])){3}$'
        telnetHost_result = re.search(telnetHost_re, telnetHost)
        if not telnetHost_result:
            return HttpResponse(json.dumps({'message': 'telnetHost输入格式错误！', 'result': telnetHost}),
                                content_type='application/json;charset=utf-8')
        ipAddress_result = re.search(ip_address_re, ipAddress)
        if not ipAddress_result:
            return HttpResponse(json.dumps({'message': 'ipAddress输入格式错误！', 'result': ipAddress}),
                                content_type='application/json;charset=utf-8')
        interface_result = re.search(interface_re, interface)
        if not interface_result:
            return HttpResponse(json.dumps({'message': 'interface输入格式错误！', 'result': interface}),
                                content_type='application/json;charset=utf-8')
        netMask_result = re.search(netMask_re, netMask)
        if not netMask_result:
            return HttpResponse(json.dumps({'message': 'netMask输入格式错误！', 'result': netMask}),
                                content_type='application/json;charset=utf-8')
        configName = 'RIP'
        routerNum = int(telnetHost.split('.')[3]) - 1
        commands = None
        if 's0/0' in interface:
            commands = ['configure terminal',
                        f'interface {interface}',
                        f'ip address {ipAddress} {netMask}',
                        'clock rate 64000',
                        'no shutdown',
                        'end']
        elif 'f0/' in interface:
            commands = ['configure terminal',
                        f'interface {interface}',
                        f'ip address {ipAddress} {netMask}',
                        'no shutdown',
                        'end']
        result_out = executeCommands(configName, routerNum, commands)
        # 存储相应配置
        router_interface_ip[telnetHost + interface] = ipAddress
        router_interface_netmask[telnetHost + interface] = netMask
        return HttpResponse(json.dumps({'message': f'{interface}接口配置成功！', 'result': result_out}),
                            content_type='application/json;charset=utf-8')


# 配置所有路由器的端口IP：默认配置，GET
def setRouterIPDefault(request):
    if request.method == 'GET':
        configName = 'RIP'
        result_out = list()
        # 配置路由器R0
        routerNum = 0
        commands = ["configure terminal",
                    "interface s0/0/0",
                    "ip address 192.168.2.1 255.255.255.0",
                    "clock rate 64000",
                    "no shutdown",
                    "end"]
        result_out.append(executeCommands(configName, routerNum, commands))
        # 配置路由器R1
        routerNum = 1
        commands = ["configure terminal",
                    "interface s0/0/0",
                    "ip address 192.168.2.2 255.255.255.0",
                    "clock rate 64000",
                    "no shutdown",
                    "end",
                    "configure terminal",
                    "interface s0/0/1",
                    "ip address 192.168.3.1 255.255.255.0",
                    "clock rate 64000",
                    "no shutdown",
                    "end"]
        result_out.append(executeCommands(configName, routerNum, commands))
        # 配置路由器R2
        routerNum = 2
        commands = ["configure terminal",
                    "interface s0/0/1",
                    "ip address 192.168.3.2 255.255.255.0",
                    "clock rate 64000",
                    "no shutdown",
                    "end"]
        result_out.append(executeCommands(configName, routerNum, commands))
        # 存储相应配置
        router_interface_ip[r'192.168.1.1s0/0/0'] = '192.168.2.1'
        router_interface_netmask[r'192.168.1.1s0/0/0'] = '255.255.255.0'
        router_interface_ip[r'192.168.1.2s0/0/0'] = '192.168.2.2'
        router_interface_netmask[r'192.168.1.2s0/0/0'] = '255.255.255.0'
        router_interface_ip[r'192.168.1.2s0/0/1'] = '192.168.3.1'
        router_interface_netmask[r'192.168.1.2s0/0/1'] = '255.255.255.0'
        router_interface_ip[r'192.168.1.3s0/0/1'] = '192.168.3.2'
        router_interface_netmask[r'192.168.1.3s0/0/1'] = '255.255.255.0'
        return HttpResponse(json.dumps({'message': '所有接口配置成功！', 'result': result_out}),
                            content_type='application/json;charset=utf-8')


# 执行一段命令，GET
# configName:string
# routerNum:int
# commands:base64(string_list)
def executeSomeCommand(request):
    if request.method == 'GET':
        configName = request.GET.get('configName')
        routerNum = int(request.GET.get('routerNum'))
        commands = base64.b64decode(request.GET.get('commands')).decode()
        commands_list = json.loads(commands)
        logger.handleMsg('[call api]\n调用时间：%s' % time.strftime("%Y-%m-%d %H.%M.%S", time.localtime()))
        logger.handleMsg("调用接口：executeSomeCommand")
        result_out = executeCommands(configName, routerNum, commands_list)
        return HttpResponse(json.dumps({'result': result_out}), content_type='application/json;charset=utf-8')


# 获取路由器配置模板命令，GET
# configName:string
# routerNum:int
def generateTemplate(request):
    if request.method == 'GET':
        configName = request.GET.get('configName')
        routerNum = int(request.GET.get('routerNum'))
        # 获取相应的所有配置
        logger.handleMsg('[call api]\n调用时间：%s' % time.strftime("%Y-%m-%d %H.%M.%S", time.localtime()))
        logger.handleMsg("调用接口：generateTemplate")
        if configName is not None:
            logger.handleMsg("configName:%s" % str(configName))
        else:
            configName = 'RIP'
        if routerNum is not None:
            logger.handleMsg("settingNum:%s" % str(routerNum))
        else:
            routerNum = 0
        # 按照configName找到要验证的路由协议
        configItem = None
        for settingItem in json_file['routerSettings']:
            if settingItem['configName'] == configName:
                configItem = settingItem
        configCommands = configItem['configDetail'][routerNum]['configCommands']
        # 对命令中的相应标志进行替换
        if not ('192.168.1.1s0/0/0' in router_interface_ip and '192.168.1.1s0/0/0' in router_interface_netmask):
            return HttpResponse(json.dumps({'message': '模板生成失败！', 'result': '路由器R0的接口未配置！请先配置路由器R0的相关接口再进行操作！'}),
                                content_type='application/json;charset=utf-8')
        if not ('192.168.1.2s0/0/0' in router_interface_ip and '192.168.1.2s0/0/0' in router_interface_netmask):
            return HttpResponse(json.dumps({'message': '模板生成失败！', 'result': '路由器R1的接口未配置！请先配置路由器R1的相关接口再进行操作！'}),
                                content_type='application/json;charset=utf-8')
        if not ('192.168.1.2s0/0/1' in router_interface_ip and '192.168.1.2s0/0/1' in router_interface_netmask):
            return HttpResponse(json.dumps({'message': '模板生成失败！', 'result': '路由器R1的接口未配置！请先配置路由器R1的相关接口再进行操作！'}),
                                content_type='application/json;charset=utf-8')
        if not ('192.168.1.3s0/0/1' in router_interface_ip and '192.168.1.3s0/0/1' in router_interface_netmask):
            return HttpResponse(json.dumps({'message': '模板生成失败！', 'result': '路由器R2的接口未配置！请先配置路由器R2的相关接口再进行操作！'}),
                                content_type='application/json;charset=utf-8')

        netarea1 = getIPArea(router_interface_ip[r'192.168.1.1s0/0/0'], router_interface_netmask[r'192.168.1.1s0/0/0'])
        netarea2 = getIPArea(router_interface_ip[r'192.168.1.2s0/0/1'], router_interface_netmask[r'192.168.1.2s0/0/1'])
        netarea3 = r'10.0.0.0'
        netarea1contrastnetmask = getContrastNetmask(router_interface_netmask[r'192.168.1.1s0/0/0'])
        netarea2contrastnetmask = getContrastNetmask(router_interface_netmask[r'192.168.1.2s0/0/1'])
        netarea3contrastnetmask = r'0.255.255.255'

        commands = list()
        for line in configCommands:
            commands.append(line.replace(r'$$netarea1$$', netarea1)
                            .replace(r'$$netarea2$$', netarea2)
                            .replace(r'$$netarea3$$', netarea3)
                            .replace(r'$$netarea1contrastnetmask$$', netarea1contrastnetmask)
                            .replace(r'$$netarea2contrastnetmask$$', netarea2contrastnetmask)
                            .replace(r'$$netarea3contrastnetmask$$', netarea3contrastnetmask))
        logger.handleMsg(f'commands: {commands}\n')
        return HttpResponse(json.dumps({'message': '模板生成成功！', 'result': commands}),
                            content_type='application/json;charset=utf-8')


# 查看路由表，GET
# configName:string
# routerNum:int
def checkIPRoute(request):
    if request.method == 'GET':
        configName = request.GET.get('configName')
        routerNum = int(request.GET.get('routerNum'))
        commands = ['show ip route']
        logger.handleMsg('[call api]\n调用时间：%s' % time.strftime("%Y-%m-%d %H.%M.%S", time.localtime()))
        logger.handleMsg("调用接口：checkIPRoute")
        result_out = executeCommands(configName, routerNum, commands)
        route_info = getInfoFromShowIPRoute(result_out)
        result_out.append('')
        result_out.append(f'共有{len(route_info)}条路由信息')
        for line in route_info:
            result_out.append(line)
        logger.handleMsg('输出结果：%s' % result_out)
        return HttpResponse(json.dumps({'message': f'获取到{len(route_info)}条路由信息！', 'result': result_out}),
                            content_type='application/json;charset=utf-8')


# 查看协议信息，GET
# configName:string
# routerNum:int
def checkIPProtocols(request):
    if request.method == 'GET':
        configName = request.GET.get('configName')
        routerNum = int(request.GET.get('routerNum'))
        commands = ['show ip protocols']
        logger.handleMsg('[call api]\n调用时间：%s' % time.strftime("%Y-%m-%d %H.%M.%S", time.localtime()))
        logger.handleMsg("调用接口：checkIPProtocols")
        result_out = executeCommands(configName, routerNum, commands)
        if_ok, message, result = getInfoFromShowIPProtocols(result_out)
        if result:
            result.append('')
            for line in result:
                result_out.append(line)
        logger.handleMsg('输出结果：%s' % result_out)
        return HttpResponse(json.dumps({'message': message, 'result': result_out}),
                            content_type='application/json;charset=utf-8')


# 查看接口信息，GET
# configName:string
# routerNum:int
def checkInterface(request):
    if request.method == 'GET':
        configName = request.GET.get('configName')
        routerNum = int(request.GET.get('routerNum'))
        commands = ['show interfaces']
        logger.handleMsg('[call api]\n调用时间：%s' % time.strftime("%Y-%m-%d %H.%M.%S", time.localtime()))
        logger.handleMsg("调用接口：checkInterface")
        result_out = executeCommands(configName, routerNum, commands)
        result_info = getInfoFromShowInterfaces(result_out)
        result_out.append('')
        for line in result_info:
            result_out.append(line)
        logger.handleMsg('输出结果：%s' % result_out)
        return HttpResponse(json.dumps({'message': '获取接口信息成功！', 'result': result_out}),
                            content_type='application/json;charset=utf-8')


# 验证配置结果，GET
# configName:string
# routerNum:int
def validateConfig(request):
    if request.method == 'GET':
        configName = request.GET.get('configName')
        routerNum = int(request.GET.get('routerNum'))
        logger.handleMsg('[call api]\n调用时间：%s' % time.strftime("%Y-%m-%d %H.%M.%S", time.localtime()))
        logger.handleMsg("调用接口：validateConfig")
        result = list()
        result.append('')
        message = ""
        # show ip route信息
        commands = ['show ip route']
        showiproute_info1 = executeCommands(configName, routerNum, commands)
        showiproute_info2 = getInfoFromShowIPRoute(showiproute_info1)
        if len(showiproute_info2) < 3:
            result.append(f"ip route验证错误，只获得了{len(showiproute_info2)}条路由信息")
            message = "ip route验证错误"
            result.append("相关输出如下：")
        else:
            result.append("ip route验证成功，配置了正确的路由！")
            message = "ip route验证成功"
            result.append("相关输出如下：")
        for line in showiproute_info2:
            result.append(line)
        # show ip protocols
        commands = ['show ip protocols']
        showipprotocols_info1 = executeCommands(configName, routerNum, commands)
        if_ok, message_protocols, showipprotocols_info2 = getInfoFromShowIPProtocols(showipprotocols_info1)
        result.append('')
        if len(showipprotocols_info1) < 5:
            result.append("ip protocols验证错误，没有正确的协议")
            message += "，ip protocols验证错误！"
        else:
            result.append("ip protocols验证正确，协议配置成功")
            message += "，ip protocols验证成功！"
            for line in showipprotocols_info2:
                result.append(line)
        # show interfaces信息
        commands = ['show interfaces']
        showinterfaces_info1 = executeCommands(configName, routerNum, commands)
        showinterfaces_info2 = getInfoFromShowInterfaces(showinterfaces_info1)
        result.append('')
        result.append('所有接口信息：')
        for line in showinterfaces_info2:
            result.append(line)
        logger.handleMsg('输出结果：%s' % result)
        return HttpResponse(json.dumps({'message': message, 'result': result}),
                            content_type='application/json;charset=utf-8')


# 清除所有配置，GET
# configName:string
# routerNum:int
def clearAllConfig(request):
    if request.method == 'GET':
        configName = request.GET.get('configName')
        routerNum = int(request.GET.get('routerNum'))
        commands = ['write erase', '', '', 'reload', 'yes', '', '', '']
        logger.handleMsg('[call api]\n调用时间：%s' % time.strftime("%Y-%m-%d %H.%M.%S", time.localtime()))
        logger.handleMsg("调用接口：clearAllConfig")
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
        # 直接调用对象的write方法进行写入，不等待输出
        logger.handleMsg("写入重置重启指令……")
        for comm in commands:
            local_telnet.tn._connection.write((comm + '\n').encode('ascii'))
        return HttpResponse(json.dumps({'message': '清除成功，正在重启……', 'result': commands}),
                            content_type='application/json;charset=utf-8')


# ping命令，GET
# configName:string
# routerNum:int
# pingAddress:base64(string)
def ping(request):
    if request.method == 'GET':
        configName = request.GET.get('configName')
        routerNum = int(request.GET.get('routerNum'))
        pingAddress = base64.b64decode(request.GET.get('pingAddress')).decode()
        commands = [f'ping {pingAddress}']
        logger.handleMsg('[call api]\n调用时间：%s' % time.strftime("%Y-%m-%d %H.%M.%S", time.localtime()))
        logger.handleMsg("调用接口：ping")
        result_out = executeCommands(configName, routerNum, commands)
        message = "ping失败！"
        for line in result_out:
            if r'!!!!!' in line:
                message = "ping成功！"
                break
        return HttpResponse(json.dumps({'message': message, 'result': result_out}),
                            content_type='application/json;charset=utf-8')
