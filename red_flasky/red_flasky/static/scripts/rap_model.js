
function Rapper(name, song, album) {
    this.name = name;
    this.song = song;
    this.album = album;
}

var rapper1 = new Rapper('Nas', 'NY State of Mind',  'Illmatic');
var rapper2 = new Rapper('2pac', 'All Eyes On Me', 'All Eyes On Me');
var rapper3 = new Rapper('50 Cent', 'Ghetto Quran', 'Power of the Dollar');

var rappers = [rapper1, rapper2, rapper3];
var rapper_number;
for (rapper_number in rappers) {
    var details1 = rappers[rapper_number].name;
    details1 += rappers[rapper_number].song;
    details1 += rappers[rapper_number].album;

    var list = document.getElementsByTagName('ul')[0];
    var newItemFirst = document.createElement('li');
    var newTextFirst = document.createTextNode(details1)
    newItemFirst.appendChild(newTextFirst);
    list.insertBefore(newItemFirst, list.firstChild);
}








