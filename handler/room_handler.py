# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-05-08 18:19:25


from . import BaseHandler
from config import code as cfg
from .model.room import Room
from .model.usr import Usr
from .msg import MsgHandler
from datetime import datetime

def boardcastLinkMsg(usr, msg, room_id, usr_id):
    room_info = Room().get_room(room_id)
    usr_info = Usr().get_usr(usr_id)
    MsgHandler.boardcast(usr, room_id, room_info[1],
        ' '.join([usr_info['name'], msg]))

class CreateHandler(BaseHandler, Room):

    def _post(self):
        name = self.get_argument('name', None)
        roommate = self.get_argument('roommate', '')
        if roommate:
            roommate = [int(x) for x in roommate.strip().split(',')]
        else:
            roommate = []
        if not name:
            name = 'Linked_{0}'.format(
            str(datetime.now().timestamp()).split('.')[1])
        print(self._usr)
        print(name)
        print(roommate)
        if self._usr and name:
            code, room = self.create(name, self._usr['id'])
            if code:
                self.join(room, roommate)
                return cfg.suc.code, {
                    'room_info': {
                        'id': room,
                        'name': name,
                    },
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

class GetHandler(BaseHandler, Room):

    def _post(self):
        room_id = int(self.get_argument('room'))
        room = self.get_room(room_id)
        print(room_id)
        print(room)
        if room:
            roommate = self.roommate_info(room_id)
            print(roommate)
            return cfg.suc.code, {
                'room': {
                    'id': room[0],
                    'name': room[1],
                    'owner': room[2],
                },
                'roommate': [
                    {
                        'id': person[0],
                        'name': person[1],
                    }
                    for person in roommate
                ],
            }
        else:
            return cfg.na.code, {
                'msg': 'room not existed',
            }

class JoinHandler(BaseHandler, Room):

    def _post(self):
        room = int(self.get_argument('room'))
        member = self.get_argument('member', None)
        if self._usr:
            usr_id = int(self._usr['id'])
            room_id = int(room)
            target = usr_id
            if member and self.check_join(room, usr_id):
                target = int(member)
            if self.check_join(room, target):
                return cfg.mis.code, {
                    'err': 'He is aleady linked.',
                }
            else:
                code = self.join(room, target)
                if code:
                    boardcastLinkMsg(self._usr, 'linked', room_id, target)
                    return cfg.suc.code, {
                        'msg': 'join successed',
                    }
                else:
                    return cfg.mis.code, {
                        'err': 'Linked error',
                    }
        else:
            return cfg.aut.code, {
                'err': cfg.aut.text,
            }

class RemoveHandler(BaseHandler, Room):

    def _post(self):
        room = int(self.get_argument('room'))
        member = self.get_argument('member', None)
        if self._usr:
            usr_id = int(self._usr['id'])
            room_id = int(room)
            target = usr_id
            is_owner = self.check_owner(room, usr_id)
            if member:
                if self.check_owner(room, usr_id):
                    target = int(member)
                else:
                    return cfg.aut.code, {
                        'err': 'You are not owner.',
                    }
            if not self.check_join(room, target):
                return cfg.mis.code, {
                    'err': 'He is not linked.',
                }
            else:
                if (usr_id == target and is_owner) or self.check_owner(room, target):
                    return cfg.mis.code, {
                        'err': 'Master can\'t unlinked',
                    }
                else:
                    code = self.remove(room, target)
                    if code:
                        boardcastLinkMsg(self._usr, 'unlinked', room_id, target)
                        return cfg.suc.code, {
                            'msg': 'remove successed',
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
        owner = int(self.get_argument('owner'))
        room = int(self.get_argument('room'))
        if owner:
            usr = int(self._usr['id'])
            if self.check_owner(room, usr):
                co
                de = self.update(room, None, owner)
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
