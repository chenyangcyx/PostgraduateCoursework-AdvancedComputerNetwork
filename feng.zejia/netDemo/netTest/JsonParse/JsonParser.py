import json


# json文件解析类
class JsonParser:
    def __init__(self, json_file_path=None):
        self.json_data = json.load(open(json_file_path, 'r', encoding='utf-8'))

    # 获取json数据：groupId
    def getData_groupId(self):
        return self.json_data['groupId']

    # 获取json数据：groupMembers的列表
    def getData_groupMembers(self):
        return self.json_data['groupMembers']

    # 获取json数据：groupMembers_item-studentId
    def getData_groupMembers_item_studentId(self, item):
        return item['studentId']

    # 获取json数据：groupMembers_item-studentName
    def getData_groupMembers_item_studentName(self, item):
        return item['studentName']

    # 获取json数据：subjectName
    def getData_subjectName(self):
        return self.json_data['subjectName']

    # 获取json数据：creationDate
    def getData_creationDate(self):
        return self.json_data['creationDate']

    # 获取json数据：routerSettings的列表
    def getData_routerSettings(self):
        return self.json_data['routerSettings']

    # 获取json数据：routerSettings_item-configName
    def getData_routerSettings_item_configName(self, item):
        return item['configName']

    # 获取json数据：routerSettings_item-configDescription
    def getData_routerSettings_item_configDescription(self, item):
        return item['configDescription']

    # 获取json数据：routerSettings_item-routerNum
    def getData_routerSettings_item_routerNum(self, item):
        return item['routerNum']

    # 获取json数据：routerSettings_item-configDetail的列表
    def getData_routerSettings_item_configDetail(self, item):
        return item['configDetail']

    # 获取json数据：routerSettings_item-configDetail_item-routerName
    def getData_routerSettings_item_configDetail_item_routerName(self, item):
        return item['routerName']

    # 获取json数据：routerSettings_item-configDetail_item-hostIp
    def getData_routerSettings_item_configDetail_item_hostIp(self, item):
        return item['hostIp']

    # 获取json数据：routerSettings_item-configDetail_item-loginPassword
    def getData_routerSettings_item_configDetail_item_loginPassword(self, item):
        return item['loginPassword']

    # 获取json数据：routerSettings_item-configDetail_item-enablePassword
    def getData_routerSettings_item_configDetail_item_enablePassword(self, item):
        return item['enablePassword']

    # 获取json数据：routerSettings_item-configDetail_item-configCommands
    def getData_routerSettings_item_configDetail_item_configCommands(self, item):
        return item['configCommands']

    # 获取json数据：routerSettings_item-configDetail_item-testCommands
    def getData_routerSettings_item_configDetail_item_testCommands(self, item):
        return item['testCommands']
