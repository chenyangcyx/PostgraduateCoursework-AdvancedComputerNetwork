export const weifei_perms= [
    {
        path: "/weifei/perm/UserAdmin",
        meta: {
            title: '用户管理',
        },
        component: () => import("../../pages/perm/UserAdmin")
    },{
        path: "/weifei/perm/RoleAdmin",
        meta: {
            title: '角色管理',
        },
        component: () => import("../../pages/perm/RoleAdmin")
    },{
        path: "/weifei/perm/ResourceAdmin",
        meta: {
            title: '资源管理',
        },
        component: () => import("../../pages/perm/ResourceAdmin")
    },
    {
        path: "/weifei/perm/CheckAllNotice",
        meta: {
            title: '所有通知',
        },
        component: () => import("../../pages/perm/CheckAllNotice")
    }
]

export const weifei_perms_slider = {
    icon: 'el-icon-s-tools',
    index:"/weifei/perm/UserAdmin",
    title: '系统管理',
    myIcon: "icons/perm/xiTong.png",
    subs: [
        {
            index: "/weifei/perm/UserAdmin",
            title: "用户管理",
            myIcon: "icons/perm/yongHu.png",
        },{
            index: "/weifei/perm/RoleAdmin",
            title: "角色管理",
            myIcon: "icons/perm/jueSe.png",
        },{
            index: "/weifei/perm/ResourceAdmin",
            title: "资源管理",
            myIcon: "icons/perm/quanXian.png",
        },{
            index: "/weifei/perm/CheckAllNotice",
            title: "通知管理",
            myIcon: "icons/perm/tongZhi.png",
        },
    ]
}
