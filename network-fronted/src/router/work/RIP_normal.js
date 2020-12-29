export const RIP_normal= [
    {
        path: "/network/work/RIP_normal_RA",
        meta: {
            title: 'normal_RA',
        },
        component: () => import("../../pages/work/RIP_normal/RIP_normal_RA")
    },
    {
        path: "/network/work/RIP_normal_RB",
        meta: {
            title: 'normal_RB',
        },
        component: () => import("../../pages/work/RIP_normal/RIP_normal_RB")
    },
    {
        path: "/network/work/RIP_normal_RC",
        meta: {
            title: 'normal_RC',
        },
        component: () => import("../../pages/work/RIP_normal/RIP_normal_RC")
    },
]

export const RIP_normal_slider = {
    icon: 'el-icon-s-tools',
    index:"/network/work/RIP_normal_RA",
    title: 'RIP_normal',
    myIcon: "icons/perm/xiTong.png",
    subs: [
        {
            index: "/network/work/RIP_normal_RA",
            title: "RIP_normal_RA",
            myIcon: "icons/perm/yongHu.png",
        },
        {
            index: "/network/work/RIP_normal_RB",
            title: "RIP_normal_RB",
            myIcon: "icons/perm/yongHu.png",
        },
        {
            index: "/network/work/RIP_normal_RC",
            title: "RIP_normal_RC",
            myIcon: "icons/perm/yongHu.png",
        },
    ]
}
