require 'test_helper'

class VentaControllerTest < ActionDispatch::IntegrationTest
  setup do
    @ventum = venta(:one)
  end

  test "should get index" do
    get venta_url, as: :json
    assert_response :success
  end

  test "should create ventum" do
    assert_difference('Ventum.count') do
      post venta_url, params: { ventum: { usuario_id: @ventum.usuario_id } }, as: :json
    end

    assert_response 201
  end

  test "should show ventum" do
    get ventum_url(@ventum), as: :json
    assert_response :success
  end

  test "should update ventum" do
    patch ventum_url(@ventum), params: { ventum: { usuario_id: @ventum.usuario_id } }, as: :json
    assert_response 200
  end

  test "should destroy ventum" do
    assert_difference('Ventum.count', -1) do
      delete ventum_url(@ventum), as: :json
    end

    assert_response 204
  end
end
