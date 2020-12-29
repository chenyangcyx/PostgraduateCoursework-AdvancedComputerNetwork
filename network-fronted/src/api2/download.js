import axios from "axios"


/**
 * 通过axios获取文件
* @type {AxiosInstance}
 */
const download = axios.create()
download.defaults.baseURL = "/api"

download.interceptors.request.use(res=>{
    res.headers.token = localStorage.getItem("weifei-token") || ''
    return res;
})

/**
 * 通过axios获取文件
 * @param url
 * @param resOpts {type="get",data=''}
 */
const getFile = function(url, resOpts = {}) {
    const { type = 'get', params = '', data='' } = resOpts
    const queryArgs = {
        url,
        method: type,
        params,
        data,
        headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json; charset=utf-8',
            withCredentials: true,
        },
        responseType: "blob"
    }
    // tips: 这里直接返回的是response整体!
    // const response = download.request(queryArgs).catch(err => console.log(err))


    download.request(queryArgs).then(res=>{
        // console.log(res);
        const response = res;
        console.log(response.headers['content-disposition']);
        let a = /filename=(.*)/i
        const fileName = response.headers['content-disposition'].match(
            a
        )[1]
        // console.log(fileName);
        // 将二进制流转为blob
        const blob = new Blob([response.data], { type: 'application/octet-stream' })
        if (typeof window.navigator.msSaveBlob !== 'undefined') {
            // 兼容IE，window.navigator.msSaveBlob：以本地方式保存文件
            window.navigator.msSaveBlob(blob, decodeURI(fileName))
        } else {
            // 创建新的URL并指向File对象或者Blob对象的地址
            const blobURL = window.URL.createObjectURL(blob)
            // 创建a标签，用于跳转至下载链接
            const tempLink = document.createElement('a')
            tempLink.style.display = 'none'
            tempLink.href = blobURL
            tempLink.setAttribute('download', decodeURI(fileName))
            // 兼容：某些浏览器不支持HTML5的download属性
            if (typeof tempLink.download === 'undefined') {
                tempLink.setAttribute('target', '_blank')
            }
            // 挂载a标签
            document.body.appendChild(tempLink)
            tempLink.click()
            document.body.removeChild(tempLink)
            // 释放blob URL地址
            window.URL.revokeObjectURL(blobURL)
        }
    })




}
export default getFile


