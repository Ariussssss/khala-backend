# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-02-02 15:23:43

from datetime import datetime
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
from .model.room import Room

class MsgHandler(SocketHandler):
    def check_origin(self, origin):
        return True

    @staticmethod
    def send(msg, to):
        print('to {0}: {1}'.format(to, msg))
        con = CnCenter.instance().get_connection(to)
        if con:
            con.write_message(json.dumps(msg))
            print('send successed')
        elif msg['type'] != msg_cfg.send.system:
            getRedisClient().sadd(KeyBuilder.unrecv(to), json.dumps(msg))
            print('not online')

    def on_message(self, msg_info):
        msg = json.loads(msg_info)
        if msg['send'] == msg_cfg.send.usr:
            new_msg = create_msg(
                self._usr, msg['type'], msg['msg'], msg['date'], None
            )
            MsgHandler.send(new_msg, msg['to']['id'])            
        elif msg['send'] == msg_cfg.send.group:
            room = Room()
            if room.check_join(msg['to']['id'], self._usr['id']):
                res = room.roommate(msg['to']['id'])
                new_msg = create_msg(
                    self._usr, msg['type'], msg['msg'], msg['date'], msg['to']
                )
                for x in res:
                    if x[0] != self._usr['id']:
                        MsgHandler.send(new_msg, x[0])
            else:
                print ('not roommate')
                new_msg = create_msg(
                    self._usr, msg_cfg.send.system,
                    '❌ Send error. You are not linked.',
                    int(datetime.now().timestamp() * 1000), msg['to']
                )
                MsgHandler.send(new_msg, self._usr['id'])
        # todo save code

    @staticmethod
    def boardcast(usr, room_id, room_name, msg):
        room = Room()
        res = room.roommate(room_id)
        for usr_id, in res:
            if usr_id != usr['id']:
                new_msg = create_msg(
                    usr, msg_cfg.send.system, msg,
                    int(datetime.now().timestamp() * 1000), {
                        'id': room_id,
                        'name': room_name,
                    },
                )
                MsgHandler.send(new_msg, usr_id)

    def beforeLogin(self):
        unrecv = getRedisClient().spop(KeyBuilder.unrecv(self._usr['id']))
        room = Room()
        all_room = room.all_room(self._usr['id'])
        for room_id, room_name in all_room:
            print('to room id: {0}, name: {1}'.format(room_id, room_name))
            self.boardcast(self._usr, room_id, room_name, '{0} link on'.format(self._usr['name']))
        while unrecv:
            self.write_message(unrecv)
            unrecv = getRedisClient().spop(KeyBuilder.unrecv(self._usr['id']))

    def beforeLogout(self):
        room = Room()
        all_room = room.all_room(self._usr['id'])
        for room_id, room_name in all_room:
            res = room.roommate(room_id)
            self.boardcast(self._usr, room_id, room_name, '{0} link off'.format(self._usr['name']))
