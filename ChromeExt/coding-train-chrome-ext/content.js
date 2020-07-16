console.log('Message from content.js');

function testContent(){
    console.log('Message from inside testContent function');

    x = document.getElementsByTagName("title")[0].innerText;
    console.log(x);
    test();
}


// let socket = io('/index');               //Conenct to SocketIO
let socket = io.connect('http://127.0.0.1:5000/index');               //Conenct to SocketIO

socket.on( 'connect', function() {
  site = document.domain;
  socket.emit( 'testws', { data: 'CHROME EXTENSION: Test Message from ' + site + ' after socket IO connect' } );
  // socket.emit( 'testws', { data: 'CHROME EXTENSION: Test Message from after socket IO connect' } );
} );

socket.on( 'test_response', function( msg ) {
    console.log( 'CHROME EXTENSION:' + msg );
});

testContent();