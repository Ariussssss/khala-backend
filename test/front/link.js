/*
* @Author: Arius
* @Date:   2019-02-07 19:08:53
* @Last Modified by:   Arius
* @Last Modified time: 2019-02-19 20:24:24
*/

const WebSocket = require('ws');
const cookie = require('cookie');
 
const ws = new WebSocket(
    'http://127.0.0.1:3154/msg',
    [],
    {
        'headers': {
            // ivy
            'Cookie': cookie.serialize('kl-auth', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50Ijp7ImlkIjo0LCJuYW1lIjoiaXZ5In0sImlhdCI6MTU1MDU3ODk4MiwiZXhwIjoxNTUxMTgzNzgyLCJzaWciOiJmRkJueE04QWxUdHVzaVVSaDlWODB3ckdwdjJyT0lvcEJQSGRSQWNzcDNMQk1QQnFHOWNVcDc5clZsSkt2dW5YNmdQRUFiRisydURHXG5aazJpK2gvNmlBPT1cbiJ9.3pVfbBWftfwuDFzL2YN9-m-je42LAKHa7ebzZOwmwuw')
        }
    }
);
 
ws.on('open', function open() {
  ws.send(JSON.stringify({
    to: 2,
    send: 1,
    type: 0,
    msg: 'hello',
    date: new Date().valueOf(),
  }));
});
 
ws.on('message', function incoming(data) {
  console.log(data);
});