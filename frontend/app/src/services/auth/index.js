import axios from 'axios'

class AuthApi {
    async login(user) {
        try {
            const { data } = await axios.post('api/auth/token/', user)
            if (data.access) {
                axios.defaults.headers.common['Authorization'] = `Bearer ${data.access}`
            }
            return data
        } catch(e) {
            console.log(e)
        }
    }
}

export default new AuthApi()