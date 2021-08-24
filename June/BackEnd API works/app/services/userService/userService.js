var express = require('express');
var app = express();
var bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({extended:false}));
app.use(express.json());

 var Theatre = require('../../models/theatre');

class User{
    static async fetchMovieDetails(req, res)
    {
        var movieName = req.body.movieName;
        Theatre.where({"moviename": movieName}).fetchAll({columns: ['moviename','theatrename','time']})
        .then((Theatre)=>{
            if(Theatre.length > 0)
                return res.json({"Movie details": Theatre});
            else
                return res.status(200).json({"Message":"Not available"});
        })
        .catch((err)=>{
            return res.status(200).json({"Message":err});
        })
    }
}
module.exports = User;