/*
* @Author: Arius
* @Date:   2019-02-07 19:08:53
* @Last Modified by:   Arius
* @Last Modified time: 2019-02-19 20:24:08
*/

const WebSocket = require('ws');
const cookie = require('cookie');
 
const ws = new WebSocket(
    'http://127.0.0.1:3154/msg',
    [],
    {
        'headers': {
            // ekolia
            'Cookie': cookie.serialize('kl-auth', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50Ijp7ImlkIjoxLCJuYW1lIjoiZWtvbGlhIn0sImlhdCI6MTU1MDU3MDI5MCwiZXhwIjoxNTUxMTc1MDkwLCJzaWciOiI0dGx6anc3NzlMWUV3NnFVbm0yNzk2NytsQTBFUmZ4YjM1blNUUTlGZ2FjdVE4R29UK253Y0tndUhKZ2U4QzJGc3lEWDBJTG0vemhQXG5zR2hCS2RJRmxBPT1cbiJ9.12oq4xbmW2dNOhv9a7poCZ2VoZb-BYxs3ONa3pzCx8A')
        }
    }
);
 
// ws.on('open', function open() {
//   ws.send(JSON.stringify(''));
// });
 
ws.on('message', function incoming(data) {
  console.log(data);
});