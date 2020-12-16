import axios from "axios"

const img = axios.create()
img.defaults.baseURL = "/api"

img.interceptors.request.use(res=>{
    res.headers.token = localStorage.getItem("weifei-token") || ''
    return res;
})
const getImg  = async function(url, params,img) {
    let res = await img.get(
        url,
        {
            //设定接收类型为blob,头部什么的自行添加
            params,
            responseType:'blob',
        }
    );
    let resUrl = window.URL.createObjectURL(res.data)
    if(img != null)
        img.setAttribute("src", res.data);
    console.log(resUrl);
    return resUrl;
};

export default getImg