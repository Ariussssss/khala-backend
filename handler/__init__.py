# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-01-24 19:01:23


from tornado import (
    web,
    websocket,
)
import json
from datetime import datetime

from config import (
    code as code_cfg,
    msg as msg_cfg,
)
from auth import verify_token as vt
from .connect_center import CnCenter

def create_msg(fro, typ, msg, dat):
    return {
        'from': fro,
        'type': typ,
        'msg': msg,
        'date': dat,
    }


class BaseHandler(web.RequestHandler):

    def _res_fmt(f):
        def wrap(self, *args, **kwargs):
            self.verify_token()
            print(self._usr)
            try:
                code, res = f(self, *args, **kwargs)
            except Exception as e:
                print(e)
                code, msg = getattr(e, 'status_code', code_cfg.mis),\
                    getattr(e, 'log_message', 'Not Found')
                res = {
                    'err': msg
                }
            finally:
                self._finish(code, res)
        return wrap
            
    def _get(self):
        self.res_error()
    
    def _post(self):
        self.res_error()

    def _finish(self, code=500, res={}):
        res = res.copy()
        res['code'] = code
        self.clear()
        self.set_status(code)
        self.finish(res)

    def verify_token(self):
        token = self.request.headers.get('KL-Auth')
        cookie = self.get_cookie('klauth')
        status, usr = vt(token)
        if status:
            self._usr = usr
        else:
            self._usr = None
    
    def res_error(self, e=None):
        code, msg = getattr(e, 'status_code', 500),\
            getattr(e, 'log_message', 'Not Found')
        self._finish(code_cfg.mis, {
            'err': msg,
        })    

    @_res_fmt
    def get(self, *arg, **kwargs):
        return self._get(*arg, **kwargs)

    @_res_fmt
    def post(self, *arg, **kwargs):
        return self._post(*arg, **kwargs)

class SocketHandler(websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def beforeLogin(self):
        pass

    def open(self):
        token = self.get_cookie('kl-auth')
        status, usr = vt(token)
        if status:
            self._usr = usr
            CnCenter.instance().add(usr['id'], self)
            self.beforeLogin()
            print('{0}\n{1} join'.format(
                datetime.now(), usr['name']))
            print(CnCenter.instance().all_members)
        else:
            self._usr = None
            self.close()
            print('{0}\n failed join'.format(
                datetime.now()))

    def on_close(self):
        print('{0}\n{1} leave'.format(
            datetime.now(), self._usr['name']))
        CnCenter.instance().remove(self._usr['id'])
        self._usr = None
        print(CnCenter.instance().all_members)

    def on_message(self, msg_info):
        pass