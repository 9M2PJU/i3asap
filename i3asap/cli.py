# -*- coding: utf-8 -*-

import click
from os.path import expanduser
import os

import time

from helpers import slugify, fetchJSON
from models import AsynkDownloader

@click.command()
@click.option('--bundle',
              prompt='What bundle do you want to use:',
              help='The bundle to configure your system after',
              default='flat-dark')
def main(bundle):
    """Console script for i3asap"""
    bundle = slugify(bundle)

    repository = "https://raw.githubusercontent.com/SteveTabernacle/i3asap"
    pwd = expanduser("~")+"/.i3asap/"+bundle+"/"

    if not os.path.exists(pwd):
        os.makedirs(pwd)

    click.echo("Downloading "+repository+"/master/bundles/" + bundle)

    manifest = fetchJSON(repository+"/master/bundles/" + bundle + "/manifest.json")

    downloads = AsynkDownloader(manifest["files"], pwd)
    downloads.start()

    click.echo("apt-get purge "+manifest["install"])
    click.echo("apt-get install "+manifest["install"])

    downloads.join()

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
