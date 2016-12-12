# -*- coding: utf-8 -*-

import click
from os.path import expanduser
import os
from i3asap import Downloader

@click.command()
def main(args=None):
    """Console script for i3asap"""
    click.echo("Replace this message by putting your code into "
               "i3asap.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")

    urls = {"bg1.jpg":"https://images.unsplash.com/photo-1462834026679-7c03bf571a67?dpr=2&auto=compress,format&fit=crop&w=1199&h=791&q=80&cs=tinysrgb&crop=",
            "bg2.jpg":"https://images.unsplash.com/photo-1476790422463-0f61b4722b8e?dpr=2&auto=compress,format&fit=crop&w=1199&h=799&q=80&cs=tinysrgb&crop="}
    directory = expanduser("~")+"/.i3asap/"

    if not os.path.exists(directory):
        os.makedirs(directory)

    for name, url in urls.items():
        thread = Downloader(url, name, directory)
        thread.start()

if __name__ == "__main__":
    main()
