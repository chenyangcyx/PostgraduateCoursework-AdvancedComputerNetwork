import {pinyinLib} from './lib/pinyin-lib';

export default {
    chineseToPinYin: function (l1) {
        let l2 = l1.length;
        let I1 = '';
        let reg = new RegExp('[a-zA-Z0-9]');
        for (let i = 0; i < l2; i++) {
            let val = l1.substr(i, 1);
            let name = this.arraySearch(val, pinyinLib);
            if (reg.test(val)) {
                I1 += val;
            } else if (name !== false) {
                I1 += name;
            }
        }
        I1 = I1.replace(/ /g, '-');
        while (I1.indexOf('--') > 0) {
            I1 = I1.replace('--', '-');
        }
        return I1;
    },
    arraySearch: function (l1, l2) {
        for (let name in pinyinLib) {
            if (pinyinLib[name].indexOf(l1) !== -1) {
                return this.ucfirst(name);
            }
        }
        return false;
    },
    ucfirst: function (l1) {
        if (l1.length > 0) {
            let first = l1.substr(0, 1).toUpperCase();
            let spare = l1.substr(1, l1.length);
            return first + spare;
        }
    },
    chineseToPinYinAbbr(l1){
        let pinyin = this.chineseToPinYin(l1);
        let res = "";
        for (let i = 0; i < pinyin.length; i++) {
            let c = pinyin.charAt(i);
            if (/^[A-Z]+$/.test(c)) {
                res += c;
            }
        }
        return res;
    }
};
