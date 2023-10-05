<template>
    <div class="container">
        <div class="column is-multiline">
            <h1 class="title">
                User Account 
            </h1>
        </div>

        <div class="column is-12">
            <router-link :to="{name: 'EditMember', params: {id: $store.state.user.id}}" class="button is-light">Edit</router-link>

            <button @click="logout()" class="button is-danger">Log out</button>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
       name: 'MyAccount',
       methods: {
        async logout() {
            await axios
                .post('/api/v1/token/logout')
                .then(response => {
                    console.log('Logged out')
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })

            axios.defaults.headers.common['Authorization'] = ''
            localStorage.removeItem('token')
            localStorage.removeItem('username')
            localStorage.removeItem('userid')
            localStorage.removeItem('team_name')
            localStorage.removeItem('team_id')
            this.$store.commit('removeToken')

            this.$router.push('/')
        }
       }
   }
</script>