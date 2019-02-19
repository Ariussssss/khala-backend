# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-01-23 21:48:15

from pypika import (
    Query,
    Table,
    Field,
    Order,
    functions as fn,
)
import time

from auth.aes import sha1
from config import tables as cfg

def sql_fmt(func):
    def wrap(self, *args, **kwargs):
        res = func(self, *args, **kwargs)
        return res.get_sql().replace('"', '`')
    return wrap

class SqlBuilder(object):

    @sql_fmt
    def login(name, pwd, arr):
        usr = Table(cfg.usr)
        q = Query.from_(usr).select(
                *arr
            ).where(
                usr.name == name
            ).where(
                usr.pwd == pwd
            )
        return q

    @sql_fmt
    def register(name, pwd):
        usr = Table(cfg.usr)
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        q = Query.into(usr).columns(
            usr.name, usr.pwd, usr.created, usr.updated
        ).insert(
            name, pwd, now, now
        )
        return q

    @sql_fmt
    def check_exist(id):
        usr = Table(cfg.usr)
        q = Query.from_(usr).select(
            fn.Count(usr.id)
        ).where(
            usr.id == id
        )
        return q

    @sql_fmt
    def update_usr(id, pwd, last_ip):
        usr = Table(cfg.usr)
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        q = Query.update(usr).set(
            usr.pwd, pwd or usr.pwd
        ).set(
            usr.update, now
        ).set(
            usr.last_ip, last_ip or usr.last_ip
        ).where(
            usr.id == id
        )
        return q

    @sql_fmt
    def create_room(owner):
        room = Table(cfg.room)
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        q = Query.into(room).columns(
                room.owner, room.updated, room.created
            ).insert(
                owner, now, now
            )
        return q

    @sql_fmt
    def join_room(room, member):
        join = Table(cfg.join)
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if isinstance(member, list):
            members = [(room, m, now) for m in member]
            q = Query.into(join).columns(
                join.room, join.member, join.created
            ).insert(
                members
            )
        else:
            q = Query.into(join).columns(
                join.room, join.member, join.created
            ).insert(
                room, member, now
            )
        return q

    @sql_fmt
    def remove_member(room, member):
        join = Table(cfg.join)
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        q = Query.into(join).columns(
                join.room, join.member, join.created
            ).insert(
                room, member, now
            )
        return q

    @sql_fmt
    def update_room(id, name, owner):
        room = Table(cfg.room)
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        q = Query.update(room).set(
            room.name, name or room.name
        ).set(
            room.updated, now
        ).set(
            room.owner, owner or room.owner
        ).where(
            room.id == id
        )
        return q

    @sql_fmt
    def check_room_owner(id, owner):
        room = Table(cfg.room)
        q = Query.from_(room).select(
            fn.Count(room.id)
        ).where(
            (room.id == id) & (room.owner == owner)
        )
        return q

    @sql_fmt
    def check_room_join(room, member):
        join = Table(cfg.join)
        q = Query.from_(join).select(
            fn.Count(join.id)
        ).where(
            (join.room == room) & (join.member == member)
        )
        return q

    @sql_fmt
    def get_all_roommate(room):
        join = Table(cfg.join)
        q = Query.from_(join).select(
            join.member
        ).where(
            join.room == room
        )
        return q

if __name__ == '__main__':
    # print (SqlBuilder.register('aaa', 'bbb'))
    # print (SqlBuilder.update_usr(1, None, 'localhost'))
    # print (SqlBuilder.create_room(10003))
    print (SqlBuilder.join_room(2, 10003))
    # print (SqlBuilder.get_all_roommate(2))
    # print (SqlBuilder.check_room_join(2, 10003))
    # print (SqlBuilder.check_room_owner(2, 10003))
    # print (SqlBuilder.check_exist(10003))

