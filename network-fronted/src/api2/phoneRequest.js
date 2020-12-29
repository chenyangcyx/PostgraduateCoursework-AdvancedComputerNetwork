import axios from "axios"
import router from '../router';
import { Message } from "element-ui";

const request = axios.create()
request.defaults.baseURL = "/api"
request.defaults.timeout = 5000

request.interceptors.request.use(res=>{
    res.headers.token = localStorage.getItem("weifei-token") || ''
    return res;
})
request.interceptors.response.use(
    response => {
        if(response.data.code == 200)
            return response.data
        else{
            Message({
                message: response.data.message,
                type: "error",
            })
            return Promise.reject('error')
        }
    },
    error => {
        console.log(error);
        console.log(11111);
        if(error.response && (error.response.status === 401 || error.response.status == 403) ){ //登录信息失效
            Message({
                message: "登录信息失效，请重新登录1111",
                type: "error",
            })
            router.push("/phone/login")
        }
    }
)
export default request;
