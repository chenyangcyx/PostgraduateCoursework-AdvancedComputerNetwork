export const work= [
    {
        path: "/network/perm/Command",
        meta: {
            title: '远程命令行',
        },
        component: () => import("../../pages/work/Command")
    }
]

export const work_slider = {
    icon: 'el-icon-s-tools',
    index:"/network/perm/Command",
    title: '计网作业',
    myIcon: "icons/perm/xiTong.png",
    subs: [
        {
            index: "/network/perm/Command",
            title: "远程命令行",
            myIcon: "icons/perm/yongHu.png",
        }
    ]
}
