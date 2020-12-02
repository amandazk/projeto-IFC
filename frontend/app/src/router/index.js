import Vue from 'vue'
import VueRouter from 'vue-router';

import Index from '../components/Index.vue'
import DescProj from '../components/DescProj.vue'
import CampanhaList from '../components/Campanha/List.vue'
import DemandaList from '../components/Demanda/List.vue'

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
      path: '/descricao-projeto',
      name: 'DescProj',
      component: DescProj
    },
    {
      path: '/campanhas',
      name: 'CampanhaList',
      component: CampanhaList
    },
    {
      path: '/demandas',
      name: 'DemandaList',
      component: DemandaList
    }



  ]
})