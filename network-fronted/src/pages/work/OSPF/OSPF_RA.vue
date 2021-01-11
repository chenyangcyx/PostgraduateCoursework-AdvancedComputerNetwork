<template>
  <router ref="router"
          @executeConfigCommand="executeConfigCommand"
          @executeTestCommand="executeTestCommand"
          @generateTemplate="generateTemplate"
          @executeCustomizedOrder="executeCustomizedOrder"
          @ping="ping"
          @clearAllConfig="clearAllConfig"
          @checkRouterTable="checkRouterTable"
          @checkRouterProtocol="checkRouterProtocol"
          @checkInterface="checkInterface"
          @validateConfig="validateConfig"
        ></router>
</template>

<script>
import  {createStdout} from 'vue-command';
import api from '@/api2/bigwork'
import Router from "@/pages/work/common/Router";
import utils from "@/utils/Commonutils";

export default {
  name: 'Command',
  components: {
  Router
  },
  created() {
  },
  mounted() {
  },
  data: () => ({
  }),
  methods: {
    //配置路由器
    executeConfigCommand(config) {
      utils.sleep(100).then(r => {
        let configName = "OSPF";
        let settingNum = 0;
        let router = this.$refs.router;
        console.log(router);
        api.executeConfigCommand(configName, settingNum).then(res => {
          router.history.push(createStdout("配置命令如下: <br>" + res.original_result.join("<br>")))
          let str = "<br>结果如下：<br>" + res.handle_result.join("<br>");
          router.history.push(createStdout(str));
        });
      })
    },
    //生成模板
    generateTemplate(){
      let router = this.$refs.router.config = 'no\n' +
          'enable\n' +
          'configure terminal\n' +
          'interface f0/0\n' +
          'ip address 192.168.1.1 255.255.255.0\n' +
          'no shutdown\n' +
          'exit\n' +
          'line vty 0 4\n' +
          'password CISCO\n' +
          'login\n' +
          'exit\n' +
          'enable password CISCO\n' +
          'exit'
    },
    //执行用户自定义命令
    executeCustomizedOrder(text){
      console.log(text.split("\n"));
    },
    //执行ping命令
    ping(){

    },
    //清除所有配置
    clearAllConfig(){

    },
    //查看路由表
    checkRouterTable(){},
    //查看路由协议
    checkRouterProtocol(){

    },
    //查看接口信息
    checkInterface(){

    },
    //验证配置结果
    validateConfig(){

    },

    //查看结果
    executeTestCommand() {
      this.sleep(100).then(res=>{
        let configName = "OSPF";
        let settingNum = 0;
        let router = this.$refs.router;
        api.executeTestCommand(configName,settingNum).then(res=>{
          router.history.push(createStdout("查询命令如下: <br>" + res.original_result.join("<br>")))
          let str = "<br>结果如下：<br>" + res.handle_result.join("<br>");
          router.history.push(createStdout(str));
        });
      })
    },
  }
};
</script>

<style scoped>

</style>
