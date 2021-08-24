const bookshelf = require('../utils/database');

const Owner = bookshelf.model('Owner',{
    tableName: 'ownerdetail',
    theatres() {
            return this.hasMany('Theatre');
    }
});

module.exports = Owner;