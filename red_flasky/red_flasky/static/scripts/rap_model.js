
function Rapper(name, song, album) {
    this.name = name;
    this.song = song;
    this.album = album;
}

// Create these using python/Jinja2 
var rapper1 = new Rapper('Nas', 'NY State of Mind',  'Illmatic');
var rapper2 = new Rapper('2pac', 'All Eyes On Me', 'All Eyes On Me');
var rapper3 = new Rapper('50 Cent', 'Ghetto Quran', 'Power of the Dollar');

var rappers = [rapper1, rapper2, rapper3];
var rapper_number;
//create quote-box divs 
var quoteContainers = document.getElementById('quote-containers');
var quote_box = `
'<h1> Some shit </h1>'
`
;

quoteContainers.innerHTML = quote_box;

$ul