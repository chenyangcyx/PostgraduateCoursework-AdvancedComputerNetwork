import Vue from 'vue';
import App from './App.vue';
import router from './router';
import ElementUI from 'element-ui';
import VueI18n from 'vue-i18n';
import { messages } from './components/common/i18n';
import 'element-ui/lib/theme-chalk/index.css'; // 默认主题
// import './assets/css/theme-green/index.css'; // 浅绿色主题
import './assets/css/icon.css';
import './components/common/directives';
import 'babel-polyfill';
import store from './store/';
import {DateUtil} from './utils/DataUtils';
import {deepClone} from './utils/CommonUtils';
import pinyin from './utils/pinyin';
import utils from './utils/utils';
import getFile from './api2/download';
import getImg from './api2/getImg';
import entities from './utils/entities';
import echarts from 'echarts'
Vue.prototype.$echarts = echarts

let javaMath = {
    INTEGER: {
        MAX_VALUE: 2147483647
    }
}
Vue.prototype.$dateUtil = DateUtil
Vue.prototype.$deepClone = deepClone
Vue.prototype.$pinyin = pinyin
Vue.prototype.$utils = utils
Vue.prototype.$getFile = getFile
Vue.prototype.$getImg = getImg
Vue.prototype.$javaMath = javaMath
Vue.prototype.$entities = entities

Vue.config.productionTip = false;
Vue.use(VueI18n);
Vue.use(ElementUI, {
    size: 'small'
});
const i18n = new VueI18n({
    locale: 'zh',
    messages
});

//使用钩子函数对路由进行权限跳转
router.beforeEach((to, from, next) => {
    document.title = `${to.meta.title} | 高级计算机网络系统`;
    next();
    //验证token，看token 信息是否失效
});

new Vue({
    router,
    i18n,
    store,
    render: h => h(App)
}).$mount('#app');
