#!/usr/bin/env python
# coding=utf-8
#
# Copyright 2014 vvovo.com
# Very way to victory.
# Let the dream set sail.


import uuid
import hashlib
import Image
import StringIO
import time
import json
import re
import urllib2
import tornado.web
import lib.jsonp

from base import *
from lib.variables import *

class AboutHandler(BaseHandler):
    def get(self, template_variables = {}):
    	template_variables["wallpaper"] = self.get_wallpaper()
        self.render("page/about.html", **template_variables)
