class ProductoRegistrosController < ApplicationController
  before_action :set_producto_registro, only: [:update, :destroy]
  before_action :search_all_register , only: [:show]

  # GET /producto_registros
  def index
    @producto_registros = ProductoRegistro.all

    render json: @producto_registros
  end

  # GET /producto_registros/1
  def show
    producto = {:producto_id=> params[:id],:cantidad=>@Nregistros}
    render json: producto
  end

  # POST /producto_registros
  def create
    @producto_registro = ProductoRegistro.new(producto_registro_params)

    if @producto_registro.save
      render json: @producto_registro, status: :created, location: @producto_registro
    else
      render json: @producto_registro.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /producto_registros/1
  def update
    if @producto_registro.update(producto_registro_params)
      render json: @producto_registro
    else
      render json: @producto_registro.errors, status: :unprocessable_entity
    end
  end

  # DELETE /producto_registros/1
  def destroy
    @producto_registro.destroy
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_producto_registro
      @producto_registro = ProductoRegistro.find(params[:id])
    end

    def search_all_register
      # buscar todos los registros de ese producto
      @Nregistros = 0
      ProductoRegistro.where(producto_id: params[:id]).find_each do | registro |
        @Nregistros += registro.cantidad
      end 
    end

    # Only allow a trusted parameter "white list" through.
    def producto_registro_params
      params.require(:producto_registro).permit(:cantidad,:producto_id)
    end
end
