console.log('Message from content.js');
let socket = io.connect('http://127.0.0.1:5000/index');               //Conenct to SocketIO
let count = 0;

socket.on( 'connect', function() {
  site = document.domain;
  socket.emit( 'testws', { data: 'CHROME EXTENSION: Test Message from ' + site + ' after socket IO connect' } );
  // socket.emit( 'testws', { data: 'CHROME EXTENSION: Test Message from after socket IO connect' } );
} );

socket.on( 'test_response', function( msg ) {
  console.log( 'CHROME EXTENSION:' + msg );
});


function getLTP(){
  ltp = document.getElementsByClassName("last-price");
  for (var i = 0; i < ltp.length; i++) {
    console.log(ltp[i].innerText); //second console output
  }
  setTimeout(() => {  getLTP(); }, 1000);
}

function getInstruments(){
  let ltp_data = {};
  try {
    let lstInst = $("[class*='index']");
    for (var i = 0; i < lstInst.length; i++) {
      instName = $(lstInst[i]).find(".nice-name")[0].innerText;
      instLTP = $(lstInst[i]).find(".last-price")[0].innerText;
      // console.log(instName + ' -> ' + instLTP ); 
      ltp_data[instName] = instLTP;
    } 
    ltp_data['count'] = count;
    count = count + 1;
    console.log(ltp_data); 
    socket.emit( 'ltp_tick', ltp_data );  
  } catch (error) {
    console.log(error);
  }
  setTimeout(() => {  getInstruments(); }, 1000);
}

// getLTP();
setTimeout(() => {  getInstruments(); }, 1000);



