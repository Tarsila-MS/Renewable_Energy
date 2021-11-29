import app = require("teem");

app.run({
    port: 3000,
    sqlConfig: {
        connectionLimit: 30,
        charset: "utf8mb4",
        host: "localhost",
        port: 3306,
        user: "root",
        password: "root",
        database: "renewableenergy"
    }
});
