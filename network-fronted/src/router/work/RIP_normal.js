export const RIP_normal= [
    {
        path: "/network/work/RIP_normal_RA",
        meta: {
            title: 'RIP_RA',
        },
        component: () => import("../../pages/work/RIP_normal/RIP_normal_RA")
    },
    {
        path: "/network/work/RIP_normal_RB",
        meta: {
            title: 'RIP_RB',
        },
        component: () => import("../../pages/work/RIP_normal/RIP_normal_RB")
    },
    {
        path: "/network/work/RIP_normal_RC",
        meta: {
            title: 'RIP_RC',
        },
        component: () => import("../../pages/work/RIP_normal/RIP_normal_RC")
    },
]

export const RIP_normal_slider = {
    icon: 'el-icon-s-tools',
    index:"/network/work/RIP_normal_RA",
    title: 'RIP',
    myIcon: "icons/perm/xiTong.png",
    subs: [
        {
            index: "/network/work/RIP_normal_RA",
            title: "RIP_RA",
            myIcon: "icons/perm/yongHu.png",
        },
        {
            index: "/network/work/RIP_normal_RB",
            title: "RIP_RB",
            myIcon: "icons/perm/yongHu.png",
        },
        {
            index: "/network/work/RIP_normal_RC",
            title: "RIP_RC",
            myIcon: "icons/perm/yongHu.png",
        },
    ]
}
