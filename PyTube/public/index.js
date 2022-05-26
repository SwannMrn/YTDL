const express = require('express');
const cors = require('cors');
const fs = require('fs')
const ytdl = require('ytdl-core');
const app = express();

const path = require('path')
app.use('/static', express.static(path.join(__dirname, 'public')))

app.use(cors());

app.listen(4000, () => {
    console.log('Server works at port 4000');
});

app.get('/', function(req,res){
  res.sendFile(__dirname + '/index.html');
}); 

app.get('/download', (req,res) => {
    var URL = req.query.URL;
    res.json({url:URL});
})

/*function download() {
  ytdl.validateURL(globalVariable.URL)
  ytdl(globalVariable.URL)
    .pipe(fs.createWriteStream('video.mp4'))
  return
}
*/