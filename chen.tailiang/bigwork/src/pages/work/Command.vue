<template>
  <div class="fillcontain">
    <el-button @click="executeSomeCommandInLinux" style="margin-bottom: 10px" type="success">配置RIP</el-button>
    <el-button @click="executeOneCommandInLinux" style="margin-bottom: 10px" type="success">查看ip路由表</el-button>

    <div class="contain">
      <vue-command
          class="vuecommand"
          ref="aa" title="高级计算机网络大作业"
          prompt="-------- this is a boundary --------"
          :history.sync="history"
          :commands.sync="commands"
          :is-in-progress="true">
      </vue-command>
    </div>
  </div>
</template>

<script>
import VueCommand, {createStdout} from 'vue-command';
import 'vue-command/dist/vue-command.css';
import api from '@/api2/bigwork'

export default {
  name: 'Command',
  components: {
    VueCommand
  },
  created() {
  },
  mounted() {
    let stdins = this.$refs.aa.$refs.stdin;
    this.stdins = stdins
    this.lastStdin = this.stdins[this.stdins.length - 1];
    this.stdinsLen = this.stdins.length
  },
  data: () => ({
    commands: {
      'echo': _ => createStdout('JSON.stringify(_, null, 2)')
    },
    remoteStr: '',
    history: [],
    lastStdin: null,
    stdinsLen: 0,
    stdins: null

  }),
  methods: {
    executeSomeCommandInLinux() {
      let configName = "RIP";
      let settingNum = 0;
      api.executeOneCommandInLinux(configName,settingNum).then(res=>{
        let str = res.handle_result.join("<br>");
        this.history.push(createStdout(str));

      });
    },
    executeOneCommandInLinux() {
      let configName = "RIP";
      let settingNum = 0;
      let command = "str";
      // 这里还需要定义一个变量，command的base64编码
      let Base64 = require('js-base64').Base64
      let command_base64=Base64.encode(command);
      api.executeOneCommandInLinux(configName,settingNum,command_base64).then(res=>{
        let str = res.handle_result.join("<br>");
        this.history.push(createStdout(str));
      });
    },
    aaa() {
      this.sleep(100).then(res=>{
        this.lastStdin.local.stdin = new String("命令1");
        this.history.push(createStdout('你坏<br>哈哈'));
        return this.sleep(100)
      })

    },
    refresh1() {
      this.lastStdin = this.stdins[this.stdins.length - 1];
    },
    sleep(time) {
      return new Promise((resolve) => setTimeout(resolve, time));
    }
  }
};
</script>

<style scoped>
.fillcontain {
  background: #fff;
  padding: 20px 20px;

}

.contain {
  height: 420px;
}

.vuecommand {
  min-height: 400px;
  max-height: 400px;
  overflow-y: scroll;
}
</style>
