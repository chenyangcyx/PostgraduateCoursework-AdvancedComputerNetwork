import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        user: {
            id: 0,
            name: "",
            phone: "",
            account: "",
            perms: "",
            roles: "",
        },
        role: null,
        token: null, // 用户登录状态
        perms: null, //权限信息 是个字符串数组
        menuTree: [],//菜单树，
        menu:[],//菜单树展开
        myMenu: [],
        noticeInterval: null,
    },
    getters: {
        getUser(state) {
            return state.user;
        },
        getRole(state){
            return state.role
        },
        getToken(state){
            return state.token
        },
        getPerms(state){
            return state.perms
        },
        getMenuTree(state){
            return state.menuTree
        },
        getMyMenu(state){
            return state.myMenu
        },
        getMenu(state){
            return state.menu
        },
        getButton(state){
            let res = state.menu.filter(item =>{
                return item.resourceType != null && item.resourceType == 2 && state.myMenu.indexOf(item.id) != -1
            })
            return res
        },
        getNoticeInterval(state){
            return state.noticeInterval
        }
    },
    mutations: {
        setRole(state, payload){
            state.role = payload.role
        },
        setUser(state, payload){
            state.user = payload.user
        },
        setToken(state, payload){
            state.token = payload.token
        },
        setPerms(state, payload){
            state.perms = payload.perms
        },
        setMenuTree(state, payload){
            state.menuTree = payload.menuTree
        },
        setMyMenu(state, payload){
            state.myMenu = payload
        },
        setMenu(state, payload){
            state.menu = payload
        },
        setNoticeInterval(state, payload){
            state.noticeInterval = payload
        }
    }

});
