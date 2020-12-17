# 判断是否带有linux字符串标识
def ifHasLinuxCMD(msg):
    if msg.find("]#") != -1 and msg.find("[") != -1:
        return True
    else:
        return False


# 判断是否是空的linux字符串
def ifEmptyLinuxCMD(msg):
    if msg[msg.find("#") + 2:] == "":
        return True
    else:
        return False


# 清理从linux终端返回的字符串
def handleMsgFromLinux(msg):
    if ifHasLinuxCMD(msg):
        if ifEmptyLinuxCMD(msg):
            return ""
        else:
            return msg[msg.find("#") + 2:]
    else:
        return msg


# 判断是否带有Router字符串标识
def ifHasRouterCMD(msg):
    if msg.find(">") != -1:
        return 1
    if msg.find("#") != -1:
        return 2
    return -1


# 判断是否是空的Router字符串
def ifEmptyRouterCMD(msg):
    if ifHasRouterCMD(msg) == 1:
        if msg[msg.find(">") + 1:] == "":
            return True
    if ifHasRouterCMD(msg) == 2:
        if msg[msg.find("#") + 1:] == "":
            return True
    return False


# 清理从Router返回的字符串
def handleMsgFromRouter(msg):
    cmd_type = ifHasRouterCMD(msg)
    if cmd_type != -1:
        if ifEmptyRouterCMD(msg):
            return ""
        else:
            if cmd_type == 1:
                return msg[msg.find(">") + 1:]
            if cmd_type == 2:
                return msg[msg.find("#") + 1:]


# 处理从linux返回的字符串，msgs是一个list
def handleAllMsg(msgs):
    all_commands = list()
    for msg in msgs:
        for one_cmd in msg.split("\n"):
            all_commands.append(one_cmd)
    handle_commands = list()
    for com in all_commands:
        handle_com = handleMsgFromLinux(com)
        if handle_com != "":
            handle_commands.append(handle_com)
    return handle_commands
