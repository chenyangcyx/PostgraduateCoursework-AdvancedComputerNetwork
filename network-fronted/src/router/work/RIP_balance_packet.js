export const RIP_balance_packet= [

    {
        path: "/network/work/RIP_balance_packet_RA",
        meta: {
            title: 'packet_RA',
        },
        component: () => import("../../pages/work/RIP_balance_packet/RIP_balance_packet_RA")
    },
    {
        path: "/network/work/RIP_balance_packet_RB",
        meta: {
            title: 'packet_RB',
        },
        component: () => import("../../pages/work/RIP_balance_packet/RIP_balance_packet_RB")
    },
    {
        path: "/network/work/RIP_balance_packet_RC",
        meta: {
            title: 'packet_RC',
        },
        component: () => import("../../pages/work/RIP_balance_packet/RIP_balance_packet_RC")
    },

]

export const RIP_balance_packet_slider = {
    icon: 'el-icon-s-tools',
    index:"/network/work/RIP_balance_packet_RA",
    title: 'RIP_balance_packet',
    myIcon: "icons/perm/xiTong.png",
    subs: [
        {
            index: "/network/work/RIP_balance_packet_RA",
            title: "RIP_balance_packet_RA",
            myIcon: "icons/perm/yongHu.png",
        },
        {
            index: "/network/work/RIP_balance_packet_RB",
            title: "RIP_balance_packet_RB",
            myIcon: "icons/perm/yongHu.png",
        },
        {
            index: "/network/work/RIP_balance_packet_RC",
            title: "RIP_balance_packet_RC",
            myIcon: "icons/perm/yongHu.png",
        },
    ]
}
