const http = require('http');
http.createServer(function (request, response) {
    // 发送 HTTP 头部
    // HTTP 状态值: 200 : OK
    // 内容类型: text/plain
    // response.writeHead(200, {'Content-Type': 'application/json'});
    // // 发送响应数据 "Hello World"
    // response.end('["a","b","c","d"]');

    let path = request.url;
    console.log(path);
    if(path.indexOf("executeOneCommandInLinux") !== -1){
        let data = {
            "original_result":
                [
                    "message1",
                    "message2"
                ],
            "handle_result":
                [
                    "message1",
                    "message2"
                ]
        }
        response.writeHead(200, {'Content-Type': 'application/json'});
        response.end(JSON.stringify(data));
        // response.
    }

}).listen(8888);
// 终端打印如下信息
console.log('Server running at http://127.0.0.1:8888/');
