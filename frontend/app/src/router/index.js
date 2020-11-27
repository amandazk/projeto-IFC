import Vue from 'vue'
import Router from 'vue-router'

import DescProj from '../DescProj.vue'
import App from '../App.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  hash: false,
  routes: [
    {
      path: '/',
      name: 'App',
      component: App
    },
    {
        path: '/descricao',
        name: 'DescProj',
        component: DescProj
      }

  ]}
)