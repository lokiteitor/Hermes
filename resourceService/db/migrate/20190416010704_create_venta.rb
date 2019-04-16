class CreateVenta < ActiveRecord::Migration[5.2]
  def change
    create_table :venta do |t|
      t.string :user_id
      t.timestamps
    end
    add_foreign_key :venta , :users, primary_key: 'email'
  end
end
