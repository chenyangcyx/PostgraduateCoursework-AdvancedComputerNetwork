import request from '../index';

/**
 * 获取所有到期的通知
 * @param condition (staffId, pageNum, size, start, end）
 * @return
 */
export function getAll(condition) {
    return request.post("/system-manage/notice/getAll", condition)
}

/**
 * 获得所有关于自己的通知
 * @param condition (staffId, pageNum, size, start, end）
 * @return
 */
export function getAllAboutMe(condition) {
    return request.post("/system-manage/notice/getAllAboutMe",condition)
}
/**
 * 添加新的通知
 * @param notice
 * @return
 */
export function add(data) {
    return request.post("/system-manage/notice/add",data)
}

/**
 * 修改通知
 * @param notice
 * @return
 */
export function updateNotice(data) {
    return request.post("/system-manage/notice/update",data)
}

/**
 * 删除一条通知
 * @param id
 * @return
 */
export function deleteNotice(id) {
    return request.get("/system-manage/notice/delete?id=" + id)
}
/**
 * 获取对应id通知的目标用户的id
 * @param id
 * @return
 */
export function getAllStakeholdersId(id) {
    return request.get("/system-manage/notice/getAllStakeholdersId?id=" + id)
}
