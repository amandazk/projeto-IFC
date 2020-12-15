import Vue from 'vue'
import Vuex from 'vuex'
import VuexPersist from 'vuex-persist'

import { auth } from './auth'

Vue.use(Vuex)

const vuexLocalStorage = new VuexPersist({
    key: 'psIfc',
    storage: window.localStorage,
})

export default new Vuex.Store({
    modules: {
        auth,
    },
    plugins: [vuexLocalStorage.plugin]
})