var express = require('express');
var router = express.Router();

// GET
router.get('/:id',function (req,res,next) {
  // obtener los datos de un usuario
  // obtener los datos de un api REST
  res.end()
})
// POST
router.post('/',function (req,res,next) {
  // crear nuevos usuarios
  res.end()
})


// auth 
router.get('/:id/auth',function (req,res,next) {
  // crear los guards de autentificacion
  // atravez de esta apiGateway todas las solicitudes se autentifican
  // TODO : crear un middleware de auth
})

module.exports = router;
