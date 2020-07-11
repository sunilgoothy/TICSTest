//contentScript.js
// x = document.title;
// y = document.getElementsByClassName('instrument-widget')[0].getElementsByTagName('span')[1].getElementsByClassName('last-price')[0].innerText
// console.log(x)
// console.log(y)
// delete x;

test()
function getNifty50() {
    y = document.getElementsByClassName('instrument-widget')[0].getElementsByTagName('span')[1].getElementsByClassName('last-price')[0].innerText;
    console.log(y);
    setTimeout(getNifty50, 1000);
};

getNifty50()
