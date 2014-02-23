#!/usr/bin/env python

import socket
import os

if __name__ == "__main__":

    client = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    client.connect("/tmp/serf.sock")

    client.send("1")
    client.send("2")
    client.send("3")

    client.close()
