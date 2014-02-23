#!/usr/bin/env python

import socket
import os
from multiprocessing import Process

from serfclient.client import SerfClient

def send_info():
    client = SerfClient()
    client.event('info', "nothing")

def get_responses():
    server = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    server.bind("/tmp/serf.sock")
    while True:
        data = server.recv(1024)
        print data

    print "shutting down"
    server.close()
    os.remove("/tmp/serf.sock")

if __name__ == '__main__':

    p = Process(target=send_info)
    p2 = Process(target=get_responses)
    p2.start()
    p.start()
    p2.join(10)
    if p2.is_alive():
        p2.terminate()

