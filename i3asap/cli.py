# -*- coding: utf-8 -*-

import click
from os.path import expanduser
import os

import time

from helpers import slugify
from models import Downloader


@click.command()
@click.option('--bundle',
              prompt='What bundle do you want to use:',
              help='The bundle to configure your system after',
              default='flat-dark')
def main(bundle):
    """Console script for i3asap"""
    bundle = slugify(bundle)

    REMOVE_APPS = "remove_apps.txt"
    INSTALL_APPS = "install_apps.txt"
    WORKING_DIR = expanduser("~")+"/.i3asap/"+bundle+"/"

    urls = {"wallpaper.jpg":"https://images.unsplash.com/photo-1462834026679-7c03bf571a67?dpr=2&auto=compress,format&fit=crop&w=1199&h=791&q=80&cs=tinysrgb&crop=",
            ".i3_config": "https://raw.githubusercontent.com/SteveTabernacle/i3asap/master/bundles/"+bundle+"/.i3_config",
            ".Xresources": "https://raw.githubusercontent.com/SteveTabernacle/i3asap/master/bundles/"+bundle+"/.Xresources",
            REMOVE_APPS: "https://raw.githubusercontent.com/SteveTabernacle/i3asap/master/bundles/"+bundle+"/remove_apps.txt",
            INSTALL_APPS: "https://raw.githubusercontent.com/SteveTabernacle/i3asap/master/bundles/"+bundle+"/install_apps.txt"}

    if not os.path.exists(WORKING_DIR):
        os.makedirs(WORKING_DIR)

    click.echo("Downloading https://github.com/SteveTabernacle/i3asap/master/bundles/" + bundle)
    downloads = Downloader(urls, WORKING_DIR)
    downloads.start()

    # do other stuff

    downloads.join()
    with open(WORKING_DIR+INSTALL_APPS, 'r') as content_file:
        apps_to_install = content_file.read().replace("\n", " ")
        click.echo("apt-get install "+apps_to_install)

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
