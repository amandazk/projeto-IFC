import Vue from 'vue'
import VueRouter from 'vue-router';

import Index from '../components/Index.vue'
import Descricao from '../components/DescProj.vue'
import CampanhaList from '../components/Campanha/List.vue'
import DemandaList from '../components/Demanda/List.vue'
import OfertaList from '../components/Oferta/List.vue'
import PessoaList from '../components/Pessoa/List.vue'
import ServicoList from '../components/Servico/List.vue'

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
      path: '/',
      name: 'Descricao',
      component: Descricao
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
    


  ]
})