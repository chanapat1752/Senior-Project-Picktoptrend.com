var mongoose = require('mongoose');
var graphSchema = mongoose.Schema({
    month : {type : String,required: true},
    year : {type : String,required: true},
    graph : {type : Array}
},{ collection : 'UI'}
);
module.exports = mongoose.model('Graph', graphSchema);