<template>
  <div class="fillcontain">
    <el-button @click="executeSomeCommandInLinux" style="margin-bottom: 10px" type="success">发送一批命令（如配置路由器？）</el-button>
    <el-button @click="executeOneCommandInLinux" style="margin-bottom: 10px" type="success">发送一条命令（如ping？）</el-button>

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
      let configName = "configName";
      let settingNum = 1;
      api.executeOneCommandInLinux(configName,settingNum).then(res=>{
        let str = res.handle_result.join("<br>");
        this.history.push(createStdout(str));

      });
    },
    executeOneCommandInLinux() {
      let configName = "configName";
      let settingNum = 1;
      let command = "str"
      api.executeOneCommandInLinux(configName,settingNum,command).then(res=>{
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
