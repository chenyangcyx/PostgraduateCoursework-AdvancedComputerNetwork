export const RIP_balance_route= [

    {
        path: "/network/work/RIP_balance_route_RA",
        meta: {
            title: 'OSPF_RA',
        },
        component: () => import("../../pages/work/RIP_balance_route/RIP_balance_route_RA")
    },
    {
        path: "/network/work/RIP_balance_route_RB",
        meta: {
            title: 'OSPF_RB',
        },
        component: () => import("../../pages/work/RIP_balance_route/RIP_balance_route_RB")
    },
    {
        path: "/network/work/RIP_balance_route_RC",
        meta: {
            title: 'OSPF_RC',
        },
        component: () => import("../../pages/work/RIP_balance_route/RIP_balance_route_RC")
    }


]

export const RIP_balance_route_slider = {
    icon: 'el-icon-s-tools',
    index:"/network/work/RIP_balance_route_RA",
    title: 'OSPF',
    myIcon: "icons/perm/xiTong.png",
    subs: [
        {
            index: "/network/work/RIP_balance_route_RA",
            title: "OSPF_RA",
            myIcon: "icons/perm/yongHu.png",
        },
        {
            index: "/network/work/RIP_balance_route_RB",
            title: "OSPF_RB",
            myIcon: "icons/perm/yongHu.png",
        },
        {
            index: "/network/work/RIP_balance_route_RC",
            title: "OSPF_RC",
            myIcon: "icons/perm/yongHu.png",
        }
    ]
}
