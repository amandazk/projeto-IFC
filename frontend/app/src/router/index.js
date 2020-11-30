import Vue from 'vue'
import VueRouter from 'vue-router';

import DescProj from '../components/DescProj.vue'
import CampanhaList from '../components/Campanha/List.vue'
import Index from '../components/Index.vue'

Vue.use(VueRouter)

export default new VueRouter({
  mode: 'history',
  hash: false,
  routes: [{
      path: '/',
      name: 'Index',
      component: Index
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



  ]})
