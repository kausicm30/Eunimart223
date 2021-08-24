const knex = require('knex')({
    client:'mysql',
    connection:{
        host: 'localhost',
        user: 'root',
        password: '',
        database: 'movieticketbooking',
        charset: 'utf8'
    }
});

 const bookshelf = require('bookshelf')(knex);

 module.exports=bookshelf;