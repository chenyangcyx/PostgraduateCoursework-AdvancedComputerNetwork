<template>
    <div class="fillcontain">
        <div class="contain">
                <table style="margin-bottom: 10px">
                    <tr>
                        <td>员工id：</td>
                        <td>
                            <el-input v-model="searchParams.staffId"></el-input>
                        </td>
                        <td><div style="margin-left: 20px">员工姓名：</div></td>
                        <td>
                            <el-input v-model="searchParams.staffName"></el-input>
                        </td>
                        <td><div style="margin-left: 20px">电话号码：</div></td>
                        <td>
                            <el-input v-model="searchParams.phone"></el-input>
                        </td>

                <el-button style="margin-left: 10px;" @click="getAll" v-if="buttonIsShow('system-manage:getAllUserInfo')" type="primary" plain>查找</el-button>
                <el-button style="margin-left: 10px;" @click="newRowDialog = true"  type="primary">新增</el-button>
                    </tr>
                </table>

            <div class="table_container">
                    <el-table
                            v-loading="loading"
                            :data="tableData"
                            border
                            stripe
                            highlight-current-row
                            header-cell-class-name="table-header-class"
                            style="width:100%">
                      <el-table-column
                          label="序号"
                          type="index"
                          width="50"
                          align='center'>
                      </el-table-column>


                      <el-table-column label="操作" type="expand">
                            <template slot-scope="scope">
                                <el-button v-if="buttonIsShow('system-manage:updateBasicInformation')" @click="updateBasicDialogOpen(scope.row)" type="primary">修改</el-button>
                                <el-button v-if="buttonIsShow('system-manage:updateAuditPassword')" @click="updateAuditPasswordDialogOpen(scope.row)" type="primary">修改审核密码</el-button>
                                <el-button v-if="buttonIsShow('system-manage:updatePassword')" @click="updatePasswordOpen(scope.row)" type="primary">修改密码</el-button>
                                <el-button v-if="buttonIsShow('system-manage:uploadSig')" @click="uploadSignatureDialogOpen(scope.row)" type="primary">更改电子签名</el-button>
                                <el-button v-if="buttonIsShow('system-manage:role:updateRoles')" type="primary" @click="updateRolesOpen(scope.row)">修改角色信息</el-button>
                            </template>
                        </el-table-column>
                        <el-table-column
                                label="员工号"
                                property="staffId"
                                align='center'>
                        </el-table-column>
                        <el-table-column
                                property="staffName"
                                label="员工姓名"
                                align='center'>
                        </el-table-column>
                        <el-table-column
                                label="电话号码"
                                property="phone"
                                align='center'>
                        </el-table-column>
                        <el-table-column
                                label="角色"
                                align='center'>
                            <template slot-scope="scope">
                                {{scope.row.roleNames.join()}}
                            </template>
                        </el-table-column>

                        <el-table-column
                                label="电子签名"
                                align='center'>
                            <template slot-scope="scope">
                                <img width="90px" height="30px" :src="'/api/system-manage/getSignature?id='+ scope.row.id  + '&' + stamp" />
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

        <el-dialog title="增加员工"  :visible.sync="newRowDialog">
            <el-form :model="newRow">
                <el-form-item label="员工姓名">
                    <el-input v-model="newRow.staffName" autocomplete="off"></el-input>
                </el-form-item>

                <el-form-item label="电话号码">
                    <el-input v-model="newRow.phone" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="登录密码">
                    <el-input type="password" v-model="newRow.password" autocomplete="off"></el-input>
                </el-form-item>

                <el-form-item label="审核密码">
                    <el-input type="password" v-model="newRow.password2" autocomplete="off"></el-input>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="newRowDialog = false">取 消</el-button>
                <el-button type="primary" @click="addNew">确 定</el-button>
            </div>
        </el-dialog>


        <el-dialog title="修改员工基本信息"  :visible.sync="updateBasicDialog">
            <el-form :model="currentRow">
                <el-form-item label="员工id" >
                    <el-input readonly v-model="currentRow.staffId" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="员工姓名">
                    <el-input v-model="currentRow.staffName" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="电话号码">
                    <el-input v-model="currentRow.phone" autocomplete="off"></el-input>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="updateBasicDialog = false">取 消</el-button>
                <el-button type="primary" @click="updateBasic">确 定</el-button>
            </div>
        </el-dialog>

        <el-dialog title="修改员工审核密码" :visible.sync="updateAuditPasswordDialog">
            <el-form>
                <el-form-item label="审核密码">
                    <el-input type="password" v-model="auditPassword" autocomplete="off"></el-input>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="updateAuditPasswordDialog = false">取 消</el-button>
                <el-button type="primary" @click="updateAuditPassword">确 定</el-button>
            </div>
        </el-dialog>

        <el-dialog title="修改员工登录密码" :visible.sync="updatePasswordDialog">
            <el-form>
                <el-form-item label="登录密码">
                    <el-input type="password" v-model="currentRow.password" autocomplete="off"></el-input>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="updatePasswordDialog = false">取 消</el-button>
                <el-button type="primary" @click="updatePassword">确 定</el-button>
            </div>
        </el-dialog>
        <el-dialog title="修改电子签名" :visible.sync="uploadSignatureDialog">
            <el-form>
                <el-form-item>
                    <my-input-file ref="sig"></my-input-file>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="uploadSignatureDialog = false">取 消</el-button>
                <el-button type="primary" @click="uploadSignature">确 定</el-button>
            </div>
        </el-dialog>
        <el-dialog title="修改角色信息" :visible.sync="updateRolesDialog">
            <el-form>
                <el-select v-model="selectedRoleIds" multiple placeholder="请选择">
                    <el-option
                            v-for="item in roles"
                            :key="item.id"
                            :label="item.roleName"
                            :value="item.id">
                    </el-option>
                </el-select>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="updateRolesDialog = false">取 消</el-button>
                <el-button type="primary" @click="updateRoles">确 定</el-button>
            </div>
        </el-dialog>
    </div>

</template>

<script>
    import { getAllUserInfo,updateBasicInformation,updateAuditPassword,updatePassword,uploadSig,getRoleInfo,updateRoles,addUser } from '../../api2/auth/system';
    import MyInputFile from '../../components/common/MyInputFile';

    export default {
        name: 'UserAdmin',
        components: { MyInputFile },
        data() {
            return {
                newRowDialog: false,
                updatePasswordDialog: false,
                updateAuditPasswordDialog: false,
                uploadSignatureDialog: false,
                auditPassword: null,
                updateBasicDialog: false,
                tableData: [],
                loading: false,
                stamp: new Date().getTime(),
                //需要给分页组件传的信息
                paginations: {
                    total: 0,        // 总数
                    pageIndex: 1,  // 当前位于哪页
                    pageSize: 10,   // 1页显示多少条
                    pageSizes: [3, 5, 10, 20],  //每页显示多少条
                    layout: 'total, sizes, prev, pager, next, jumper'   // 翻页属性
                },

                searchParams: {
                    staffId: null,
                    phone: null,
                    staffName: null
                },
                currentRow: {
                    staffId : null,
                    staffName: null,
                    phone: null
                },
                roles: [],
                selectedRoleIds: [],
                updateRolesDialog: false,
                newRow: {

                }
            };
        },
        created() {
            this.getAll();
        },
        methods: {
            buttonIsShow(perm){
                return this.$store.getters.getButton.findIndex(item=>item.resourcePerm == perm) != -1
            },
            getAll() {
                this.loading = true;
                let sea = {}
                sea.pageNum = this.paginations.pageIndex
                sea.size= this.paginations.pageSize
                sea.staffName = this.searchParams.staffName != null ?"%" + this.searchParams.staffName + "%" : null
                sea.staffId = this.searchParams.staffId != null ?"%" + this.searchParams.staffId + "%" : null
                sea.phone = this.searchParams.phone != null ?"%" + this.searchParams.phone + "%" : null

                this.stamp = new Date()
                getAllUserInfo(sea).then(res => {
                    this.tableData = res.data.list;
                    this.paginations.total = res.data.total;
                    this.paginations.pageIndex = res.data.pageNum;
                    this.loading = false;
                });
            },
            handleCurrentChange(page) {
                this.paginations.pageIndex = page;
                this.getAll();
            },
            handleSizeChange(pageSize) {
                this.paginations.pageSize = pageSize;
                this.getAll();
            },
            updateBasic(){
                updateBasicInformation(this.currentRow).then(res=>{
                    this.$message.success("更新成功")
                    this.updateBasicDialog = false
                    this.getAll()
                    this.currentRow = {}
                })
            },
            updateBasicDialogOpen(row){
                this.updateBasicDialog = true
                this.currentRow = row
            },
            updateAuditPasswordDialogOpen(row){
                this.updateAuditPasswordDialog = true
                this.currentRow = row
            },
            updateAuditPassword(){
                updateAuditPassword(this.currentRow.id, this.auditPassword).then(res=>{
                    this.$message.success("修改成功！")
                    this.currentRow = {}
                    this.updateAuditPasswordDialog = false
                })
            },
            updatePasswordOpen(row){
                this.updatePasswordDialog = true
                this.currentRow = row
            },
            updatePassword(){
                updatePassword(this.currentRow.id, this.currentRow.password).then(res=>{
                    this.$message.success("修改成功")
                    this.currentRow = {}
                    this.updatePasswordDialog = false
                })
            },
            uploadSignatureDialogOpen(row){
                this.uploadSignatureDialog = true
                this.currentRow = row
            },
            uploadSignature(){
                console.log(this.$refs.sig.file);
                console.log(this.currentRow.id);
                uploadSig(this.currentRow.id, this.$refs.sig.file).then(res=>{
                    this.$message.success("上传成功！")
                    this.uploadSignatureDialog = false
                    this.stamp = new Date().getTime()
                })
            },
            updateRolesOpen(row){
                this.currentRow = row
                getRoleInfo(row.id).then(res=>{
                    this.roles = res.data.roles
                    this.selectedRoleIds = res.data.selectedRoleIds
                    this.updateRolesDialog = true;
                })
            },
            updateRoles(){
                updateRoles(this.currentRow.id,this.selectedRoleIds.join(",")).then(res=>{
                    this.$message.success("修改成功！")
                    this.getAll();
                    this.updateRolesDialog = false;
                    this.roles = []
                    this.selectedRoleIds = []
                })
            },
            addNew(){
                addUser(this.newRow).then(res=>{
                    this.$alert('新账户为：' + res.data, '账户信息', {
                        confirmButtonText: "确认",
                        callback: action => {
                            this.newRowDialog = false
                            this.newRow = {}
                           this.getAll()

                        }
                    });
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
</style>
