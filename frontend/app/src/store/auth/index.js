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
        login({ commit }, user) {
            return AuthApi.login(user).then( (user) => {
                commit('loginSuccess', user)
                return Promise.resolve(user)
            }, (error) => {
                commit('loginFailure')
                return Promise.reject(error)
            })
        },
        // logout () {
        //     localStorage.removeItem('psIfc')
        
        //     this.$router.push('/login')
        // }
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