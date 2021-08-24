const bookshelf = require('../utils/database');

const Threatre = bookshelf.model('Theatre',{
    tableName: 'theatredetail'
});

module.exports = Threatre;