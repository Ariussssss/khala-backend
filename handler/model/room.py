# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-02-10 17:29:17


from db.mysql.sql_builder import SqlBuilder as sql
from . import OrmBase

class Room(OrmBase):

    def create(self, name, owner):
        q = sql.create_room(name, owner)
        code, server = self._mc.do(q)
        if code:
            self.join(server.last_id(), owner)
            return code, server.last_id()
        else:
            return code, None
    
    def get_room(self, room):
        q = sql.get_room(room)
        code, server = self._mc.do(q)
        res = server.first()
        if code and res:
            return res
        else:
            return {}

    def join(self, room, member):
        q = sql.join_room(room, member)
        print(q)
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

    def all_room(self, member):
        q = sql.get_all_room(member)
        code, server = self._mc.do(q)
        return server.all()

    def roommate_info(self, room):
        q = sql.get_all_roommate_info(room)
        code, server = self._mc.do(q)
        return server.all()

    def remove(self, room, member):
        q = sql.remove_member(room, member)
        code, _ = self._mc.do(q)
        return True
