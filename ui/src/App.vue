<template>
  <div id="app">
    <!-- Navegacion -->
    <nav class="navbar navbar-expand-md navbar-light bg-light">
      <a class="navbar-brand" href="#" @click="inicio">Inicio</a>
      <button class="navbar-toggler d-lg-none" type="button" data-toggle="collapse" data-target="#navBar" aria-controls="navBar"
          aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navBar">
        <ul class="navbar-nav mr-auto mt-2 mt-lg-0">
          <li class="nav-item">
            <a class="nav-link" href="#" @click="login">Login</a>            
          </li>
          <li class="nav-item">
            <a href="#" class="nav-link" @click="registro">Registro</a>
          </li>
          <li class="nav-item">
            <a href="#" class="nav-link" @click="inventario">Inventario</a>
          </li>
          <li class="nav-item">
            <a href="#" class="nav-link" @click="venta">Punto de Venta</a>
          </li>
        </ul>
      </div>
    </nav>
    <router-view/>
  </div>
</template>
<script>
export default {
  methods:{
    inventario(){
      this.$router.push('/inventario')
    },
    venta(){
      this.$router.push('/venta')
    },
    login(){
      this.$router.push('/login')
    },
    registro(){
      this.$router.push('/registro')
    },
    inicio(){
      this.$router.push('/')
    }

  }
}
</script>


