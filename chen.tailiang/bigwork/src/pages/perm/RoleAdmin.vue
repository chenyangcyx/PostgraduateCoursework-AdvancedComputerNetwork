<template>
    <div>
        <!-- 卡片视图 -->
        <el-card>
            <!-- 添加角色按钮区域 -->
            <el-row style="margin-bottom: 5px">
                <el-col>
                    <el-button v-if="buttonIsShow('system-manage:role:addRole')" @click="addDialog = true"  type="primary">添加角色</el-button>
                </el-col>
            </el-row>

            <!-- 角色列表区域 -->
            <el-table  :data="rolelist" border stripe>
                <!-- 展开列 -->
              <el-table-column
                  label="序号"
                  type="index"
                  width="50"
                  align='center'>
              </el-table-column>

              <el-table-column label="详情" type="expand">
                    <template slot-scope="scope">
                        <el-row :class="['bdbottom', i1 === 0 ? 'bdtop' : '', 'vcenter']" v-if="isShow(scope.row.perms, item1.resourcePerm)"  v-for="(item1, i1) in $store.getters.getMenuTree" :key="item1.id">
                            <!-- 渲染一级权限 -->
                            <el-col :span="5">
                                <el-tag>{{item1.resourceName}}</el-tag>
                                <i class="el-icon-caret-right"></i>
                            </el-col>
                            <!-- 渲染二级和三级权限 -->
                            <el-col :span="19">
                                <!-- 通过 for 循环 嵌套渲染二级权限 -->
                                <el-row :class="[i2 === 0 ? '' : 'bdtop', 'vcenter']" v-if="isShow(scope.row.perms, item2.resourcePerm)"  v-for="(item2, i2) in item1.children" :key="item2.id">
                                    <el-col :span="6">
                                        <el-tag type="success">{{item2.resourceName}}</el-tag>
                                        <i class="el-icon-caret-right"></i>
                                    </el-col>
                                    <el-col :span="18">
                                        <el-tag type="warning" v-for="item3 in item2.children" v-if="isShow(scope.row.perms, item3.resourcePerm)" :key="item3.id">{{item3.resourceName}}</el-tag>
                                    </el-col>
                                </el-row>
                            </el-col>
                        </el-row>
                    </template>
                </el-table-column>
                <!-- 索引列 -->
<!--                <el-table-column type="index"></el-table-column>-->
                <el-table-column label="角色名称" prop="roleName"></el-table-column>
                <el-table-column label="角色描述" prop="desc"></el-table-column>
                <el-table-column v-if="buttonIsShow('system-manage:role:updateRole') || buttonIsShow('system-manage:role:resource:updateRoleResource') " label="操作" width="300px">
                    <template slot-scope="scope">
                        <el-button v-if="buttonIsShow('system-manage:role:updateRole')"  size="mini" type="primary" @click="updateDialogOpen(scope.row)"  icon="el-icon-edit">编辑</el-button>
                        <el-button size="mini" v-if="buttonIsShow('system-manage:role:resource:updateRoleResource')" type="warning" icon="el-icon-setting" @click="showSetRightDialog(scope.row)">分配权限</el-button>
                    </template>
                </el-table-column>
            </el-table>
        </el-card>

        <!-- 分配权限的对话框 -->
        <el-dialog title="分配权限" :visible.sync="setRightDialogVisible" destroy-on-close width="50%" @close="setRightDialogClosed">
            <!-- 树形控件 -->
            <el-tree :data="$store.getters.getMenuTree"
                     :props="treeProps"
                     :show-checkbox="true"
                     node-key="id"
                     default-expand-all
                     :default-checked-keys="defKeys"
                     ref="treeRef"></el-tree>
            <span slot="footer" class="dialog-footer">
        <el-button @click="setRightDialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="allotRights">确 定</el-button>
      </span>
        </el-dialog>


        <el-dialog title="添加新的角色" :visible.sync="addDialog">
            <el-form :model="newRow">
                <el-form-item label="角色名称">
                    <el-input v-model="newRow.roleName" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="角色描述">
                    <el-input v-model="newRow.desc" autocomplete="off"></el-input>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="addDialog = false">取 消</el-button>
                <el-button type="primary" @click="addNew">确 定</el-button>
            </div>
        </el-dialog>

        <el-dialog title="更新角色" :visible.sync="updateDialog">
            <el-form :model="currentRow">
                <el-form-item label="角色名称">
                    <el-input v-model="currentRow.roleName" autocomplete="off"></el-input>
                </el-form-item>
                <el-form-item label="角色描述">
                    <el-input v-model="currentRow.desc" autocomplete="off"></el-input>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click="updateDialog = false">取 消</el-button>
                <el-button type="primary" @click="updateCurrent">确 定</el-button>
            </div>
        </el-dialog>
    </div>
</template>

<script>
    import {listRole,updateRoleResource,addRole,updateRole} from '../../api2/auth/system';

    export default {
        name: 'RoleAdmin',
        data() {
            return {
                // 所有角色列表数据
                rolelist: [],
                // 控制分配权限对话框的显示与隐藏
                setRightDialogVisible: false,
                // 树形控件的属性绑定对象
                treeProps: {
                    label: 'resourceName',
                    children: 'children'
                },
                // 默认选中的节点Id值数组
                defKeys: [],
                // 当前即将分配权限的角色id
                roleId: '',
                currentRow: {},
                newRow: {},
                addDialog: false,
                updateDialog: false,
              // data: {}
            }
        },
        created() {
            this.getRolesList();
        },
        methods: {
            buttonIsShow(perm){
                return this.$store.getters.getButton.findIndex(item=>item.resourcePerm == perm) != -1
            },
            isShow(myPerms, perms){
                return myPerms.findIndex(item=>item.resourcePerm == perms) != -1
            },
            // 获取所有角色的列表
            getRolesList() {
               listRole().then(res=>{
                   let data = res.data;
                   for(let data of res.data){
                       if(data.resourceIdList != null){
                           console.log(data.resourceIdList);
                           // console.log(this.$store.getters.getMenu);
                           data.perms = this.$store.getters.getMenu.filter(item=>{
                               return item.resourceType != null && data.resourceIdList.indexOf(item.id) != -1
                           })
                       }
                   }
                   this.rolelist = res.data
               })
            },
            // 展示分配权限的对话框
            showSetRightDialog(role) {
                this.currentRow = role
                this.setRightDialogVisible = true
                // this.defKeys = role.resourceIdList.length == 0 ? [] : role.resourceIdList
                let res = role.resourceIdList.filter(item =>{
                    return this.$store.getters.getMenu.findIndex(e => e.resourceType != null && e.resourceType == 2 &&   e.id == item) != -1
                })


                this.defKeys = res
            },

            // 监听分配权限对话框的关闭事件
            setRightDialogClosed() {
                this.defKeys = []
            },
            // 点击为角色分配权限
            allotRights() {
                let selectedNode = this.$refs.treeRef.getCheckedNodes(false, true)
                // console.log(this.$refs.treeRef.getCheckedNodes(false, true));
                let resourceIdList = []
                if(selectedNode != null && selectedNode.length > 0){
                    resourceIdList = selectedNode.map(item => item.id)
                }
                let data ={resourceIdList, roleId: this.currentRow.id}
                console.log(data);
                updateRoleResource(data).then(res=>{
                    this.$message.success("更新成功")
                    this.getRolesList();
                    this.setRightDialogVisible = false
                    this.currentRow = {}
                })
            },
            addNew(){
                addRole(this.newRow).then(res=>{
                    this.newRow = {}
                    this.$message.success("添加成功！")
                    this.addDialog = false
                    this.getRolesList();
                })
            },
            updateDialogOpen(row){
                this.currentRow = { id: row.id, roleName: row.roleName, desc: row.desc }
                this.updateDialog = true
            },
            updateCurrent(){
                updateRole(this.currentRow).then(res=>{
                    this.$message.success("更新成功！")
                    this.updateDialog = false
                    this.currentRow = {}
                    this.getRolesList();
                })
            }
        }
    };
</script>

<style scoped>
    .el-tag {
        margin: 7px;
    }

    .bdtop {
        border-top: 1px solid #eee;
    }

    .bdbottom {
        border-bottom: 1px solid #eee;
    }

    .vcenter {
        display: flex;
        align-items: center;
    }
</style>
