var express = require('express');
var router = express.Router();
var request = require('request');
var config = require('../config');

// GET
router.get('/:id',function (req,res,next) {
  // obtener los datos de un usuario
  // obtener los datos de un api REST
  let options = {
    url: config.URL+'/users/'+req.params.id,  
  }
  
  request(options,function (error,response,body) {
    res.set('Content-Type','json/application');
    if (response.statusCode == 200) {
      res.send(body);
    }
    else{
      console.log(error);
      res.send(body);
    }
  })
})
// POST
router.post('/',function (req,res,next) {
  // crear nuevos usuarios
  // leer los datos y transformar a json
  let user = {
    "user":{
      username: req.param("username"),
      password: req.param("password"),
      email: req.param("email")
    }
  }

  var headers = {
    'Content-Type' : 'application/json'
  };

  var options = {
    url : config.URL+'/users',
    method: 'POST',
    headers: headers,
    json: true,
    body: user
  };
  console.log(options);
  request(options,function (error,response,body) {
    res.set('Content-Type','json/application');
    if (response.statusCode == 200) {
      res.send(body);
    }
    else{
      console.log(error);
      
      res.send(body);      
    }
  })  
})


// auth 
router.get('/:id/auth',function (req,res,next) {
  // crear los guards de autentificacion
  // atravez de esta apiGateway todas las solicitudes se autentifican
  // TODO : crear un middleware de auth
})

module.exports = router;
