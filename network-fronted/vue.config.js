module.exports = {
    baseUrl: './',
    assetsDir: 'static',
    productionSourceMap: false,
    // https:{
    //     client_max_body_size : "100MB"
    // },
    devServer: {
        disableHostCheck: true,
        host: "0.0.0.0",
        port: 22222, // 端口号
        https: false, // https:{type:Boolean}
        open: true, //配置自动启动浏览器
        // 配置多个代理
        proxy: {
            "/api": {
                target: "http://localhost:8000",
                // target: "http://101.132.103.184:9999",
                ws: true,// 是否启用websockets

                changeOrigin: true, //开启代理：在本地会创建一个虚拟服务端，然后发送请求的数据，并同时接收请求的数据，这样服务端和服务端进行数据的交互就不会有跨域问题
                pathRewrite: {
                    '^/api': '' //这里理解成用'/api'代替target里面的地址,如我要调用'http://40.00.100.100:3002/user/add'，直接写'/api/user/add'即可
                }
            },
            "/foo": {
                target: "<other_url>"
            }
        }
    },

}
