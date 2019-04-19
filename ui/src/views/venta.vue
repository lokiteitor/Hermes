<template>
    <div class="container-fluid">
        <br>
        <h3 class="text-center">Punto de venta</h3>
        <div class="row">
            <imagen></imagen>
            <div class="col-md-7">
                <div class="form-group">
                  <label for="descripcion">Descripcion</label>
                  <input type="text"
                    class="form-control" name="descripcion" id="descripcion" aria-describedby="helpdescp" placeholder="descripcion">
                  <small id="helpdescp" class="form-text text-muted">Descricion del producto</small>
                </div>
                <div class="form-group">
                  <label for="precio">Precio Unitario</label>
                  <input type="number"
                    class="form-control" name="precio" id="precio" aria-describedby="helpprecio" placeholder="precio">
                  <small id="helpprecio" class="form-text text-muted">Precio por unidad</small>
                </div>                
                <div class="form-group">
                  <label for="cantidad">Cantidad</label>
                  <input type="number"
                    class="form-control" name="cantidad" id="cantidad" aria-describedby="helpcant" placeholder="cantidad">
                  <small id="helpcant" class="form-text text-muted">Ingrese la cantidad a vender</small>
                </div>
                <div class="form-group">
                  <label for="subtotal">Subtotal</label>
                  <input type="number" name="subtotal" id="subtotal" class="form-control" placeholder="subtotal" aria-describedby="helpSubt">
                  <small id="helpSubt" class="text-muted">Subtotal</small>
                </div>
                <div class="row">
                    <div class="col-md-auto">
                        <a name="add" id="add" class="btn btn-success btn-lg " href="#" role="button">Añadir</a>
                    </div>
                    <div class="col-md-auto">
                        <a name="cancelar" id="cancelar" class="btn btn-danger btn-lg " href="#" role="button">Cancelar</a>
                    </div>
                </div>                
            </div>        
        </div>
        <br>
        <div class="row">
            <div class="col-md-8 offset-md-2">
                <table class="table">
                    <thead>
                        <tr>
                            <th>Producto</th>
                            <th>Cantidad</th>
                            <th>Precio</th>
                            <th>Subtotal</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td scope="row">N producto</td>
                            <td>N cantidad</td>
                            <td>N precio</td>
                            <td>N subtotal</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>
<script>
import imagen from './components/imagen'
export default {
    components:{
        imagen
    }
}
</script>
