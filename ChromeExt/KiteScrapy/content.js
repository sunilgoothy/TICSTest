// console.log('content.js started....');
let socket = io.connect('http://127.0.0.1:5000/index');               //Conenct to SocketIO
let count = 0;
let getLTP_loop_started = false;
let get_interval = 1000; //loop interval in ms for reading ltp

socket.on( 'connect', function() {
  site = document.domain;
  socket.emit( 'testws', { data: 'CHROME EXTENSION: Test Message from ' + site + ' after socket IO connect' } );
  // socket.emit( 'testws', { data: 'CHROME EXTENSION: Test Message from after socket IO connect' } );
} );

socket.on( 'test_response', function( msg ) {
  console.log( 'CHROME EXTENSION:' + msg );
});

function getLTP(){
  let ltp_data = {};
  try {
    let lstInst = $("[class*='index']");
    for (var i = 0; i < lstInst.length; i++) {
      instName = $(lstInst[i]).find(".nice-name")[0].innerText;
      instLTP = $(lstInst[i]).find(".last-price")[0].innerText;
      ltp_data[instName] = instLTP;
    } 
    ltp_data['count'] = count;
    count = count + 1;
    console.log(ltp_data); 
    socket.emit( 'ltp_tick', ltp_data );  
  } catch (error) {
    console.log(error);
  }
  if(getLTP_loop_started){
    setTimeout(() => {  getLTP(); }, get_interval);
  }
};


chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {
    if( request.message === "startKite" ) {
      console.log("Start Event received from popup");
      if(!getLTP_loop_started){
        setTimeout(() => {  getLTP(); }, 1000);
        getLTP_loop_started = true;
        chrome.runtime.sendMessage({"message": "kite_started"});
      }else{
        chrome.runtime.sendMessage({"message": "kite_already_started"});
      }
     }
   }
 );

 chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {
    if( request.message === "stopKite" ) {
      console.log("Stop Event received from popup");
      getLTP_loop_started = false;
      chrome.runtime.sendMessage({"message": "kite_stopped"});
     }
   }
 );


