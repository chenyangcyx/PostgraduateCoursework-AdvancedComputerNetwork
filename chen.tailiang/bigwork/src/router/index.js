import Vue from 'vue';
import Router from 'vue-router';
import {originChildren} from "./originChildren";
import {weifei_perms} from './weifei/perms';
import {work} from '@/router/work/work';

Vue.use(Router);
originChildren.push(...weifei_perms)

originChildren.push(...work);




export default new Router({
    routes: [
        {
            path: '/',
            redirect: '/login'
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
