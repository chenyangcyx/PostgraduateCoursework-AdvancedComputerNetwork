import request from "../index"
import { Base64 } from 'js-base64'

export default {
    /*旧的接口*/
    /*
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
    */
    /*旧的接口*/

    /***************新的接口***************/
    // 设置路由器接口IP地址，GET
    // telnetHost:base64(string)
    // interface:base64(string)
    // ipAddress:base64(string)
    // netMask:base64(string)
    setRouterIP(telnetHost,interface,ipAddress,netMask){
        return request.request({
            url: `/setRouterIP/?telnetHost=${Base64.encode(telnetHost)}&interface=${Base64.encode(interface)}&ipAddress=${Base64.encode(ipAddress)}&netMask=${Base64.encode(netMask)}}`,
            method: "get"
        })
    },

    // 配置所有路由器的端口IP：默认配置，GET
    setRouterIPDefault(){
        return request.request({
            url: `/setRouterIPDefault/`,
            method: "get"
        })
    },


    // 执行一段命令，POST
    // configName:string
    // routerNum:int
    // commands:list
    executeSomeCommand(configName,routerNum,commands){
        return request.request({
            url: '/executeSomeCommand/',
            method: "post",
            data: {
                configName,
                routerNum,
                commands
            }
        })
    },


    // 获取路由器配置模板命令，GET
    // configName:string
    // routerNum:int
    generateTemplate(configName,routerNum){
        return request.request({
            url: `/generateTemplate/?configName=${configName}&routerNum=${routerNum}`,
            method: "get"
        })
    },

    // 查看路由表，GET
    // configName:string
    // routerNum:int
    checkIPRoute(configName,routerNum){
        return request.request({
            url: `/checkIPRoute/?configName=${configName}&routerNum=${routerNum}`,
            method: "get"
        })
    },

    // 查看接口信息，GET
    // configName:string
    // routerNum:int
    // interface:base64(string)
    checkInterface(configName,routerNum,interface){
        return request.request({
            url: `/checkInterface/?configName=${configName}&routerNum=${routerNum}&interface=${Base64.encode(interface)}`,
            method: "get"
        })
    },

    // 验证配置结果，GET
    // configName:string
    // routerNum:int
    validateConfig(configName,routerNum){
        return request.request({
            url: `/validateConfig/?configName=${configName}&routerNum=${routerNum}`,
            method: "get"
        })
    },

    // 清除所有配置，GET
    // configName:string
    // routerNum:int
    clearAllConfig(configName,routerNum){
        return request.request({
            url: `/clearAllConfig/?configName=${configName}&routerNum=${routerNum}`,
            method: "get"
        })
    },

    // ping命令，GET
    // configName:string
    // routerNum:int
    // pingAddress:base64(string)
    ping(configName,routerNum,pingAddress){
        return request.request({
            url: `/ping/?configName=${configName}&routerNum=${routerNum}&pingAddress=${Base64.encode(pingAddress)}`,
            method: "get"
        })
    }
    /***************新的接口***************/
}
