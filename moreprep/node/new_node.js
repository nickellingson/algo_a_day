const http = require("http")
const fs = require("http")

http.createServer((req, res) => {
    res.end("hello world")
}).listen("8080")


http.createServer((req, res) => {
    fs.readFile("index.html", (err, data) => {
        if (err) {
            res.writeHead(500, {"content-type":"text/plain"})
            res.end("internal server error")
        }
        else {
            res.writeHead(200, {"content-type":"text/html"})
            res.end(data)
        }
    })
})