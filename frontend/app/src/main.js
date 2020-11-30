//import { createApp } from 'vue'
import App from './App.vue'
//import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
// import 'bootstrap-vue/dist/bootstrap-vue.css'
import VueRouter from 'vue-router'
import Vue from 'vue'
import router from './router/index'
// import DescProj from './components/DescProj.vue'


// const router = new VueRouter({
//     routes: [

//         { path: '/', 
//         component: App
//         },

//         { path: '/descricao-projeto',
//         component: DescProj
//         }   

//     ]
//   });

//Vue.use(BootstrapVue)
//Vue.use(IconsPlugin)
Vue.use(VueRouter);

new Vue({
    router,
    render: h => h(App,)
}).$mount('#app')
