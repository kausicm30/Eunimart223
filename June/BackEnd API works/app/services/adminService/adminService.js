var express = require('express');
var app = express();
var bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({extended:false}));
app.use(express.json());
var Owner = require('../../models/admin');
var Theatre = require('../../models/theatre');

class Admin{
    static async fetchAllDetails(req, res)
    {
         Owner.fetchAll({withRelated:['theatres']})
        .then((Owner)=>{
            return res.json({"Owner details with his theatre details": Owner});
        })
        .catch((err)=>{
            return res.status(200).json({"Message":err});
        })
    }
    static async fetchDetailsusingparameter(req, res)
    {
         Owner.where({email:req.params.email}).fetch({withRelated:['theatres']})
        .then((Owner)=>{
            return res.json({"Owner details with his theatre details": Owner});
        })
        .catch((err)=>{
            return res.status(200).json({"Message":err});
        })
    }
    static async fetchOwnerDetails(req, res)
    {
        var email = req.query.email;
        var id= req.query.id;
        Owner.where({email:email,id:id}).fetch()
        .then(Owner=>{
            return res.status(200).json({"Ownerdetails":Owner});
        })
        .catch(err=>{
            return res.status(200).json({"Message" : err});
        })
    }
    static async addTheatreDetails(req, res) {
        var email = req.body.email;
        var movieName = req.body.movieName;
        var time = req.body.time;
        var theatreName = req.body.theatreName;
        Owner.where({"email": email}).fetch()
        .then((Owner)=>{
            var oid = Owner.id;
            Theatre.forge({ownerdetail_id :oid, moviename : movieName, time:time, theatrename : theatreName}).save()
            .then(()=>{
                return res.status(200).json({"message":"successfully inserted"});
            })
            .catch((err)=>{
                return res.status(200).json({"Message":err});
            })
        })
        .catch((err)=>{
            return res.status(200).json({"Message":err});
        });
    }
    static async updateMovieDetails(req, res){
        var email = req.body.email;
        var theatreName = req.body.theatreName;
        var movieName = req.body.movieName;
        Owner.where({"email":email}).fetch()
        .then((Owner)=>{
            var oid = Owner.id;
            Theatre.where({"ownerdetail_id":oid,"theatrename" : theatreName}).save({"moviename":movieName},{patch:true})
            .then(()=>{
                return res.status(200).json({"message":"successfully updated"});
            })
            .catch((err)=>{
                return res.status(200).json({"Message":err});
            })
        })
        .catch((err)=>{
            return res.status(200).json({"Message":err});
        });
    }
    static async deleteTheatreDetails(req, res){
        var email = req.body.email;
        var theatreName = req.body.theatreName;
        Owner.where({"email":email}).fetch()
        .then((Owner)=>{
            var oid = Owner.id;
            Theatre.where({"ownerdetail_id":oid,"theatrename" : theatreName}).destroy()
            .then(()=>{
                return res.status(200).json({"Message":"successfully removed"});
            })
            .catch((err)=>{
                return res.status(200).json({"Message":err});
            })
        })
        .catch((err)=>{
            return res.status(200).json({"Message":err});
        });
    }
}

module.exports = Admin;