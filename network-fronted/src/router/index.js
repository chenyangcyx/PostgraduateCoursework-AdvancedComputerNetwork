import Vue from 'vue';
import Router from 'vue-router';
import {originChildren} from "./originChildren";
import {work} from '@/router/work/work';
import {RIP} from "@/router/work/RIP";
import {OSPF} from "@/router/work/OSPF";

Vue.use(Router);

originChildren.push(...work);
originChildren.push(...RIP)
originChildren.push(...OSPF)



export default new Router({
    routes: [
        {
            path: '/',
            redirect: '/network/perm/topu'
        },

        {
            path: '/',
            component: () => import(/* webpackChunkName: "home" */ '../components/common/Home.vue'),
            meta: { title: '自述文件' },
            children:originChildren
        },
        {
            path: '/login',
            component: () => import(/* webpackChunkName: "login" */ '../pages/Login'),
            meta: { title: '登录' }
        },
        {
            path: '*',
            redirect: '/404'
        },
    ]
});
