var express = require('express');
var router = express.Router();
var request = require('request');
var config = require('../config');

// POST /venta
router.post('/',function (req,res,next) {
    // crear la venta por lotes
    // crear venta
    let ticket = {
        venta:{
            usuario_id: req.param("usuario")
        },
        productos: req.param("productos")
    }    

    let options = {
        url: config.URL+'/venta',
        method: 'POST',
        json: true,
        body: ticket
    }
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

module.exports = router;
