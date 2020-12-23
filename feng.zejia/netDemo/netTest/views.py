from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
import json
import time

from netTest.Telnet import OutputLogger, TelnetClient, MessageHandle


@csrf_exempt
def run_job(request):
    # 判断请求头是否为json
    if request.content_type != 'application/json':
        # 如果不是的话，返回405
        return HttpResponse('only support json data', status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
    # 判断是否为post 请求
    if request.method == 'POST':
        try:
            # 解析请求的json格式入参
            data = JSONParser().parse(request)
            # 将参数存入test.json文件中
            filename = 'netTest/commands/test.json'
            with open(filename, 'w') as file_obj:
                json.dump(data, file_obj)
            # 声明logger对象，用来屏幕输出和写文件记录
            logger = OutputLogger(True, True, "telnet_log/%s.txt" % time.strftime("%Y-%m-%d %H.%M.%S", time.localtime()))
            # 读取参数，对各个参数进行解析
            json_file = json.load(open(filename, 'r', encoding='utf-8'))
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
            # 将输出信息
            with open(logger.outfile, 'r') as file_obj:
                content = file_obj.read()
        except Exception as why:
            print(why.args)
        else:
            # 在这里设置返回的信息
            print(content)
            # 返回自定义请求内容content,200状态码
            return JsonResponse(data=content, status=status.HTTP_200_OK)
    # 如果不是post 请求返回不支持的请求方法
    return HttpResponseNotAllowed(permitted_methods=['POST'])
