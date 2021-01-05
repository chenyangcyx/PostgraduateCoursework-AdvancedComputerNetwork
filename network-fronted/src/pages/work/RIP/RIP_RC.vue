<template>
  <div class="fillcontain">
    <el-button @click="executeConfigCommand" style="margin-bottom: 10px" type="success">配置路由器</el-button>
    <el-button @click="executeTestCommand" style="margin-bottom: 10px" type="success">查看结果</el-button>

    <div class="contain">
      <vue-command
          class="vuecommand"
          ref="aa" title="高级计算机网络大作业"
          prompt=""
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
import command from "@/pages/work/RIP/RC.json";

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
    executeConfigCommand() {

      this.sleep(100).then(res=>{
        //在这里输入配置信息
        let configName = "RIP_normal";
        let settingNum = 2;
        api.executeConfigCommand(configName,settingNum).then(res=>{
          this.history.push(createStdout("配置命令如下: <br>" + res.original_result.join("<br>")))
          let str = "<br>结果如下：<br>" + res.handle_result.join("<br>");
          this.history.push(createStdout(str));
        });
      })
    },
    executeTestCommand() {
      this.sleep(100).then(res=>{
        let configName = "RIP_normal";
        let settingNum = 2;
        api.executeTestCommand(configName,settingNum).then(res=>{
          this.history.push(createStdout("查询命令如下: <br>" + res.original_result.join("<br>")))
          let str = "<br>结果如下：<br>" + res.handle_result.join("<br>");
          this.history.push(createStdout(str));
        });
      })
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
