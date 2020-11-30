import Vue from 'vue'
import VueRouter from 'vue-router';

import DescProj from '../components/DescProj.vue'
import App from '../App.vue'
import CampanhaList from '../components/Campanha/List.vue'

Vue.use(VueRouter)

export default new VueRouter({
  mode: 'history',
  hash: false,
  routes: [{
      path: '/',
      name: 'App',
      component: App
    },
    {
      path: '/descricao',
      name: 'DescProj',
      component: DescProj
    },
    {
      path: '/campanhas',
      name: 'CampanhaList',
      component: CampanhaList
    },


  ]
})