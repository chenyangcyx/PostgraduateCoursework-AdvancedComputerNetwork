import Vue from 'vue';
import Router from 'vue-router';
import {originChildren} from "./originChildren";
import {work} from '@/router/work/work';
import {RIP_normal} from "@/router/work/RIP_normal";
import {RIP_balance_route} from "@/router/work/RIP_balance_route";
import {RIP_balance_packet} from "@/router/work/RIP_balance_packet";

Vue.use(Router);

originChildren.push(...work);
originChildren.push(...RIP_normal)
originChildren.push(...RIP_balance_packet)
originChildren.push(...RIP_balance_route)



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
