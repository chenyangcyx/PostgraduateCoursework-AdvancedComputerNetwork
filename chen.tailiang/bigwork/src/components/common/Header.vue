<template>
    <div class="header" style="background-color:#324157;border-bottom:  1px solid white">
        <!-- 折叠按钮 -->
        <div class="collapse-btn" @click="collapseChage">
            <i v-if="!collapse" class="el-icon-s-fold"></i>
            <i v-else class="el-icon-s-unfold"></i>
        </div>
        <div class="logo">高级计算机网络系统</div>
        <div class="header-right">
            <div class="header-user-con">
                <!-- 全屏显示 -->
                <!--                <div class="btn-fullscreen" @click="handleFullScreen">-->
                <!--                    <el-tooltip effect="dark" :content="fullscreen?`取消全屏`:`全屏`" placement="bottom">-->
                <!--                        <i class="el-icon-rank"></i>-->
                <!--                    </el-tooltip>-->
                <!--                </div>-->

                <div v-if="!fullscreen" class="btn-fullscreen" @click="handleFullScreen">
                    <el-tooltip effect="dark" content="全屏" placement="bottom">
                        <i class="el-icon-rank"></i>
                    </el-tooltip>
                </div>

                <div v-if="fullscreen" class="btn-not-fullscreen" @click="handleFullScreen">
                    <el-tooltip effect="dark" content="取消全屏" placement="bottom">
                        <i class="el-icon-close"></i>
                    </el-tooltip>
                </div>
                <!-- 用户头像 -->
                <div class="user-avator">
                    <img src="../../assets/img/yonghu1.png"/>
                </div>
                <!-- 用户名下拉菜单 -->
                <el-dropdown class="user-name" trigger="click" @command="handleCommand">
                    <span class="el-dropdown-link">
                        {{$store.getters.getUser.name}}
                        <i class="el-icon-caret-bottom"></i>
                    </span>
                    <el-dropdown-menu slot="dropdown">
                        <el-dropdown-item divided command="loginout">退出登录</el-dropdown-item>
                    </el-dropdown-menu>
                </el-dropdown>
            </div>
        </div>

        <el-dialog @open="updateBasicInformationDialogOpen" title="修改个人基本信息"
                   :visible.sync="updateBasicInformationDialog">
            <el-form :model="basicInformation">
                <el-form-item label="员工id">
                    <el-input readonly v-model="basicInformation.staffId" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="员工姓名">
                    <el-input v-model="basicInformation.staffName" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="电话号码">
                    <el-input v-model="basicInformation.phone" autocomplete="off"></el-input>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="updateBasicInformationDialog = false">取 消</el-button>
                <el-button type="primary" @click="updateBasic">确 定</el-button>
            </div>
        </el-dialog>

        <el-dialog @open="updatePasswordDialogOpen" title="修改登录密码" :visible.sync="updatePasswordDialog">
            <el-form >
                <el-form-item label="请输入旧密码">
                    <el-input v-model="oldPassword" type="password" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="请输入新密码">
                    <el-input v-model="newPassword" type="password" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="请再次输入新密码">
                    <el-input v-model="newPasswordRepeat" type="password" autocomplete="off"></el-input>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="updatePasswordDialog = false">取 消</el-button>
                <el-button type="primary" @click="updatePassword">确 定</el-button>
            </div>
        </el-dialog>
        <el-dialog @open="updatePasswordDialogOpen" title="修改审核密码" :visible.sync="updateAuditPasswordDialog">
            <el-form >
                <el-form-item label="请输入旧密码">
                    <el-input v-model="oldPassword" type="password" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="请输入新密码">
                    <el-input v-model="newPassword" type="password" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="请再次输入新密码">
                    <el-input v-model="newPasswordRepeat" type="password" autocomplete="off"></el-input>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="updateAuditPasswordDialog = false">取 消</el-button>
                <el-button type="primary" @click="updateAuditPassword">确 定</el-button>
            </div>
        </el-dialog>

        <el-dialog title="修改电子签名" destroy-on-close :visible.sync="uploadSigDialog">
            <el-form>
                <el-form-item label="原电子签名">
                    <img width="90px" height="30px" :src="'/api/system-manage/getSignature?id='+ this.$store.getters.getUser.id  + '&' + stamp" />
                </el-form-item>
                <el-form-item label="请上传新的电子签名">
                    <my-input-file ref="sig"></my-input-file>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="uploadSigDialog = false">取 消</el-button>
                <el-button type="primary" @click="uploadSig">确 定</el-button>
            </div>
        </el-dialog>
    </div>
</template>
<script>
    import bus from '../common/bus';
    import {
        login,
        reloadPersonalInformation,
        resourceMenuTab,
        updateBasicInformation,
        uploadSig,
        userUpdateAuditPassword,
        userUpdatePassword
    } from '../../api2/auth/system';
    import { getUserInfoByToken } from '../../utils/CommonUtils';
    import MyInputFile from '../../components/common/MyInputFile';
    export default {
        components: {MyInputFile},
        data() {
            return {
                collapse: true,
                fullscreen: false,
                name: 'linxin',
                message: 2,
                uploadSigDialog: false,
                updateAuditPasswordDialog: false,
                updatePasswordDialog: false,
                updateBasicInformationDialog: false,
                basicInformation: {
                    phone: null,
                    staffName: null,
                    staffId: null,
                },
                oldPassword: null,
                newPassword: null,
                newPasswordRepeat: null,
                stamp: new Date()
            };
        },
        created() {
        },
        computed: {
            username() {
                let username = localStorage.getItem('ms_username');
                return username ? username : this.name;
            }
        },
        methods: {
            updateBasicInformationDialogOpen() {
                let data = this.$deepClone(this.$store.getters.getUser);
                console.log(data);
                this.basicInformation.staffId = data.account;
                this.basicInformation.staffName = data.name
                this.basicInformation.phone = data.phone
                this.basicInformation.id = data.id

            },
            // 用户名下拉菜单选择事件
            handleCommand(command) {
                if (command == 'loginout') {
                    let interval = this.$store.getters.getNoticeInterval;
                    if(interval != null)
                      clearInterval(interval)
                    localStorage.removeItem('weifei-token');
                    this.$router.push('/login');
                } else {
                    switch (command) {
                        case 'updateBasicInformation':
                            this.updateBasicInformationDialog = true;
                            break;
                        case 'updatePassword':
                            this.updatePasswordDialog = true;
                            break;
                        case 'updateAuditPassword':
                            this.updateAuditPasswordDialog = true;
                            break;
                        case 'uploadSig':
                            this.uploadSigDialog = true;
                            break;
                    }
                }

            },
            // 侧边栏折叠
            collapseChage() {
                this.collapse = !this.collapse;
                bus.$emit('collapse', this.collapse);
            },
            // 全屏事件
            handleFullScreen() {
                let element = document.documentElement;
                if (this.fullscreen) {
                    if (document.exitFullscreen) {
                        document.exitFullscreen();
                    } else if (document.webkitCancelFullScreen) {
                        document.webkitCancelFullScreen();
                    } else if (document.mozCancelFullScreen) {
                        document.mozCancelFullScreen();
                    } else if (document.msExitFullscreen) {
                        document.msExitFullscreen();
                    }
                } else {
                    if (element.requestFullscreen) {
                        element.requestFullscreen();
                    } else if (element.webkitRequestFullScreen) {
                        element.webkitRequestFullScreen();
                    } else if (element.mozRequestFullScreen) {
                        element.mozRequestFullScreen();
                    } else if (element.msRequestFullscreen) {
                        // IE11
                        element.msRequestFullscreen();
                    }
                }
                this.fullscreen = !this.fullscreen;
            },
            updateBasic() {
                updateBasicInformation(this.basicInformation).then(res => {
                    this.$message.success('更新成功');
                    this.updateBasicInformationDialog = false;
                    //
                    return reloadPersonalInformation(this.basicInformation.staffId);
                }).then(res => {
                    if (res.message == 'success') {
                        this.basicInformation = {phone: null, staffName: null,staffId: null,};
                        // this.$message.success('登录成功~');
                        this.$store.commit('setToken', { token: res.data });
                        localStorage.setItem('weifei-token', res.data);
                        let user = getUserInfoByToken(res.data);
                        this.$store.commit('setUser', { user });
                    }
                });
            },
            updatePassword(){
                if(this.newPasswordRepeat != this.newPassword ){
                    this.$message.error("2次密码输入不同！")
                    return;
                }
                userUpdatePassword(this.$store.getters.getUser.account,this.oldPassword, this.newPassword).then(res=>{
                    if(res.message == "success"){
                        this.$message.success("修改成功！")
                        this.updatePasswordDialogOpen()
                        this.updatePasswordDialog = false
                    }
                })
            },
            updateAuditPassword(){
                if(this.newPasswordRepeat != this.newPassword ){
                    this.$message.error("2次密码输入不同！")
                    return;
                }
                userUpdateAuditPassword(this.$store.getters.getUser.account,this.oldPassword, this.newPassword).then(res=>{
                    if(res.message == "success"){
                        this.$message.success("修改成功！")
                        this.updatePasswordDialogOpen()
                        this.updateAuditPasswordDialog = false
                    }
                })
            },
            updatePasswordDialogOpen(){
                this.oldPassword = null
                this.newPassword = null;
                this.newPasswordRepeat = null
            },
            uploadSig(){
                uploadSig(this.$store.getters.getUser.id, this.$refs.sig.file).then(res=>{
                    this.$message.success("上传成功！")
                    this.stamp = new Date().getTime()
                    this.uploadSigDialog = false
                })
            }
        },

        mounted() {
            if (document.body.clientWidth < 1500) {
                this.collapseChage();
            }
        }
    };
</script>
<style scoped>
    .header {
        position: relative;
        box-sizing: border-box;
        width: 100%;
        height: 70px;
        font-size: 22px;
        color: #fff;
    }

    .collapse-btn {
        float: left;
        padding: 0 21px;
        cursor: pointer;
        line-height: 70px;
    }

    .header .logo {
        float: left;
        width: 300px;
        line-height: 70px;
    }

    .header-right {
        float: right;
        padding-right: 50px;
    }

    .header-user-con {
        display: flex;
        height: 70px;
        align-items: center;
    }

    .btn-fullscreen {
        transform: rotate(45deg);
        margin-right: 5px;
        font-size: 24px;
    }

    .btn-not-fullscreen {
        margin-right: 5px;
        font-size: 24px;
        cursor: pointer;
    }

    .btn-bell,
    .btn-fullscreen {
        position: relative;
        width: 30px;
        height: 30px;
        text-align: center;
        border-radius: 15px;
        cursor: pointer;
    }

    .btn-bell-badge {
        position: absolute;
        right: 0;
        top: -2px;
        width: 8px;
        height: 8px;
        border-radius: 4px;
        background: #f56c6c;
        color: #fff;
    }

    .btn-bell .el-icon-bell {
        color: #fff;
    }

    .user-name {
        margin-left: 10px;
    }

    .user-avator {
        margin-left: 20px;
    }

    .user-avator img {
        display: block;
        width: 40px;
        height: 40px;
        /*border-radius: 50%;*/
    }

    .el-dropdown-link {
        color: #fff;
        cursor: pointer;
    }

    .el-dropdown-menu__item {
        text-align: center;
    }
</style>
