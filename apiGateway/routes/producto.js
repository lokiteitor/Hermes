var express = require('express');
var router = express.Router();
var request = require('request');
var config = require('../config');


// POST /producto/
router.post("/",function (req,res,next) {
    // crear el producto
    let producto = {
        "product":{
            description: req.param("description"),
            cost: req.param("cost")
        }
    }

    var options = {
        url : config.URL+'/productos',
        method: 'POST',
        json: true,
        body: producto
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

// GET /producto/:id
router.get("/:id",function (req,res,next) {
    // obtener los datos de un producto especifico 
    // incluyendo sus datos de inventario
    let options = {
        url: config.URL+'/productos/'+req.params.id,
        method: 'GET'
    }
    console.log(options)
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

// POST /producto/inventario
router.post("/inventario",function (req,res,next) {
  // registrar un producto en el inventario
  let registro = {
    producto_registro: {
      producto_id: req.param("producto_id"),
      cantidad: req.param("cantidad")
    }
  }
  let options = {
    url : config.URL+'/producto_registros',
    method:'POST',
    json: true,
    body: registro
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

// GET /producto/:id/inventario
router.get("/:id/inventario",function (req,res,next) {
  // obtener los registros de inventario en crudo 
  // procesar y hacer el recuento en base a la tabla ventas
  let options = {
      url: config.URL+'/producto_registros/'+req.params.id,
      method: 'GET'
  }
  
  console.log(options)
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


module.exports = router;
