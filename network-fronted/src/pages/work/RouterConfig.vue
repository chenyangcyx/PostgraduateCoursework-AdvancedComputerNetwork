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
        <el-form-item label="接口" >
          <el-input   v-model="interface1" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="子网掩码" >
          <el-input   v-model="mask" autocomplete="off"></el-input>
        </el-form-item>

        <el-form-item>
          <el-button type="primary" @click="submitForm()">提交</el-button>
          <el-button type="primary" @click="defaultConfig()">默认配置</el-button>
          <el-button @click="resetForm()">重置</el-button>
        </el-form-item>
      </el-form>

    </div>

  </div>
</template>

<script>
import api from "@/api2/bigwork"
export default {
  name: "RouterConfig",
  data(){
    return {
      host : null,
      interface1: null,
      ip: null,
      mask: null,

    }
  },
  methods: {
    submitForm(){
      api.setRouterIP(this.host,this.interface1,this.ip,this.mask)
    },
    resetForm(){
      this.host = null;
      this.port = null;
      this.ip = null;
      this.mask = null
    },
    defaultConfig(){
      api.setRouterIPDefault()
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
