var http = require("http")

http.createServer((res, req) => {

    const data = {
        message: {
            hello: "world",
            world: "hello"
        }
    }
    res.end(JSON.Stringify(data))
}).listen("8080")