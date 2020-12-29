import request from "../index"

export default {
    executeConfigCommand(configName='str',settingNum=0){
        return request.request({
            url: `/executeConfigCommand/?configName=${configName}&settingNum=${settingNum}`,
            method: "get"
        })
    },
    executeTestCommand(configName='str',settingNum=0){
        return request.request({
            url: `/executeTestCommand/?configName=${configName}&settingNum=${settingNum}`,
            method: "get"
        })
    },
    executeOneCommand(configName='str', settingNum=0, command='str'){
        return request.request({
            url: '/executeOneCommand/',
            method: "get",
            params: {
                configName,settingNum,command
            }
        })
    },
    executeCommand(host='host', loginpassword='loginpassword', enablepassword='enablepassword', isSingleCommand=0, command='command', terminalType='terminalType'){
        return request.request({
            url: '/executeCommand/',
            method: "get",
            params: {
                host,loginpassword,enablepassword,isSingleCommand,command,terminalType
            }
        })
    },
}
