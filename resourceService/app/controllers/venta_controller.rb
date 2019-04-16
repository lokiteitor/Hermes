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
      params[:productos].each do |value|
        # por cada producto guardar un registro
        registro = VentaRegistro.new(producto_id:value[:producto_id],cantidad:value[:cantidad])
        registro.save      
        resultado[:productos].push(registro)
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
      params.require(:venta).permit(:usuario_id)
    end
end
