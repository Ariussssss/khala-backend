# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-02-02 15:23:43

import json

from . import (
    SocketHandler,
    create_msg,
)
from .connect_center import CnCenter
from db.redis_db import getRedisClient
from db.redis.key_builder import KeyBuilder
from config import (
    msg as msg_cfg,
)

class MsgHandler(SocketHandler):
    def check_origin(self, origin):
        return True

    def on_message(self, msg_info):
        msg = json.loads(msg_info)
        if msg['send'] == msg_cfg.send.usr:
            con = CnCenter.instance().get_connection(msg['to'])
            new_msg = create_msg(
                self._usr, msg['type'], msg['msg'], msg['date']
                )
            if con:
                con.write_message(json.dumps(new_msg))
                print('send successed')
            else:
                getRedisClient().sadd(KeyBuilder.unrecv(msg['to']), json.dumps(new_msg))
                print('not online')
                pass
        # todo save pic
        # todo save meme
        # todo save code
        # todo save to group

    def beforeLogin(self):
        unrecv = getRedisClient().spop(KeyBuilder.unrecv(self._usr['id']))
        while unrecv:
            self.write_message(unrecv)
            unrecv = getRedisClient().spop(KeyBuilder.unrecv(self._usr['id']))


