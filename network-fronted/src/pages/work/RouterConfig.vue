<template>
  <div class="fillcontain">
    <h2 style="text-align: center">路由器配置</h2>
    <div style="display: flex;justify-content: center">
      <el-form style="width: 50%" label-width="120px;" >
        <el-form-item  label="Telnet主机">
          <el-input   v-model="host" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item  label="ip地址">
          <el-input   v-model="ip" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="端口" >
          <el-input   v-model="port" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="子网掩码" >
          <el-input   v-model="mask" autocomplete="off"></el-input>
        </el-form-item>

        <el-form-item>
          <el-button type="primary" @click="submitForm()">提交</el-button>
          <el-button @click="resetForm()">重置</el-button>
        </el-form-item>
      </el-form>

    </div>

  </div>
</template>

<script>
export default {
  name: "RouterConfig",
  data(){
    return {
      host : null,
      port: null,
      ip: null,
      mask: null,

    }
  },
  methods: {
    submitForm(){

    },
    resetForm(){
      this.host = null;
      this.port = null;
      this.ip = null;
      this.mask = null
    }
  }
}
</script>

<style scoped>
.fillcontain {
  background: #fff;
  padding: 20px 20px;

}
</style>
