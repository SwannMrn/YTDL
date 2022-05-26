// Imports
const express = require('express')
const cors = require('cors');
const ytdl = require('ytdl-core');
const app = express()
const port = 5000

// Use cors for GET requests
app.use(cors())

// Listen on Port 5000
app.listen(port, () => console.info(`App listening on port ${port}`))

// Static Files
app.use(express.static('public'));

app.get('/', function(req,res){
  res.sendFile(__dirname + '/public/index.html');
}); 

app.get('/download', (req,res) => {
    var URL = req.query.URL;
    res.json({url:URL});
})
