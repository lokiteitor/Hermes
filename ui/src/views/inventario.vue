<template>
    <div class="container-fluid">
        <br>
        <h3 class="text-center">Sistema de inventario</h3>
        <div class="row">

            <imagen></imagen>
            <div class="col-md-7">
                <ul class="nav nav-tabs" id="menu" role="tablist">
                <li class="nav-item">
                    <a class="nav-link active" id="registro-tab" data-toggle="tab" href="#registro" role="tab" aria-controls="registro" aria-selected="true">Registro</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" id="info-tab" data-toggle="tab" href="#info" role="tab" aria-controls="info" aria-selected="false">Informacion</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" id="add-tab" data-toggle="tab" href="#add" role="tab" aria-controls="add" aria-selected="false">Añadir</a>
                </li>
                </ul>    
                <div class="tab-content" id="myTabContent">
                    <div class="tab-pane fade show active" id="registro" role="tabpanel" aria-labelledby="registro-tab">
                        <registro ></registro>
                    </div>
                    <div class="tab-pane fade" id="info" role="tabpanel" aria-labelledby="info-tab">
                        <info></info>
                    </div>
                    <div class="tab-pane fade" id="add" role="tabpanel" aria-labelledby="add-tab">
                        <registro v-bind:isregistro='true'></registro>
                    </div>
                </div>                                                
            </div>

        </div>
    </div>
</template>
<script>
import registro from './components/registroInventario'
import info from './components/infoInventario'
import imagen from './components/imagen'

export default {
    components:{
        imagen,
        registro,
        info
    }
}
</script>
