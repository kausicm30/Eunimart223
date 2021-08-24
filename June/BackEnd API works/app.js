var express = require('express');
var app = express();
const session = require('express-session');
var bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({extended:false}));
app.use(express.json());

const adminRoutes = require('./app/routes/adminRoutes');
const userRoutes = require('./app/routes/userRoutes');

app.use('/', userRoutes);
app.use('/admin', adminRoutes);


var port =3030;
var server=app.listen(port,function()
{
    console.log(`Server listen on port ${port}`);
});