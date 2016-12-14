# -*- coding: utf-8 -*-
import os
import subprocess
import urllib2

from threading import Thread

from os.path import expanduser

import crypt


class AsynkDownloader(Thread):
    """
    """

    def __init__(self, urls, directory, base_url):
        Thread.__init__(self)
        self.urls = urls
        self.directory = directory
        self.base_url = base_url

    def run(self):
        for remote_file in self.urls:
            handle = urllib2.urlopen(self.base_url + remote_file["name"])
            fname = self.directory + remote_file["name"]
            # todo download to correct folder directly
            with open(fname, "wb") as f_handler:
                while True:
                    chunk = handle.read(1024)
                    if not chunk:
                        break
                    f_handler.write(chunk)


class NixSystem():
    def install(self, programs):
        pass

    def uninstall(self, programs):
        pass

    def i3_base_packages(self):
        pass

    def home_dir(self):
        pass

    """
    Execute and return stdout
    """
    def bash(self, cmd):
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        stdout = []
        while True:
            line = p.stdout.readline()
            stdout.append(line)
            if line == '' and p.poll() is not None:
                break
        return (''.join(stdout)).strip()


class KaliLinux(NixSystem):
    def install(self, programs):
        print("apt-get install " + programs)

    def uninstall(self, programs):
        print("apt-get purge " + programs)

    def i3_base_packages(self):
        return self.install("i3 suckless-tools")

    def home_dir(self):
        return expanduser("~")

    def create_user(self, name, username, password):
        encrypted = crypt.crypt(password, "22")  # todo found only why tf is salt "22"?
        return self.bash(
            "useradd"
            " -p " + encrypted +
            " -s " + "/bin/bash" +
            " -d " + "/home/" + username +
            " -m " +
            " -c \"" + name + "\" " + username)

# Roadmap: this would be cool
#
# class BlackArch(IOperatingSystem):
#
#   def install(self, programs):
#        print("pacman -S " + programs)
#
#    def uninstall(self, programs):
#        print("apt-get -R " + programs)
#
#    def i3_base_packages(self):
#        return self.install("i3")
