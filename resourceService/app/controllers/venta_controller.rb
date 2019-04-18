class VentaController < ApplicationController
  before_action :set_ventum, only: [:show, :update, :destroy]

  # GET /venta
  def index
    @venta = Ventum.all

    render json: @venta
  end

  # GET /venta/1
  def show
    render json: @ventum
  end

  # POST /venta
  def create
    @ventum = Ventum.new(ventum_params)
    
    resultado = {:venta=>{},:productos=>[]}
    vres = @ventum.save
    if vres
      @ventas.each do |value|
        if disponibilidad value
          # por cada producto guardar un registro
          registro = RegistroVentum.new(producto_id:value[:producto_id],cantidad:value[:cantidad],ventum_id:@ventum.id)
          registro.save      
          resultado[:productos].push(registro)          
        end
      end
    end
        
    if vres
      resultado[:venta] = @ventum
      render json: resultado, status: :created, location: @ventum
    else
      render json: @ventum.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /venta/1
  def update
    if @ventum.update(ventum_params)
      render json: @ventum
    else
      render json: @ventum.errors, status: :unprocessable_entity
    end
  end

  # DELETE /venta/1
  def destroy
    @ventum.destroy
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_ventum
      @ventum = Ventum.find(params[:id])
    end

    # Only allow a trusted parameter "white list" through.
    def ventum_params
      @ventas = params[:venta][:productos]
      puts @ventas      
      params.require(:venta).permit(:user_id)
    end

    def disponibilidad producto
      # revisar la diponibilidad de los productos requeridos 
      # producto comparar registros con ventas
      # buscar los registros en el inventario
      cantidad = 0
      flag = false
      ProductoRegistro.where(producto_id: producto[:producto_id]).find_each do | registro |
        cantidad += registro.cantidad
      end
      # buscar las ventas y restar los  registros
      RegistroVentum.where(producto_id:producto[:producto_id]).find_each do | registro |
        cantidad -= registro.cantidad
      end

      puts producto[:producto_id]
      puts cantidad
      if cantidad > 0
        flag = true
      end
      return flag
    end
end
