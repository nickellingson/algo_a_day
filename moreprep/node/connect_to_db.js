var mysql = require('mysql');

var con = mysql.createConnection({
    host:"test",
    user:"user",
    password: "pass"
})


con.connect( function (err) {
    if (err) throw err;
    con.query("SELECT * FROM customers", function (err, result, fields){
        if (err) throw err;
        console.log(result)
    })
})