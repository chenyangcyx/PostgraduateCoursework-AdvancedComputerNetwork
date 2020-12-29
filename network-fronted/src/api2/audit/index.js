import request from '../index';

/**
 * 样品接收
 * @param data, id,
 *              staffId, 实体id
 *              account, 账户，也就是员工号
 *              auditPassword,
 *              phone,
 *              receivePerson
 * @returns {AxiosPromise<any>}
 */
export function receiveSamplingRecord(data){
    return request.post("/weifei/audit/receiveSamplingRecord",data)
}

/**
 * 化验申请单接收
 *
 * @param data staffId,
 *             auditPassword,
 *             account, 账户，也就是员工号
 *             id,
 *             sampleReceivedDate yyyy-MM-dd, string,
 *             sampleReceivedPerson
 * @return
 */
export function applicationReceived(data) {
    return request.post("/weifei/audit/applicationReceived",data);
}

/**
 * 化验申请单备份样品接收
 *
 * @param data staffId,
 *             auditPassword,
 *             account, 账户，也就是员工号
 *             id,
 *             backupSampleReceivedPerson,
 *             backupSampleReceivedDate yyyy-MM-dd, string 可以为null,,
 * @return
 */
export function applicationBackupReceived(data) {
    return request.post("/weifei/audit/applicationBackupReceived",data)
}

/**
 * 测试报告 检测人员审核
 *
 * @param data staffId，
 *             auditPassword，
 *             account, 账户，也就是员工号
 *             id,
 * @return
 */
export function detectionDetectionPersonAudit(data) {
    return request.post("/weifei/audit/detectionDetectionPersonAudit",data)
}

/**
 * 测试报告 复核人员审核
 *
 * @param data
 *             staffId，
 *             auditPassword，
 *             account, 账户，也就是员工号
 *             id,
 * @return
 */
export function detectionReviewerPersonAudit(data) {
    return request.post("/weifei/audit/detectionReviewerPersonAudit",data)
}
/**
 * 测试报告 审核人员审核
 *
 * @param data
 *             staffId，
 *             auditPassword，
 *             account, 账户，也就是员工号
 *             id,
 * @return
 */
export function detectionAuditorPersonAudit(data) {
    return request.post("/weifei/audit/detectionAuditorPersonAudit",data)
}


/**
 * 化验申请单部门审核人审核
 * @param data
 *             staffId，
 *             auditPassword，
 *             account, 账户，也就是员工号
 *             id,
 *             deptReviewer
 * @return
 */
export function applicationDeptReviewerAudit(data) {
    return request.post("/weifei/audit/applicationDeptReviewerAudit",data)
}

/**
 * 化验申请单，审批人审批
 * @param data
 *             staffId，
 *             auditPassword，
 *             account, 账户，也就是员工号
 *             id,
 *             confirmPerson
 * @return
 */
export function applicationReviewerAudit(data) {
    return request.request({
        method: "post",
        url: "/weifei/audit/applicationReviewerAudit",
        data
    })
}


/**
 * 液体指纹取样检测人审核
 * @param data
 *	        auditPassword，
 *          account, 账户，也就是员工号
 *          id,
 *          samplingAndDetectionPersonId,
 *          samplingAndDetectionPerson
 *
 * @return
 */
export function fingerprintingLiquorSamplingAndDetectionPersonAudit(data) {
    return request.post("/weifei/audit/fingerprintingLiquorSamplingAndDetectionPersonAudit",data)
}

/**
 * 液体指纹审核人审核
 * @param data
 *	        auditPassword，
 *          account, 账户，也就是员工号
 *          id,
 *          confirmPersonId,
 *          confirmPerson
 * @return
 */
export function fingerprintingLiquorConfirmPersonAudit(data) {
    return request.post("/weifei/audit/fingerprintingLiquorConfirmPersonAudit",data)
}



/**
 * 危废预接收确认书-技术部门审核
 * @param data
 *	        auditPassword，
 *          account, 账户，也就是员工号
 *          id,
 *          confirmPersonId,
 *          confirmPerson
 * @return
 */
export function wastePreTecAudit(data) {
    return request.post("/weifei/audit/wastePreTecAudit",data)
}

/**
 * 危废预接收确认书-物控部审核
 * @param data
 *	        auditPassword，
 *          account, 账户，也就是员工号
 *          id,
 *          confirmPersonId,
 *          confirmPerson
 * @return
 */
export function wastePreControlAudit(data) {
    return request.post("/weifei/audit/wastePreControlAudit",data)
}

/**
 * 危废预接收确认书-安环部审核
 * @param data
 *	        auditPassword，
 *          account, 账户，也就是员工号
 *          id,
 *          confirmPersonId,
 *          confirmPerson
 * @return
 */
export function wastePreEhsAudit(data) {
    return request.post("/weifei/audit/wastePreEhsAudit",data)
}

/**
 * 危废预接收确认书-生产部门审核
 * @param data
 *	        auditPassword，
 *          account, 账户，也就是员工号
 *          id,
 *          confirmPersonId,
 *          confirmPerson
 * @return
 */
export function wastePreProductAudit(data) {
    return request.post("/weifei/audit/wastePreProductAudit",data)
}

/**
 * 危废预接收确认书-分管领导确认
 * @param data
 *	        auditPassword，
 *          account, 账户，也就是员工号
 *          id,
 *          confirmPersonId,
 *          confirmPerson
 * @return
 */
export function wastePreManagerAudit(data) {
    return request.post("/weifei/audit/wastePreManagerAudit",data)
}

/**
 * 固体指纹取样检测人审核
 * @param data
 *	        auditPassword，
 *          account, 账户，也就是员工号
 *          id,
 *          samplingAndDetectionPersonId,
 *          samplingAndDetectionPerson
 *
 * @return
 */
export function fingerprintingSolidSamplingAndDetectionPersonAudit(data) {
    return request.post("/weifei/audit/fingerprintingSolidSamplingAndDetectionPersonAudit",data);
}


/**
 * 固体指纹审核人审核
 * @param data
 *	        auditPassword，
 *          account, 账户，也就是员工号
 *          id,
 *          confirmPersonId,
 *          confirmPerson
 * @return
 */
export function fingerprintingSolidConfirmPersonAudit(data) {
    return request.post("/weifei/audit/fingerprintingSolidConfirmPersonAudit",data);
}

export function appearanceTestAudit(data) {
    return request.post("/weifei/audit/appearanceTestAudit",data)
}

/**
 * 危废管理卡-质量技术部填写确认
 * @param data(account,auditPassword, staffName, staffId, managementCartId)
 * @return
 */
export function managementCartTecAudit(data){
    return request.post("/weifei/audit/managementCartTecAudit",data)
}
/**
 * 危废管理卡-市场部填写确认
 * @param data(account,auditPassword, staffName, staffId, managementCartId)
 * @return
 */
export function managementCartMarketAudit(data){
    return request.post("/weifei/audit/managementCartMarketAudit",data)
}

/**
 * 危废管理卡-物控部填写确认
 * @param data(account,auditPassword, staffName, staffId, managementCartId)
 * @return
 */
export function managementCartControlAudit(data){
    return request.post("/weifei/audit/managementCartControlAudit", data)
}

/**
 * 危废管理卡-生产部部填写确认
 * @param data(account,auditPassword, staffName, staffId, managementCartId)
 * @return
 */

export function managementCartPropAudit(data){
    return request.post("/weifei/audit/managementCartPropAudit", data)
}

/**
 * 危废管理卡-EHS部填写确认
 * @param data(account,auditPassword, staffName, staffId, managementCartId)
 * @return
 */
export function managementEHSAudit(data){
    return request.post("/weifei/audit/managementEHSAudit",data)
}

/**
 * 危废管理卡-分管副总经理审批
 * @param data(account,auditPassword, staffName, staffId, managementCartId)
 * @return
 */
export function managementCartEhsViceManagerAudit(data){
    return request.post("/weifei/audit/managementCartEhsViceManagerAudit",data)
}

/**
 * 危废管理卡-总经理审批
 * @param data(account,auditPassword, staffName, staffId, managementCartId)
 * @return
 */
export function managementCartManagerAudit(data){
    return request.post("/weifei/audit/managementCartManagerAudit", data)
}

/****************************************************************************
* 合同审批流程-业务部门审批
* @param data(account,auditPassword, staffName, staffId, contractApprovalId)
* @return
*/
export function contractApprovalBusinessDepAudit(data){
    return request.post("/weifei/audit/contractApprovalBusinessDepAudit", data)
}
/**
 * 合同审批流程-财务部门审批
 * @param data(account,auditPassword, staffName, staffId, contractApprovalId)
 * @return
 */
export function contractApprovalAccountingDepAudit(data){
    return request.post("/weifei/audit/contractApprovalAccountingDepAudit", data)
}

/**
 * 合同审批流程-副总经理审批
 * @param data(account,auditPassword, staffName, staffId, contractApprovalId)
 * @return
 */
export function contractApprovalViceManagerAudit(data){
    return request.post("/weifei/audit/contractApprovalViceManagerAudit", data)
}

/**
 * 合同审批流程-总经理审批
 * @param data(account,auditPassword, staffName, staffId, contractApprovalId)
 * @return
 */
export function contractApprovalGeneralManagerAudit(data){
    return request.post("/weifei/audit/contractApprovalGeneralManagerAudit", data)
}

/**
 * 合同审批流程-总部市场管理部审批
 * @param data(account,auditPassword, staffName, staffId, contractApprovalId)
 * @return
 */
export function contractApprovalMarketManagementDepAudit(data){
    return request.post("/weifei/audit/contractApprovalMarketManagementDepAudit", data)
}

/**
 * 合同审批流程-市场总监审批
 * @param data(account,auditPassword, staffName, staffId, contractApprovalId)
 * @return
 */
export function contractApprovalMarketDirectorAudit(data){
    return request.post("/weifei/audit/contractApprovalMarketDirectorAudit", data)
}

/**
 * 现场检查市场部现场人签字确认
 * @param map(account,auditPassword, staffName, staffId, spotCheckId)
 * @return
 */
export function spotCheckMarketAudit(data) {
    return request.post("/weifei/audit/spotCheckMarketAudit", data)
}

/**
 * 现场检查质量部现场人签字确认
 * @param map(account,auditPassword, staffName, staffId, spotCheckId)
 * @return
 */
export function spotCheckQualityAudit(data) {
    return request.post("/weifei/audit/spotCheckQualityAudit", data)
}

/**
 * 现场检查物控部现场人签字确认
 * @param map(account,auditPassword, staffName, staffId, spotCheckId)
 * @return
 */
export function spotCheckControlAudit(data) {
    return request.post("/weifei/audit/spotCheckControlAudit", data)
}

/**
 * 现场检查Ehs部现场人签字确认
 * @param map(account,auditPassword, staffName, staffId, spotCheckId)
 * @return
 */
export function spotCheckEhsAudit(data) {
    return request.post("/weifei/audit/spotCheckEhsAudit", data)
}



