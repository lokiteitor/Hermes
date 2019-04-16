require 'test_helper'

class ProductoRegistrosControllerTest < ActionDispatch::IntegrationTest
  setup do
    @producto_registro = producto_registros(:one)
  end

  test "should get index" do
    get producto_registros_url, as: :json
    assert_response :success
  end

  test "should create producto_registro" do
    assert_difference('ProductoRegistro.count') do
      post producto_registros_url, params: { producto_registro: { cantidad: @producto_registro.cantidad } }, as: :json
    end

    assert_response 201
  end

  test "should show producto_registro" do
    get producto_registro_url(@producto_registro), as: :json
    assert_response :success
  end

  test "should update producto_registro" do
    patch producto_registro_url(@producto_registro), params: { producto_registro: { cantidad: @producto_registro.cantidad } }, as: :json
    assert_response 200
  end

  test "should destroy producto_registro" do
    assert_difference('ProductoRegistro.count', -1) do
      delete producto_registro_url(@producto_registro), as: :json
    end

    assert_response 204
  end
end
