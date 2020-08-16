document.querySelector('#kiteStart').addEventListener('click', () => {
    chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
        chrome.tabs.sendMessage(tabs[0].id, {"message": "startKite"});
    });
    console.log("Kite Start Requested");
});

document.querySelector('#kiteStop').addEventListener('click', () => {
    chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
        chrome.tabs.sendMessage(tabs[0].id, {"message": "stopKite"});
    });
    console.log("Kite Stop Requested");
});


chrome.runtime.onMessage.addListener(
    function(request, sender, sendResponse) {
        if( request.message === "kite_started" ) {
            let statusText = "Kite Scrapper Started";
            document.querySelector("#response").innerHTML = statusText;
            console.log(statusText);
        }
        if( request.message === "kite_stopped" ) {
            let statusText = "Kite Scrapper Stopped";
            document.querySelector("#response").innerHTML = statusText;
            console.log(statusText);
        }
        if( request.message === "kite_already_started" ) {
            let statusText = "Kite is already Running";
            document.querySelector("#response").innerHTML = statusText;
            console.log(statusText);
        }
    }
);