import request from "../index"

export default {
    executeSomeCommandInLinux(configName='str',settingNum=1){
        return request.request({
            url: `/executeSomeCommandInLinux?configName=${configName}&settingNum=${settingNum}`,
            method: "get"
        })
    },
    executeOneCommandInLinux(configName='str', settingNum=1, command='str'){
        return request.request({
            url: '/executeSomeCommandInLinux',
            method: "get",
            params: {
                configName,settingNum,command
            }
        })
    }
}
