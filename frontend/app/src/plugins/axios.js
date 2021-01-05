import axios from 'axios'

axios.defaults.baseURL = 'http://localhost:8000/' // Tem que mudar quando fazer o Deploy process.env.....

axios.interceptors.request.use(
    (config) => {
        const storage = JSON.parse(localStorage.getItem('psIfc'))
        if (storage && storage.auth) {
            if (storage.auth.loggedIn) {
                config.headers.common['Authorization'] = 'Bearer ${storage.auth.user.access}'
            }
        }
        return config
    }
)