export const originChildren = [
    {
        path: '/dashboard',
        component: () => import(/* webpackChunkName: "dashboard" */ '../components/page/Dashboard.vue'),
        meta: { title: '系统首页' }
    },
]
