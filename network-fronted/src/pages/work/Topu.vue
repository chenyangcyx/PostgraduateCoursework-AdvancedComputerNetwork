<template>
  <div class="fillcontain">
    <h2>拓扑图</h2>
    <div class="img-content">
      <el-image class="img" :src="imgsrc">
        <div slot="placeholder" class="image-slot">
          加载中<span class="dot">...</span>
        </div>
      </el-image>
    </div>

  </div>
</template>

<script>
export default {
  name: "Topu",
  data() {
    return {
      imgsrc: "https://gitee.com/CTLQAQ/picgo/raw/master/topu.PNG"
    }
  }
}
</script>

<style scoped>
.fillcontain {
  background: #fff;
  padding: 20px 20px;
  /*width: 100%;*/
}

h2 {
  text-align: center;
}

.img {
  text-align: center;
}

.img-content {
  width: 100%;
  display: flex;
  justify-content: center;
  /*　　justify-content: center;*/
  /*　　align-items: center;*/
}

</style>
