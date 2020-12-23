import base64

from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
import json
import time

from netTest.Telnet import OutputLogger, TelnetClient, MessageHandle


# @csrf_exempt
# def run_job(request):
#     # 判断请求头是否为json
#     if request.content_type != 'application/json':
#         # 如果不是的话，返回405
#         return HttpResponse('only support json data', status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
#     # 判断是否为post 请求
#     if request.method == 'POST':
#         try:
#         except Exception as why:
#             print(why.args)
#         else:
#             # 在这里设置返回的信息
#
#             # 返回自定义请求内容content,200状态码
#             return JsonResponse(data=content, status=status.HTTP_200_OK)
#     # 如果不是post 请求返回不支持的请求方法
#     return HttpResponseNotAllowed(permitted_methods=['POST'])
#

def executeConfigInst(request):
    global configItem
    if request.method == 'GET':
        result = {}
        configName = request.GET.get('configName')
        settingNUm = int(request.GET.get('settingNum'))  # 选择不同的路由器的配置，具体见json文件内容

        json_file = json.load(open("./netTest/commands/setting.json", 'r', encoding='utf-8'))
        # 声明logger对象，用来屏幕输出和写文件记录
        logger = OutputLogger(True, True,
                              "./netTest/telnet_log/%s.txt" % time.strftime("%Y-%m-%d %H.%M.%S", time.localtime()))

        # 按照configName找到要验证的路由协议
        for settingItem in json_file['routerSettings']:
            if settingItem['configName'] == configName:
                configItem = settingItem

        # 读取参数，对各个参数进行解析
        host_ip = configItem['configDetail'][settingNUm]['hostIp']
        password_login = configItem['configDetail'][settingNUm]['loginPassword']
        password_enable = configItem['configDetail'][settingNUm]['enablePassword']
        configCommands = configItem['configDetail'][settingNUm]['configCommands']
        testCommands = configItem['configDetail'][settingNUm]['testCommands']
        logger.handleMsg('具体配置：')
        logger.handleMsg(host_ip)
        logger.handleMsg(password_login)
        logger.handleMsg(password_enable)
        logger.handleMsg(configCommands)
        logger.handleMsg(testCommands)
        logger.handleMsg("")

        # 测试连接功能
        # 实例化一个TelnetClient类，传入logger对象
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
            original_result_out, handle_result_out = telnet_client_Router.executeSomeCommand(configCommands,
                                                                                             "Router")
        logger.handleMsg("\n\n*****清理后的输出*****")
        result_out2 = MessageHandle.handleAllMsg(handle_result_out)
        for out in result_out2:
            logger.handleMsg(out)

        # 读入所有输出信息，并返回给前端
        with open(logger.outfile, 'r') as file_obj:
            result = file_obj.read()
        print(result)
        json.dumps(result)
        return HttpResponse(result, content_type='application/json;charset=utf-8')


def executeSingleInst(request):
    if request.method == 'GET':
        result = {}
        command = request.GET.get('command')
        base64.decode("utf-8", command)

        # 声明logger对象，用来屏幕输出和写文件记录
        logger = OutputLogger(True, True,
                              "./netTest/telnet_log/%s.txt" % time.strftime("%Y-%m-%d %H.%M.%S", time.localtime()))

        # 实例化一个TelnetClient类，传入logger对象
        telnet_client_Router = TelnetClient(logger)
        logger.handleMsg("*****原始输出*****")

        handle_result_out = telnet_client_Router.executeSomeCommand(command, "Router")
        logger.handleMsg("\n\n*****清理后的输出*****")
        result_out2 = MessageHandle.handleAllMsg(handle_result_out)
        for out in result_out2:
            logger.handleMsg(out)

        # 读入所有输出信息，并返回给前端
        with open(logger.outfile, 'r') as file_obj:
            result = file_obj.read()
            print(result)
            json.dumps(result)
        return HttpResponse(result, content_type='application/json;charset=utf-8')
