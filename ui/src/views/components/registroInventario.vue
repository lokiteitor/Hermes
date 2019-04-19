<template>
    <div class="col-md-7">
        <div class="form-group">
            <label for="descripcion">Descripcion del producto</label>
            <input type="text" class="form-control" name="descripcion" id="descripcion" aria-describedby="helpId" placeholder="descripcion">
            <small id="helpId" class="form-text text-muted">Ingrese la descripcion del producto</small>
        </div>        
        <div class="form-group">
          <label for="cantidad">Cantidad</label>
          <input type="number"
            class="form-control" name="cantidad" id="cantidad" aria-describedby="cantidadID" placeholder="cantidad">
          <small id="cantidadID" class="form-text text-muted">Ingrese la cantidad de producto a registrar</small>
        </div>
        <div class="form-group">
          <label for="precio">Precio</label>
          <input type="number"
            class="form-control" name="precio" id="precio" aria-describedby="precioHelp" placeholder="precio">
          <small id="precioHelp" class="form-text text-muted">Precio del producto</small>
        </div>
        <div class="row">
            <div class="col-md-auto">
                <a name="" id="" class="btn btn-success" href="#" role="button">Registrar</a>
            </div>
            <div class="col-md-auto">
                <a name="cancelarButton" id="cancelarButton" class="btn btn-danger" href="#" role="button">Cancelar</a>
            </div>
            
        </div>
    </div>
</template>
