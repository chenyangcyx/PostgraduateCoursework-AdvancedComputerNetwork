<template>
  <div class="fillcontain">
    <div  style="display: flex;width: 100%; justify-content: space-between;flex-wrap: wrap">
      <div style="width: 30%">
        <span style="margin-bottom: 10px" >配置</span><br>
        <el-button @click="configDialog = true" style="margin-bottom: 10px" type="success">配置路由器</el-button>
        <el-button @click="customizedConfigDialog = true" style="margin-bottom: 10px" type="success">自定义配置</el-button>
        <el-button @click="clearAllConfig" style="margin-bottom: 10px" type="success">清除所有配置</el-button>
      </div>
      <div style="width: 60%">
        <span style="margin-bottom: 10px">查看</span><br>
        <el-button @click="checkRouterTable" style="margin-bottom: 10px" type="success">查看路由表</el-button>
        <el-button @click="checkRouterProtocol" style="margin-bottom: 10px" type="success">查看路由协议</el-button>
        <el-button @click="checkInterface" style="margin-bottom: 10px" type="success">查看接口信息</el-button>

        <el-button @click="validateConfig" style="margin-bottom: 10px" type="success">验证配置结果</el-button>
      </div>
      <div style="width: 100%;margin-bottom: 10px">
        ping!!!
      </div>
      <div style="width: 30%">
        <el-input v-model="pingIp" autocomplete="off"></el-input>
      </div>
      <div style="width:50%">
        <el-button @click="ping" style="margin-bottom: 10px" type="success">ping!</el-button>
      </div>
      <div style="width:10%;margin-right:15px">
        <el-button @click="clearCommand" style="margin-bottom: 10px" type="success">Clear Command</el-button>
      </div>


    </div>


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


    <el-dialog title="配置路由器" :visible.sync="configDialog">
      <el-form>
        <el-form-item label="详细配置">
          <el-input type="textarea" :rows="15" v-model="config" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="configDialog  = false">取 消</el-button>
        <el-button type="info" @click="generateTemplate">生成模板</el-button>
        <el-button type="primary" @click="executeConfigCommand">执 行</el-button>
      </div>
    </el-dialog>

    <el-dialog title="用户自定义配置" :visible.sync="customizedConfigDialog">
      <el-form>
        <el-form-item>
          <el-input type="textarea" :rows="15" v-model="customizedConfig" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="customizedConfigDialog  = false">取 消</el-button>
        <el-button type="primary" @click="executeCustomizedOrder">执 行</el-button>
      </div>
    </el-dialog>

    <el-dialog title="ping! " :visible.sync="pingDialog">
      <el-form :rules="rules" :model="pingItem">
        <el-form-item label="请输入ip地址，多个ip请使用,分割" prop="pingIp">
          <el-input    v-model="pingItem.pingIp" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="pingDialog  = false">取 消</el-button>
        <el-button type="primary" @click="ping">执 行</el-button>
      </div>
    </el-dialog>
  </div>


</template>

<script>
import VueCommand, {createStdout} from 'vue-command';
import 'vue-command/dist/vue-command.css';

export default {
  name: 'Router',
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
  data() {

   let validateIPAddress =  (rule, value, callback) =>  {
      // return callback(new Error('请输入iP地址'));
      let regexp = /^((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}$/;
      let valdata = value.split(',');
      let isCorrect = true;
      if (valdata.length) {
        for (let i = 0; i < valdata.length; i++) {
          if (regexp.test(valdata[i]) === false) {
            isCorrect = false;
          }
        }
      }

      if (value === '') {
        return callback(new Error('请输入iP地址'));
      } else if (!isCorrect) {
        callback(new Error('请输入正确对ip地址'));
      } else {
        callback()
      }
    }

    return {

      commands: {
        'echo': _ => createStdout('JSON.stringify(_, null, 2)')
      },
      remoteStr: '',
      history: [],
      lastStdin: null,
      stdinsLen: 0,
      stdins: null,
      configDialog: false,
      config: null,
      pingDialog: false,
      pingIp: null,
      pingItem: {
        pingIp: ""
      },
      rules: {
        pingIp: [
          {required: true, validator: validateIPAddress, trigger: 'blur'}]

      },
      customizedConfigDialog: false,
      customizedConfig: null

    }
  },
  methods: {
    clearCommand(){
        this.history = []
    },
    executeConfigCommand() {
      this.$emit("executeConfigCommand",this.config);
    },
    executeTestCommand() {
      this.$emit("executeTestCommand")
    },
    generateTemplate() {
      this.$emit("generateTemplate")
    },
    executeCustomizedOrder(){
      this.$emit("executeCustomizedOrder", this.customizedConfig);
    },
    //这里调用ping
    ping() {
      this.$emit("ping",this.pingIp)
    },
    clearAllConfig(){
        this.$emit("clearAllConfig")
    },
    checkRouterTable(){
      this.$emit("checkRouterTable")
    },
    checkRouterProtocol(){
      this.$emit("checkRouterProtocol")
    },
    checkInterface(){
      this.$emit("checkInterface")
    },
    validateConfig(){
      this.$emit("validateConfig")
    },
    aaa() {
      this.sleep(100).then(res => {
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
    },

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
