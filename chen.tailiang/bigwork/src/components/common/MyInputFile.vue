<template>
    <div>
        <input  name="file" type="file" @change="loadImg($event)"/><br><br>
        <img ref="img" :width="width" :height="height"  alt="请选择图片"  />
    </div>
</template>

<script>
    export default {
        name: 'MyInputFile',
        data() {
          return {
              imgFile: null,
              file: null
          }
        },
        props: {
            width: {
                type: String,
                default: "150px"
            },
            height: {
                type: String,
                default: "50px"
            }
        },
        methods:{
            loadImg(event){
                let file = event.target.files[0];
                this.file = file;
                //创建读取文件的对象
                let reader = new FileReader();
                //为文件读取成功设置事件
                reader.onload=(e)=> {
                    let imgFile = e.target.result;
                    // console.log(imgFile);
                    this.imgFile = imgFile
                    console.log(this.$refs.img);
                    this.$refs.img.setAttribute("src", imgFile);
                };
                //正式读取文件
                reader.readAsDataURL(file);
            }
        }
    };
</script>

<style scoped>

</style>