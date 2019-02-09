/*
* @Author: Arius
* @Date:   2019-02-07 19:08:53
* @Last Modified by:   Arius
* @Last Modified time: 2019-02-09 17:29:01
*/

const WebSocket = require('ws');
const cookie = require('cookie');
 
const ws = new WebSocket(
    'http://127.0.0.1:3154/msg',
    [],
    {
        'headers': {
            // arius
            'Cookie': cookie.serialize('kl-auth', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50Ijp7ImlkIjoxMDAwMywibmFtZSI6ImFyaXVzIn0sImlhdCI6MTU0OTUzOTU1NSwiZXhwIjoxNTUwMTQ0MzU1LCJzaWciOiJFV1ljS2VKMkQ4RUtUN1hkdnVyNHlTRTNUQ1h0RWo4RUx5ZlorcEc4VklxTXd4TkNPNjRVUTRMN2RDdWNqZ2lQdjJGY3h1alNBOXRPXG5xM1BNZ2hNNmxnPT1cbiJ9.R8Ah7Qyfdlh3JljvaQCuthL-xqTPOWEjOdDGNwRbdmY')
        }
    }
);
 
ws.on('open', function open() {
  ws.send(JSON.stringify({
    to: 10004,
    send: 0,
    type: 0,
    msg: 'hello',
    date: new Date().valueOf(),
  }));
});
 
ws.on('message', function incoming(data) {
  console.log(data);
});