<template>
    <div class="col-md-7">
        <div class="form-group">
            <label for="descripcion">Descripcion del producto</label>
            <input type="text" class="form-control" name="descripcion" id="descripcion" aria-describedby="helpId" placeholder="descripcion" v-model="descripcion">
            <small id="helpId" class="form-text text-muted">Ingrese la descripcion del producto</small>
        </div>        
        <div class="form-group" v-if="registro">
          <label for="cantidad">Cantidad</label>
          <input type="number"
            class="form-control" name="cantidad" id="cantidad" aria-describedby="cantidadID" placeholder="cantidad" v-model="cantidad" >
          <small id="cantidadID" class="form-text text-muted">Ingrese la cantidad de producto a registrar</small>
        </div>
        <div class="form-group">
          <label for="precio">Precio</label>
          <input type="number"
            class="form-control" name="precio" id="precio" aria-describedby="precioHelp" placeholder="precio" v-model="precio" >
          <small id="precioHelp" class="form-text text-muted">Precio del producto</small>
        </div>
        <div class="row">
            <div class="col-md-auto">                
                <a name="addelementos" id="addelementos" class="btn btn-success btn-lg" href="#" role="button" v-if="registro" @click="addToStock">Añadir elementos</a>
                <a name="registrarelementos" id="registrarelementos" class="btn btn-success btn-lg " href="#" role="button" v-else @click="registrarToStock">Registrar</a>
            </div>
            <div class="col-md-auto">
                <a name="cancelarButton" id="cancelarButton" class="btn btn-danger btn-lg " href="#" role="button" @click="limpiar">Cancelar</a>
            </div>
            
        </div>
    </div>
</template>
<script>
import axios from 'axios'
export default {
  props:['isregistro'],
  data(){
    return{
      descripcion:null,
      precio:null,
      cantidad:null,
      registro:this.isregistro
    }
  },
  methods:{
    addToStock(){
      // producto registro
      // añadir n cantidad de elementos del producto al 
      // inventario
      // TODO :para modificar primero se debe buscar el producto por nombre o
      // foto
    },
    limpiar(){
      // limpiar la entrada de datos
      this.descripcion = ""
      this.precio = ""

    },
    registrarToStock(){
      // producto
      // añadir un tipo de producto al inventario
      console.log("Registrando")
      axios({
        method:'post',
        baseURL: process.env.VUE_APP_API_URL,
        url: '/producto',
        responseType: 'json',
        data:{
          description : this.descripcion,
          cost: this.precio
        }
      }).then(res => {
        console.log("Exito"+res.toString())
        this.limpiar()
      }).catch(err => {
        console.log("Error"+err.toString());
      })

    }
  }
}
</script>

