const express = require('express');
const cors = require('cors');
const fs = require('fs')
const ytdl = require('ytdl-core');
const app = express();

app.use(cors());

app.listen(4000, () => {
    console.log('Server works at port 4000');
});

app.use(express.static('Server'))

app.get('/download', (req,res) => {
    var URL = req.query.URL;
    res.json({url:URL});
})

app.get('/', function(req,res){
 res.sendfile(__dirname + '/index.html');
}); 

function download() {
  ytdl.validateURL()
  ytdl('')
    .pipe(fs.createWriteStream('video.mp4'))
  return
}