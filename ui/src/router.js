import Vue from 'vue'
import Router from 'vue-router'


// vistas
import Login from './views/login'
import Inventario from './views/inventario'
import Venta from './views/venta'
import Registro from './views/registro'


Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [{
    path:'/login',
    name: 'Login',
    component: Login
  },{
    path: '/inventario',
    name: 'Inventario',
    component: Inventario    
  },{
    path: '/venta',
    name: 'Punto de venta',
    component: Venta
  },{
    path: '/registro',
    name: 'Registro',
    component: Registro
  }
  ]
})
