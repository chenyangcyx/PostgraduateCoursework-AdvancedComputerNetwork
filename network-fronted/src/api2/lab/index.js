import request from '../index';

/**
 * 查看所有的错误处理报告
 * @param condition
 * @returns {AxiosPromise<any>}
 */
export function getAllErrReport(condition) {
    return request.request({
        method:"post",
        url: "/weifei/lab/getAllErrReport",
        data: condition
    })
}

/**
 * 获取错误报告唯一编号
 * @returns {AxiosPromise<any>}
 */
export function getErrReportUniqueNum() {
    return request.request({
        method: "get",
        url: "/weifei/lab/getErrReportUniqueNum"
    })
}

/**
 * 添加错误处理报告
 * @param data
 * @returns {AxiosPromise<any>}
 */
export function addNewErrReport(data) {
    return request.request({
        method: "post",
        url: "/weifei/lab/addNewErrReport",
        data
    })
}

/**
 * 更新异常报告
 * @param data
 * @returns {AxiosPromise<any>}
 */
export function updateErrReport(data) {
    return request.request({
        method: "post",
        url: "/weifei/lab/updateErrReport",
        data
    })
}

/**
 * 删除对应的测试报告
 * @param id
 * @returns {AxiosPromise<any>}
 */
export function deleteErrReport(id) {
    return request.request({
        method: "get",
        url: "/weifei/lab/deleteErrReport",
        params: {id}
    })
}

/**
 * 获取所有的测试项目
 * @param condition
 * @returns {AxiosPromise<any>}
 */
export function getAllTest(condition) {
    return request.request({
        method: "post",
        url: "/weifei/lab/getAllTest",
        data: condition
    })
}

/**
 * 添加新的测试项目
 * @param data
 * @returns {AxiosPromise<any>}
 */
export function addNewTest(data) {
    return request.request({
        method: "post",
        url: "/weifei/lab/addNewTest",
        data
    })
}

/**
 * 更新测试项目
 * @param data
 * @returns {AxiosPromise<any>}
 */
export function updateTest(data) {
    return request.request({
        method: "post",
        url: "/weifei/lab/updateTest",
        data
    })
}

/**
 * 获取所有的实验室
 * @returns {AxiosPromise<any>}
 */
export function getAllLabs() {
    return request.request({
        method: "get",
        url: "/weifei/lab/getAllLabs",
    })
}

/**
 * 获取所有的实验室
 * @returns {AxiosPromise<any>}
 */
export function getAllLab() {
    return request.request({
        method: "get",
        url: "/weifei/lab/getAllLab",
    })
}

/**
 * 获取所有的测试分类信息
 * @returns {AxiosPromise<any>}
 */
export function getAllTestCategory() {
    return request.request({
        method: "get",
        url: "/weifei/lab/getAllTestCategory"
    })
}

/**
 * 添加新的测试分类
 * @param data
 * @returns {AxiosPromise<any>}
 */
export function addTestCategory(data) {
    return request.request({
        method: "post",
        url: "/weifei/lab/addTestCategory",
        data
    })
}




/**
 * 更新测试分类项目
 * @param data
 * @returns {AxiosPromise<any>}
 */
export function updateTestCategory(data) {
    return request.request({
        method: "post",
        url: "/weifei/lab/updateTestCategory",
        data
    })
}




/**
 *为对应的测试分类添加测试项目
 * @param testCategoryId 测试分类id
 * @param tests 测试（）数组
 * @returns {AxiosPromise<any>}
 */
export function addTestForTestCategory(testCategoryId, tests) {
    return request.request({
        method: "get",
        url:  "/weifei/lab/addTestForTestCategory",
        params: {
            testCategoryId,tests
        }
    })
}

/**
 * 删除指定测试分类指定的测试项目
 * @param testCategoryId
 * @param testId
 * @returns {AxiosPromise<any>}
 */
export function deleteTestOfTestCategory(testCategoryId, testId) {
    return request.request({
        method: "get",
        url:  "/weifei/lab/deleteTestOfTestCategory",
        params: {testCategoryId, testId}
    })
}



/**
 * 根据分类Id 获取测试项目们
 * @param testCategoryId
 * @returns {AxiosPromise<any>}
 */
export function getTestByTestCategoryId(testCategoryId) {
    return request.request({
        method: "get",
        url: "/weifei/lab/getTestByTestCategoryId",
        params: {testCategoryId}
    })
}

/**
 * 根据测试分类ID获取所有绑定了测试项目
 * @param testCategoryId
 * @returns {AxiosPromise<any>}
 */
export function getUnboundTestByTestCategoryId(testCategoryId) {
    return request.request({
        method: "get",
        url: "/weifei/lab/getUnboundTestByTestCategoryId",
        params: {testCategoryId}
    })
}

/**
 * 获取所有的检测报告
 * @param condition
 * @returns {AxiosPromise<any>}
 */
export function getAllDetectionReport(condition) {
    return request.request({
        method: "post",
        url: "/weifei/lab/getAllDetectionReport",
        data: condition
    })
}

/**
 * 更新检测报告
 * @param data
 * @returns {AxiosPromise<any>}
 */
export function updateDetectionReport(data) {
    return request.request({
        method: "post",
        url:  "/weifei/lab/updateDetectionReport",
        data
    })
}

/**
 * 获取所有检测报告对应的测试项目
 * @param detectionId
 * @returns {AxiosPromise<any>}
 */
export function getAllRelDetectionReportTest(detectionId) {
    return request.request({
        method: "get",
        url: "/weifei/lab/getAllRelDetectionReportTest",
        params: {detectionId}
    })
}

/**
 * 获取对应测试报告的测试进度
 * @param detectionId
 * @returns {AxiosPromise<any>}
 */
export function getProcessOfDetectionReport(detectionId) {
    return request.request({
        method: "get",
        url: "/weifei/lab/getProcessOfDetectionReport",
        params: {detectionId}
    })
}

/**
 * 为测试报告的某一项录入结果
 * @param data
 * @returns {AxiosPromise<any>}
 */
export function addRelDetectionTestResult(data) {
    return request.request({
        method: "post",
        url: "/weifei/lab/addRelDetectionTestResult",
        data
    })
}

export function referStaff(data) {
    return request.post("/weifei/lab/referStaff",data);
}

/***
 * 审核，并上传检测人和审核人电子签名照
 * @param id
 * @param detectionPerson
 * @param reviewerPerson
 * @returns {AxiosPromise<any>}
 */
export function detectionReportUpload(id, detectionPerson, reviewerPerson) {
    let formData = new FormData();
    formData.append("id",id);
    formData.append("detectionPerson", detectionPerson);
    formData.append("reviewerPerson",reviewerPerson);
    return request.request({
        headers: { "Content-Type": "multipart/form-data" },
        method: "post",
        url: "/weifei/pic/detectionReport/upload",
        data: formData
    })
}

/**
 * 根据工号，或者姓名，进行模糊查询
 * @param condition
 * @returns {AxiosPromise<any>}
 */
export function fuzzySearchStaff(condition) {
    return request.request({
        method: "get",
        url: "/weifei/lab/fuzzySearchStaff",
        params:{condition}
    })
}

/**
 *
 * @param data
*                  pageNum int 页面好<br>
*                  size int 页面大小<br>
*                  start string 开始日期<br>
*                  end   string  结束日期<br>
*                  num  string 表单编号
 * @returns {AxiosPromise<any>}
 */
export function getAllFingerprintingLiquors(data) {
    return request.request({
        method: "post",
        url: "/weifei/lab/getAllFingerprintingLiquors",
        data
    })
}

/**
 * 获取所有未与液体指纹绑定的样品记录
 * @param fingerprintingLiquorId
 * @returns {AxiosPromise<any>}
 */
export function getAllFingerprintingLiquorUnboundSamplingRecords(fingerprintingLiquorId) {
    return request.request({
        url: "/weifei/lab/getAllFingerprintingLiquorUnboundSamplingRecords",
        params: {
            fingerprintingLiquorId
        }
    })
}
/**
 * 增加液体指纹检测
 * @param data
 * @returns {AxiosPromise<any>}
 */
export function addFingerprintingLiquor(data) {
    return request.request({
        method: "post",
        url: "/weifei/lab/addFingerprintingLiquor",
        data
    })
}

/**
 * 修改液体指纹检测项目
 * @param data
 * @returns {AxiosPromise<any>}
 */
export function updateFingerprintingLiquor(data) {
    return request.request({
        method: "post",
        url: "/weifei/lab/updateFingerprintingLiquor",
        data
    })
}

/**
 *
 * @param condition <br>
 *                  pageNum int 页面号<br>
 *                  size int 页面大小<br>
 *                  start string 开始日期<br>
 *                  end   string  结束日期<br>
 *                  num  string 表单编号
 * @returns {AxiosPromise<any>}
 */
export function getTFingerprintingSolid(condition) {
    return request.request({
        method: "post",
        url: "/weifei/lab/getTFingerprintingSolid",
        data: condition
    })
}

/**
 * 获取所有未与固体指纹绑定的样品记录
 * @param fingerprintingSolidId
 * @returns {AxiosPromise<any>}
 */
export function getAllTFingerprintingSolidUnboundSamplingRecords(fingerprintingSolidId) {
    return request.request({
        url: "/weifei/lab/getAllTFingerprintingSolidUnboundSamplingRecords",
        params: {fingerprintingSolidId}
    })
}

/**
 * 增加固体检测项目
 * @param data
 * @returns {AxiosPromise<any>}
 */
export function addTFingerprintingSolid(data) {
    return request.request({
        method: "post",
        url: "/weifei/lab/addTFingerprintingSolid",
        data
    })
}

/**
 * 更新固体检测项目
 * @param data
 * @returns {AxiosPromise<any>}
 */
export function updateTFingerprintingSolid(data) {
    return request.request({
        method: "post",
        url: "/weifei/lab/updateTFingerprintingSolid",
        data
    })
}


/**
 *上传液体指纹检测项目样品检测人电子签名
 * @param id
 * @param samplingAndDetectionPerson
 * @param samplingAndDetectionPersonPic
 * @returns {AxiosPromise<any>}
 */
export function uploadFingerprintingLiquorSamplingAndDetectionPerson(id, samplingAndDetectionPerson, samplingAndDetectionPersonPic){
    let formData = new FormData();
    formData.append('id', id);
    formData.append('samplingAndDetectionPerson', samplingAndDetectionPerson);
    formData.append('samplingAndDetectionPersonPic', samplingAndDetectionPersonPic);
    return request.request({
        headers: { 'Content-Type': 'multipart/form-data' },
        method: 'post',
        url: '/weifei/pic/fingerprintingLiquor/upload/samplingAndDetectionPerson',
        data: formData
    });
}

/**
 * 上传液体指纹检测项目样品检测人电子签名
 * @param id
 * @param confirmPerson
 * @param confirmPersonPic
 * @returns {AxiosPromise<any>}
 */
export function uploadFingerprintingLiquorConfirmPerson(id, confirmPerson, confirmPersonPic) {
    let formData = new FormData();
    formData.append('id', id);
    formData.append('confirmPerson', confirmPerson);
    formData.append('confirmPersonPic', confirmPersonPic);
    return request.request({
        headers: { 'Content-Type': 'multipart/form-data' },
        method: 'post',
        url: '/weifei/pic/fingerprintingLiquor/upload/confirmPerson',
        data: formData
    });
}

export function getAllUnfinishedApplications(condition) {
    return request.post("/weifei/lab/getAllUnfinishedApplications",condition)
}

export function getAllStaffs() {
    return request.get("/weifei/lab/getAllStaffs")
}

export function getAllJobSchedule(condition) {
    return request.post("/weifei/lab/getAllJobSchedule",condition)
}


export function getAllPlanFinishedRate() {
    return request.get("/weifei/lab/getAllPlanFinishedRate")
}

export function deleteFingerprintingSolid(id) {
    return request.get("/weifei/lab/deleteFingerprintingSolid",{params:{id}})
}

export function deleteFingerprintingLiquor(id) {
    return request.get("/weifei/lab/deleteFingerprintingLiquor",{params:{id}})
}

export function getGbTypeTree() {
    return request.get("/weifei/lab/getGbTypeTree")
}

export function insertNewType(parentId,name,code,character) {
    return request.get("/weifei/lab/insertNewType",{params:{parentId,name,code,character}})
}

export function deleteType(id) {
    return request.get("/weifei/lab/deleteType?id=" + id);
}

export function getAllGbWasteTypes() {
    return request.get("/weifei/lab/getAllGbWasteTypes")
}

export function updateGBType(data) {
    return request.post("/weifei/lab/updateGBType",data)
}

export function deleteApplication(id) {
    return request.get("/weifei/lab/deleteApplication?id=" + id)
}


export function addLab(lab) {
    return request.post("/weifei/lab/addLab",lab)
}

export function updateLab(lab) {
    return request.post("/weifei/lab/updateLab",lab)
}

export function deleteTest(id) {
    return request.get("/weifei/lab/deleteTest?id=" + id)
}


export function deleteTestCategory(id) {
    return request.get("/weifei/lab/deleteTestCategory?id=" + id)
}
