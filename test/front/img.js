/*
* @Author: Arius
* @Date:   2019-02-07 19:08:53
* @Last Modified by:   Arius
* @Last Modified time: 2019-05-17 07:45:20
*/

const WebSocket = require('ws');
const cookie = require('cookie');

const ws = new WebSocket(
    'http://127.0.0.1:3154/msg',
    [],
    {
        'headers': {
            // Ekolia
            'Cookie': cookie.serialize('kl-auth', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50Ijp7ImlkIjoxNSwibmFtZSI6IkxlbmEifSwiaWF0IjoxNTU4MDUwMjAxLCJleHAiOjE1NTg2NTUwMDEsInNpZyI6IjlqMkxNVmpZWis5TWdRdXlDeXN1a2NIV29YR0hUZnUvRzJkZTY5bTZBOU92ZUJIRHhwbUVmcC9uTU9XZUc5RGZ2MWxNVjJ4RFVWY1FcblAwdlEwQkxWanc9PVxuIn0.5OyssEqnoo3EFeMix96Rw1glYnQAzN7azvYmM9GcXDg')
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
    msg: 'Hi',
    date: new Date().valueOf(),
  }));
  ws.send(JSON.stringify({
    to: {
      id: 2,
      name: 'arius',
    },
    send: 0,
    type: 1,
    msg: 'https://oimagec6.ydstatic.com/image?id=8190213621634606592&product=adpublish&w=640&h=480&sc=0&rm=2&gsb=0&gsbd=60',
    date: new Date().valueOf(),
  }));
});