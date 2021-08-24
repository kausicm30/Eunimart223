var express = require('express');
var router = express();
var { Validator, ValidationError } = require('express-json-validator-middleware');
var validator = new Validator({allErrors: true});
var validate = validator.validate;
var adminSchema = require('../routes/validationSchemas/adminSchema');
var Admin = require('../services/adminService/adminService');

//fetch all admin details with theatre details also
router.get('/displayDetails', function(req, res)
{
   Admin.fetchAllDetails(req, res);
});

//fetch one admin details with respective details theatre details also by using parameter value
router.get('/details/:email', function(req, res)
{
   Admin.fetchDetailsusingparameter(req, res);
});

//fetch admin details
router.get('/ownerdetails',function(req,res)
{
   Admin.fetchOwnerDetails(req,res);
});

//add theatre details with movies
router.post('/addTheatreDetails',validate({body:adminSchema.addDetailsSchema}),function(req, res)
{
   Admin.addTheatreDetails(req, res);
});

//update movie details
router.post('/updateMovieDetails',validate({body:adminSchema.updateDetailsSchema}),function(req, res)
{
   Admin.updateMovieDetails(req, res);
});

//delete theatre details with respect to owner
router.post('/deleteTheatreDetails',validate({body:adminSchema.deleteDetailsSchema}),function(req, res)
{
   Admin.deleteTheatreDetails(req, res);
});

router.use(function(err, req, res, next) {
   if (err instanceof ValidationError) {
       res.status(400).send(err);
   }
   else next(err);
});

module.exports = router;