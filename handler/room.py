# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-02-10 17:29:17


from . import BaseHandler
from config import code as cfg
from db.mysql.sql_builder import SqlBuilder as sql
from db.mysql_db import MysqlClient

class Room(object):
    _mc = MysqlClient.instance()

    def create(self, owner):
        q = sql.create_room(owner)
        code, server = self._mc.do(q)
        if code:
            self.join(server.last_id(), owner)
            return code, server.last_id()
        else:
            return code, None
    
    def join(self, room, member):
        q = sql.join_room(room, member)
        code, _ = self._mc.do(q)
        return code

    def check_join(self, room, member):
        q = sql.check_room_join(room, member)
        code, server = self._mc.do(q)
        if code and server.first()[0]:
            return True
        else:
            return False


    def check_owner(self, room, owner):
        q = sql.check_room_owner(room, owner)
        code, server = self._mc.do(q)
        if code and server.first()[0]:
            return True
        else:
            return False

    def update(self, room, name, owner):
        q = sql.update_room(room, name, owner)
        code, _ = self._mc.do(q)
        return code
    
    def roommate(self, room):
        q = sql.get_all_roommate(room)
        code, server = self._mc.do(q)
        return server.all()

class CreateHandler(BaseHandler, Room):

    def _post(self):
        roommate = self.get_argument('roommate', None)
        if roommate:
            roommate = roommate.strip().split(',')
        else:
            roommate = []
        if self._usr:
            code, room = self.create(self._usr['id'])
            if code:
                roommate.append(self._usr['id'])
                print(roommate)
                print (self.join(room, roommate))
                return cfg.suc.code, {
                    'msg': 'create successed',
                }
            else:
                return cfg.svr.code, {
                    'err': 'create error',
                }
        else:
            return cfg.na.code, {
                'err': cfg.na.text,
            }

class JoinHandler(BaseHandler, Room):

    def _post(self):
        room = self.get_argument('room')
        if self._usr:
            usr = int(self._usr['id'])
            room = int(room)
            print(room)
            print(usr)
            if self.check_join(room, usr):
                return cfg.mis.code, {
                    'err': cfg.mis.text,
                }
            else:
                code = self.join(room, usr)
                if code:
                    return cfg.suc.code, {
                        'msg': 'join successed',
                    }
                else:
                    return cfg.mis.code, {
                        'err': cfg.mis.text,
                    }
        else:
            return cfg.aut.code, {
                'err': cfg.aut.text,
            }

class UpdateNameHandler(BaseHandler, Room):

    def _post(self):
        name = self.get_argument('name')
        room = int(self.get_argument('room'))
        usr = int(self._usr['id'])
        if self.check_join(room, usr):
            code = self.update(room, name, None)
            if code:
                return cfg.suc.code, {
                    'msg': 'update successed',
                }
            else:
                return cfg.svr.code, {
                    'err': cfg.svr.text,
                }

        else:
            return cfg.aut.code, {
                'err': cfg.aut.text,
            }

class UpdateOwnerHandler(BaseHandler, Room):

    def _post(self):
        owner = int(self.get_argument('owner', '0'))
        room = int(self.get_argument('room'))
        if owner:
            usr = int(self._usr['id'])
            if self.check_owner(room, usr):
                code = self.update(room, None, owner)
                if code:
                    return cfg.suc.code, {
                        'msg': 'update successed',
                    }
                else:
                    return cfg.svr.code, {
                        'err': cfg.svr.text,
                    }
            else:
                return cfg.mis.code, {
                    'err': cfg.mis.text,
                }
        else:
            return cfg.aut.code, {
                'err': cfg.aut.text,
            }
