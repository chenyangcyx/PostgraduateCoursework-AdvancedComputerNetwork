export const OSPF= [

    {
        path: "/network/work/OSPF_RA",
        meta: {
            title: 'OSPF_RA',
        },
        component: () => import("../../pages/work/OSPF/OSPF_RA")
    },
    {
        path: "/network/work/OSPF_RB",
        meta: {
            title: 'OSPF_RB',
        },
        component: () => import("../../pages/work/OSPF/OSPF_RB")
    },
    {
        path: "/network/work/OSPF_RC",
        meta: {
            title: 'OSPF_RC',
        },
        component: () => import("../../pages/work/OSPF/OSPF_RC")
    }


]

export const OSPF_slider = {
    icon: 'el-icon-s-tools',
    index:"/network/work/OSPF_RA",
    title: 'OSPF',
    myIcon: "icons/perm/xiTong.png",
    subs: [
        {
            index: "/network/work/OSPF_RA",
            title: "OSPF_RA",
            myIcon: "icons/perm/yongHu.png",
        },
        {
            index: "/network/work/OSPF_RB",
            title: "OSPF_RB",
            myIcon: "icons/perm/yongHu.png",
        },
        {
            index: "/network/work/OSPF_RC",
            title: "OSPF_RC",
            myIcon: "icons/perm/yongHu.png",
        }
    ]
}
