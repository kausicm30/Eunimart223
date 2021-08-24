var addDetailsSchema ={
    type:'object',
    required:['email','movieName','time','theatreName'],
    properties:{
        email:{
            type:'string'
        },
        movieName: {
            type:'string',
            minLength:1
        },
        time: {
            type:'string'
        },
        theatreName: {
            type:'string'
        }
    }
}
var updateDetailsSchema ={
    type:'object',
    required:['email','theatreName','movieName'],
    properties:{
        email:{
            type:'string'
        },
        theatreName: {
            type:'string'
        },
        movieName: {
            type:'string',
            minLength:1
        }
    }
}
var deleteDetailsSchema ={
    type:'object',
    required:['email','theatreName'],
    properties:{
        email:{
            type:'string'
        },
        theatreName: {
            type:'string'
        }
    }
}
var AdminSchema = {"addDetailsSchema":addDetailsSchema,
                    "updateDetailsSchema":updateDetailsSchema,
                    "deleteDetailsSchema":deleteDetailsSchema};
module.exports = AdminSchema;