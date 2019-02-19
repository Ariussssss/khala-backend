# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-02-02 15:23:43

import json

from . import (
    SocketHandler,
    create_msg,
)
from config import (
    msg as msg_cfg,
)
from db.redis_db import getRedisClient
from db.redis.key_builder import KeyBuilder
from .connect_center import CnCenter
from .room import Room

class MsgHandler(SocketHandler):
    def check_origin(self, origin):
        return True

    def send(self, msg, to):
        con = CnCenter.instance().get_connection(to)
        if con:
            con.write_message(json.dumps(msg))
            print('send successed')
        else:
            getRedisClient().sadd(KeyBuilder.unrecv(to), json.dumps(msg))
            print('not online')

    def on_message(self, msg_info):
        msg = json.loads(msg_info)
        new_msg = create_msg(
            self._usr, msg['type'], msg['msg'], msg['date']
            )
        if msg['send'] == msg_cfg.send.usr:
            self.send(new_msg, msg['to'])            
        elif msg['send'] == msg_cfg.send.group:
            room = Room()
            if room.check_join(msg['to'], self._usr['id']):
                res = room.roommate(msg['to'])
                for x in res:
                    self.send(new_msg, x[0])
            else:
                # todo no auth
                print ('not roommate')

        # todo save pic
        # todo save meme
        # todo save code

    def beforeLogin(self):
        unrecv = getRedisClient().spop(KeyBuilder.unrecv(self._usr['id']))
        while unrecv:
            self.write_message(unrecv)
            unrecv = getRedisClient().spop(KeyBuilder.unrecv(self._usr['id']))


