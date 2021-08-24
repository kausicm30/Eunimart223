var express = require('express');
var router = express();
var { Validator, ValidationError } = require('express-json-validator-middleware');
var validator = new Validator({allErrors: true});
var validate = validator.validate;
var userSchema = require('../routes/validationSchemas/userSchema');
var User = require('../services/userService/userService');

router.get('/', function(req, res)
{
   res.status(200).json({"Message":"server running successfully"});
});

//get the theatre details while enter the movie name
router.post('/getMovieDetails', validate({body:userSchema}),function(req, res)
{
   User.fetchMovieDetails(req, res);
});
router.use(function(err, req, res, next) {
   if (err instanceof ValidationError) {
       res.status(400).send(err);
   }
   else next(err);
});

module.exports = router;