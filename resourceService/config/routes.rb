Rails.application.routes.draw do
  resources :venta
  resources :producto_registros
  get 'users/:id', to: 'users#show', constraints: { id: /[^\/]+/} , as: 'show'
  resources :productos
  resources :users
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
