import json


# json文件解析类
class JsonParser:
    def __init__(self, json_file_path=None):
        self.json_data = json.load(open(json_file_path, 'r',encoding='utf-8'))
        # 获取后是否打印输出
        self.if_print = True

    # 获取json数据：groupId(string)
    def getData_groupId(self):
        if self.if_print:
            print(self.json_data['groupId'])
        return self.json_data['groupId']

    # 获取json数据：groupMembers(List)
    def getData_groupMembers(self):
        if self.if_print:
            for student_data in self.json_data['groupMembers']:
                print("studentId: %s"%student_data['studentId'])
                print("studentName: %s" % student_data['studentName'])
        return self.json_data['groupMembers']

    # 获取json数据：subjectName
    def getData_subjectName(self):
        if self.if_print:
            print(self.json_data['subjectName'])
        return self.json_data['subjectName']

    # 获取json数据：creationDate
    def getData_creationDate(self):
        if self.if_print:
            print(self.json_data['creationDate'])
        return self.json_data['creationDate']

    # 获取json数据：routerNum
    def getData_routerNum(self):
        if self.if_print:
            print(self.json_data['routerNum'])
        return self.json_data['routerNum']

    # 获取json数据：routerSettings
    def getData_routerSettings(self):
        if self.if_print:
            for router_data in self.json_data['routerSettings']:
                print("routerName: %s"%router_data['routerName'])
                print("host_ip: %s" % router_data['host_ip'])
                print("loginUsername: %s" % router_data['loginUsername'])
                print("loginPassword: %s" % router_data['loginPassword'])
                print("commands:")
                for command in router_data['commands']:
                    print(command)
                print()
        return self.json_data['routerSettings']