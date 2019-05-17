/*
* @Author: Arius
* @Date:   2019-02-07 19:08:53
* @Last Modified by:   Arius
* @Last Modified time: 2019-05-17 07:42:15
*/

const WebSocket = require('ws');
const cookie = require('cookie');

const ws = new WebSocket(
    'http://127.0.0.1:3154/msg',
    [],
    {
        'headers': {
            // Ekolia
            'Cookie': cookie.serialize('kl-auth', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50Ijp7ImlkIjoxLCJuYW1lIjoiZWtvbGlhIn0sImlhdCI6MTU1ODA0OTk2MywiZXhwIjoxNTU4NjU0NzYzLCJzaWciOiIyN2dzT2hLTnd3YTIzd3BFcXZTdlUwUC9PQzQ2bmlPWEFFTEhxeEVkNEcrMU1SODVrczl0eStvNFJXQ1ZVWXk1Z2h4Q29KM0Q4MTRBXG5NcTdkMHdnTWtnPT1cbiJ9.cEzwLzLh87aPblMhg-JM7xp0s0wftq2NoUInsvmKUzY')
        }
    }
);

const io = require('socket.io-client');
ws.on('open', function open() {
  ws.send(JSON.stringify({
    to: {
      id: 3,
      name: 'Dream Team',
    },
    send: 1,
    type: 0,
    msg: 'Good Morning~',
    date: new Date().valueOf(),
  }));
});
 
// var opts = {
//   // Cookie: 'kl-auth=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50Ijp7ImlkIjoyLCJuYW1lIjoiYXJpdXMifSwiaWF0IjoxNTU2Njk1MjIyLCJleHAiOjE1NTczMDAwMjIsInNpZyI6IkE3OTFyd1lsSHNsc042L2dmYTVjTCtsNDdYS1JwL0hmWW5QMEFOQTBDY2hvdGVLcGdHNTBxTEdXNlVVZDhxbkZxaXdQckRLbHltK1Fcbjh3SXBtWXhLV2c9PVxuIn0.5rHFObilMvbLuZSINiYWVaXEW5ESf22WzZMlgtnjg48',
//   headers: {
//     Cookie: 'kl-auth=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50Ijp7ImlkIjoyLCJuYW1lIjoiYXJpdXMifSwiaWF0IjoxNTU2Njk1MjIyLCJleHAiOjE1NTczMDAwMjIsInNpZyI6IkE3OTFyd1lsSHNsc042L2dmYTVjTCtsNDdYS1JwL0hmWW5QMEFOQTBDY2hvdGVLcGdHNTBxTEdXNlVVZDhxbkZxaXdQckRLbHltK1Fcbjh3SXBtWXhLV2c9PVxuIn0.5rHFObilMvbLuZSINiYWVaXEW5ESf22WzZMlgtnjg48',
//   },
//   // extraHeaders: {
//   //   'X-Custom-Header-For-My-Project': 'my-secret-access-token',
//   //   'Cookie': 'user_session=NI2JlCKF90aE0sJZD9ZzujtdsUqNYSBYxzlTsvdSUe35ZzdtVRGqYFr0kdGxbfc5gUOkR9RGp20GVKza; path=/; expires=Tue, 07-Apr-2015 18:18:08 GMT; secure; HttpOnly'
//   // }
// };
// const cookie = c.serialize('kl-auth', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50Ijp7ImlkIjoyLCJuYW1lIjoiYXJpdXMifSwiaWF0IjoxNTU2Njk1MjIyLCJleHAiOjE1NTczMDAwMjIsInNpZyI6IkE3OTFyd1lsSHNsc042L2dmYTVjTCtsNDdYS1JwL0hmWW5QMEFOQTBDY2hvdGVLcGdHNTBxTEdXNlVVZDhxbkZxaXdQckRLbHltK1Fcbjh3SXBtWXhLV2c9PVxuIn0.5rHFObilMvbLuZSINiYWVaXEW5ESf22WzZMlgtnjg48')
// const ws = new WebSocket('http://127.0.0.1:3154/msg', '', opts);

// ws.on('message', function incoming(data) {
//   console.log(data);
// });