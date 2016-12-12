# -*- coding: utf-8 -*-
import subprocess
import urllib2

from threading import Thread


class AsynkDownloader(Thread):
    """
    urls: format {"saveAs": "remote url"}
    """
    def __init__(self, urls, directory):
        Thread.__init__(self)
        self.urls = urls
        self.directory = directory

    def run(self):
        for name, url in self.urls.items():
            handle = urllib2.urlopen(url)
            fname = self.directory+name
            with open(fname, "wb") as f_handler:
                while True:
                    chunk = handle.read(1024)
                    if not chunk: break
                    f_handler.write(chunk)


class Terminal(object):
    def __init__(self):
        self.bash_history = []

    def run(self, cmd):
        self.bash_history.append(cmd)
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        stdout = []
        while True:
            line = p.stdout.readline()
            stdout.append(line)
            if line == '' and p.poll() != None:
                break
        return (''.join(stdout)).strip()
