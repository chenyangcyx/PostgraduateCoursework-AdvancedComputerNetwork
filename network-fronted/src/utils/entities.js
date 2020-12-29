export default {
    riskCharacters: [
        {
            label: "爆炸性",
            value: "baozhaxing"
        },
        {
            label: "有毒",
            value: "youdu"
        },
        {
            label: "易燃",
            value: "yiran"
        },
        {
            label: "有害",
            value: "youhai"
        },
        {
            label: "腐蚀性",
            value: "fushixing"
        },
        {
            label: "石棉",
            value: "shimian"
        },
        {
            label: "刺激性",
            value: "cijixing"
        },
        {
            label: "助燃",
            value: "zhuran"
        },
    ],
    applicationStatus: ['已登记', '已接受', '备份样品已接受', '已指定化验项目', '已完成','已审核'],
    samplingRecordIsSecond: [
        {
            value: 0,
            label: "初检"
        },
        {
            value: 1,
            label: "复检"
        }
    ],
    inventoryStatus: [
        {
            value: 0,
            label: "已创建"
        },{
            value: 1,
            label: "已检测"
        },{
            value: 2,
            label: "已入库"
        },
        {
            value: 3,
            label: "已出库"
        },{
            value: 4,
            label: "已处理"
        },{
            value: -1,
            label: "检测未通过"
        }
    ]
}
