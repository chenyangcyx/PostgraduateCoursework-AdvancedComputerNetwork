import re


# 重新组织原始输出
def reformatOriginalResult(in_list):
    result_out = "Router#"
    for msg in in_list:
        result_out += msg
    message_list=list()
    for msg in result_out.split('\n'):
        message_list.append(msg)
    return message_list

# 删除所有带命令行前缀的行
def deleteLineWithCmdPrefix(hostname, in_list):
    handle_result = list()
    re_text = hostname + r".*(>|#).*?"
    for message in in_list:
        if not re.search(re_text, message):
            handle_result.append(message)
    return handle_result


# 删除所有带前缀的空白输入行
def deleteBlankLineWithPrefix(hostname, in_list):
    handle_result = list()
    re_text = hostname + r".*(>|#).*?"
    for message in in_list:
        if not (re.search(re_text, message) and re.sub(re_text, '', message).strip() == ''):
            handle_result.append(message)
    return handle_result


# 删除所有命令行前缀
def deleteAllPrefix(hostname, in_list):
    handle_result = list()
    re_text = hostname + r".*(>|#).*?"
    for message in in_list:
        handle_result.append(re.sub(re_text, '', message))
    return handle_result


# 删除所有空白行
def deleteAllBlackLine(in_list):
    handle_result = list()
    for message in in_list:
        if not message.strip() == '':
            handle_result.append(message)
    return handle_result
