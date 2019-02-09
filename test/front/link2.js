/*
* @Author: Arius
* @Date:   2019-02-07 19:08:53
* @Last Modified by:   Arius
* @Last Modified time: 2019-02-09 16:19:00
*/

const WebSocket = require('ws');
const cookie = require('cookie');
 
const ws = new WebSocket(
    'http://127.0.0.1:3154/msg',
    [],
    {
        'headers': {
            // ekolia
            'Cookie': cookie.serialize('kl-auth', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50Ijp7ImlkIjoxMDAwNCwibmFtZSI6ImVrb2xpYSJ9LCJpYXQiOjE1NDk3MDAyOTksImV4cCI6MTU1MDMwNTA5OSwic2lnIjoiK3Q5ZzJvcW9YMWdYVEdNWFhvWlNlQzk5czgyMWlaWmJQNzJwZUhEMnViOGhMTDAvb2R3aGdqTVpVakZXRHZjcFhlWDJoTVNSOTJyZ1xuL25RREQ4QXZ4QT09XG4ifQ.CjPNBHxQEOfgSB6ljmf4XxQesE5Jf8bx6oaqmqBdj7k')
        }
    }
);
 
// ws.on('open', function open() {
//   ws.send(JSON.stringify(''));
// });
 
ws.on('message', function incoming(data) {
  console.log(data);
});