<template>
    <div class="container-fluid">
        <div class="col-md-4 offset-md-4">
            <br>
            <div class="card">
                <div class="card-header">
                    Login
                </div>
                <div class="card-body">

                    <div class="form-group">
                      <label for="email">Email</label>
                      <input type="email" class="form-control" name="email" id="email" aria-describedby="emailHelpId" placeholder="Email" v-model="email">
                      <small id="emailHelpId" class="form-text text-muted">Ingrese tu correo</small>
                    </div>
                    <div class="form-group">
                      <label for="password">Password</label>
                      <input type="password" class="form-control" name="password" id="password" placeholder="password" v-model="password">
                    </div>
                </div>
                <div class="card-footer text-muted row justify-content-center">
                    <a name="inicio" id="inicio" class="btn btn-primary" href="#" role="button" @click="login">Iniciar Session</a>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    data(){
        return{
            email: null,
            password: null
        }
    },
    methods:{
        login(){
            // Cuando el usuario ingresa se coteja sus datos en la base de datos
            // no implementamos un sistema solido de authentificacion 
            // solo revisamos que el usuario exista
            axios({
                method: 'get',
                url: '/users/'+this.email,
                baseURL: process.env.VUE_APP_API_URL,
                responseType: 'json',
            }).then(res => {
                // obviamente esta forma de autentificar es malicima 
                // pero para los propositos actuales no se necesita 
                // otro metodo de autentificacion
                if(res.data.password == this.password){
                    console.log("logueado")
                    this.$router.push('/inventario')
                }
                else{
                    console.log("no logueado")
                    this.email = ""
                    this.password = ""
                }
            }).catch(err => {
                console.log("Error "+err.toString())
            })
        }
    }
}
</script>
