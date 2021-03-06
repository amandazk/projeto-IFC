import Vue from 'vue'
import VueRouter from 'vue-router';

import Index from '../components/Index.vue'
import InfoProj from '../components/InfoProj.vue'
import Covid from '../components/Covid.vue'
import CampanhaList from '../components/Campanha/List.vue'
import CampanhaListUni from '../components/Campanha/ListUni.vue'
import DemandaList from '../components/Demanda/List.vue'
import OfertaList from '../components/Oferta/List.vue'
import PessoaList from '../components/Pessoa/List.vue'
import PessoaCreate from '../components/Pessoa/Create.vue'
import ServicoList from '../components/Servico/List.vue'
import VoluntariadoList from '../components/Voluntariado/List.vue'
import Login from '@/views/Login.vue'
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
      path: '/campanhaListUni/:campanha_id',
      name: 'CampanhaListUni',
      component: CampanhaListUni
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
      path: '/pessoas/cadastro',
      name: 'PessoaCreate',
      component: PessoaCreate
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
      path: '/login',
      name: Login,
      component: Login
    },
    


  ]
})