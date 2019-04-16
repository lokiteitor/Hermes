class CreateProductos < ActiveRecord::Migration[5.2]
  def change
    create_table :productos do |t|
      t.text :description
      t.float :cost
      t.timestamps
    end  
  end
end
