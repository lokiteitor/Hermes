var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
var cors = require('cors');
//var bodyParser = require('body-parser')

//var indexRouter = require('./routes/index');
var usersRouter = require('./routes/users');
var productRouter = require('./routes/producto');
var ventaRoute = require('./routes/venta');

var app = express();

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));
app.use(cors({
    origin: 'http://localhost:8080'
}));
//app.use(bodyParser.json());

//app.use('/', indexRouter);
app.use('/users', usersRouter);
app.use('/producto',productRouter);
app.use('/venta',ventaRoute);

module.exports = app;
