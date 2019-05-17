# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-01-24 19:05:10

from handler.auth import (
    LoginHandler as alh,
    RegisHandler as arh,
    CheckHandler as ach,
)
from handler.search import (
    SearchHandler as ssh,
    UsrSearchHandler as sush,
)
from handler.room_handler import (
    GetHandler as rgh,
    CreateHandler as rch,
    JoinHandler as rjh,
    RemoveHandler as rrh,
    UpdateOwnerHandler as uoh,
    UpdateNameHandler as unh,
)
from handler.msg import (
    MsgHandler as mmh,
)
from handler.upload import (
    UploadHandler as uh,
    StaticHandler as sh,
)

urls = [
    (r'/auth/login', alh),
    (r'/auth/register', arh),
    (r'/auth/check', ach),
    (r'/msg', mmh),
    (r'/search', ssh),
    (r'/search/usr', sush),
    (r'/room/get', rgh),
    (r'/room/create', rch),
    (r'/room/join', rjh),
    (r'/room/remove', rrh),
    (r'/room/update/owner', uoh),
    (r'/room/update/name', unh),
    (r'/upload', uh),
    (r'/static/(.*)', sh, {'path':'./cache/'}),
]