# -*- coding: utf-8 -*-
__author__ = 'tyr'
import logging
import os
import time


class Log(object):
    def __init__(self,logger):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.INFO)
        current_time = time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))
        file_path = os.path.dirname(os.getcwd()+'/logs/')
        file_name = file_path+current_time+'.log'
        fh = logging.FileHandler(file_name)
        fh.setLevel(logging.INFO)
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s %(filename)s [line:%(levelno)d] %(levelname)s %(message)s")
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def get_log(self):
        return self.logger
