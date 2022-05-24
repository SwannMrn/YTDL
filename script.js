var convertBtn = document.querySelector('.convert-button');
var URLinput = document.querySelector('.URL-input');

function sendURL(URL) {
    fetch(`http://localhost:4000/download?URL=${URL}`, {
        method:'GET'
    }).then(res => res.json())
    .then(json => console.log(json));
}

convertBtn.addEventListener('click', () => {
    console.log(`URL: ${URLinput.value}`);
    sendURL(URLinput.value);
});
