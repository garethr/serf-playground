#!/usr/bin/env python

import os
import sys
import socket
import fileinput
import logging

from serfclient.client import SerfClient
from serf_master import SerfHandler, SerfHandlerProxy

logging.basicConfig(filename='/var/log/serf-test.log', level=logging.DEBUG)

class BaseHandler(SerfHandler):
	def info(self):
		logging.debug("info called")
		client = SerfClient()
		client.event('collect', self.name)	

class LbHandler(BaseHandler):
	def collect(self):
		command_client = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
		command_client.connect("/tmp/serf.sock")
		payload = "".join(fileinput.input())
		logging.debug("collect called")
		logging.info(payload)
        	command_client.send(payload)

class WebHandler(BaseHandler):
	pass


if __name__ == '__main__':
	handler = SerfHandlerProxy()
	handler.register('lb', LbHandler())
	handler.register('web', WebHandler())
	handler.register('default', WebHandler())
	handler.run()
