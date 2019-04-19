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
                      <input type="email" class="form-control" name="email" id="email" aria-describedby="emailHelpId" placeholder="Email">
                      <small id="emailHelpId" class="form-text text-muted">Ingrese tu correo</small>
                    </div>
                    <div class="form-group">
                      <label for="password">Password</label>
                      <input type="password" class="form-control" name="password" id="password" placeholder="password">
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
export default {
    methods:{
        login(){
            this.$router.push('/inicio');
        }
    }
}
</script>
