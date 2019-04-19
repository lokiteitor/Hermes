<template>
    <div class="container-fluid">
        <br>
        <div>
            <div class="col-md-6 offset-md-3 ">
                <div class="card">
                    <div class="card-header">
                        Ingrese los datos del usuario
                    </div>
                    <div class="card-body">
                        <div class="form-group">
                          <label for="email">Email</label>
                          <input type="email" class="form-control" name="email" id="email" aria-describedby="hemail" placeholder="email" v-model="email">
                          <small id="hemail" class="form-text text-muted">Ingrese el correo electronico</small>
                        </div>
                        <div class="form-group">
                          <label for="username">Nombre de usuario</label>
                          <input type="text"
                            class="form-control" name="username" id="username" aria-describedby="husername" placeholder="username" v-model="username">
                          <small id="husername" class="form-text text-muted">Ingrese el nombre de usuario</small>
                        </div>
                        <div class="form-group">
                          <label for="password">Password</label>
                          <input type="password"
                            class="form-control" name="password" id="password" aria-describedby="hpassword" placeholder="password" v-model="password">
                          <small id="hpassword" class="form-text text-muted">Ingrese la contraseña</small>
                        </div>
                    </div>
                    <div class="card-footer text-muted row justify-content-center">
                        <div class="col-md-auto ">
                            <a name="registrar" id="registrar" class="btn btn-success btn-lg" @click="registrar" href="#" role="button">Registrar</a>
                        </div>
                    </div>
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
            email:  null,
            password:  null,
            username:  null            
        }
    },
    methods:{
        registrar(){
            // para registrar un usuario se debe estar logueado
            // enviar mediante POST los datos del usuario            
            console.log(process.env.VUE_APP_API_URL)
            axios({
                method:"post",
                url: '/users',
                baseURL: process.env.VUE_APP_API_URL,
                responseType: 'json',
                data:{
                    username: this.username,
                    email: this.email,
                    password: this.password
                }
            }).then(res => {
                console.log("Exito  "+ res)
                this.$router.push('/login')  
            }).catch(err => {
                console.log("Error: "+ err)
                // mensaje de alerta
            })
            //
        }
    }
}
</script>
