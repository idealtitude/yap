# -*- coding: utf-8 -*-

import json


class ConfManager:
    def __init__(self, app_path):
        self.conf_file = f'{app_path}/data/conf.json'
        self.config = None
        self.load_config()

    def load_config(self):
        fd = open(self.conf_file)
        conf = fd.read()
        self.config = json.loads(conf)
        fd.close()

