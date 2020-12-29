import request from '../index';

/**
 *
 * @param account 员工号
 * @param password 密码
 * @returns {AxiosPromise<any>}
 */
export function login(account, password) {
    return request.request({
        method: "post",
        url: "/system-manage/login",
        params: {account, password}
    })
}

/**
 * 重新加载个人信息
 * @return
 */
export function reloadPersonalInformation(account) {
    return request.get("/system-manage/reloadPersonalInformation?account=" + account)
}

/**
 * 获取员工号
 * @returns {AxiosPromise<any>}
 */
export function get() {
    return request.request({
        method: "post",
        url: "/system-manage/get"
    })
}


export function resourceMenuTab() {
    return request.request({
        url: "/system-manage/resource/menu/tab"
    })
}

export function getAllUserInfo(condition) {
    return request.post("/system-manage/getAllUserInfo",condition)
}

export function updateBasicInformation(data) {
    return request.post("/system-manage/updateBasicInformation",data);
}

export function updateAuditPassword(id, newPassword) {
    return request.get("/system-manage/updateAuditPassword",{params:{id,newPassword}})
}

export function updatePassword(id, newPassword) {
    return request.get("/system-manage/updatePassword",{params: {id, newPassword}})
}

export function uploadSig(id, signature) {
    let formData = new FormData();
    formData.append('id', id);
    formData.append('signature', signature);
    return request.request({
        headers: { 'Content-Type': 'multipart/form-data' },
        method: 'post',
        url: '/system-manage/uploadSig',
        data: formData
    });
}


/**
 * 用户修改审核密码
 * @param account
 * @param oldPassword
 * @param newPassword
 * @return
 */
export function userUpdateAuditPassword(account, oldPassword, newPassword) {
    return request.get("/system-manage/userUpdateAuditPassword",{params:{account,oldPassword,newPassword}})
}

/**
 * 用户修改登录密码
 * @param account
 * @param oldPassword
 * @param newPassword
 * @return
 */
export function userUpdatePassword(account, oldPassword, newPassword) {
    return request.get("/system-manage/userUpdatePassword", {params: {account, oldPassword,newPassword}})
}

export function getRoleInfo(staffId) {
    return request.get("/system-manage/role/getRoleInfo",{params:{staffId}})
}

export function updateRoles(staffId, roleIds) {
    return request.get("/system-manage/role/updateRoles",{params:{staffId, roleIds}})
}

export function getMenuTree() {
    return request.get("/system-manage/resource/menu/tab")
}
export function getMenu() {
    return request.get("/system-manage/resource/menu")
}
export function getMyMenu(id) {
    return request.get("/system-manage/getMyMenu?id="+id)
}

export function listRole() {
    return request.get("/system-manage/role/listRole")
}

export function updateRoleResource(data) {
    return request.post("/system-manage/role/resource/updateRoleResource",data)
}

export function addRole(data) {
    return request.post("/system-manage/role/addRole",data)
}

export function updateRole(data) {
    return request.post("/system-manage/role/updateRole",data)
}


export function addUser(data) {
    return request.post("/system-manage/addUser",data)
}




