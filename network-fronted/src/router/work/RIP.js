export const RIP= [
    {
        path: "/network/work/RIP_RA",
        meta: {
            title: 'RIP_RA',
        },
        component: () => import("../../pages/work/RIP/RIP_RA")
    },
    {
        path: "/network/work/RIP_RB",
        meta: {
            title: 'RIP_RB',
        },
        component: () => import("../../pages/work/RIP/RIP_RB")
    },
    {
        path: "/network/work/RIP_RC",
        meta: {
            title: 'RIP_RC',
        },
        component: () => import("../../pages/work/RIP/RIP_RC")
    },
]

export const RIP_slider = {
    icon: 'el-icon-s-tools',
    index:"/network/work/RIP_RA",
    title: 'RIP',
    myIcon: "icons/perm/xiTong.png",
    subs: [
        {
            index: "/network/work/RIP_RA",
            title: "RIP_RA",
            myIcon: "icons/perm/yongHu.png",
        },
        {
            index: "/network/work/RIP_RB",
            title: "RIP_RB",
            myIcon: "icons/perm/yongHu.png",
        },
        {
            index: "/network/work/RIP_RC",
            title: "RIP_RC",
            myIcon: "icons/perm/yongHu.png",
        },
    ]
}
