var userSchema = {
    type:'object',
    required: ['movieName'],
    properties:{
        movieName: {
            type:'string',
            minLength:1
        }
    }
}

module.exports =userSchema;
