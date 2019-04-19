<template>
    <div class="container-fluid">
        <h3>Sistema de inventario</h3>
        <div class="row">
            <div class="col-md-3 offset-md-1">
                <img src="../assets/logo.png" class="img-thumbnail" alt="">
            </div>
            <!-- <registro></registro> -->
            <!-- <info></info> -->
            <add></add>
        </div>
    </div>
</template>
<script>
// import registro from './components/registroInventario'
// import info from './components/infoInventario'
import add from './components/addInventario'
export default {
    components:{
        add
    }
}
</script>
