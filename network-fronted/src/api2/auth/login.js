
import request from "../index"

/**
 *通过手机号和密码登录，并返回token
 * @param phone
 * @param password
 * @returns {AxiosPromise}
 */
export function login(phone, password) {
    console.log(request);
    return request.request({
        url: "/weifei/auth/login",
        method: "post",
        params: {
            phone,password
        }
    })
}


/**
 * 根据自己的token，获取权限信息
 * @param token
 */
export function getPerms(token) {
    return request.request({
        url: "/weifei/auth/getPerms",
        method: "post",
        params: {
            token
        }
    })
}
// export function getPerms(token) {
//     return axios.create({
//         timeout: 5000,
//         baseURL: "api",
//         url: "/weifei/auth/getPerms",
//         method: "post",
//         params: {
//             token
//         }
//     })()
// }

