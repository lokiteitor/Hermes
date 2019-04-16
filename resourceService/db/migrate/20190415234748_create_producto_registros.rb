class CreateProductoRegistros < ActiveRecord::Migration[5.2]
  def change
    create_table :producto_registros do |t|
      t.integer :cantidad
      t.bigint :producto_id
      t.timestamps
    end    
    add_foreign_key :producto_registros , :productos
  end  
end
