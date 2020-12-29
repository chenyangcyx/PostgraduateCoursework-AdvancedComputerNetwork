<template>
    <div>
        <el-card>
            <el-table
                    :data="tableData"
                    style="width: 100%;margin-bottom: 20px;"
                    row-key="id"
                    border
                    default-expand-all
                    :tree-props="{children: 'children'}">
                <el-table-column
                        prop="resourceName"
                        label="资源名称">
                </el-table-column>
                <el-table-column
                        prop="resourcePerm"
                        label="资源标识">
                </el-table-column>
                <el-table-column
                        label="资源类型">
                    <template slot-scope="scope">
                        {{scope.row.resourceType == 1 ? "菜单" : "按钮"}}
                    </template>
                </el-table-column>
            </el-table>


        </el-card>
    </div>
</template>

<script>
    export default {
        name: 'ResourceAdmin',
        data(){
          return {
              tableData: []
          }
        },
        created() {
            if(this.$store.getters.getMenuTree){
                this.tableData = this.$store.getters.getMenuTree
            }
        }
    };
</script>

<style scoped>

</style>
