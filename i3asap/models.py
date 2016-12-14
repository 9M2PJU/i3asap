# -*- coding: utf-8 -*-
import os
import subprocess
import urllib2

from threading import Thread

from sys import platform
from os.path import expanduser

import crypt


class AsynkDownloader(Thread):
    """
    """

    def __init__(self, urls, base_url):
        Thread.__init__(self)
        self.urls = urls
        self.base_url = base_url

    def create_dl_folder(self, path):
        folder = os.path.dirname(path)
        if not os.path.exists(folder):
            os.makedirs(folder)

    def run(self):
        for remote_file in self.urls:
            handle = urllib2.urlopen(self.base_url + remote_file["name"])
            self.create_dl_folder(remote_file["saveAs"])
            with open(remote_file["saveAs"], "wb") as f_handler:
                while True:
                    chunk = handle.read(1024)
                    if not chunk:
                        break
                    f_handler.write(chunk)


class LinuxSystem(object):
    def __init__(self):
        pass

    def install(self, programs):
        pass

    def uninstall(self, programs):
        pass

    def i3_base_packages(self):
        pass

    def home_dir(self):
        pass

    def verify_os(self):
        if platform != "linux" and platform != "linux2":
            return False
        return True
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


class DebianLinux(LinuxSystem):
    def install(self, programs):
        return self.bash("DEBIAN_FRONTEND=noninteractive apt-get -yq install " + programs)

    def uninstall(self, programs):
        return self.bash("DEBIAN_FRONTEND=noninteractive apt-get -yq purge " + programs)

    def i3_base_packages(self):
        return "i3 suckless-tools"

    def home_dir(self):
        return expanduser("~")

    def create_user(self, name, username, password):
        encrypted = crypt.crypt(password, "22")  # todo why t-f is salt "22"?
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
