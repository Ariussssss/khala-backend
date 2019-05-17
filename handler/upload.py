# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-04-25 14:29:23

from tornado import web
import os
from . import BaseHandler
from config import code as cfg
from util import random_str

class UploadHandler(BaseHandler):
    def _post(self):
        if self._usr:
            upload_path = os.path.join(os.path.dirname(__file__), '../cache')
            file_metas = self.request.files.get('file', None)
            if not file_metas:
                return cfg.mis.code, {
                    'err': cfg.mis.text,
                }

            files_list = []
            for meta in file_metas:
                filename = random_str(10) + meta['filename']
                file_path = os.path.join(upload_path, filename)

                try:
                    print(file_path)
                    with open(file_path, 'wb+') as up:
                        up.write(meta['body'])
                    files_list.append('./static/' + filename)
                except Exception as e:
                    return cfg.mis.code, {
                        'err': str(e),
                    }

            return cfg.suc.code, {
                'msg': 'upload successed',
                'files_list': files_list,
            }
        else:
            return cfg.aut.code, {
                'err': cfg.aut.text,
            }

class StaticHandler(web.StaticFileHandler):  
    def set_extra_headers(self, path):  
        self.set_header("Cache-control", "no-cache")  