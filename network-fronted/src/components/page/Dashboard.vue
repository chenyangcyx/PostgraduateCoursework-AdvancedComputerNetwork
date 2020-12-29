<template>
    <div>
        <el-row :gutter="20">
            <el-col :span="8">
                <el-card shadow="hover" class="mgb20" style="height:533px;">
                    <div class="user-info">
                        <img src="../../assets/img/yonghuxinxi.png" class="user-avator" alt/>
                    </div>
                    <div class="user-info-list"
                         style="border-bottom: 2px solid #ccc;padding-bottom:5px; margin-bottom: 20px;">
                        <h3>用户基本信息</h3>
                    </div>

                    <div class="user-info-list">
                        账户：
                        <span></span>
                    </div>
                    <div class="user-info-list">
                        姓名：
                        <span></span>
                    </div>
                    <div class="user-info-list">
                        电话：
                        <span></span>
                    </div>
                    <div class="user-info-list">
                        角色：
                        <span></span>
<!--                        <span>{{$store.getters.getUser.roles}}</span>-->
                    </div>
                </el-card>

            </el-col>
            <el-col :span="16" style="position: relative;">
                <el-card shadow="hover" style="height:533px">
                    <div slot="header" class="clearfix">
                        <span>通知公告</span>
                        <el-button  style="float: right; padding: 3px 0" type="text">查看所有</el-button>
                    </div>
                    <el-table :show-header="false" :data="notices" style="width:100%;">
                        <el-table-column>
                            <template slot-scope="scope">
                                <div
                                        class="todo-item"
                                        :style="scope.row.emergencyDegree == 1? 'color:#F56C6C': (scope.row.emergencyDegree == 2) ? 'color:#E6A23C':'color:#409EFF'"
                                        @click="display(scope.row)"
                                >{{scope.row.subject}}
                                </div>
                            </template>
                        </el-table-column>


                    </el-table>
                </el-card>
            </el-col>
        </el-row>
            <el-dialog
                    title="通知内容"
                    :visible.sync="noticeDialog"
                    width="30%">
                <table cellpadding="5px" cellspacing="5px">
                    <tr>
                        <td>主题：</td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>内容：</td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>到期时间：</td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>紧急程度：</td>
                        <td></td>
                    </tr>
                </table>
                <span slot="footer" class="dialog-footer">
        <el-button @click="noticeDialog = false">取 消</el-button>
        <el-button type="primary" @click="noticeDialog = false">确 定</el-button>
      </span>
            </el-dialog>

    </div>
</template>

<script>



    export default {
        name: 'dashboard',
        created() {
        },
        data() {
            return {
                notices: [],
                currentNotice: {  },
                noticeDialog: false,
                emergencyDegrees: ["", "非常紧急", "一般紧急", "不紧急"]

            };
        },

        computed: {},

        methods: {
            display(notice) {
                this.noticeDialog = true
                this.currentNotice = notice;
            },

        }
    };
</script>


<style scoped>
    .el-row {
        margin-bottom: 20px;
    }

    .grid-content {
        display: flex;
        align-items: center;
        height: 100px;
    }

    .grid-cont-right {
        flex: 1;
        text-align: center;
        font-size: 14px;
        color: #999;
    }

    .grid-num {
        font-size: 30px;
        font-weight: bold;
    }

    .grid-con-icon {
        font-size: 50px;
        width: 100px;
        height: 100px;
        text-align: center;
        line-height: 100px;
        color: #fff;
    }

    .grid-con-1 .grid-con-icon {
        background: rgb(45, 140, 240);
    }

    .grid-con-1 .grid-num {
        color: rgb(45, 140, 240);
    }

    .grid-con-2 .grid-con-icon {
        background: rgb(100, 213, 114);
    }

    .grid-con-2 .grid-num {
        color: rgb(45, 140, 240);
    }

    .grid-con-3 .grid-con-icon {
        background: rgb(242, 94, 67);
    }

    .grid-con-3 .grid-num {
        color: rgb(242, 94, 67);
    }

    .user-info {
        display: flex;
        align-items: center;
        padding-bottom: 20px;
        /*border-bottom: 2px solid #ccc;*/
        /*margin-bottom: 20px;*/
    }


    .user-avator {
        width: 120px;
        height: 120px;
        /*border-radius: 50%;*/
    }

    .user-info-cont {
        padding-left: 50px;
        flex: 1;
        font-size: 14px;
        color: #999;
    }

    .user-info-cont div:first-child {
        font-size: 30px;
        color: #222;
    }

    .user-info-list {
        font-size: 14px;
        color: #999;
        line-height: 25px;
    }

    .user-info-list span {
        margin-left: 70px;
    }

    .mgb20 {
        margin-bottom: 20px;
    }

    .todo-item {
        font-size: 14px;

    }

    .todo-item:hover {
        cursor: pointer
    }

    .todo-item-del {
        text-decoration: line-through;
        color: #999;
    }

    .schart {
        width: 100%;
        height: 300px;
    }
</style>
