require 'test_helper'

class ProductosControllerTest < ActionDispatch::IntegrationTest
  setup do
    @producto = productos(:one)
  end

  test "should get index" do
    get productos_url, as: :json
    assert_response :success
  end

  test "should create producto" do
    assert_difference('Producto.count') do
      post productos_url, params: { producto: { cost: @producto.cost, descripcion: @producto.descripcion, id_producto: @producto.id_producto } }, as: :json
    end

    assert_response 201
  end

  test "should show producto" do
    get producto_url(@producto), as: :json
    assert_response :success
  end

  test "should update producto" do
    patch producto_url(@producto), params: { producto: { cost: @producto.cost, descripcion: @producto.descripcion, id_producto: @producto.id_producto } }, as: :json
    assert_response 200
  end

  test "should destroy producto" do
    assert_difference('Producto.count', -1) do
      delete producto_url(@producto), as: :json
    end

    assert_response 204
  end
end
