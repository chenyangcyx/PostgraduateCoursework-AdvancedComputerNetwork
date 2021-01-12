import base64
import re
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
        interface_result = re.search(interface_re, interface)
        if not interface_result:
            return HttpResponse(json.dumps({'message': 'interface输入格式错误！', 'result': interface}),
                                content_type='application/json;charset=utf-8')
        ipAddress_result = re.search(ip_address_re, ipAddress)
        if not ipAddress_result:
            return HttpResponse(json.dumps({'message': 'ipAddress输入格式错误！', 'result': ipAddress}),
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


# 执行一段命令，POST
# configName:string
# routerNum:int
# commands:list
def executeSomeCommand(request):
    if request.method == 'POST':
        configName = request.POST.get('configName')
        routerNum = int(request.POST.get('routerNum'))
        commands = request.POST.get('commands')
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

        return HttpResponse(json.dumps({'result': result_out}), content_type='application/json;charset=utf-8')


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
        return HttpResponse(json.dumps({'result': result_out}), content_type='application/json;charset=utf-8')


# 查看接口信息，GET
# configName:string
# routerNum:int
def checkInterface(request):
    if request.method == 'GET':
        configName = request.GET.get('configName')
        routerNum = int(request.GET.get('routerNum'))
        commands = [f'show interfaces']
        logger.handleMsg('[call api]\n调用时间：%s' % time.strftime("%Y-%m-%d %H.%M.%S", time.localtime()))
        logger.handleMsg("调用接口：checkInterface")
        result_out = executeCommands(configName, routerNum, commands)
        return HttpResponse(json.dumps({'result': result_out}), content_type='application/json;charset=utf-8')


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
        # 获取ip route结果
        commands = ['show ip route']
        ip_route_result = executeCommands(configName, routerNum, commands)
        logger.handleMsg(f'ip_route_result: {ip_route_result}')
        result_start = 0
        for i in range(len(ip_route_result)):
            if 'Gateway of' in ip_route_result[i]:
                result_start = i + 2
                break
        ip_route_validate = list()
        for i in range(result_start, len(ip_route_result) - 1):
            ip_route_validate.append(ip_route_result[i])
        if len(ip_route_validate) < 3:
            result.append("ip route验证错误，没有准确的路由")
            result.append("相关输出如下：")
            if_success = False
        else:
            result.append("ip route验证成功，得到了准确的路由")
            result.append("相关输出如下：")
            if_success = True
        for line in ip_route_validate:
            result.append(line)
        # 获取ip protocols
        commands = ['show ip protocols']
        ip_protocols_result = executeCommands(configName, routerNum, commands)
        logger.handleMsg(f'ip_protocols_result: {ip_protocols_result}')
        if len(ip_protocols_result) < 5:
            result.append("ip protocols验证错误，没有正确的协议")
            if_success = False
        else:
            result.append("ip protocols验证正确，协议配置成功")
            if_success = True
            # 路由协议
            for line in ip_protocols_result:
                if 'Routing Protocol is' in line:
                    result.append('路由协议：' + line.replace(r'"').replace(r'Routing Protocol is '))
                break
            # 路由详情
            for i in range(len(ip_protocols_result)):
                if 'Routing for Networks' in ip_protocols_result[i]:
                    result.append('路由详情：')
                    result.append(ip_protocols_result[i + 1].strip())
                    result.append(ip_protocols_result[i + 2].strip())
                    break
        if if_success:
            message = '验证成功！'
        else:
            message = '验证失败！'
        logger.handleMsg('**接口返回值**')
        for line in result:
            logger.handleMsg(line)
        logger.handleMsg('\n')
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
        return HttpResponse(json.dumps({'result': result_out}), content_type='application/json;charset=utf-8')
