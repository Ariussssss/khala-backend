const WebSocket = require('ws');
const cookie = require('cookie');

const ws = new WebSocket(
    'http://127.0.0.1:3154/msg',
    [],
    {
        'headers': {
            // Ivy
            'Cookie': cookie.serialize('kl-auth', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50Ijp7ImlkIjoxNCwibmFtZSI6Ikl2eSJ9LCJpYXQiOjE1NTgwNTAwNTYsImV4cCI6MTU1ODY1NDg1Niwic2lnIjoiM3pSOUxJeFZvNTBQV2NxcmxNZFpKQXAwUTBlUjVEd2tkMEZrSStQYW1KWnBwSXd2WFBUQTdzejVidU14SzBrVGZkUDBtLzZGRElCQ1xuZjQ0RktuQUJPZz09XG4ifQ.zdrHIaWXvPyrvf720NhGE2q6lQR7PAU11HfckX_gkag')
        }
    }
);

const io = require('socket.io-client');
ws.on('open', function open() {
  ws.send(JSON.stringify({
    to: {
      id: 2,
      name: 'arius',
    },
    send: 0,
    type: 0,
    msg: 'Nice to meet you.My name is Ivy.',
    date: new Date().valueOf(),
  }));
});