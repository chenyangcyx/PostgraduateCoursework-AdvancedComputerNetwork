<template>
  <div class="sidebar">
    <el-menu
        class="sidebar-el-menu"
        :default-active="onRoutes"
        :collapse="collapse"
        background-color="#324157"

        text-color="#BFCBD9"
        active-text-color="#ffd04b"
        unique-opened
        router
    >
      <template v-for="item in items">
        <template v-if="item.subs">
          <el-submenu  :index="item.index" :key="item.index">
            <template slot="title">
              <!--                            <i :class="item.icon"></i>-->
              <img v-if="item.myIcon != null"
                   width="20px" height="18px"
                   style="display: inline-block;margin-right: 5px;"
                   :src="require('../../assets/' + item.myIcon)" alt="">
              <span slot="title">{{ item.title }}</span>
            </template>
            <template  v-for="subItem in item.subs">
              <el-menu-item
                  :index="subItem.index"
                  :key="subItem.index"


              >
                <div :id="subItem.index" ref="aaa" class="aaa" @click="changeColor">
                  <img v-if="subItem.myIcon != null"
                       width="20px" height="18px"
                       style="display: inline-block;margin-right: 5px;"
                       :src="require('../../assets/' + subItem.myIcon)" alt="">
                  {{ subItem.title }}
                </div>
              </el-menu-item>
            </template>
          </el-submenu>
        </template>
        <template v-else>
          <el-menu-item :index="item.index" :key="item.index">
            <img v-if="item.myIcon != null"
                 width="20px" height="18px"
                 style="display: inline-block;margin-right: 5px;mix-blend-mode: difference; "
                 :src="require('../../assets/' + item.myIcon)" alt="">
            <span slot="title">{{ item.title }}</span>
          </el-menu-item>
        </template>
      </template>
    </el-menu>
  </div>
</template>

<script>
import bus from '../common/bus';
import {RIP_slider} from "@/router/work/RIP";
import {OSPF_slider} from "@/router/work/OSPF";

export default {
  data() {
    return {
      collapse: false,
      items: [

        {
          icon: 'el-icon-lx-home',
          index: '/network/RouterConfig',
          title: '路由器配置',
          myIcon: "icons/perm/quanXian.png",
        },
        RIP_slider,
        OSPF_slider,
        {
          icon: 'el-icon-lx-home',
          index: '/network/perm/topu',
          title: '拓扑图',
          myIcon: "icons/perm/quanXian.png",
        },
        // {
        //   icon: 'el-icon-lx-home',
        //   index: '/network/perm/list',
        //   title: '命令解释',
        //   myIcon: "icons/perm/jueSe.png",
        // },
      ],
      myMenu: [],
    };
  },
  computed: {
    onRoutes() {
      return this.$route.path.replace('/', '');
    }
  },
  created() {
    // 通过 Event Bus 进行组件间通信，来折叠侧边栏
    bus.$on('collapse', msg => {
      this.collapse = msg;
      bus.$emit('collapse-content', msg);
    });
  },
  methods: {

    changeColor(event) {
      this.$refs.aaa.forEach(item => item.style['color'] = "#BFCBD9")
      event.target.style['color'] = "#20A0FF";
      console.log(event);
      // background-color="#324157"
      // active-text-color="#ffd04b"
    }
  }
};
</script>

<style scoped>
.sidebar {
  display: block;
  position: absolute;
  left: 0;
  top: 70px;
  bottom: 0;
  overflow-y: scroll;
}

.sidebar::-webkit-scrollbar {
  width: 0;
}

.sidebar-el-menu:not(.el-menu--collapse) {
  width: 250px;
}

.sidebar > ul {
  height: 100%;
}
</style>
