//backgroundScript.js
//Below script is executed whenever extension button is clicked
console.log("Inside backgrouns.js");
chrome.browserAction.onClicked.addListener(
    function(tab) {
        chrome.tabs.executeScript(tab.id, {
        "file": "contentScript.js"
    });
});

