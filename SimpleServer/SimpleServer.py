# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 21:55:33 2018

@author: danny
"""

import http.server

server_address = ("", 8000)
handler_class = http.server.SimpleHTTPRequestHandler #ハンドラを設定
simple_server = http.server.HTTPServer(server_address, handler_class)
simple_server.serve_forever()
