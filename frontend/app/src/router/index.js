import Vue from 'vue'
import VueRouter from 'vue-router';

import Index from '../components/Index.vue'
import InfoProj from '../components/InfoProj.vue'
import Covid from '../components/Covid.vue'
import CampanhaList from '../components/Campanha/List.vue'
import DemandaList from '../components/Demanda/List.vue'
import OfertaList from '../components/Oferta/List.vue'
import PessoaList from '../components/Pessoa/List.vue'
import ServicoList from '../components/Servico/List.vue'
import VoluntariadoList from '../components/Voluntariado/List.vue'
import Cadastro from '../components/Cadastro/Cadastro.vue'
import Login from '../components/Login/Login.vue'
//import { component } from 'vue/types/umd';

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
      path: '/informacao-projeto',
      name: 'InfoProj',
      component: InfoProj
    },
    {
      path: '/cuidados-covid',
      name: 'Covid',
      component: Covid
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
    },
    {
      path: '/ofertas',
      name: 'OfertaList',
      component: OfertaList
    },
    {
      path: '/pessoas',
      name: 'PessoaList',
      component: PessoaList
    },
    {
      path: '/servicos',
      name: 'ServicoList',
      component: ServicoList
    },
    {
      path: '/voluntariados',
      name: 'VoluntariadoList',
      component: VoluntariadoList
    },
    {
      path: '/cadastro',
      name: Cadastro,
      component: Cadastro
    },
    {
      path: '/login',
      name: Login,
      component: Login
    },
    


  ]
})