class CreateRegistroVenta < ActiveRecord::Migration[5.2]
  def change
    create_table :registro_venta do |t|
      t.integer :cantidad
      t.bigint :ventum_id
      t.bigint :producto_id
      t.timestamps
    end
    add_foreign_key :registro_venta , :venta
    add_foreign_key :registro_venta, :productos
  end
end
