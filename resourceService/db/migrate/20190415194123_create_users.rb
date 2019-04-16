class CreateUsers < ActiveRecord::Migration[5.2]
  def change
    create_table :users, id: false do |t|
      t.string :username
      t.string :password
      t.string :email    
      t.timestamps          
    end
    add_index :users,:email,unique: true
  end
end
