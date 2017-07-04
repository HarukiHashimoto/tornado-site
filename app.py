#!/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import os
from tornado import ioloop, gen, web    # tornado 読込
from tornado.web import url
import tornado_mysql    # データベース接続用モジュール

class IndexHandler(web.RequestHandler):
    def get(self):
        self.render("index.html", title="INDEX")

class AboutHandler(web.RequestHandler):
    def get(self):
        self.render("about.html", title="ABOUT")

application = web.Application([
    url(r"/", IndexHandler, name="index"),
    url(r"/about/", AboutHandler, name="about"),
    ],
    template_path=os.path.join(os.getcwd(),"templates"),
    static_path=os.path.join(os.getcwd(),"static"),
)

if __name__ == "__main__":
    application.listen(8080)
    print("Server is up ...")
    ioloop.IOLoop.instance().start()
