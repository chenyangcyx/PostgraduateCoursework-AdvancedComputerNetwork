import jwtDecode from 'jwt-decode';


/**
 * 判断一个字符串是为电话号码
 * @param str
 * https://www.runoob.com/js/js-regexp.html
 */
export const isTelCode = function(str) {
    let reg = /^((0\d{2,3}-\d{7,8})|(1[3-9]\d{9}))$/;
    return reg.test(str);
};

/**
 * 判断字符串数组中是否包含对应的字符串
 * @param array 字符串数组
 * @param item 字符串
 */
export const isContainsItem = function(array, item) {
    for (let i = 0; i < array.length; i++) {
        if (array[i] == item)
            return true;
    }
    return false;
};

export const getUserInfoByToken = function(token) {
    return jwtDecode(token);
};

/**
 * 深拷贝
 * @param target
 * @returns {{}}
 */
export const deepClone = function(target) {
    // 定义一个变量
    let result;
    // 如果当前需要深拷贝的是一个对象的话
    if (typeof target === 'object') {
        // 如果是一个数组的话
        if (Array.isArray(target)) {
            result = []; // 将result赋值为一个数组，并且执行遍历
            for (let i in target) {
                // 递归克隆数组中的每一项
                result.push(deepClone(target[i]));
            }
            // 判断如果当前的值是null的话；直接赋值为null
        } else if (target === null) {
            result = null;
            // 判断如果当前的值是一个RegExp对象的话，直接赋值
        } else if (target.constructor === RegExp) {
            result = target;
        } else  if(target instanceof  Date){
            result = new Date(target)
        } else {
            // 否则是普通对象，直接for in循环，递归赋值对象的所有值
            result = {};
            for (let i in target) {
                result[i] = deepClone(target[i]);
            }
        }
        // 如果不是对象的话，就是基本数据类型，那么直接赋值
    } else {
        result = target;
    }
    // 返回最终结果
    return result;
};


export const image2Base64 = function(img) {
    let canvas = document.createElement('canvas');
    canvas.width = img.width;
    canvas.height = img.height;
    let ctx = canvas.getContext('2d');
    ctx.drawImage(img, 0, 0, img.width, img.height);
    let dataURL = canvas.toDataURL('image/png');
    return dataURL;
};

export const isStrAndIsNotBlank = function(str){
    if(str == null || str == undefined || !(typeof str == 'string') || str == "")
        return false;
    return true
}

export const isBlank = function(str) {
    if(str == null || str == ""){
        return true
    }

    return false
}




