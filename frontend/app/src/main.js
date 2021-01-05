  
import App from './App.vue'
import 'bootstrap/dist/css/bootstrap.css'
import VueRouter from 'vue-router'
import Vue from 'vue'
import router from './router'
import store from './store'
import './plugins/axios'

Vue.use(VueRouter);

new Vue({
    router,
    store,
    render: h => h(App,)
}).$mount('#app')