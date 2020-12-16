<template>
    <div class="fillcontain">
        <div class="contain">
            <label > 开始日期：</label>
            <el-date-picker
                    v-model="searchParams.start"
                    align="right"
                    type="date"
                    placeholder="选择日期"
                    :picker-options="pickerOptions">
            </el-date-picker>
            <label style="margin-left: 5px;">结束日期：</label>
            <el-date-picker
                    v-model="searchParams.end"
                    align="right"
                    type="date"
                    placeholder="选择日期"
                    :picker-options="pickerOptions">
            </el-date-picker>
            <br>
            <el-button style="margin-bottom: 10px;margin-top: 15px" @click="getAll" type="primary">查找</el-button>
            <el-button v-if="buttonIsShow('system-manage:notice:add')" style="margin-bottom: 10px;margin-top: 15px" @click="addDialog = true" type="primary">新增</el-button>
            <div class="table_container">
                <el-table  :data="tableData" border stripe style="width:100%;">
                  <el-table-column
                      label="序号"
                      type="index"
                      width="50"
                      align='center'>
                  </el-table-column>

                  <el-table-column label="详情" type="expand">
                        <template slot-scope="props">
                            <el-form label-position="left" inline class="demo-table-expand">
                                <el-form-item label="内容：">
                                    <span>{{ props.row.content }}</span>
                                </el-form-item>
                            </el-form>
                        </template>
                    </el-table-column>
<!--                    <el-table-column-->
<!--                            type="index"-->
<!--                            width="50">-->
<!--                    </el-table-column>-->
                    <el-table-column label="主题">
                        <template slot-scope="scope">
                            <div
                                    class="todo-item"
                                    :style="scope.row.emergencyDegree == 1? 'color:#F56C6C': (scope.row.emergencyDegree == 2) ? 'color:#E6A23C':'color:#409EFF'"
                                    @click="display(scope.row)"
                            >{{scope.row.subject}}
                            </div>
                        </template>
                    </el-table-column>
                    <el-table-column label="紧急程度">
                        <template slot-scope="scope">
                            <div>
                                {{ emergencyDegrees[scope.row.emergencyDegree]}}
                            </div>
                        </template>
                    </el-table-column>
                    <el-table-column label="创建时间">
                        <template slot-scope="scope">
                            <div>
                                {{ $dateUtil.formatDateTime(scope.row.createTime)}}
                            </div>
                        </template>
                    </el-table-column>
                    <el-table-column label="到期时间">
                        <template slot-scope="scope">
                            <div>
                                {{ $dateUtil.formatDateTime(scope.row.expiredTime)}}
                            </div>
                        </template>
                    </el-table-column>
                    <el-table-column label="操作">
                        <template slot-scope="scope">
                            <el-button type="primary" v-if="buttonIsShow('system-manage:notice:update')" @click="updateNoticeOpen(scope.row)">修改</el-button>
                            <el-button type="warning" v-if="buttonIsShow('system-manage:notice:delete')" @click="deleteNotice(scope.row.id)">删除</el-button>
                        </template>
                    </el-table-column>
                </el-table>
                <el-row>
                    <el-col :span="24">
                        <div class="pagination">
                            <el-pagination
                                    v-if='paginations.total > 0'
                                    background
                                    :page-sizes="paginations.pageSizes"
                                    :page-size="paginations.pageSize"
                                    :layout="paginations.layout"
                                    :total="paginations.total"
                                    :current-page='paginations.pageIndex'
                                    @current-change='handleCurrentChange'
                                    @size-change="handleSizeChange">
                            </el-pagination>
                        </div>
                    </el-col>
                </el-row>
            </div>
        </div>
        <el-dialog
                title="通知内容"
                :visible.sync="noticeDialog"
                width="30%">
            <table cellpadding="5px" cellspacing="5px">
                <tr>
                    <td>主题：</td>
                    <td>{{currentNotice.subject}}</td>
                </tr>
                <tr>
                    <td>内容：</td>
                    <td>{{currentNotice.content}}</td>
                </tr>
                <tr>
                    <td>到期时间：</td>
                    <td>{{$dateUtil.formatDateTime(currentNotice.expiredTime) }}</td>
                </tr>
                <tr>
                    <td>紧急程度：</td>
                    <td>{{emergencyDegrees[currentNotice.emergencyDegree]}}</td>
                </tr>
            </table>
            <span slot="footer" class="dialog-footer">
        <el-button @click="noticeDialog = false">取 消</el-button>
        <el-button type="primary" @click="noticeDialog = false">确 定</el-button>
      </span>
        </el-dialog>

        <el-dialog
                title="新增通知"
                :visible.sync="addDialog"
                width="50%">

            <el-form :model="newRow">
                <el-form-item label="通知主题" >
                    <el-input v-model="newRow.subject" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="通知内容" >
                    <el-input type="textarea" v-model="newRow.content" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="通知的有效日期" >
                    <el-date-picker
                            v-model="newRow.expiredTime"
                            align="right"
                            type="date"
                            placeholder="选择日期"
                            :picker-options="pickerOptions">
                    </el-date-picker>
                </el-form-item>
                <el-form-item label="紧急程度" >
                    <el-radio-group v-model="newRow.emergencyDegree">
                        <el-radio :label="1">非常紧急</el-radio>
                        <el-radio :label="2">一般紧急</el-radio>
                        <el-radio :label="3">不紧急</el-radio>
                    </el-radio-group>
                </el-form-item>
                <el-form-item label="目标用户" >
                    <el-radio-group v-model="newRow.targetIsAll">
                        <el-radio :label="true">全体用户</el-radio>
                        <el-radio :label="false">特定用户</el-radio>
                    </el-radio-group>
                </el-form-item>
                <el-form-item v-if="newRow.targetIsAll === false"   label="请选择用户" >
                    <el-select
                            v-model="newRow.stakeholders"
                            multiple
                            filterable
                            placeholder="请选择">
                        <el-option
                                v-for="item in staffs"
                                :key="item.id"
                                :label="item.staffId + '(' + item.staffName + ')'"
                                :value="item.id">
                        </el-option>
                    </el-select>
                </el-form-item>
            </el-form>
            <span slot="footer" class="dialog-footer">
        <el-button @click="noticeDialog = false">取 消</el-button>
        <el-button type="primary" @click="addNew">确 定</el-button>
      </span>
        </el-dialog>

        <el-dialog
                title="修改通知"
                :visible.sync="updateDialog"
                width="50%">

            <el-form :model="currentRow">
                <el-form-item label="通知主题" >
                    <el-input v-model="currentRow.subject" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="通知内容" >
                    <el-input type="textarea" v-model="currentRow.content" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="通知的有效日期" >
                    <el-date-picker
                            v-model="currentRow.expiredTime"
                            align="right"
                            type="date"
                            placeholder="选择日期"
                            :picker-options="pickerOptions">
                    </el-date-picker>
                </el-form-item>
                <el-form-item label="紧急程度" >
                    <el-radio-group v-model="currentRow.emergencyDegree">
                        <el-radio :label="1">非常紧急</el-radio>
                        <el-radio :label="2">一般紧急</el-radio>
                        <el-radio :label="3">不紧急</el-radio>
                    </el-radio-group>
                </el-form-item>
                <el-form-item label="目标用户" >
                    <el-radio-group v-model="currentRow.targetIsAll">
                        <el-radio :label="true">全体用户</el-radio>
                        <el-radio :label="false">特定用户</el-radio>
                    </el-radio-group>
                </el-form-item>
                <el-form-item v-if="currentRow.targetIsAll == false" label="请选择用户" >
                    <el-select
                            v-model="currentRow.stakeholders"
                            multiple
                            filterable
                            placeholder="请选择">
                        <el-option
                                v-for="item in staffs"
                                :key="item.id"
                                :label="item.staffId + '(' + item.staffName + ')'"
                                :value="item.id">
                        </el-option>
                    </el-select>
                </el-form-item>
            </el-form>
            <span slot="footer" class="dialog-footer">
        <el-button @click="updateDialog = false">取 消</el-button>
        <el-button type="primary" @click="updateNotice">确 定</el-button>
      </span>
        </el-dialog>
    </div>

</template>

<script>
    import {getAll,add,updateNotice,deleteNotice,getAllStakeholdersId} from '../../api2/auth/notice';
    import { DateUtil } from '../../utils/DataUtils';
    import {getAllStaffs} from '../../api2/lab';

    export default {
        name: 'CheckAllErrReport',
        data() {
            return {
                tableData: [],
                loading: false,
                //需要给分页组件传的信息
                paginations: {
                    total: 0,        // 总数
                    pageIndex: 1,  // 当前位于哪页
                    pageSize: 10,   // 1页显示多少条
                    pageSizes: [3, 5, 10, 20],  //每页显示多少条
                    layout: 'total, sizes, prev, pager, next, jumper'   // 翻页属性
                },
                currentRow: {},
                currentNotice: {  },
                noticeDialog: false,
                emergencyDegrees: ["", "非常紧急", "一般紧急", "不紧急"],

                searchParams: {
                    start: null,//开始时间
                    end: null,
                    staffId: null,
                },
                pickerOptions: {
                    shortcuts: [{
                        text: '今天',
                        onClick(picker) {
                            picker.$emit('pick', new Date());
                        }
                    }, {
                        text: '昨天',
                        onClick(picker) {
                            const date = new Date();
                            date.setTime(date.getTime() - 3600 * 1000 * 24);
                            picker.$emit('pick', date);
                        }
                    }],

                },
                updateDialog: false,
                addDialog: false,
                newRow: {
                    stakeholders: []
                },
                staffs:[]

            };
        },
        created() {
            this.getAll()
            getAllStaffs().then(res=>{
                this.staffs = res.data
            })
        },
        methods: {
          buttonIsShow(perm) {
            return this.$store.getters.getButton.findIndex(item => item.resourcePerm == perm) != -1;
          },

          getAll() {
                this.loading = true;
                console.log(this.searchParams);
                if (this.searchParams.start != null && typeof this.searchParams.start != 'string')
                    this.searchParams.start = DateUtil.formatDateTime(this.searchParams.start, 'yyyy-MM-dd') + ' 00:00:00';
                if (this.searchParams.end != null && typeof this.searchParams.end != 'string')
                    this.searchParams.end = DateUtil.formatDateTime(this.searchParams.end, 'yyyy-MM-dd') + ' 23:59:59';

                getAll({
                    pageNum: this.paginations.pageIndex,
                    size: this.paginations.pageSize,
                    start: this.searchParams.start,
                    end: this.searchParams.end,
                }).then(res => {
                    this.tableData = res.data.list;
                    this.paginations.total = res.data.total;
                    this.paginations.pageIndex = res.data.pageNum;
                    this.loading = false;
                })
            },
            handleCurrentChange(page) {
                this.paginations.pageIndex = page;
                this.getAllErrReport();
            },
            handleSizeChange(pageSize) {
                this.paginations.pageSize = pageSize;
                this.getAllErrReport();
            },
            display(notice) {
                this.noticeDialog = true
                this.currentNotice = notice;
            },
            deleteNotice(id){
                this.$confirm('此操作将永久删除该通知, 是否继续?', '提示', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    type: 'warning'
                }).then(res=>{
                    return deleteNotice(id)
                }).then(res=>{
                    if(res.message == "success"){
                        this.$message.success("删除成功！")
                        this.getAll()
                    }
                })
            },
            updateNoticeOpen(row){
                this.currentRow = this.$deepClone(row)
                if(this.currentRow.targetIsAll == false){
                    getAllStakeholdersId(this.currentRow.id).then(res=>{
                        this.currentRow.stakeholders = res.data
                    })
                }
                this.updateDialog = true
            },
            addNew(){
                this.newRow.expiredTime = this.$dateUtil.formatDateTime(new Date(this.newRow.expiredTime),"yyyy-MM-dd HH:mm:ss")
                add(this.newRow).then(res=>{
                    if(res.message == "success"){
                        this.$message.success("添加成功！")
                        this.addDialog = false
                        this.newRow = {}
                        this.getAll()
                    }
                })
            },
            updateNotice(){
                console.log(this.currentRow);
                delete this.currentRow.createTime
                this.currentRow.expiredTime = this.$dateUtil.formatDateTime(new Date(this.currentRow.expiredTime),"yyyy-MM-dd HH:mm:ss")
                updateNotice(this.currentRow).then(res=>{
                    if(res.message == "success"){
                        this.$message.success("更新成功！")
                        this.updateDialog = false
                        this.currentRow = {}
                        this.getAll()
                    }
                })
            }
        }
    };
</script>

<style scoped>
    .fillcontain {
        background: #fff;
        padding: 20px 20px;
    }
    .demo-table-expand {
        font-size: 0;
    }
    .demo-table-expand label {
        width: 90px;
        color: #99a9bf;
    }
    .demo-table-expand .el-form-item {
        margin-right: 0;
        margin-bottom: 0;
        width: 50%;
    }
    .todo-item {
        font-size: 14px;

    }

    .todo-item:hover {
        cursor: pointer
    }
    .demo-table-expand {
        font-size: 0;
    }
    .demo-table-expand label {
        width: 90px;
        color: #99a9bf;
    }
    .demo-table-expand .el-form-item {
        margin-right: 0;
        margin-bottom: 0;
        width: 50%;
    }
</style>
