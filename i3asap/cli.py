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
    i3_base_packages = "i3-wm i3-lock i3-bar dwm-tools suckless-tools"
    repository = "https://raw.githubusercontent.com/SteveTabernacle/i3asap/"
    pwd = expanduser("~") + "/.i3asap/" + bundle + "/"
    bundle = slugify(bundle)

    if not os.path.exists(pwd):
        os.makedirs(pwd)

    # Download manifest to get started
    click.echo("Downloading " + bundle)

    manifest = fetchJSON(repository + "master/bundles/" + bundle + "/manifest.json")

    # Download all specified files, e.g. dotfiles and wallpaper
    downloads = AsynkDownloader(manifest["files"], pwd, repository + "master/bundles/" + bundle + "/bundle/")
    downloads.start()

    # Purge specified programs
    if "purge" in manifest and len(manifest["purge"]) > 1:
        click.echo("apt-get purge " + manifest["purge"])

    # Install specified programs
    if "install" in manifest and len(manifest["install"]) > 1:
        click.echo("apt-get install " + manifest["install"])

    # Install i3
    click.echo("apt-get install " + i3_base_packages)

    # todo Create new user

    # Wait until downloads are complete
    downloads.join()

    # todo Move dotfiles, wallpapers etc to proper paths
    # todo Set wallpaper if specified
    # todo Switch user to new user

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
