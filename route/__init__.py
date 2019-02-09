# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-01-24 19:05:10

from handler.auth import (
    LoginHandler,
    RegisHandler,
)

from handler.msg import (
    MsgHandler,
)

urls = [
    (r'/auth/login', LoginHandler),
    (r'/auth/register', RegisHandler),
    (r'/msg', MsgHandler),
]