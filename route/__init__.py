# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-01-24 19:05:10

from handler.auth import (
    LoginHandler as alh,
    RegisHandler as arh,
)
from handler.room import (
    CreateHandler as rch,
    JoinHandler as rjh,
    UpdateOwnerHandler as uoh,
    UpdateNameHandler as unh,
)
from handler.msg import (
    MsgHandler as mmh,
)

urls = [
    (r'/auth/login', alh),
    (r'/auth/register', arh),
    (r'/msg', mmh),
    (r'/room/create', rch),
    (r'/room/join', rjh),
    (r'/room/update/owner', uoh),
    (r'/room/update/name', unh),
]