# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os
import sys
import subprocess
import argparse
import urllib2
import re
 
from threading import Thread


class Downloader(Thread):
    def __init__(self, url, name, directory):
        Thread.__init__(self)
        self.name = name
        self.url = url
        self.directory = directory

    def run(self):
        """Run the thread"""
        handle = urllib2.urlopen(self.url)
        fname = self.directory+self.name
        with open(fname, "wb") as f_handler:
            while True:
                chunk = handle.read(1024)
                if not chunk: break
                f_handler.write(chunk)
        msg = "Finished downloading %s!" % self.url
        print(msg)


def sh(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout = []
    while True:
        line = p.stdout.readline()
        stdout.append(line)
        if line == '' and p.poll() != None:
            break
    return (''.join(stdout)).strip()
