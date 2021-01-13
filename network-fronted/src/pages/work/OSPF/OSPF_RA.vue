<template>
  <router ref="router"
          @executeConfigCommand="executeConfigCommand"
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
import {createStdout} from 'vue-command';
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
    configName: "OSPF",
    routerNum: 0
  }),
  methods: {
    //配置路由器
    executeConfigCommand(config) {
      utils.sleep(100).then(r => {
        let commands = config.split("\n");
        let router = this.$refs.router;
        api.executeSomeCommand(this.configName, this.routerNum, commands).then(res => {
          router.history.push(createStdout(res.result.join("<br>")))
        })
      })
    },
    //生成模板
    generateTemplate() {
      let router = this.$refs.router;
      api.generateTemplate(this.configName, this.routerNum).then(res => {
        router.config = res.result.join('\n');
      })
    },
    //执行用户自定义命令
    executeCustomizedOrder(config) {
      let commands = config.split("\n");
      let router = this.$refs.router;
      api.executeSomeCommand(this.configName, this.routerNum, commands).then(res => {
        router.history.push(createStdout(res.result.join("<br>")))
      })
    },
    //执行ping命令,如果有多个ip，使用，分割
    ping(ips) {
      let router = this.$refs.router;
      api.ping(this.configName, this.routerNum, ips).then(res => {
        router.history.push(createStdout(res.result.join("<br>")))
      })
    },
    //清除所有配置
    clearAllConfig() {
      api.clearAllConfig(this.configName, this.routerNum)
    },
    //查看路由表
    checkRouterTable() {
      let router = this.$refs.router;
      api.checkIPRoute(this.configName,this.routerNum).then(res=>{
        router.history.push(createStdout(res.result.join("<br>")))
      })

    },
    //查看路由协议
    checkRouterProtocol() {
      let router = this.$refs.router;
      api.checkRouterProtocol(this.configName,this.routerNum).then(res=>{
        router.history.push(createStdout(res.result.join("<br>")))
      })

    },
    //查看接口信息
    checkInterface() {
      let router = this.$refs.router;
      api.checkInterface(this.configName,this.routerNum).then(res=>{
        router.history.push(createStdout(res.result.join("<br>")))
      })

    },
    //验证配置结果
    validateConfig() {
      let router = this.$refs.router;
      api.validateConfig(this.configName,this.routerNum).then(res=>{
        router.history.push(createStdout(res.result.join("<br>")))
      })
    },
  }
};
</script>

<style scoped>

</style>
