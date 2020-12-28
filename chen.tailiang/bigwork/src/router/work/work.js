export const work= [
    {
        path: "/network/perm/Command",
        meta: {
            title: '远程命令行',
        },
        component: () => import("../../pages/work/Command")
    },
    {
        path: "/network/perm/topu",
        meta: {
            title: '拓扑图',
        },
        component: () => import("../../pages/work/Topu")
    },
    {
        path: "/network/perm/list",
        meta: {
            title: '命令解释',
        },
        component: () => import("../../pages/work/list")
    },
]

export const work_slider = {
    icon: 'el-icon-s-tools',
    index:"/network/perm/Command",
    title: '路由配置',
    myIcon: "icons/perm/xiTong.png",
    subs: [
        {
            index: "/network/perm/Command",
            title: "远程命令行",
            myIcon: "icons/perm/yongHu.png",
        }
    ]
}
