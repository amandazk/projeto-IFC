import AuthApi from '@/services/auth'

const storage = JSON.parse(localStorage.getItem('psIfc'))
if (storage && storage.auth) {
    var _loggedIn = storage.auth.loggedIn
    var _user = storage.auth.user
} else {
    var _loggedIn = false
    var _user = {}
}


export const auth = {
    namespaced: true,
    state: {
        loggedIn: _loggedIn,
        user: _user
    },

    actions: {
        async login({ commit }, user) {
            try {
              const userData = await AuthApi.login(user)
              console.log(userData)
              commit('loginSuccess', userData)
              return Promise.resolve(userData)
            } catch (error) {
              commit('loginFailure')
              return Promise.reject(error)
            }
        }
    },
    

    mutations: {
        loginSuccess(state, user) {
            state.loggedIn = true
            state.user = user
        },

        loginFailure(state) {
            state.loggedIn = false
            state.user = {}
        }
    }
}