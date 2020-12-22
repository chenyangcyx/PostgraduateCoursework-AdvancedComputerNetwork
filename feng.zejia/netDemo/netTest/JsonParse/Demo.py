from JsonParse import *

if __name__ == '__main__':
    # JsonParse的使用示例
    if __name__ == '__main__':
        json_parse = JsonParser("demo_json.json")
        # groupId
        print(json_parse.getData_groupId())
        # groupMembers
        groupMembers_list = json_parse.getData_groupMembers()
        print(groupMembers_list)
        for item in groupMembers_list:
            # studentId
            print(json_parse.getData_groupMembers_item_studentId(item))
            # studentName
            print(json_parse.getData_groupMembers_item_studentName(item))
        # subjectName
        print(json_parse.getData_subjectName())
        # creationDate
        print(json_parse.getData_creationDate())
        # routerSettings
        routerSettings_list = json_parse.getData_routerSettings()
        print(routerSettings_list)
        for item in routerSettings_list:
            # configName
            print(json_parse.getData_routerSettings_item_configName(item))
            # configDescription
            print(json_parse.getData_routerSettings_item_configDescription(item))
            # routerNum
            print(json_parse.getData_routerSettings_item_routerNum(item))
            # configDetail
            configDetail_list = json_parse.getData_routerSettings_item_configDetail(item)
            print(configDetail_list)
            for item2 in configDetail_list:
                # routerName
                print(json_parse.getData_routerSettings_item_configDetail_item_routerName(item2))
                # hostIp
                print(json_parse.getData_routerSettings_item_configDetail_item_hostIp(item2))
                # loginPassword
                print(json_parse.getData_routerSettings_item_configDetail_item_loginPassword(item2))
                # enablePassword
                print(json_parse.getData_routerSettings_item_configDetail_item_enablePassword(item2))
                # configCommands
                print(json_parse.getData_routerSettings_item_configDetail_item_configCommands(item2))
                # testCommands
                print(json_parse.getData_routerSettings_item_configDetail_item_testCommands(item2))
