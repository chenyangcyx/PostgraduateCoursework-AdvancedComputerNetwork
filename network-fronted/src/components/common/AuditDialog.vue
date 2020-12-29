<template>
    <div>
        <el-dialog :title="title"
                   :visible.sync="flag"
                   width="40%"
                   show-close
                   destroy-on-close
        >
            <el-form v-model="obj">
                <el-form-item label="请输入审核密码" label-width="120px">
                    <el-input type="password" v-model="obj.auditPassword"
                              autocomplete="off"></el-input>
                </el-form-item>
            </el-form>
            <br>
            <div slot="footer" class="dialog-footer">
                <el-button @click="flag = false">取 消</el-button>
                <el-button type="primary" @click="confirm">确认</el-button>
            </div>
        </el-dialog>
    </div>

</template>

<script>
    export default {
        name: 'AuditDialog',
        props: {
            title: {
                type: String,
                default: "审核"
            },
            dialog: {
                type: Boolean,
                default: false
            }
        },
        data(){
            return {
                obj: {
                    auditPassword: null
                },
                flag: this.$deepClone(this.dialog)
            }
        },
        watch: {
            dialog(newVal, oldVal) {
                // 在监听你使用update事件来更新word,而在父组件不需要调用该函数
                // this.$emit('update:dialog', newVal);
                this.flag = this.$deepClone(this.dialog)
            },
            flag(newVal, oldVal){
                if(newVal == false)
                    this.$emit('close');
            }

        },
        methods: {
            confirm(){
                this.$emit("confirm", this.obj.auditPassword);
            }

        }
    };
</script>

<style scoped>

</style>