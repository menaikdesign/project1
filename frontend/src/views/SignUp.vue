<template>
     <div class="container">
        <div class="column is-4 is-offset-4">
            <h1 class="title">Sign Up</h1>

            <form @submit.prevent="submitForm">
                <div class="field">
                    <label>Email</label>
                    <input type="email" name="email" class="input" v-model="username" placeholder="Enter Username">
                </div>

                <div class="field">
                    <label>Password</label>
                    <input type="password" name="password1" class="input" v-model="password1" placeholder="Enter Password">
                </div>

                <div class="field">
                    <label>Confirm Password</label>
                    <input type="password" name="password2" class="input" v-model="password2" placeholder="Enter Password">
                </div>

                 <div class="notification is-danger" v-if="errors.length">
                    <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                 </div>
                <div>

                <div class="control">
                    <button class="button is-success">
                        Submit
                    </button>
                </div>

            </div>

            </form>

        </div>
     </div>
</template>

<script>
import axios from 'axios'
import {toast} from 'bulma-toast'

export default {
        name: 'SignUp',
        data(){
            return {
                username: '',
                password: '',
                errors: []
            }
        },
        methods: {
           async submitForm(){
                this.errors = []

                if(this.username === ''){
                    this.errors.push('Username cannot be empty')
                }

                if(this.password1 === ''){
                    this.errors.push('password must be above 2 character')
                }

                if(this.password1 !== this.password2){
                    this.errors.push('password does not match')
                }

                if(!this.errors.length){
                    this.$store.commit('setIsLoading', true)
                    
                    const FormData = {
                        username: this.username,
                        password: this.password1
                    }
                    //send to the database
                   await axios
                        .post('/api/v1/users/', FormData)
                        .then(response => {
                            toast({
                               message: 'Account Create  Succefully Please Log in',
                               type: 'is-success',
                               dismissible: true,
                               pauseOnHover: true,
                               duration: 2000,
                               position: 'bottom-right'
                            })

                            this.$router.push('/log-in')
                        })
                        .catch(error => {
                            if(error.response){
                                for(const property in error.response.data){
                                  this.errors.push(`${property}: ${error.response.data[property]}`)      
                                }
                            }else if(error.message){
                                this.errors.push('Something went wrong. Please try again')
                            }
                        })

                        this.$store.commit('setIsLoading', false)
                }
            }
        }
    }
</script>